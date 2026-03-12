# phpMyAdmin Setup Guide for Attendance System

This guide will help you set up phpMyAdmin to manage your attendance system database instead of MySQL Workbench.

## What is phpMyAdmin?

phpMyAdmin is a free, web-based tool for managing MySQL databases. It runs in your browser and provides an easy-to-use interface for:
- Creating databases and tables
- Running SQL queries
- Viewing and editing data
- Importing/Exporting data
- Managing users and permissions

## Installation Options

### Option 1: Install with XAMPP (Recommended for Beginners)

XAMPP includes MySQL, phpMyAdmin, and Apache web server in one package.

#### Step 1: Download XAMPP
1. Go to [https://www.apachefriends.org/](https://www.apachefriends.org/)
2. Download XAMPP for Windows
3. Run the installer

#### Step 2: Install XAMPP
1. Choose installation directory (default: `C:\xampp`)
2. Select components (make sure MySQL and phpMyAdmin are checked)
3. Complete the installation

#### Step 3: Start Services
1. Open XAMPP Control Panel
2. Click **Start** next to **Apache**
3. Click **Start** next to **MySQL**
4. Both should show green "Running" status

#### Step 4: Access phpMyAdmin
1. Open your browser
2. Go to: `http://localhost/phpmyadmin`
3. You should see the phpMyAdmin interface

### Option 2: Install with WAMP (Alternative)

1. Download WAMP from [https://www.wampserver.com/](https://www.wampserver.com/)
2. Install and start WAMP
3. Access phpMyAdmin at `http://localhost/phpmyadmin`

### Option 3: Standalone phpMyAdmin (Advanced)

If you already have MySQL installed separately:

1. Download phpMyAdmin from [https://www.phpmyadmin.net/](https://www.phpmyadmin.net/)
2. Extract to your web server directory
3. Configure `config.inc.php` with your MySQL credentials
4. Access through your web server

## Setting Up the Database

### Method 1: Using the SQL File (Easiest)

1. Open phpMyAdmin in your browser: `http://localhost/phpmyadmin`
2. Click on **Import** tab at the top
3. Click **Choose File**
4. Select `database_setup.sql` from your project folder
5. Click **Go** at the bottom
6. You should see "Import has been successfully finished"

### Method 2: Manual Setup

1. Open phpMyAdmin
2. Click **New** in the left sidebar
3. Database name: `attendance_system`
4. Collation: `utf8mb4_unicode_ci`
5. Click **Create**
6. Click on the new database in the left sidebar
7. Click **SQL** tab
8. Copy and paste the contents of `database_setup.sql`
9. Click **Go**

## Configuring Your Application

### Update .env File

Make sure your `.env` file has the correct database settings:

```env
# Database Configuration
DB_HOST=localhost
DB_PORT=3306
DB_NAME=attendance_system
DB_USER=root
DB_PASSWORD=

# If you set a MySQL password in XAMPP, update DB_PASSWORD
# Otherwise leave it empty for default XAMPP installation
```

**Note:** Default XAMPP MySQL has:
- Username: `root`
- Password: (empty/blank)

## Common phpMyAdmin Tasks

### Viewing Student Data
1. Open phpMyAdmin
2. Click `attendance_system` database
3. Click `students` table
4. Click **Browse** to see all students

### Viewing Attendance Records
1. Click `attendance` table
2. Click **Browse** to see attendance records
3. Use **Search** tab to filter by date or student

### Exporting Data
1. Select your database or table
2. Click **Export** tab
3. Choose format (SQL, CSV, Excel, etc.)
4. Click **Go** to download

### Importing Data
1. Click **Import** tab
2. Choose your file (SQL, CSV, etc.)
3. Click **Go**

### Running SQL Queries
1. Click **SQL** tab
2. Type your query, for example:
   ```sql
   SELECT * FROM students WHERE department = 'Computer Science';
   ```
3. Click **Go**

### Backing Up Database
1. Click on `attendance_system` database
2. Click **Export** tab
3. Select **Quick** export method
4. Format: **SQL**
5. Click **Go**
6. Save the file in a safe location

## Troubleshooting

### Can't Access phpMyAdmin

**Problem:** Browser shows "This site can't be reached"

**Solutions:**
1. Make sure Apache and MySQL are running in XAMPP Control Panel
2. Check if you're using the correct URL: `http://localhost/phpmyadmin`
3. Try `http://127.0.0.1/phpmyadmin`

### MySQL Won't Start in XAMPP

**Problem:** MySQL shows error when starting

**Solutions:**
1. **Port Conflict:** Another program might be using port 3306
   - Open XAMPP Control Panel
   - Click **Config** next to MySQL
   - Click **my.ini**
   - Change port from 3306 to 3307
   - Update your `.env` file: `DB_PORT=3307`

2. **Previous MySQL Installation:**
   - Stop any other MySQL services
   - Open Windows Services (`services.msc`)
   - Stop any MySQL services running

### Access Denied Error

**Problem:** "Access denied for user 'root'@'localhost'"

**Solutions:**
1. Check your `.env` file has correct credentials
2. In phpMyAdmin, go to **User accounts**
3. Edit `root` user and set/reset password
4. Update password in `.env` file

### Import Failed

**Problem:** "Error importing file"

**Solutions:**
1. Check file size - phpMyAdmin has upload limits
2. Increase limits in `php.ini`:
   ```ini
   upload_max_filesize = 64M
   post_max_size = 64M
   ```
3. Restart Apache after changing `php.ini`

## Security Best Practices

### For Development (Local Machine)
- Default settings are fine for learning
- Keep XAMPP/WAMP running only when needed

### For Production (If Deploying)
1. **Set MySQL Root Password:**
   - In phpMyAdmin, go to **User accounts**
   - Click **Edit privileges** for `root`
   - Click **Change password**
   - Set a strong password
   - Update `.env` file

2. **Secure phpMyAdmin:**
   - Add authentication to phpMyAdmin folder
   - Change default URL
   - Restrict access by IP

3. **Use Environment Variables:**
   - Never commit `.env` file to Git
   - Use different credentials for production

## Useful phpMyAdmin Features

### 1. Designer View
- Visual database schema
- Click **Designer** tab to see table relationships

### 2. Search
- Search across entire database
- Click **Search** tab in database view

### 3. Operations
- Rename tables
- Copy/Move tables
- Change table collation

### 4. Structure
- View table structure
- Add/modify columns
- Create indexes

## Next Steps

1. ✅ Install XAMPP or WAMP
2. ✅ Start Apache and MySQL
3. ✅ Access phpMyAdmin
4. ✅ Import `database_setup.sql`
5. ✅ Update `.env` file
6. ✅ Run your Flask application: `python app.py`
7. ✅ Login and start using the system!

## Additional Resources

- [phpMyAdmin Documentation](https://docs.phpmyadmin.net/)
- [XAMPP Documentation](https://www.apachefriends.org/docs/)
- [MySQL Tutorial](https://www.mysqltutorial.org/)

## Need Help?

If you encounter issues:
1. Check the Troubleshooting section above
2. Verify all services are running in XAMPP Control Panel
3. Check the error logs in XAMPP (click **Logs** button)
4. Make sure your `.env` file matches your MySQL configuration
