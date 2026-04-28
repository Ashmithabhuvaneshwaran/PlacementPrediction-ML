# 🎓 Placement Prediction Using Machine Learning - Complete Guide

A comprehensive Flask-based web application that predicts student placement outcomes and expected salary using Random Forest Machine Learning models.

**GitHub Repository:** https://github.com/Ashmithabhuvaneshwaran/PlacementPrediction-ML.git

---

## 📋 Table of Contents

1. [Project Overview](#project-overview)
2. [Features](#features)
3. [System Requirements](#system-requirements)
4. [Installation & Setup](#installation--setup)
5. [Project Structure](#project-structure)
6. [How to Use](#how-to-use)
7. [Input Guide](#input-guide)
8. [Model Information](#model-information)
9. [Results & Performance](#results--performance)
10. [Deployment Guide](#-deploy-on-render)
11. [Troubleshooting](#troubleshooting)
12. [Contributing](#contributing)
13. [License](#license)

---

## 🎯 Project Overview

**Placement Prediction ML** is an intelligent system designed to help:
- **Students**: Understand factors affecting placement and predict their placement chances
- **Educational Institutions**: Analyze placement trends and improve recruitment strategies
- **Recruiters**: Identify promising candidates based on comprehensive metrics

The project uses advanced **Random Forest Machine Learning algorithms** trained on real campus recruitment data to provide accurate predictions for:
- **Placement Probability**: Will the student get placed?
- **Salary Estimation**: What will be the expected salary if placed?

---

## ✨ Features

- ✅ **Accurate Placement Prediction**: 88.7% accuracy using Random Forest classifier
- ✅ **Salary Estimation**: Predicts expected salary for placed students
- ✅ **Web Interface**: User-friendly Flask-based web application
- ✅ **Real-time Predictions**: Instant results based on student profile
- ✅ **Comprehensive Analytics**: Confusion matrix, ROC curves, feature importance
- ✅ **Secure & Scalable**: Built with Flask and SQLAlchemy
- ✅ **Data-Driven**: Trained on authentic campus recruitment datasets
- ✅ **Visual Dashboard**: Performance metrics and statistics
- ✅ **User Profiles**: Track prediction history and results

---

## 🔧 System Requirements

| Requirement | Specification |
|------------|---------------|
| **Python Version** | 3.8 or higher |
| **Operating System** | Windows, macOS, or Linux |
| **RAM** | Minimum 2GB (4GB recommended) |
| **Disk Space** | ~500MB for dependencies and models |
| **Internet** | Required for initial setup (pip install) |

### Required Python Packages
```
Flask==3.0.0
Scikit-Learn==1.5.0
Pandas==2.2.0
Numpy==1.26.0
Matplotlib==3.9.0
Seaborn==0.13.0
Flask-Login==0.6.3
Flask-SQLAlchemy==3.1.1
```

---

## 📦 Installation & Setup

### **RECOMMENDED: One-Command Setup**

This is the **easiest and fastest way** to get started.

#### Windows (PowerShell):
```powershell
cd 'd:\placement prediction ml\Placement_Prediction_Using_Machine-Learning'
python run_app.py
```

#### Windows (Command Prompt):
```cmd
cd d:\placement prediction ml\Placement_Prediction_Using_Machine-Learning
python run_app.py
```

#### macOS/Linux:
```bash
cd ~/placement_prediction_ml
python run_app.py
```

**What `run_app.py` does automatically:**
- ✓ Checks Python version (3.8+)
- ✓ Verifies all required dependencies
- ✓ Installs missing packages automatically
- ✓ Checks and trains ML models if needed
- ✓ Verifies data files are present
- ✓ Validates template files
- ✓ Starts Flask development server
- ✓ Opens application in default browser
- ✓ Displays server information

---

### **MANUAL Setup (Step-by-Step)**

#### Step 1: Navigate to Project Directory
```bash
cd "d:\placement prediction ml\Placement_Prediction_Using_Machine-Learning"
```

#### Step 2: Create Virtual Environment (Recommended)
```bash
python -m venv venv
```

Activate Virtual Environment:
- **Windows (PowerShell):**
  ```powershell
  .\venv\Scripts\Activate.ps1
  ```
- **Windows (Command Prompt):**
  ```cmd
  venv\Scripts\activate.bat
  ```
- **macOS/Linux:**
  ```bash
  source venv/bin/activate
  ```

#### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

#### Step 4: Train Machine Learning Models
```bash
python retrain_models.py
```

This will:
- Load training data from CSV files
- Train placement prediction model
- Train salary prediction model
- Save models as pickle files (model.pkl, model1.pkl)

#### Step 5: Verify Models (Optional)
```bash
python verify_models.py
```

#### Step 6: Run Flask Application
```bash
python app.py
```

The server will start with output like:
```
* Running on http://127.0.0.1:5000
* Debug mode: on
```

#### Step 7: Access Application
Open your web browser and navigate to:
```
http://127.0.0.1:5000
```

#### Step 8: Stop the Server
Press `CTRL + C` in the terminal to stop the Flask server.

---

## 📁 Project Structure

```
Placement_Prediction_Using_Machine-Learning/
│
├── 📄 app.py                          # Main Flask application
├── 📄 run_app.py                      # Automated setup & run script
├── 📄 config.py                       # Configuration settings
├── 📄 models.py                       # SQLAlchemy database models
├── 📄 auth.py                         # Authentication module
├── 📄 retrain_models.py               # Model training script
├── 📄 verify_models.py                # Model verification script
├── 📄 requirements.txt                # Python dependencies
├── 📄 FINAL_README.md                 # This file
│
├── 📊 Models (Trained Machine Learning)
│   ├── model.pkl                      # Placement prediction model
│   └── model1.pkl                     # Salary prediction model
│
├── 📂 data (Training Datasets)
│   ├── Placement_Prediction_data.csv  # Campus placement data
│   └── Salary_prediction_data.csv     # Salary data
│
├── 📂 templates (HTML Pages)
│   ├── home.html                      # Landing/home page
│   ├── index.html                     # Prediction input form
│   ├── output.html                    # Results display page
│   ├── about.html                     # About page
│   ├── admin_login.html               # Admin login
│   ├── admin_dashboard.html           # Admin dashboard
│   ├── user_dashboard.html            # User dashboard
│   ├── login.html                     # User login
│   ├── register.html                  # User registration
│   ├── 403.html                       # Forbidden error page
│   ├── 404.html                       # Not found error page
│   └── 500.html                       # Server error page
│
├── 📂 static (CSS & Images)
│   ├── 📂 css/
│   │   ├── style.css                  # Main stylesheet
│   │   ├── style1.css                 # Alternative theme 1
│   │   ├── style2.css                 # Alternative theme 2
│   │   └── style3.css                 # Alternative theme 3
│   │
│   └── 📂 images/
│       ├── pl1.png                    # Screenshot 1
│       ├── pl2.png                    # Screenshot 2
│       ├── pl3.png                    # Screenshot 3
│       ├── confusion_matrix.png       # Model evaluation chart
│       ├── feature_importance.png     # Feature importance chart
│       └── roc_curve.png              # ROC curve chart
│
├── 📂 instance (Database)
│   └── placement_users.db             # SQLite database
│
└── 📂 __pycache__                      # Python cache (auto-generated)
```

---

## 🚀 How to Use the Application

### Login/Registration

**First Time Users:**
1. Click on "Register" on the home page
2. Enter email and password
3. Click "Sign Up"
4. Log in with your credentials

**Existing Users:**
1. Click "Login"
2. Enter email and password
3. Click "Sign In"

### Making a Prediction

#### Step 1: Access Prediction Page
After logging in, click on "Make Prediction" or navigate to the prediction form

#### Step 2: Fill Student Information
Enter the following details in the form:

| Field | Type | Description | Range | Example |
|-------|------|-------------|-------|---------|
| **Name** | Text | Student's full name | Any text | John Doe |
| **CGPA** | Decimal | Cumulative GPA | 0.0 - 10.0 | 8.5 |
| **Major Projects** | Integer | Number of major projects completed | 0+ | 3 |
| **Workshops/Certifications** | Integer | Certifications/workshops attended | 0+ | 2 |
| **Mini Projects** | Integer | Number of mini projects | 0+ | 2 |
| **Skills** | Text | Technical skills (comma-separated) | Any | Python,Java,ML |
| **Communication Rating** | Decimal | Communication skills rating | 0.0 - 5.0 | 4.0 |
| **Internship** | Yes/No | Did internship? | Yes/No | Yes |
| **Hackathon** | Yes/No | Participated in hackathons? | Yes/No | Yes |
| **12th Grade %** | Integer | 12th grade percentage | 0 - 100 | 80 |
| **10th Grade %** | Integer | 10th grade percentage | 0 - 100 | 85 |
| **Backlogs** | Integer | Number of academic backlogs | 0+ | 0 |

#### Step 3: Submit and Get Results
Click "Predict" button to see:
- **Placement Status**: Placed ✅ or Not Placed ❌
- **Expected Salary**: If placed, annual salary in INR
- **Confidence Score**: Probability percentage

---

## 📝 Input Guide with Examples

### Example 1: Strong Candidate (High Placement Probability)

**Input:**
```
Name: Raj Kumar
CGPA: 8.5
Major Projects: 4
Workshops/Certifications: 3
Mini Projects: 5
Skills: Python,Java,Machine Learning,Data Analytics
Communication Rating: 4.5
Internship: Yes
Hackathon: Yes
12th Percentage: 85
10th Percentage: 88
Backlogs: 0
```

**Expected Output:**
- **Status:** ✅ PLACED
- **Expected Salary:** ₹600,000 - ₹750,000 per annum
- **Confidence:** 94%

---

### Example 2: Average Candidate (Moderate Placement Probability)

**Input:**
```
Name: Priya Singh
CGPA: 7.2
Major Projects: 2
Workshops/Certifications: 1
Mini Projects: 2
Skills: Python,JavaScript
Communication Rating: 3.5
Internship: Yes
Hackathon: No
12th Percentage: 72
10th Percentage: 75
Backlogs: 0
```

**Expected Output:**
- **Status:** ✅ PLACED
- **Expected Salary:** ₹400,000 - ₹500,000 per annum
- **Confidence:** 78%

---

### Example 3: Weak Candidate (Low Placement Probability)

**Input:**
```
Name: Amit Sharma
CGPA: 5.8
Major Projects: 1
Workshops/Certifications: 0
Mini Projects: 1
Skills: Java
Communication Rating: 2.5
Internship: No
Hackathon: No
12th Percentage: 55
10th Percentage: 60
Backlogs: 2
```

**Expected Output:**
- **Status:** ❌ NOT PLACED
- **Expected Salary:** Not applicable
- **Confidence:** 45%

---

## 🤖 Model Information

### Machine Learning Models Used

#### 1. **Placement Prediction Model**
- **Algorithm:** Random Forest Classifier
- **Training Data:** 215 students
- **Features:** 11 input parameters
- **Output:** Binary (Placed/Not Placed)
- **File:** `model.pkl`

#### 2. **Salary Prediction Model**
- **Algorithm:** Random Forest Regressor
- **Training Data:** Salary records of placed students
- **Features:** 11 input parameters
- **Output:** Numeric (Salary in INR)
- **File:** `model1.pkl`

### Model Training Process

1. **Data Loading:** CSV files are loaded into Pandas DataFrames
2. **Data Cleaning:** Missing values handled, outliers removed
3. **Feature Encoding:** Categorical variables converted to numeric
4. **Feature Scaling:** Standardization using StandardScaler
5. **Train-Test Split:** 80-20 split for training and testing
6. **Model Training:** Random Forest with 100 estimators
7. **Hyperparameter Tuning:** Grid Search for optimal parameters
8. **Model Evaluation:** Performance metrics calculated
9. **Model Serialization:** Models saved as pickle files

---

## 📊 Results & Performance

### Placement Prediction Model Performance

| Metric | Value | Interpretation |
|--------|-------|-----------------|
| **Accuracy** | 88.7% | Correct predictions in 88.7% of cases |
| **Precision** | 0.93 | 93% of predicted placements are correct |
| **Recall** | 0.86 | Model catches 86% of actual placements |
| **F1-Score** | 0.90 | Strong overall balance |
| **ROC-AUC Score** | 0.94 | Excellent discrimination ability |

### Key Features Influencing Placement

**Top Contributing Factors (Ranked):**
1. **CGPA** - Academic performance is critical
2. **Internship Experience** - Hands-on experience matters
3. **Communication Skills** - Essential for interviews
4. **Workshops/Certifications** - Shows initiative
5. **10th & 12th Percentages** - Academic foundation
6. **Major Projects** - Practical experience
7. **Skills** - Technical competency
8. **Hackathon Participation** - Innovation potential

### Performance Visualizations

The application includes:
- **Confusion Matrix**: True positives, false positives, etc.
- **ROC Curve**: Trade-off between sensitivity and specificity
- **Feature Importance Chart**: Which factors matter most
- **Accuracy Distribution**: Model confidence levels

---

## 🔧 Troubleshooting

### Issue 1: Python Not Found
**Problem:** "Python is not recognized as an internal or external command"

**Solution:**
- Ensure Python 3.8+ is installed
- Add Python to PATH environment variable
- Restart your terminal
- Verify with: `python --version`

---

### Issue 2: Port 5000 Already in Use
**Problem:** "Address already in use"

**Solution:**
```bash
# Kill process using port 5000
# Windows:
netstat -ano | findstr :5000
taskkill /PID <PID> /F

# macOS/Linux:
lsof -i :5000
kill -9 <PID>
```

---

### Issue 3: Module Not Found Errors
**Problem:** "ModuleNotFoundError: No module named 'flask'"

**Solution:**
```bash
# Reinstall dependencies
pip install --upgrade pip
pip install -r requirements.txt
```

---

### Issue 4: Models Not Found
**Problem:** "model.pkl or model1.pkl not found"

**Solution:**
```bash
# Retrain models
python retrain_models.py

# Verify installation
python verify_models.py
```

---

### Issue 5: Database Issues
**Problem:** "SQLite database locked or corrupted"

**Solution:**
```bash
# Delete and recreate database
rm instance/placement_users.db  # or delete in Windows

# Restart application
python run_app.py
```

---

## 🔐 Security Features

- **Password Hashing:** bcrypt for secure password storage
- **Session Management:** Flask-Login for user sessions
- **CSRF Protection:** WTForms for form security
- **Input Validation:** Email and data validation
- **User Authentication:** Login/Register system
- **Database Security:** SQLAlchemy ORM prevents SQL injection

---

## 🚀 Deploy on Render

This project is ready for Render deployment with the included `render.yaml` blueprint.

### 1. Push the project to GitHub
Make sure the repository contains:
- `app.py`
- `requirements.txt`
- `render.yaml`
- `Placement_Prediction_data.csv`
- `Salary_prediction_data.csv`

### 2. Create a new Render Web Service
In Render, choose **New > Web Service** and connect your GitHub repository.

### 3. Use the Render settings from `render.yaml`
Render will use these settings:
- **Build Command:** `pip install -r requirements.txt && python retrain_models.py`
- **Start Command:** `gunicorn app:app`

### 4. Add environment variables
Set these in the Render dashboard:
- `SECRET_KEY` - any long random string
- `MONGO_URI` - your MongoDB Atlas connection string
- `DATABASE_URL` - optional; if omitted, the app uses local SQLite

### 5. Deploy
After the first deploy, Render will install dependencies, train the ML models, and start the Flask app through Gunicorn.

### Notes
- The ML models are generated during the Render build step, so `model.pkl` and `model1.pkl` do not need to be committed.
- If you want persistent user data, connect `DATABASE_URL` to a managed PostgreSQL database instead of the default SQLite file.

---

## 📈 Performance Optimization Tips

1. **Use High-Spec Computer:** More RAM speeds up predictions
2. **Close Background Apps:** Free up system resources
3. **Cache Models:** Models are pre-trained and cached
4. **Browser Performance:** Use modern browsers for UI
5. **Network:** Ensure stable internet for updates

---

## 🤝 Contributing

We welcome contributions! To contribute:

1. **Fork the repository** on GitHub
2. **Create a feature branch:**
   ```bash
   git checkout -b feature/your-feature
   ```
3. **Make your changes** and test thoroughly
4. **Commit with clear messages:**
   ```bash
   git commit -m "Add feature: description"
   ```
5. **Push to your branch:**
   ```bash
   git push origin feature/your-feature
   ```
6. **Create a Pull Request** with detailed description

### Areas for Contribution:
- Model improvements and optimization
- UI/UX enhancements
- New features and functionality
- Bug fixes and error handling
- Documentation improvements
- Performance optimization

---

## 📞 Support & Contact

For issues, questions, or suggestions:

- **GitHub Issues:** https://github.com/Ashmithabhuvaneshwaran/PlacementPrediction-ML/issues
- **Email:** ashmithabhuvaneshwaran@gmail.com
- **Documentation:** See README files in project root

---

## 📄 License

This project is open source and available under the **MIT License**.

You are free to:
- ✅ Use this project for educational purposes
- ✅ Modify and distribute
- ✅ Use commercially with attribution
- ✅ Create derivative works

See LICENSE file for full details.

---

## 🙏 Acknowledgments

This project was developed as an educational initiative to demonstrate:
- Machine Learning applications in real-world scenarios
- Flask web application development
- Data preprocessing and model training
- Web design and user experience
- Full-stack application development

---

## 📚 Additional Resources

- **Scikit-Learn Documentation:** https://scikit-learn.org/
- **Flask Documentation:** https://flask.palletsprojects.com/
- **Pandas Tutorial:** https://pandas.pydata.org/docs/
- **Random Forest Guide:** https://en.wikipedia.org/wiki/Random_forest
- **Machine Learning Basics:** https://developers.google.com/machine-learning/crash-course

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | April 2026 | Initial release |
| 1.1 | In Development | Enhanced UI and features |

---

## 🎯 Quick Reference Commands

```bash
# Setup and Run (One Command)
python run_app.py

# Manual Setup
python -m venv venv           # Create virtual environment
venv\Scripts\activate         # Activate (Windows)
source venv/bin/activate      # Activate (macOS/Linux)
pip install -r requirements.txt
python retrain_models.py
python app.py

# Verify Installation
python verify_models.py

# Access Application
# Open browser: http://127.0.0.1:5000

# Stop Server
# Press: CTRL + C
```

---

## 📋 Checklist Before First Use

- [ ] Python 3.8+ installed
- [ ] Repository cloned or downloaded
- [ ] All files present in project directory
- [ ] No network issues for initial pip install
- [ ] Port 5000 is available
- [ ] At least 500MB free disk space
- [ ] 2GB+ RAM available

---

**Last Updated:** April 28, 2026  
**Maintained By:** Ashmitha Bhuvaneshwaran  
**Repository:** https://github.com/Ashmithabhuvaneshwaran/PlacementPrediction-ML.git

---

## 🌟 Show Your Support

If you found this project helpful, please:
- ⭐ Star the repository on GitHub
- 📢 Share with others
- 💬 Provide feedback and suggestions
- 🔗 Contribute to the project

Thank you for using Placement Prediction ML! 🎉

