from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from flask_login import login_user, logout_user, login_required, current_user
from models import db, User
from werkzeug.security import generate_password_hash

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        if not username or not password:
            flash('Please fill in all fields', 'error')
            return render_template('login.html')
        
        # Check for admin credentials
        if username == 'admin' and password == 'admin':
            # Create admin user if doesn't exist
            admin = User.query.filter_by(username='admin').first()
            if not admin:
                admin = User(
                    username='admin',
                    email='admin@attendance.com',
                    first_name='Admin',
                    last_name='User'
                )
                admin.set_password('admin')
                db.session.add(admin)
                db.session.commit()
            login_user(admin)
            flash('Welcome, Admin!', 'success')
            return redirect(url_for('dashboard'))
        
        # Check database for user
        user = User.query.filter_by(username=username).first()
        
        if user and user.check_password(password):
            login_user(user, remember=True)
            flash(f'Welcome back, {user.first_name}!', 'success')
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('dashboard'))
        else:
            flash('Invalid username or password', 'error')
    
    return render_template('login.html')

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    
    if request.method == 'POST':
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        contact = request.form.get('contact')
        email = request.form.get('email')
        username = request.form.get('username')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        security_question = request.form.get('security_question')
        security_answer = request.form.get('security_answer')
        terms = request.form.get('terms')
        
        # Validation
        if not all([first_name, last_name, email, username, password, confirm_password, security_question, security_answer]):
            flash('All fields are required', 'error')
            return render_template('register.html')
        
        if password != confirm_password:
            flash('Passwords do not match', 'error')
            return render_template('register.html')
        
        if not terms:
            flash('Please agree to the terms and conditions', 'error')
            return render_template('register.html')
        
        # Check if user already exists
        if User.query.filter_by(email=email).first():
            flash('Email already registered', 'error')
            return render_template('register.html')
        
        if User.query.filter_by(username=username).first():
            flash('Username already taken', 'error')
            return render_template('register.html')
        
        # Create new user
        new_user = User(
            first_name=first_name,
            last_name=last_name,
            contact=contact,
            email=email,
            username=username,
            security_question=security_question,
            security_answer=security_answer
        )
        new_user.set_password(password)
        
        try:
            db.session.add(new_user)
            db.session.commit()
            flash('Registration successful! Please log in.', 'success')
            return redirect(url_for('auth.login'))
        except Exception as e:
            db.session.rollback()
            flash('An error occurred during registration', 'error')
            print(f"Registration error: {e}")
    
    return render_template('register.html')

@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out successfully', 'success')
    return redirect(url_for('auth.login'))

@auth_bp.route('/forgot-password', methods=['GET', 'POST'])
def forgot_password():
    if request.method == 'POST':
        email = request.form.get('email')
        security_answer = request.form.get('security_answer')
        new_password = request.form.get('new_password')
        
        user = User.query.filter_by(email=email).first()
        
        if user and user.security_answer == security_answer:
            user.set_password(new_password)
            db.session.commit()
            flash('Password reset successful! Please log in.', 'success')
            return redirect(url_for('auth.login'))
        else:
            flash('Invalid email or security answer', 'error')
    
    return render_template('forgot_password.html')
