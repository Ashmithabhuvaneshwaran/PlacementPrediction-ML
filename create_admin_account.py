#!/usr/bin/env python
"""
Create Admin Account Script
Run this to create the admin account in MongoDB
"""

from app import app, mongo
from models import User
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

def create_admin():
    """Create admin account"""
    with app.app_context():
        try:
            db = mongo.db
            
            # First, clean up any bad documents with _id: None
            try:
                result = db.users.delete_many({'_id': None})
                if result.deleted_count > 0:
                    print(f"🧹 Cleaned up {result.deleted_count} bad document(s)")
            except:
                pass
            
            # Check if admin already exists
            existing_admin = db.users.find_one({'username': 'admin'})
            if existing_admin:
                print("❌ Admin account already exists!")
                print(f"   Username: {existing_admin['username']}")
                return False
            
            # Create admin user
            admin_user = User(
                username='admin',
                email='admin@example.com',
                password=None,  # Will be set by set_password
                role='admin'
            )
            
            # Set the password
            admin_user.set_password('Admin@123')
            
            # Convert to dictionary and insert
            admin_dict = admin_user.to_dict()
            result = db.users.insert_one(admin_dict)
            
            print("✅ Admin account created successfully!")
            print(f"📝 Username: admin")
            print(f"🔑 Password: Admin@123")
            print(f"📊 Role: admin")
            print(f"🆔 ID: {result.inserted_id}")
            
            return True
            
        except Exception as e:
            print(f"❌ Error creating admin account: {e}")
            import traceback
            traceback.print_exc()
            return False

if __name__ == '__main__':
    print("=" * 50)
    print("Admin Account Creation Script")
    print("=" * 50)
    create_admin()
    print("=" * 50)
