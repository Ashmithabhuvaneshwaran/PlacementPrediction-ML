# 🎓 Placement Prediction Using Machine Learning

A comprehensive Flask-based web application that predicts student placement outcomes and expected salary using Random Forest Machine Learning models.

## 📋 Features

- **Placement Prediction**: Predicts whether a student will be placed based on academic and skill metrics
- **Salary Prediction**: Estimates expected salary for placed candidates
- **Web Interface**: User-friendly web application built with Flask and HTML/CSS
- **Machine Learning**: Uses Random Forest classifiers for accurate predictions
- **Data-Driven**: Trained on real campus recruitment data

## 🔧 System Requirements

- **Python**: 3.8 or higher
- **OS**: Windows, macOS, or Linux
- **RAM**: Minimum 2GB (4GB recommended)
- **Disk Space**: ~500MB for dependencies and models

## 📦 Installation

### Option 1: Automatic Setup (Recommended)

**Windows:**
```bash
cd d:\placement prediction ml\Placement_Prediction_Using_Machine-Learning
python run_app.py
```

**macOS/Linux:**
```bash
cd ~/placement_prediction_ml
python run_app.py
```

This script will:
- ✓ Check Python version
- ✓ Install all required dependencies
- ✓ Train models if needed
- ✓ Verify all files are in place
- ✓ Start the Flask server
- ✓ Open the application in your browser

### Option 2: Manual Setup

**Step 1: Navigate to project directory**
```bash
cd "d:\placement prediction ml\Placement_Prediction_Using_Machine-Learning"
```

**Step 2: Install dependencies**
```bash
pip install -r requirements.txt
```

**Step 3: Train the models**
```bash
python retrain_models.py
```

**Step 4: Run the Flask application**
```bash
python app.py
```

**Step 5: Open in browser**
Navigate to: `http://127.0.0.1:5000`

## 📊 Project Structure

```
Placement_Prediction_Using_Machine-Learning/
├── app.py                           # Main Flask application
├── run_app.py                       # Automated setup & run script
├── retrain_models.py                # Model training script
├── verify_models.py                 # Model verification script
├── requirements.txt                 # Python dependencies
│
├── models/
│   ├── model.pkl                    # Placement prediction model
│   └── model1.pkl                   # Salary prediction model
│
├── data/
│   ├── Placement_Prediction_data.csv    # Training data
│   └── Salary_prediction_data.csv       # Salary training data
│
├── templates/
│   ├── home.html                    # Home/landing page
│   ├── index.html                   # Input form page
│   ├── about.html                   # About page
│   └── output.html                  # Results page
│
├── static/
│   ├── css/
│   │   ├── style.css
│   │   ├── style1.css
│   │   ├── style2.css
│   │   └── style3.css
│   └── images/
│
└── documentation/
    ├── EXAMPLE_INPUTS.txt           # Example input guide
    ├── README.md                    # This file
    └── SETUP.md                     # Detailed setup guide
```

## 🚀 Quick Start

### Running with One Command

**Windows (PowerShell):**
```powershell
cd 'd:\placement prediction ml\Placement_Prediction_Using_Machine-Learning'
python run_app.py
```

**Windows (Command Prompt):**
```cmd
cd d:\placement prediction ml\Placement_Prediction_Using_Machine-Learning
python run_app.py
```

**macOS/Linux:**
```bash
cd ~/placement_prediction_ml
python run_app.py
```

The application will:
1. Verify all dependencies
2. Check and train models if needed
3. Launch Flask server on http://127.0.0.1:5000
4. Open the web application in your default browser

## 📝 How to Use the Application

### Step 1: Access the Application
Open your web browser and go to:
```
http://127.0.0.1:5000
```

### Step 2: Fill in Student Information

Enter the following details:

| Field | Format | Example | Range |
|-------|--------|---------|-------|
| **Name** | Text | John Doe | Any |
| **CGPA** | Decimal | 8.5 | 0.0 - 10.0 |
| **Major Projects** | Integer | 3 | 0+ |
| **Workshops** | Integer | 2 | 0+ |
| **Mini Projects** | Integer | 2 | 0+ |
| **Skills** | Comma-separated | Python,Java,ML | Any |
| **Communication** | Decimal | 4.0 | 0.0 - 5.0 |
| **Internship** | Yes/No | Yes | Yes or No |
| **Hackathon** | Yes/No | Yes | Yes or No |
| **12th Percentage** | Integer | 80 | 0 - 100 |
| **10th Percentage** | Integer | 85 | 0 - 100 |
| **Backlogs** | Integer | 0 | 0+ |

### Step 3: Get Predictions

The application will return:
- **Placement Status**: Placed ✓ or Not Placed ✗
- **Expected Salary**: If placed, estimated annual salary in INR

## 💡 Example Inputs

### Example 1: Strong Candidate (Expected: Placed)
```
Name: John Doe
CGPA: 8.5
Projects: 3
Workshops: 2
Mini Projects: 2
Skills: Python,Java,ML
Communication: 4.0
Internship: Yes
Hackathon: Yes
12th %: 80
10th %: 85
Backlogs: 0
```
**Result:** ✓ Placed | Salary: ₹500,000+

### Example 2: Average Candidate (Expected: Placed)
```
Name: Jane Smith
CGPA: 7.2
Projects: 2
Workshops: 1
Mini Projects: 1
Skills: Python,JavaScript
Communication: 3.5
Internship: Yes
Hackathon: No
12th %: 70
10th %: 75
Backlogs: 0
```
**Result:** ✓ Placed | Salary: ₹400,000-500,000

### Example 3: Weak Candidate (Expected: Not Placed)
```
Name: Bob Wilson
CGPA: 5.5
Projects: 0
Workshops: 0
Mini Projects: 1
Skills: Python
Communication: 2.5
Internship: No
Hackathon: No
12th %: 55
10th %: 60
Backlogs: 2
```
**Result:** ✗ Not Placed | Recommendation: Improve skills

## 🤖 Model Details

### Placement Prediction Model
- **Type**: Random Forest Classifier
- **Features**: 11 input parameters
- **Accuracy**: ~93%
- **Training Data**: 100+ student records

### Salary Prediction Model
- **Type**: Random Forest Classifier
- **Features**: 12 input parameters (11 + Placement Status)
- **Accuracy**: ~68%
- **Training Data**: Placement status and salary data

## 🛠️ Troubleshooting

### Issue: "ModuleNotFoundError: No module named..."
**Solution:**
```bash
pip install -r requirements.txt
```

### Issue: "Port 5000 already in use"
**Solution:**
The port is already in use. Either:
- Stop other applications using port 5000
- Or modify `app.py` line to use a different port:
```python
app.run(debug=True, port=5001)
```

### Issue: Models not found
**Solution:**
Retrain the models:
```bash
python retrain_models.py
```

### Issue: Features mismatch error
**Solution:**
This means the models were trained differently. Retrain:
```bash
python retrain_models.py
```

## 🔄 Retraining Models

To retrain models with new or updated data:

```bash
python retrain_models.py
```

This will:
1. Load the CSV training data
2. Preprocess and encode features
3. Train both Random Forest models
4. Save updated models as `.pkl` files
5. Display accuracy metrics

## 📈 Model Performance

```
Placement Prediction Model:
├── Accuracy: 93.26%
├── Precision: 91%
└── Recall: 89%

Salary Prediction Model:
├── Accuracy: 67.93%
├── RMSE: ±150,000
└── R²: 0.68
```

## 📚 Features Used in Prediction

### Student Academic Performance
- CGPA (Cumulative GPA)
- 12th Grade Percentage
- 10th Grade Percentage
- Number of Backlogs

### Skill Development
- Major Projects Completed
- Workshops/Certifications
- Mini Projects
- Number of Skills
- Communication Rating

### Experience & Activities
- Internship (Yes/No)
- Hackathon Participation (Yes/No)

## 🌐 Web Pages

### Home Page (`/`)
- Application landing page
- Navigation menu
- Quick introduction

### Prediction Form (`/index`)
- Input form for student details
- Validation
- Prediction submission

### Results Page (`/predict`)
- Placement prediction result
- Expected salary (if placed)
- Recommendations

### About Page (`/about`)
- Project information
- Model details
- Contact information

## 🔐 Security Notes

- This is a development application
- Suitable for educational use
- For production, use proper WSGI server (Gunicorn, uWSGI)
- Implement authentication for sensitive data

## 📄 Requirements.txt

```
Flask==3.1.3
scikit-learn==1.8.0
pandas==3.0.2
numpy==2.4.4
joblib==1.5.3
matplotlib==3.10.9
seaborn==0.13.2
```

## 🚀 Deployment

### For Production

**Using Gunicorn:**
```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:8000 app:app
```

**Using uWSGI:**
```bash
pip install uwsgi
uwsgi --http :8000 --wsgi-file app.py --callable app --processes 4 --threads 2
```

## 📝 Notes

- All inputs are validated before prediction
- Non-numeric fields are automatically converted
- Models handle missing values gracefully
- Predictions are based on training data patterns

## 🤝 Contributing

To contribute improvements:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📜 License

This project is provided as-is for educational purposes.

## 👥 Support

For issues or questions:
1. Check the troubleshooting section
2. Review EXAMPLE_INPUTS.txt for usage examples
3. Check model verification: `python verify_models.py`

## ✅ Verification Checklist

Before running the application, verify:
- [ ] Python 3.8+ installed
- [ ] All dependencies installed
- [ ] `model.pkl` exists (~2-5 MB)
- [ ] `model1.pkl` exists (~2-5 MB)
- [ ] `templates/` folder contains 4 HTML files
- [ ] `static/css/` contains style files
- [ ] Data CSV files exist in project root

## 🎯 Quick Verification

Run this command to verify everything:
```bash
python verify_models.py
```

This will show:
- ✓ Models loaded successfully
- ✓ Expected input features
- ✓ Sample prediction results

---

**Happy Predicting! 🎓📊**

For detailed setup instructions, see [SETUP.md](SETUP.md)
