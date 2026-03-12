# Attendance Monitoring System

A modern, web-based attendance monitoring system with face recognition capabilities built with Flask and OpenCV.

## Features

- 🔐 **User Authentication** - Secure login and registration system
- 👨‍🎓 **Student Management** - Add, edit, and manage student records
- 📸 **Face Recognition** - Automatic attendance marking using face detection
- 📊 **Attendance Tracking** - View and manage attendance records
- 📥 **CSV Import/Export** - Import and export attendance data
- 🎨 **Modern UI** - Beautiful, responsive design with dark theme
- 🔍 **Search & Filter** - Easy search and filtering capabilities

## Prerequisites

- Python 3.8 or higher
- MySQL Server with phpMyAdmin (recommended: XAMPP or WAMP)
- Webcam (for face recognition)

## Installation

### 1. Clone or Download the Project

```bash
cd "d:/Projects/Attendence System"
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

### 3. Activate Virtual Environment

**Windows:**
```bash
venv\Scripts\activate
```

**Linux/Mac:**
```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Set Up MySQL Database with phpMyAdmin

#### Quick Setup (Recommended)

1. **Install XAMPP** (includes MySQL + phpMyAdmin):
   - Download from [https://www.apachefriends.org/](https://www.apachefriends.org/)
   - Install and start Apache + MySQL services

2. **Access phpMyAdmin**:
   - Open browser and go to: `http://localhost/phpmyadmin`

3. **Import Database**:
   - Click **Import** tab
   - Choose file: `database_setup.sql` (in project folder)
   - Click **Go**

#### Detailed Setup Guide

For complete installation instructions, troubleshooting, and phpMyAdmin usage, see:
📖 **[PHPMYADMIN_SETUP.md](PHPMYADMIN_SETUP.md)**

#### Alternative: Manual Setup

If you prefer to create the database manually:

```sql
CREATE DATABASE attendance_system;
```

Then the application will automatically create the required tables on first run.

### 6. Configure Environment Variables

1. Copy `.env.example` to `.env`:

```bash
copy .env.example .env
```

2. Edit `.env` and update your MySQL credentials:

```
DB_PASSWORD=your-mysql-password-here
```

### 7. Run the Application

```bash
python app.py
```

The application will be available at: **http://localhost:5000**

## Default Login

- **Username:** `admin`
- **Password:** `admin`

> ⚠️ **Important:** Change the default admin password after first login!

## Usage Guide

### 1. Register Students

1. Login to the system
2. Click "Students" in the navigation
3. Click "Add Student"
4. Fill in student details
5. Click "Save Student"

### 2. Capture Face Photos

1. Go to "Face Recognition" page
2. Click "Start Camera"
3. Select a student from the dropdown
4. Click "Capture for Training"
5. The system will automatically capture 100 photos
6. Repeat for all students

### 3. Train the Model

1. After capturing photos for all students
2. Click "Train Model" button
3. Wait for training to complete

### 4. Mark Attendance

1. Go to "Face Recognition" page
2. Click "Start Camera"
3. Click "Recognize Face"
4. The system will automatically mark attendance for recognized students

### 5. View Attendance

1. Click "Attendance" in the navigation
2. Use filters to view specific dates or departments
3. Export to CSV if needed

## Project Structure

```
Attendence System/
├── app.py                 # Main Flask application
├── config.py              # Configuration settings
├── models.py              # Database models
├── requirements.txt       # Python dependencies
├── routes/                # Route blueprints
│   ├── auth.py           # Authentication routes
│   ├── students.py       # Student management routes
│   ├── attendance.py     # Attendance routes
│   └── face_recognition.py # Face recognition routes
├── templates/             # HTML templates
│   ├── base.html
│   ├── login.html
│   ├── register.html
│   ├── dashboard.html
│   ├── students.html
│   ├── student_form.html
│   ├── attendance.html
│   └── face_recognition.html
├── static/                # Static files
│   ├── css/
│   │   └── style.css     # Main stylesheet
│   └── js/
│       ├── main.js       # Main JavaScript
│       └── camera.js     # Camera functionality
├── data/                  # Student face images (auto-created)
├── ml_models/             # Trained models (auto-created)
└── static/uploads/        # Uploaded files (auto-created)
```

## Troubleshooting

### Camera Not Working

- Ensure your browser has camera permissions
- Use HTTPS in production (required for camera access)
- Check if another application is using the camera

### Database Connection Error

- Verify MySQL is running (check XAMPP Control Panel)
- Check database credentials in `.env`
- Ensure the database exists (check in phpMyAdmin)
- Default XAMPP credentials: username=`root`, password=(empty)
- See [PHPMYADMIN_SETUP.md](PHPMYADMIN_SETUP.md) for detailed troubleshooting

### Face Recognition Not Working

- Ensure you've captured photos for students
- Train the model after capturing photos
- Check lighting conditions (good lighting improves accuracy)

## Technologies Used

- **Backend:** Flask, SQLAlchemy, Flask-Login
- **Database:** MySQL
- **Face Recognition:** OpenCV, LBPH Face Recognizer
- **Frontend:** HTML5, CSS3, JavaScript
- **Styling:** Custom CSS with modern design

## Security Notes

- Change default admin credentials
- Use strong passwords
- Keep `.env` file secure
- Use HTTPS in production
- Regularly backup your database

## License

This project is for educational purposes.

## Support

For issues or questions, please check the troubleshooting section or contact your system administrator.
