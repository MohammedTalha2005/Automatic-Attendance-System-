import os
from flask import Flask
from models import db
from config import config
from dotenv import load_dotenv

load_dotenv()

def test_db():
    app = Flask(__name__)
    app.config.from_object(config['development'])
    db.init_app(app)
    
    with app.app_context():
        try:
            print(f"Connecting to: {app.config['SQLALCHEMY_DATABASE_URI']}")
            # Try a simple query
            db.session.execute(db.text('SELECT 1'))
            print("Successfully connected to database!")
            
            print("Verifying tables...")
            from sqlalchemy import inspect
            inspector = inspect(db.engine)
            tables = inspector.get_table_names()
            print(f"Tables found: {tables}")
            
            # Check for students table specifically
            if 'students' in tables:
                columns = [c['name'] for c in inspector.get_columns('students')]
                print(f"Columns in 'students': {columns}")
            
            if 'attendance' in tables:
                columns = [c['name'] for c in inspector.get_columns('attendance')]
                print(f"Columns in 'attendance': {columns}")
                
        except Exception as e:
            print("\n!!! DATABASE ERROR !!!")
            print(str(e))
            import traceback
            traceback.print_exc()

if __name__ == '__main__':
    test_db()
