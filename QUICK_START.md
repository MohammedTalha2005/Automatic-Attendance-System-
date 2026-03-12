# Quick Start: Database Setup with phpMyAdmin

## 🚀 Super Quick Setup (5 Minutes)

### Step 1: Install XAMPP
1. Download: https://www.apachefriends.org/
2. Install (keep default settings)
3. Open XAMPP Control Panel
4. Click **Start** for Apache
5. Click **Start** for MySQL

### Step 2: Setup Database
1. Open browser → `http://localhost/phpmyadmin`
2. Click **Import** tab
3. Click **Choose File** → Select `database_setup.sql`
4. Click **Go** button
5. ✅ Done! Database is ready

### Step 3: Configure App
1. Copy `.env.example` to `.env`
2. Edit `.env`:
   ```env
   DB_HOST=localhost
   DB_PORT=3306
   DB_NAME=attendance_system
   DB_USER=root
   DB_PASSWORD=
   ```
   (Leave password empty for default XAMPP)


### 🚀 Running the App
1.  **Open VS Code** in the project folder.
2.  Press **F5** or run `python app.py`.
3.  Access locally: `http://127.0.0.1:5001`

### 🌐 How to Share with Others
To allow others to use the system, you have two main options:

#### 1. Local Network (Same WiFi)
Anyone on your WiFi can access the system using your Computer's IP address:
- **Link**: `http://192.168.31.200:5001`
- **Tip**: Ensure your Windows Firewall allows port **5001**. If it doesn't work, try turning off the Firewall temporarily to test.

#### 2. Public Access (For Anyone, Anywhere)
If you want to share it with someone outside your building, the fastest way is using **Ngrok**:
1.  Download and install [Ngrok](https://ngrok.com/).
2.  Run this command in a terminal: `ngrok http 5001`
3.  Share the provided `.ngrok-free.app` link.

---
*Note: The system is currently optimized for local/LAN use with a MySQL backend (XAMPP).*

Login: `admin` / `admin`

---

## 📋 Default XAMPP Settings

- **phpMyAdmin URL:** http://localhost/phpmyadmin
- **MySQL Username:** root
- **MySQL Password:** (empty/blank)
- **MySQL Port:** 3306

---

## ⚠️ Common Issues

### MySQL won't start?
- Another MySQL is running → Stop it in Windows Services
- Port 3306 is busy → Change to 3307 in XAMPP config

### Can't access phpMyAdmin?
- Make sure Apache is running (green in XAMPP)
- Try: http://127.0.0.1/phpmyadmin

### Database connection error in app?
- Check MySQL is running in XAMPP
- Verify `.env` has correct settings
- Password should be empty for default XAMPP

---

## 📖 Need More Help?

See detailed guide: **[PHPMYADMIN_SETUP.md](PHPMYADMIN_SETUP.md)**
