import os
from datetime import timedelta
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    """Base configuration"""
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key-change-in-production'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static', 'uploads')
    DATA_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data')
    MODEL_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'ml_models')
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB max file size
    PERMANENT_SESSION_LIFETIME = timedelta(hours=24)
    
    # Database configuration
    DB_HOST = os.environ.get('DB_HOST') or 'localhost'
    DB_PORT = os.environ.get('DB_PORT') or '3306'
    DB_USER = os.environ.get('DB_USER') or 'root'
    # Use empty string if DB_PASSWORD is set to empty in .env, otherwise use default
    DB_PASSWORD = os.environ.get('DB_PASSWORD')
    if DB_PASSWORD is None:
        DB_PASSWORD = '' # Default to empty for XAMPP if not in .env at all
        
    DB_NAME = os.environ.get('DB_NAME') or 'attendance_system'
    
    SQLALCHEMY_DATABASE_URI = f"mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    
    # Face recognition settings
    FACE_CONFIDENCE_THRESHOLD = int(os.environ.get('FACE_CONFIDENCE_THRESHOLD') or 77)
    FACE_SAMPLES_COUNT = 100
    print(f"DEBUG: FACE_SAMPLES_COUNT initialized to {FACE_SAMPLES_COUNT}")
    
    # Ensure required directories exist
    @staticmethod
    def init_app(app):
        os.makedirs(Config.UPLOAD_FOLDER, exist_ok=True)
        os.makedirs(Config.DATA_FOLDER, exist_ok=True)
        os.makedirs(Config.MODEL_FOLDER, exist_ok=True)
        os.makedirs(os.path.join(Config.UPLOAD_FOLDER, 'students'), exist_ok=True)

class DevelopmentConfig(Config):
    """Development configuration"""
    DEBUG = True

class ProductionConfig(Config):
    """Production configuration"""
    DEBUG = False
    SECRET_KEY = os.environ.get('SECRET_KEY')

config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
