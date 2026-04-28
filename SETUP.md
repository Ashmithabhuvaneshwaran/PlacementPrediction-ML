# Placement Prediction System - Complete Setup Guide

This guide will help you set up and run the complete Placement Prediction System with Admin Dashboard, MongoDB, and User Authentication.

## 📋 Prerequisites

- Python 3.8+
- MongoDB (Local or Atlas)
- Git (optional)
- pip (Python package manager)

## 🚀 Installation Steps

### Step 1: Install MongoDB

#### Option A: Local MongoDB Installation

**Windows:**
1. Download MongoDB Community Edition from: https://www.mongodb.com/try/download/community
2. Run the installer and follow the installation wizard
3. MongoDB will be installed as a Windows Service and run automatically

**Linux (Ubuntu/Debian):**
```bash
sudo apt-get update
sudo apt-get install -y mongodb
sudo systemctl start mongodb
sudo systemctl enable mongodb
```

**macOS:**
```bash
brew tap mongodb/brew
brew install mongodb-community
brew services start mongodb-community
```

#### Option B: MongoDB Atlas (Cloud)

1. Visit https://www.mongodb.com/cloud/atlas
2. Create a free account
3. Create a new cluster
4. Get your connection string (looks like: `mongodb+srv://username:password@cluster.mongodb.net/dbname`)

### Step 2: Set Up Python Environment

1. Navigate to the project directory:
```bash
cd "d:\placement prediction ml\Placement_Prediction_Using_Machine-Learning"
```

2. Create a virtual environment (if not already created):
```bash
python -m venv .venv
```

3. Activate the virtual environment:

**Windows (PowerShell):**
```powershell
.\.venv\Scripts\Activate.ps1
```

**Windows (Command Prompt):**
```cmd
.venv\Scripts\activate.bat
```

**Linux/macOS:**
```bash
source .venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Configure Environment Variables

1. Edit the `.env` file in the project root:

```env
# For Local MongoDB:
MONGO_URI=mongodb://localhost:27017/placement_prediction

# For MongoDB Atlas:
MONGO_URI=mongodb+srv://username:password@cluster.mongodb.net/placement_prediction

# Change this to a secure random string in production
SECRET_KEY=your-super-secret-key-change-this-12345

# Flask Environment
FLASK_ENV=development
FLASK_DEBUG=True
```

Replace with your actual MongoDB connection string if using MongoDB Atlas.

### Step 5: Create Initial Admin Account

The system requires at least one admin account. You can create it through the database or via the web interface.

**Option A: Create Admin via MongoDB Compass**

1. Download and install MongoDB Compass from: https://www.mongodb.com/products/compass
2. Connect to your MongoDB instance
3. Create a new database: `placement_prediction`
4. Create a new collection: `users`
5. Insert a new document for admin:

```json
{
  "username": "admin",
  "email": "admin@example.com",
  "password": "$2b$12$...",  // bcrypt hashed password
  "role": "admin",
  "created_at": {"$date": "2024-01-01T00:00:00.000Z"},
  "updated_at": {"$date": "2024-01-01T00:00:00.000Z"}
}
```

**Option B: Create Via Python Script**

Create a file `create_admin.py`:

```python
from pymongo import MongoClient
from werkzeug.security import generate_password_hash
from datetime import datetime

client = MongoClient('mongodb://localhost:27017')
db = client['placement_prediction']

admin_data = {
    'username': 'admin',
    'email': 'admin@example.com',
    'password': generate_password_hash('Admin@123'),
    'role': 'admin',
    'created_at': datetime.utcnow(),
    'updated_at': datetime.utcnow()
}

result = db.users.insert_one(admin_data)
print(f"Admin user created with ID: {result.inserted_id}")
```

Run it:
```bash
python create_admin.py
```

## ▶️ Running the Application

1. Make sure your virtual environment is activated
2. Make sure MongoDB is running
3. Navigate to the project directory
4. Run the application:

```bash
python app.py
```

The application will start on `http://localhost:5000`

## 🔐 Default Login Credentials

- **Admin Account:**
  - Username: `admin`
  - Password: `Admin@123` (or whatever you set)

## 📍 Access Points

- **Home Page:** http://localhost:5000/
- **About Page:** http://localhost:5000/about
- **Register:** http://localhost:5000/register
- **Login:** http://localhost:5000/login
- **User Dashboard:** http://localhost:5000/dashboard (requires login)
- **Admin Dashboard:** http://localhost:5000/admin (requires admin login)

## 🎯 User Features

- Register and create account
- Login with username/password
- Make placement predictions
- View prediction history
- View personal profile
- Track statistics

## ⚙️ Admin Features

- View all users
- View all predictions
- Delete users
- Delete predictions
- Create new admin accounts
- View admin activity logs
- System statistics and analytics

## 🗄️ Database Collections

The system creates the following MongoDB collections:

1. **users** - Stores user accounts
```json
{
  "_id": ObjectId,
  "username": "string",
  "email": "string",
  "password": "hashed_string",
  "role": "admin|user",
  "created_at": ISODate,
  "updated_at": ISODate
}
```

2. **predictions** - Stores placement predictions
```json
{
  "_id": ObjectId,
  "user_id": "string",
  "student_name": "string",
  "cgpa": number,
  "projects": number,
  "workshops": number,
  "mini_projects": number,
  "skills": "string",
  "communication_skills": number,
  "internship": "Yes|No",
  "hackathon": "Yes|No",
  "tw_percentage": number,
  "te_percentage": number,
  "backlogs": number,
  "placement_prediction": "Placed|Not Placed",
  "salary_prediction": number,
  "created_at": ISODate
}
```

3. **admin_logs** - Stores admin activities
```json
{
  "_id": ObjectId,
  "admin_id": "string",
  "action": "string",
  "details": "string",
  "timestamp": ISODate
}
```

## 📊 Model Files

The system requires the following ML model files:
- `model.pkl` - Placement prediction model
- `model1.pkl` - Salary prediction model

These files should be in the project root directory.

## 🔧 Troubleshooting

### MongoDB Connection Error
- Check if MongoDB is running
- Verify MONGO_URI in .env file
- For MongoDB Atlas, ensure IP is whitelisted in network settings

### Port Already in Use
The default port is 5000. To use a different port:
```python
# In app.py, change the last line:
app.run(debug=True, host='0.0.0.0', port=8000)  # Use port 8000
```

### Module Not Found Errors
```bash
# Upgrade pip
pip install --upgrade pip

# Reinstall requirements
pip install -r requirements.txt --force-reinstall
```

### Static Files Not Loading
Ensure the `static/` folder structure is correct:
```
static/
  ├── css/
  │   ├── style.css
  │   ├── style1.css
  │   └── ...
  └── images/
```

## 🚀 Deployment (Production)

For production deployment:

1. Change FLASK_ENV to `production`
2. Generate a strong SECRET_KEY:
```python
import secrets
print(secrets.token_hex(32))
```

3. Use a production WSGI server like Gunicorn:
```bash
pip install gunicorn
gunicorn app:app
```

4. Set up environment variables securely
5. Use HTTPS with SSL certificates
6. Enable MongoDB authentication
7. Set up proper database backups

## 📞 Support

For issues or questions, contact the development team or check the documentation.

## 📄 License

This project is provided as-is for educational purposes.

## ✨ Features Summary

- ✅ User Authentication & Authorization
- ✅ MongoDB Integration
- ✅ Placement Prediction (ML-based)
- ✅ Salary Prediction (ML-based)
- ✅ Admin Dashboard
- ✅ User Management
- ✅ Prediction History
- ✅ Activity Logging
- ✅ Responsive UI
- ✅ Error Handling
- ✅ Security Features (Password Hashing, Session Management)
- ✅ Pagination Support
