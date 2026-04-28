#!/usr/bin/env python
"""
Fetch Users from MongoDB Database
"""

from pymongo import MongoClient
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# MongoDB Connection
MONGO_URI = os.getenv('MONGO_URI', 'mongodb+srv://ashmithabhuvaneshwaran07_db_user:5sxDJYqrcFMQOBmF@ml.2dfjelx.mongodb.net/placement_prediction?appName=ML')

try:
    print("=" * 70)
    print("FETCHING USERS FROM MONGODB DATABASE")
    print("=" * 70)
    
    # Connect to MongoDB
    client = MongoClient(MONGO_URI)
    db = client['placement_prediction']
    users_collection = db['users']
    
    print("✅ Connected to MongoDB successfully!\n")
    
    # Fetch all users
    users = list(users_collection.find())
    
    if users:
        print(f"📊 Total Users Found: {len(users)}\n")
        print("-" * 70)
        
        for idx, user in enumerate(users, 1):
            print(f"\n👤 USER #{idx}")
            print(f"   Username: {user.get('username', 'N/A')}")
            print(f"   Email: {user.get('email', 'N/A')}")
            print(f"   Role: {user.get('role', 'N/A')}")
            print(f"   Created: {user.get('created_at', 'N/A')}")
            print(f"   Password (Encrypted): {user.get('password', 'N/A')[:50]}...")
        
        print("\n" + "-" * 70)
        print("\n📝 LOGIN CREDENTIALS SUMMARY:\n")
        
        admin_users = [u for u in users if u.get('role') == 'admin']
        regular_users = [u for u in users if u.get('role') == 'user']
        
        print(f"👨‍💼 ADMIN ACCOUNTS ({len(admin_users)}):")
        for user in admin_users:
            print(f"   • Username: {user.get('username')} (Password: Use stored credentials)")
        
        print(f"\n👤 REGULAR USERS ({len(regular_users)}):")
        for user in regular_users:
            print(f"   • Username: {user.get('username')} (Password: Use stored credentials)")
        
        print("\n" + "=" * 70)
        print("✅ All user data fetched successfully!")
        print("=" * 70)
    else:
        print("❌ No users found in the database!")
    
    client.close()
    
except Exception as e:
    print(f"❌ Error connecting to MongoDB: {e}")
    import traceback
    traceback.print_exc()
