from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify, send_file
from flask_login import login_required, current_user
from models import db, Attendance, Student
from datetime import datetime
import csv
import io
import os

attendance_bp = Blueprint('attendance', __name__)

@attendance_bp.route('/')
@login_required
def index():
    """Display attendance records"""
    # Get filter parameters
    date_filter = request.args.get('date', '')
    department_filter = request.args.get('department', '')
    
    query = Attendance.query
    
    if date_filter:
        query = query.filter_by(date=date_filter)
    if department_filter:
        query = query.filter_by(department=department_filter)
    
    attendance_records = query.order_by(Attendance.created_at.desc()).all()
    
    # Get unique departments for filter
    departments = db.session.query(Student.department).distinct().all()
    departments = [d[0] for d in departments if d[0]]
    
    return render_template('attendance.html', 
                         attendance_records=attendance_records,
                         departments=departments,
                         date_filter=date_filter,
                         department_filter=department_filter)

@attendance_bp.route('/mark', methods=['POST'])
@login_required
def mark():
    """Manually mark attendance"""
    student_id = request.form.get('student_id')
    status = request.form.get('status', 'Present')
    
    student = Student.query.filter_by(student_id=student_id).first()
    
    if not student:
        flash('Student not found', 'error')
        return redirect(url_for('attendance.index'))
    
    # Check if already marked today
    today = datetime.now().strftime('%Y-%m-%d')
    existing = Attendance.query.filter_by(
        student_id=student_id,
        date=today
    ).first()
    
    if existing:
        flash(f'Attendance already marked for {student.name} today', 'warning')
        return redirect(url_for('attendance.index'))
    
    # Create attendance record
    now = datetime.now()
    attendance = Attendance(
        student_id=student.student_id,
        roll_no=student.roll_no,
        name=student.name,
        department=student.department,
        time=now.strftime('%H:%M:%S'),
        date=today,
        status=status
    )
    
    try:
        db.session.add(attendance)
        db.session.commit()
        flash(f'Attendance marked for {student.name}', 'success')
    except Exception as e:
        db.session.rollback()
        flash('Error marking attendance', 'error')
        print(f"Mark attendance error: {e}")
    
    return redirect(url_for('attendance.index'))

@attendance_bp.route('/update/<int:id>', methods=['POST'])
@login_required
def update(id):
    """Update attendance record"""
    attendance = Attendance.query.get_or_404(id)
    
    attendance.status = request.form.get('status', attendance.status)
    attendance.time = request.form.get('time', attendance.time)
    
    try:
        db.session.commit()
        flash('Attendance updated successfully', 'success')
    except Exception as e:
        db.session.rollback()
        flash('Error updating attendance', 'error')
        print(f"Update attendance error: {e}")
    
    return redirect(url_for('attendance.index'))

@attendance_bp.route('/delete/<int:id>', methods=['POST'])
@login_required
def delete(id):
    """Delete attendance record"""
    attendance = Attendance.query.get_or_404(id)
    
    try:
        db.session.delete(attendance)
        db.session.commit()
        flash('Attendance record deleted', 'success')
    except Exception as e:
        db.session.rollback()
        flash('Error deleting attendance', 'error')
        print(f"Delete attendance error: {e}")
    
    return redirect(url_for('attendance.index'))

@attendance_bp.route('/export/csv')
@login_required
def export_csv():
    """Export attendance to CSV"""
    date_filter = request.args.get('date', '')
    department_filter = request.args.get('department', '')
    
    query = Attendance.query
    
    if date_filter:
        query = query.filter_by(date=date_filter)
    if department_filter:
        query = query.filter_by(department=department_filter)
    
    attendance_records = query.all()
    
    # Create CSV in memory
    output = io.StringIO()
    writer = csv.writer(output)
    
    # Write header
    writer.writerow(['ID', 'Student ID', 'Roll No', 'Name', 'Department', 'Time', 'Date', 'Status'])
    
    # Write data
    for record in attendance_records:
        writer.writerow([
            record.id,
            record.student_id,
            record.roll_no,
            record.name,
            record.department,
            record.time,
            record.date,
            record.status
        ])
    
    # Prepare file for download
    output.seek(0)
    filename = f"attendance_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
    
    return send_file(
        io.BytesIO(output.getvalue().encode('utf-8')),
        mimetype='text/csv',
        as_attachment=True,
        download_name=filename
    )

@attendance_bp.route('/import/csv', methods=['POST'])
@login_required
def import_csv():
    """Import attendance from CSV"""
    if 'file' not in request.files:
        flash('No file uploaded', 'error')
        return redirect(url_for('attendance.index'))
    
    file = request.files['file']
    
    if file.filename == '':
        flash('No file selected', 'error')
        return redirect(url_for('attendance.index'))
    
    if not file.filename.endswith('.csv'):
        flash('Please upload a CSV file', 'error')
        return redirect(url_for('attendance.index'))
    
    try:
        # Read CSV
        stream = io.StringIO(file.stream.read().decode("UTF8"), newline=None)
        csv_reader = csv.reader(stream)
        
        # Skip header
        next(csv_reader, None)
        
        imported_count = 0
        for row in csv_reader:
            if len(row) >= 7:
                # Check if record already exists
                existing = Attendance.query.filter_by(
                    student_id=row[1],
                    date=row[6]
                ).first()
                
                if not existing:
                    attendance = Attendance(
                        student_id=row[1],
                        roll_no=row[2],
                        name=row[3],
                        department=row[4],
                        time=row[5],
                        date=row[6],
                        status=row[7] if len(row) > 7 else 'Present'
                    )
                    db.session.add(attendance)
                    imported_count += 1
        
        db.session.commit()
        flash(f'Successfully imported {imported_count} attendance records', 'success')
    except Exception as e:
        db.session.rollback()
        flash('Error importing CSV file', 'error')
        print(f"Import CSV error: {e}")
    
    return redirect(url_for('attendance.index'))

@attendance_bp.route('/api/today')
@login_required
def today_attendance():
    """Get today's attendance"""
    today = datetime.now().strftime('%Y-%m-%d')
    records = Attendance.query.filter_by(date=today).all()
    return jsonify([record.to_dict() for record in records])

@attendance_bp.route('/api/stats')
@login_required
def stats():
    """Get attendance statistics"""
    today = datetime.now().strftime('%Y-%m-%d')
    
    total_students = Student.query.count()
    today_present = Attendance.query.filter_by(date=today, status='Present').count()
    today_absent = total_students - today_present
    
    return jsonify({
        'total_students': total_students,
        'present': today_present,
        'absent': today_absent,
        'attendance_percentage': round((today_present / total_students * 100) if total_students > 0 else 0, 2)
    })
