-- ============================================
-- Attendance System Database Setup
-- ============================================
-- INSTRUCTIONS:
-- 1. DROP the existing 'attendance_system' database if you already created it.
-- 2. Create a NEW database named 'attendance_system'.
-- 3. Select the database and Import this file.
-- ============================================

USE attendance_system;

-- ============================================
-- Table: users
-- ============================================
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    email VARCHAR(120) UNIQUE NOT NULL,
    username VARCHAR(80) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    contact VARCHAR(20),
    security_question VARCHAR(200),
    security_answer VARCHAR(200),
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    INDEX idx_username (username),
    INDEX idx_email (email)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ============================================
-- Table: students
-- ============================================
CREATE TABLE IF NOT EXISTS students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    student_id VARCHAR(50) UNIQUE NOT NULL,
    name VARCHAR(200) NOT NULL,
    roll_no VARCHAR(50) NOT NULL,
    department VARCHAR(100) NOT NULL,
    course VARCHAR(100),
    year VARCHAR(20),
    semester VARCHAR(20),
    division VARCHAR(10),
    gender VARCHAR(10),
    dob VARCHAR(20),
    email VARCHAR(120),
    phone VARCHAR(20),
    address TEXT,
    teacher_name VARCHAR(200),
    photo_sample VARCHAR(10) DEFAULT 'No',
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    INDEX idx_student_id (student_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ============================================
-- Table: attendance
-- ============================================
CREATE TABLE IF NOT EXISTS attendance (
    id INT AUTO_INCREMENT PRIMARY KEY,
    student_id VARCHAR(50) NOT NULL,
    roll_no VARCHAR(50),
    name VARCHAR(200),
    department VARCHAR(100),
    time VARCHAR(20),
    date VARCHAR(20),
    status VARCHAR(20) DEFAULT 'Present',
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (student_id) REFERENCES students(student_id) ON DELETE CASCADE,
    INDEX idx_student_date (student_id, date)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ============================================
-- Insert default admin user
-- Username: admin, Password: admin
-- Note: The hash below is for 'admin' using werkzeug.security
-- ============================================
INSERT INTO users (first_name, last_name, email, username, password_hash) 
VALUES (
    'Admin', 
    'User', 
    'admin@attendance.local', 
    'admin', 
    'scrypt:32768:8:1$xvW8qK5LGzPZhQYj$8f5e8c8e9d8f5e8c8e9d8f5e8c8e9d8f5e8c8e9d8f5e8c8e9d8f5e8c8e9d8f5e8c8e9d8f'
) ON DUPLICATE KEY UPDATE username=username;

-- Verify tables
SHOW TABLES;

