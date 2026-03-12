from flask import Blueprint, render_template, request, jsonify, Response
from flask_login import login_required
from models import db, Student, Attendance
import cv2
import numpy as np
import os
from datetime import datetime
from config import Config
import base64

face_bp = Blueprint('face', __name__)

@face_bp.route('/config')
@login_required
def get_config():
    """Get face recognition configuration"""
    return jsonify({
        'face_samples_count': Config.FACE_SAMPLES_COUNT,
        'face_confidence_threshold': Config.FACE_CONFIDENCE_THRESHOLD
    })

@face_bp.route('/')
@login_required
def index():
    """Face recognition page"""
    return render_template('face_recognition.html')

@face_bp.route('/capture-photos/<int:student_id>', methods=['POST'])
@login_required
def capture_photos(student_id):
    """Capture and save student photos for training"""
    student = Student.query.get_or_404(student_id)
    
    try:
        # Get image data from request
        image_data = request.json.get('images', [])
        
        if not image_data:
            return jsonify({'success': False, 'message': 'No images provided'})
        
        # Ensure student-specific data directory exists
        student_folder = os.path.join(Config.DATA_FOLDER, f"student_{student.id}")
        os.makedirs(student_folder, exist_ok=True)
        
        # Load face cascade
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        
        if face_cascade.empty():
            print("ERROR: Could not load face cascade classifier")
            return jsonify({'success': False, 'message': 'Internal error: face detector failed to load'})

        saved_count = 0
        received_count = len(image_data)
        target_count = Config.FACE_SAMPLES_COUNT
        print(f"DEBUG: Starting capture for student {student.id}. Received: {received_count}, Target: {target_count}")

        for idx, img_base64 in enumerate(image_data):
            try:
                # Decode base64 image
                img_data = base64.b64decode(img_base64.split(',')[1])
                nparr = np.frombuffer(img_data, np.uint8)
                img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
                
                if img is None:
                    print(f"Skipping frame {idx}: could not decode image")
                    continue

                # Convert to grayscale
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                
                # Detect faces - using more lenient parameters (scaleFactor=1.1, minNeighbors=4)
                faces = face_cascade.detectMultiScale(gray, 1.1, 4)
                
                if len(faces) == 0:
                    # Try with even more lenient parameters if no face found
                    faces = face_cascade.detectMultiScale(gray, 1.05, 3)

                for (x, y, w, h) in faces:
                    # Crop face
                    face = gray[y:y+h, x:x+w]
                    face_resized = cv2.resize(face, (450, 450))
                    
                    # Save image
                    filename = f"user.{student.id}.{saved_count + 1}.jpg"
                    filepath = os.path.join(student_folder, filename)
                    cv2.imwrite(filepath, face_resized)
                    saved_count += 1
                    
                    if saved_count >= Config.FACE_SAMPLES_COUNT:
                        break
                
                if saved_count >= Config.FACE_SAMPLES_COUNT:
                    break
            except Exception as e:
                print(f"Error processing frame {idx}: {e}")
                continue
        
        print(f"Successfully saved {saved_count} face samples")
        # Update student photo status
        student.photo_sample = 'Yes'
        db.session.commit()
        
        return jsonify({
            'success': True,
            'message': f'Captured {saved_count} photos successfully',
            'count': saved_count
        })
        
    except Exception as e:
        print(f"Capture photos error: {e}")
        return jsonify({'success': False, 'message': str(e)})

@face_bp.route('/recognize', methods=['POST'])
@login_required
def recognize():
    """Recognize face from uploaded image"""
    log_file = "recognition_debug.log"
    with open(log_file, "a") as f:
        f.write(f"\n--- RECOGNITION ATTEMPT: {datetime.now()} ---\n")
        try:
            # 1. Get and Validate JSON Data
            if not request.is_json:
                f.write("ERROR: Request is not JSON\n")
                return jsonify({'success': False, 'message': 'Invalid request format'})

            image_data = request.json.get('image')
            if not image_data:
                f.write("ERROR: No image data\n")
                return jsonify({'success': False, 'message': 'No image provided'})
            
            # 2. Decode Image
            try:
                img_data = base64.b64decode(image_data.split(',')[1])
                nparr = np.frombuffer(img_data, np.uint8)
                img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
            except Exception as e:
                f.write(f"ERROR: Base64 decode failed: {e}\n")
                return jsonify({'success': False, 'message': 'Could not process image data'})
            
            if img is None:
                f.write("ERROR: OpenCV imdecode failed\n")
                return jsonify({'success': False, 'message': 'Invalid image format'})

            f.write(f"Image decoded. Size: {img.shape}\n")

            # 3. Setup Classifier and Recognizer
            cascade_path = os.path.join(cv2.data.haarcascades, 'haarcascade_frontalface_default.xml')
            face_cascade = cv2.CascadeClassifier(cascade_path)
            if face_cascade.empty():
                f.write(f"ERROR: Cascade failed to load from {cascade_path}\n")
                return jsonify({'success': False, 'message': 'Internal error: Detector missing'})

            classifier_path = os.path.join(Config.MODEL_FOLDER, 'classifier.xml')
            if not os.path.exists(classifier_path):
                f.write(f"ERROR: Model file not found at {classifier_path}\n")
                return jsonify({'success': False, 'message': 'Model not trained. Capture photos and click Train Model first.'})
            
            recognizer = cv2.face.LBPHFaceRecognizer_create()
            recognizer.read(classifier_path)
            
            # 4. Process Image
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            
            # 5. Face Detection (Multi-stage/Lenient)
            # Stage 1: Standard
            faces = face_cascade.detectMultiScale(gray, 1.1, 5)
            if len(faces) == 0:
                f.write("Stage 1 (1.1, 5) found 0 faces. Trying Stage 2...\n")
                # Stage 2: More lenient
                faces = face_cascade.detectMultiScale(gray, 1.05, 3)
            if len(faces) == 0:
                f.write("Stage 2 (1.05, 3) found 0 faces. Trying Stage 3 (extreme lenient)...\n")
                # Stage 3: Extreme lenient
                faces = face_cascade.detectMultiScale(gray, 1.05, 1)

            f.write(f"Final detected face count: {len(faces)}\n")
            
            if len(faces) == 0:
                f.write("FAILURE: Still no faces detected after 3 stages\n")
                return jsonify({'success': False, 'message': 'No face detected. Please face the camera directly and ensure good lighting.'})
            
            # 6. Recognition
            recognized_students = []
            for idx, (x, y, w, h) in enumerate(faces):
                student_db_id, confidence = recognizer.predict(gray[y:y+h, x:x+w])
                
                # LBPH: 0 is a perfect match. Threshold is usually 80-100.
                f.write(f"Face {idx}: ID {student_db_id}, Confidence (Dist)={confidence:.2f}\n")
                
                # Map confidence to a 0-100 score
                score = int(100 * (1 - confidence / 300))
                if score < 0: score = 0
                
                f.write(f"Calculated Score: {score}% (Required > {Config.FACE_CONFIDENCE_THRESHOLD}%)\n")
                
                if score > Config.FACE_CONFIDENCE_THRESHOLD:
                    student = Student.query.get(student_db_id)
                    if student:
                        f.write(f"MATCH CONFIRMED: {student.name}\n")
                        # Mark attendance...
                        today = datetime.now().strftime('%Y-%m-%d')
                        existing = Attendance.query.filter_by(student_id=student.student_id, date=today).first()
                        if not existing:
                            attendance = Attendance(
                                student_id=student.student_id,
                                roll_no=student.roll_no,
                                name=student.name,
                                department=student.department,
                                time=datetime.now().strftime('%H:%M:%S'),
                                date=today,
                                status='Present'
                            )
                            db.session.add(attendance)
                            db.session.commit()
                            f.write("Attendance recorded in DB\n")
                        else:
                            f.write("Attendance already marked for today\n")
                        
                        # ALIGNED WITH FRONTEND (camera.js)
                        recognized_students.append({
                            'student_id': student.student_id,
                            'name': student.name,
                            'roll_no': student.roll_no,
                            'department': student.department,
                            'confidence': score,
                            'attendance_marked': not existing,
                            'message': 'Attendance marked' if not existing else 'Already marked'
                        })
                    else:
                        f.write(f"WARNING: Predicted ID {student_db_id} not found in students table\n")
            
            if recognized_students:
                f.write(f"SUCCESS: Successfully recognized {len(recognized_students)} students\n")
                return jsonify({'success': True, 'students': recognized_students})
            else:
                f.write("FAILURE: Face detected but confidence too low for all matches\n")
                return jsonify({'success': False, 'message': 'Face recognized but confidence score is too low. Try training with more photos or better lighting.'})
                
        except Exception as e:
            import traceback
            error_trace = traceback.format_exc()
            f.write(f"CRITICAL CRASH: {str(e)}\n{error_trace}\n")
            return jsonify({'success': False, 'message': f'Server error: {str(e)}'})

@face_bp.route('/train-model', methods=['POST'])
@login_required
def train_model():
    """Train face recognition model"""
    try:
        data_folder = Config.DATA_FOLDER
        student_id = request.json.get('student_id') if request.is_json else None
        
        if not os.path.exists(data_folder) or not os.listdir(data_folder):
            return jsonify({
                'success': False,
                'message': 'No training data found. Please capture student photos first.'
            })
        
        # Prepare training data
        recognizer = cv2.face.LBPHFaceRecognizer_create()
        classifier_path = os.path.join(Config.MODEL_FOLDER, 'classifier.xml')
        
        faces = []
        ids = []
        
        if student_id:
            # Train ONLY for a specific student (Incremental/Update)
            student_folder = os.path.join(data_folder, f"student_{student_id}")
            if not os.path.exists(student_folder):
                return jsonify({'success': False, 'message': f'No images found for student ID {student_id}'})
                
            for filename in os.listdir(student_folder):
                if filename.endswith('.jpg'):
                    img_path = os.path.join(student_folder, filename)
                    img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
                    if img is not None:
                        faces.append(img)
                        ids.append(int(student_id))
            
            if faces:
                if os.path.exists(classifier_path):
                    recognizer.read(classifier_path)
                    recognizer.update(faces, np.array(ids))
                else:
                    recognizer.train(faces, np.array(ids))
                
                recognizer.save(classifier_path)
                return jsonify({
                    'success': True,
                    'message': f'Model updated with {len(faces)} images for student {student_id}'
                })
        
        # Full Train (Global)
        for item in os.listdir(data_folder):
            item_path = os.path.join(data_folder, item)
            if os.path.isdir(item_path):
                for filename in os.listdir(item_path):
                    if filename.endswith('.jpg'):
                        parts = filename.split('.')
                        if len(parts) >= 3:
                            s_id = int(parts[1])
                            img = cv2.imread(os.path.join(item_path, filename), cv2.IMREAD_GRAYSCALE)
                            if img is not None:
                                faces.append(img)
                                ids.append(s_id)
            elif item.endswith('.jpg'):
                parts = item.split('.')
                if len(parts) >= 3:
                    s_id = int(parts[1])
                    img = cv2.imread(os.path.join(data_folder, item), cv2.IMREAD_GRAYSCALE)
                    if img is not None:
                        faces.append(img)
                        ids.append(s_id)
        
        if len(faces) == 0:
            return jsonify({'success': False, 'message': 'No valid training images found'})
        
        recognizer.train(faces, np.array(ids))
        os.makedirs(Config.MODEL_FOLDER, exist_ok=True)
        recognizer.save(classifier_path)
        
        return jsonify({
            'success': True,
            'message': f'Model trained successfully with {len(faces)} images from {len(set(ids))} students'
        })
        
    except Exception as e:
        print(f"Training error: {e}")
        return jsonify({'success': False, 'message': str(e)})
