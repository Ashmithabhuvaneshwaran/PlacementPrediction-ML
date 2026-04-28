# 🎓 Placement Prediction System - Full Stack Web Application

A complete web application with **User Authentication**, **Admin Dashboard**, **MongoDB Integration**, and **Machine Learning** predictions for student placement success.

## ✨ Features

### User Features
- ✅ User Registration & Login
- ✅ Create Placement Predictions
- ✅ View Prediction History
- ✅ User Profile Management
- ✅ Secure Session Management
- ✅ Password Hashing with bcrypt

### Admin Features
- ✅ Comprehensive Admin Dashboard
- ✅ User Management (View, Delete)
- ✅ Prediction Management (View, Delete)
- ✅ Admin Account Creation
- ✅ Activity Logging & Audit Trail
- ✅ System Statistics & Analytics
- ✅ Pagination Support

### Technical Features
- ✅ MongoDB Database Integration
- ✅ User Authentication & Authorization
- ✅ Role-Based Access Control (RBAC)
- ✅ RESTful API Routes
- ✅ Error Handling & Logging
- ✅ Responsive Design
- ✅ Security Best Practices
- ✅ Database Indexing

## 🏗️ Project Structure

```
Placement_Prediction_Using_Machine-Learning/
├── app.py                          # Main Flask application
├── config.py                       # Configuration settings
├── models.py                       # Database models
├── auth.py                         # Authentication utilities
├── requirements.txt                # Python dependencies
├── .env                           # Environment variables
├── SETUP.md                       # Setup guide
├── README.md                      # This file
├── model.pkl                      # Placement prediction model
├── model1.pkl                     # Salary prediction model
├── Placement_Prediction_data.csv  # Training data
├── Salary_prediction_data.csv     # Salary data
│
├── templates/                     # HTML Templates
│   ├── home.html                 # Public home page
│   ├── about.html                # About page
│   ├── login.html                # Login page
│   ├── register.html             # Registration page
│   ├── index.html                # Prediction form
│   ├── output.html               # Prediction results
│   ├── user_dashboard.html       # User dashboard
│   ├── user_profile.html         # User profile
│   ├── prediction_detail.html    # Prediction details
│   ├── admin_dashboard.html      # Admin dashboard
│   ├── admin_users.html          # User management
│   ├── admin_predictions.html    # Prediction management
│   ├── admin_logs.html           # Activity logs
│   ├── create_admin.html         # Create admin
│   ├── 404.html                  # 404 error page
│   ├── 403.html                  # 403 error page
│   └── 500.html                  # 500 error page
│
├── static/                        # Static files
│   ├── css/
│   │   ├── style.css
│   │   ├── style1.css
│   │   ├── style2.css
│   │   └── style3.css
│   └── images/
│
└── Placement_Prediction.py        # Data preprocessing
```

## 🚀 Quick Start

### 1. Prerequisites
```bash
# Ensure you have Python 3.8+ and MongoDB installed
python --version
mongo --version
```

### 2. Install Dependencies
```bash
# Navigate to project directory
cd "d:\placement prediction ml\Placement_Prediction_Using_Machine-Learning"

# Activate virtual environment
# Windows (PowerShell):
.\.venv\Scripts\Activate.ps1
# Windows (CMD):
.venv\Scripts\activate.bat
# Linux/Mac:
source .venv/bin/activate

# Install packages
pip install -r requirements.txt
```

### 3. Configure MongoDB
```bash
# Start MongoDB
# Windows: MongoDB runs as a service
# Linux: sudo systemctl start mongodb
# Mac: brew services start mongodb-community

# Update .env file with your MongoDB URI
MONGO_URI=mongodb://localhost:27017/placement_prediction
```

### 4. Create Admin Account
```bash
# Option 1: Via MongoDB Compass (GUI)
# Create database: placement_prediction
# Create collection: users
# Insert admin document

# Option 2: Via Python script (see SETUP.md)
python create_admin.py
```

### 5. Run the Application
```bash
python app.py
```

Visit: `http://localhost:5000`

## 📚 Usage Guide

### For Students

1. **Register** → Create new account with email
2. **Login** → Use credentials to log in
3. **Dashboard** → View your prediction history
4. **Predict** → Fill form and submit for prediction
5. **View Results** → See placement status and salary prediction
6. **Track Progress** → Monitor multiple predictions

### For Administrators

1. **Login** → Use admin credentials
2. **Dashboard** → View system statistics
3. **Users** → Manage user accounts
4. **Predictions** → View and delete predictions
5. **Logs** → Check admin activity trail
6. **Create Admin** → Add new administrators

## 🔐 Default Credentials

| Role | Username | Password |
|------|----------|----------|
| Admin | admin | Admin@123 |

⚠️ **Change these credentials in production!**

## 📊 Database Schema

### Users Collection
```json
{
  "_id": ObjectId,
  "username": String,
  "email": String,
  "password": String (hashed),
  "role": String ("admin" or "user"),
  "created_at": DateTime,
  "updated_at": DateTime
}
```

### Predictions Collection
```json
{
  "_id": ObjectId,
  "user_id": String,
  "student_name": String,
  "cgpa": Number,
  "projects": Number,
  "workshops": Number,
  "mini_projects": Number,
  "skills": String,
  "communication_skills": Number,
  "internship": String,
  "hackathon": String,
  "tw_percentage": Number,
  "te_percentage": Number,
  "backlogs": Number,
  "placement_prediction": String,
  "salary_prediction": Number,
  "created_at": DateTime
}
```

### Admin Logs Collection
```json
{
  "_id": ObjectId,
  "admin_id": String,
  "action": String,
  "details": String,
  "timestamp": DateTime
}
```

## 🔗 API Routes

### Public Routes
```
GET  /                 - Home page
GET  /about            - About page
GET  /register         - Register page
POST /register         - Create account
GET  /login            - Login page
POST /login            - Authenticate user
```

### User Routes (requires login)
```
GET  /dashboard        - User dashboard
GET  /predict          - Prediction form
POST /predict          - Make prediction
GET  /profile          - User profile
GET  /prediction/<id>  - View prediction details
GET  /logout           - Logout
```

### Admin Routes (requires admin role)
```
GET  /admin                      - Admin dashboard
GET  /admin/users                - Manage users
GET  /admin/predictions          - Manage predictions
GET  /admin/logs                 - View activity logs
GET  /admin/create-admin         - Create admin form
POST /admin/create-admin         - Create new admin
POST /admin/delete-user/<id>     - Delete user
POST /admin/delete-prediction/<id> - Delete prediction
```

## 🛠️ Technologies Used

| Component | Technology |
|-----------|-----------|
| Backend | Python Flask |
| Database | MongoDB |
| Frontend | HTML5, CSS3, JavaScript |
| Authentication | Flask-Login, Werkzeug |
| ML Models | Scikit-Learn, Joblib |
| Data Processing | Pandas, NumPy |
| Password Hashing | bcrypt |
| Environment Variables | python-dotenv |

## 📝 Configuration

### Environment Variables (.env)
```env
# MongoDB Configuration
MONGO_URI=mongodb://localhost:27017/placement_prediction

# Flask Configuration
SECRET_KEY=your-secret-key-here
FLASK_ENV=development
FLASK_DEBUG=True
```

### Session Configuration (config.py)
```python
SESSION_COOKIE_SECURE = False  # Set True for HTTPS
SESSION_COOKIE_HTTPONLY = True
SESSION_COOKIE_SAMESITE = 'Lax'
PERMANENT_SESSION_LIFETIME = 1800  # 30 minutes
```

## 🔒 Security Features

- ✅ Password Hashing (bcrypt)
- ✅ Session Management with Security Cookies
- ✅ Role-Based Access Control
- ✅ Login Required Decorators
- ✅ CSRF Protection Ready
- ✅ Input Validation
- ✅ Error Handling
- ✅ Database Encryption Ready
- ✅ Admin Activity Logging

## 📈 Prediction Model

The system uses two ML models:

1. **Placement Prediction Model** (`model.pkl`)
   - Predicts if a student will be placed
   - Output: "Placed" or "Not Placed"

2. **Salary Prediction Model** (`model1.pkl`)
   - Predicts expected salary
   - Output: Salary amount (if placed)

Features used:
- CGPA
- Major Projects
- Workshops/Certifications
- Mini Projects
- Skills Count
- Communication Skills
- Internship Experience
- Hackathon Participation
- 12th Percentage
- 10th Percentage
- Backlogs

## 🐛 Troubleshooting

### Issue: MongoDB Connection Error
**Solution:**
```bash
# Check if MongoDB is running
# Windows: Check Services app
# Linux: sudo systemctl status mongodb
# Mac: brew services list

# Verify connection string in .env
MONGO_URI=mongodb://localhost:27017/placement_prediction
```

### Issue: Module Import Error
**Solution:**
```bash
# Upgrade pip
pip install --upgrade pip

# Reinstall requirements
pip install -r requirements.txt --force-reinstall
```

### Issue: Port Already in Use
**Solution:**
```python
# Change port in app.py
app.run(debug=True, port=8000)  # Use port 8000 instead
```

### Issue: Static Files Not Loading
**Solution:**
```
Ensure directory structure:
static/
  ├── css/
  │   └── style.css
  └── images/
```

## 🚀 Deployment

### Using Gunicorn (Production)
```bash
pip install gunicorn
gunicorn app:app --bind 0.0.0.0:5000 --workers 4
```

### Using Docker (Optional)
```dockerfile
FROM python:3.9
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:5000"]
```

## 📊 System Statistics

The admin dashboard displays:
- Total number of users
- Total predictions made
- Placement rate percentage
- Average salary (if placed)
- Recent prediction activity
- Admin activity logs

## 🎯 Future Enhancements

- [ ] Email notifications
- [ ] Data export functionality
- [ ] Advanced analytics charts
- [ ] Student internship recommendations
- [ ] Interview preparation resources
- [ ] Resume building assistance
- [ ] Mobile application
- [ ] Real-time notifications
- [ ] Advanced filtering and search
- [ ] Batch prediction upload

## 📞 Support & Documentation

For detailed setup instructions, see [SETUP.md](SETUP.md)

For API documentation and technical details, see inline code comments.

## 📄 License

This project is provided as-is for educational purposes.

## 👥 Contributors

- Development Team
- Machine Learning Engineers
- UI/UX Designers

## 🎉 Acknowledgments

Built with Python, Flask, MongoDB, and Machine Learning to help students achieve their placement goals.

---

**Ready to predict your success?** [Get Started Now](http://localhost:5000/register)

