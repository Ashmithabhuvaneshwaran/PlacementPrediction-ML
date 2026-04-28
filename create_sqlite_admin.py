#!/usr/bin/env python
"""
Create Admin Account in SQLite Database
"""

from app import app, db, Admin

def create_admin():
    """Create admin account in SQLite"""
    with app.app_context():
        try:
            # Check if admin already exists
            existing_admin = Admin.query.filter_by(username='admin').first()
            if existing_admin:
                print("⚠️  Admin 'admin' already exists in SQLite!")
                print(f"   Email: {existing_admin.email}")
                
                # Ask if user wants to reset password
                response = input("\n❓ Do you want to reset the admin password? (yes/no): ").strip().lower()
                if response in ['yes', 'y']:
                    new_password = input("Enter new password: ").strip()
                    if new_password:
                        existing_admin.set_password(new_password)
                        db.session.commit()
                        print(f"✅ Admin password updated!")
                        print(f"   Username: admin")
                        print(f"   New Password: {new_password}")
                    else:
                        print("❌ Password cannot be empty!")
                return False
            
            # Create new admin
            admin = Admin(
                username='admin',
                email='admin@placement.com'
            )
            admin.set_password('Admin@123')
            
            db.session.add(admin)
            db.session.commit()
            
            print("=" * 60)
            print("✅ Admin account created successfully!")
            print("=" * 60)
            print(f"📝 Username: admin")
            print(f"🔑 Password: Admin@123")
            print(f"📧 Email: admin@placement.com")
            print("=" * 60)
            print("\n🌐 Now you can login at: http://localhost:5000/admin-login")
            print("=" * 60)
            
            return True
            
        except Exception as e:
            print(f"❌ Error creating admin account: {e}")
            import traceback
            traceback.print_exc()
            return False

if __name__ == '__main__':
    print("=" * 60)
    print("SQLite Admin Account Creation")
    print("=" * 60)
    create_admin()
