# Build & Deployment Instructions

## Local Development Setup

### 1. Clone/Navigate to Project
```bash
cd "d:\placement prediction ml\Placement_Prediction_Using_Machine-Learning"
```

### 2. Create Virtual Environment
```bash
python -m venv venv
```

### 3. Activate Virtual Environment

**Windows (PowerShell):**
```powershell
.\venv\Scripts\Activate.ps1
```

**Windows (Command Prompt):**
```cmd
venv\Scripts\activate.bat
```

**macOS/Linux:**
```bash
source venv/bin/activate
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

### 5. Train ML Models
```bash
python retrain_models.py
```

Expected output:
```
Training Placement Prediction Model...
Placement Model Accuracy: 0.93+
Placement Model saved successfully!

Training Salary Prediction Model...
Salary Model Accuracy: 0.65+
Salary Model saved successfully!
```

### 6. Verify Models
```bash
python verify_models.py
```

### 7. Run Locally
```bash
python app.py
```

Visit: `http://127.0.0.1:5000`

### 8. Run with Gunicorn (Production Mode)
```bash
gunicorn app:app
```

Visit: `http://127.0.0.1:8000`

---

## Files Generated During Build

After running the above, these files are created automatically:

| File | Size | Purpose |
|------|------|---------|
| `model.pkl` | ~5-10 MB | Placement prediction model |
| `model1.pkl` | ~5-10 MB | Salary prediction model |
| `placement_users.db` | Variable | SQLite database (users & predictions) |

These are in `.gitignore` and NOT committed to GitHub. They are regenerated during deployment.

---

## Project Structure

```
Placement_Prediction_Using_Machine-Learning/
│
├── Core Application Files
│   ├── app.py                      # Flask application
│   ├── config.py                   # Configuration settings
│   ├── auth.py                     # Authentication module
│   ├── models.py                   # Database models
│
├── ML & Data Processing
│   ├── retrain_models.py           # Train ML models
│   ├── verify_models.py            # Verify trained models
│   ├── Placement_Prediction_data.csv
│   └── Salary_prediction_data.csv
│
├── Web Interface
│   ├── templates/                  # HTML files
│   │   ├── home.html
│   │   ├── index.html
│   │   ├── output.html
│   │   ├── login.html
│   │   ├── register.html
│   │   ├── user_dashboard.html
│   │   ├── admin_dashboard.html
│   │   └── ...
│   │
│   └── static/                     # CSS & Images
│       ├── css/
│       │   ├── style.css
│       │   └── ...
│       └── images/
│
├── Deployment Configuration
│   ├── requirements.txt            # Python dependencies
│   ├── render.yaml                 # Render configuration
│   ├── Procfile                    # Heroku/alt deploy
│   ├── runtime.txt                 # Python version
│   ├── .env.example                # Environment template
│   ├── .gitignore                  # Git ignore rules
│   │
│   └── Documentation
│       ├── FINAL_README.md         # Full user guide
│       ├── DEPLOYMENT.md           # Deployment guide
│       ├── BUILD.md                # This file
│       └── TECHNICAL_REPORT.md
│
└── Generated Files (not committed)
    ├── model.pkl                   # Generated at build
    ├── model1.pkl                  # Generated at build
    ├── placement_users.db          # Generated at runtime
    └── __pycache__/                # Python cache
```

---

## Troubleshooting

### Issue: "ModuleNotFoundError: No module named 'flask'"
**Solution:**
```bash
pip install -r requirements.txt
```

### Issue: Models not found
**Solution:**
```bash
python retrain_models.py
python verify_models.py
```

### Issue: Port 5000 already in use
**Solution:**
```bash
# Windows
netstat -ano | findstr :5000
taskkill /PID <PID> /F

# macOS/Linux
lsof -i :5000
kill -9 <PID>
```

### Issue: Database locked
**Solution:**
```bash
# Delete SQLite database and restart
rm placement_users.db
python app.py
```

---

## Key Commands Summary

```bash
# Setup
pip install -r requirements.txt
python retrain_models.py

# Development
python app.py                          # Run on http://localhost:5000

# Production (like Render/Heroku)
python retrain_models.py               # Train models
gunicorn app:app                       # Start app on http://localhost:8000

# Testing
python verify_models.py                # Test ML models
```

---

## Environment Variables (Production)

Create a `.env` file based on `.env.example`:

```
SECRET_KEY=your_long_random_secret_key_here
MONGO_URI=your_mongodb_atlas_connection_string
DATABASE_URL=optional_postgres_url
FLASK_ENV=production
```

**Never commit `.env` file** — it contains secrets.

---

## Next: Deploy to Render

See `DEPLOYMENT.md` for step-by-step Render deployment guide.
