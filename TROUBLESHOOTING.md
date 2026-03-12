# Database Setup Troubleshooting

## Error: "#1932 - Table doesn't exist in engine"

This error means the tables weren't created. Here's how to fix it:

### Solution: Manual Step-by-Step Setup

#### Step 1: Create Database First
1. Open phpMyAdmin: `http://localhost/phpmyadmin`
2. Click **"New"** in the left sidebar
3. Database name: `attendance_system`
4. Collation: `utf8mb4_unicode_ci`
5. Click **"Create"**
6. ✅ You should see "attendance_system" in the left sidebar

#### Step 2: Select the Database
1. Click on **"attendance_system"** in the left sidebar
2. Make sure it's highlighted/selected

#### Step 3: Create Tables Using SQL Tab
1. Click the **"SQL"** tab at the top
2. Copy and paste the SQL from `database_setup.sql`
3. Click **"Go"** button
4. ✅ You should see "4 tables created" or similar success message

#### Step 4: Verify Tables Exist
1. Click on **"attendance_system"** in left sidebar
2. You should see 4 tables:
   - ✅ users
   - ✅ students
   - ✅ attendance
   - ✅ face_training_data

### Alternative: Create Tables Manually

If the SQL import still doesn't work, create each table manually:

#### 1. Create Users Table
```sql
CREATE TABLE users (
    id INT NOT NULL AUTO_INCREMENT,
    username VARCHAR(80) NOT NULL,
    email VARCHAR(120) NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    full_name VARCHAR(100) DEFAULT NULL,
    role VARCHAR(20) DEFAULT 'user',
    is_active TINYINT(1) DEFAULT 1,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (id),
    UNIQUE KEY username (username),
    UNIQUE KEY email (email)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
```

#### 2. Create Students Table
```sql
CREATE TABLE students (
    id INT NOT NULL AUTO_INCREMENT,
    student_id VARCHAR(50) NOT NULL,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    email VARCHAR(120) DEFAULT NULL,
    phone VARCHAR(20) DEFAULT NULL,
    department VARCHAR(100) DEFAULT NULL,
    year VARCHAR(20) DEFAULT NULL,
    section VARCHAR(10) DEFAULT NULL,
    enrollment_date DATE DEFAULT NULL,
    photo_path VARCHAR(255) DEFAULT NULL,
    face_encoding_path VARCHAR(255) DEFAULT NULL,
    is_active TINYINT(1) DEFAULT 1,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (id),
    UNIQUE KEY student_id (student_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
```

#### 3. Create Attendance Table
```sql
CREATE TABLE attendance (
    id INT NOT NULL AUTO_INCREMENT,
    student_id INT NOT NULL,
    date DATE NOT NULL,
    time TIME NOT NULL,
    status VARCHAR(20) DEFAULT 'present',
    marked_by VARCHAR(50) DEFAULT 'face_recognition',
    confidence_score FLOAT DEFAULT NULL,
    notes TEXT DEFAULT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (id),
    UNIQUE KEY unique_attendance (student_id, date),
    FOREIGN KEY (student_id) REFERENCES students(id) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
```

#### 4. Create Face Training Data Table
```sql
CREATE TABLE face_training_data (
    id INT NOT NULL AUTO_INCREMENT,
    student_id INT NOT NULL,
    image_path VARCHAR(255) NOT NULL,
    training_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    is_used_in_training TINYINT(1) DEFAULT 1,
    PRIMARY KEY (id),
    FOREIGN KEY (student_id) REFERENCES students(id) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
```

#### 5. Insert Admin User
```sql
INSERT INTO users (username, email, password_hash, full_name, role) 
VALUES ('admin', 'admin@attendance.local', 'pbkdf2:sha256:600000$salt$hash', 'System Administrator', 'admin');
```

### Common Mistakes

❌ **Importing without selecting database first**
- Always click on "attendance_system" before importing

❌ **Database doesn't exist**
- Create the database manually first

❌ **Wrong collation**
- Use `utf8mb4_unicode_ci`

❌ **File encoding issues**
- Make sure SQL file is saved as UTF-8

### Still Not Working?

Try this simple test:

1. Open phpMyAdmin
2. Select `attendance_system` database
3. Click SQL tab
4. Run this simple command:
   ```sql
   CREATE TABLE test (id INT);
   ```
5. If this works, the issue is with the SQL file
6. If this fails, there's a MySQL/phpMyAdmin configuration issue

### Check MySQL Version

Some SQL syntax might not work on older MySQL versions:

1. In phpMyAdmin, look at the top right
2. You should see MySQL version (e.g., "MySQL 8.0.30")
3. If version is below 5.7, you might need to modify the SQL

### Need More Help?

1. Check XAMPP Control Panel - MySQL should be green/running
2. Check phpMyAdmin error messages carefully
3. Try restarting MySQL in XAMPP
4. Check MySQL error logs in XAMPP
