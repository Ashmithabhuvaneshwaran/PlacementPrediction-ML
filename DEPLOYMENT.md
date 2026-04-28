# Deployment Guide

This application is ready to deploy on **Render**, **Heroku**, or any platform supporting Python + Gunicorn.

## Quick Deploy to Render

### Step 1: Push to GitHub
```bash
cd "d:\placement prediction ml\Placement_Prediction_Using_Machine-Learning"
git add .
git commit -m "Add Render deployment configuration"
git push origin main
```

### Step 2: Connect to Render
1. Go to [https://render.com](https://render.com)
2. Sign up or log in
3. Click **New > Web Service**
4. Connect your GitHub repository
5. Select the branch to deploy (usually `main`)

### Step 3: Configure Settings
In the Render dashboard, set:

**Name:** `placement-prediction-ml` (or your preferred name)

**Environment:** `Python 3`

**Build Command:** (leave as default or use from render.yaml)
```
pip install -r requirements.txt && python retrain_models.py
```

**Start Command:** (leave as default or use from render.yaml)
```
gunicorn app:app
```

### Step 4: Set Environment Variables
In the Render dashboard under **Environment**:

```
SECRET_KEY=<generate-a-long-random-string>
MONGO_URI=<your-mongodb-atlas-connection-string>
DATABASE_URL=<leave-empty-for-sqlite-or-set-postgres-url>
FLASK_ENV=production
```

**Generate SECRET_KEY:**
```python
python -c "import secrets; print(secrets.token_hex(32))"
```

### Step 5: Deploy
Click **Deploy** and wait for the build to complete.

---

## Deploy to Heroku

### Step 1: Install Heroku CLI
Download from [https://devcenter.heroku.com/articles/heroku-cli](https://devcenter.heroku.com/articles/heroku-cli)

### Step 2: Login to Heroku
```bash
heroku login
```

### Step 3: Create Heroku App
```bash
heroku create your-app-name
```

### Step 4: Set Environment Variables
```bash
heroku config:set SECRET_KEY=<your-secret-key>
heroku config:set MONGO_URI=<your-mongodb-uri>
```

### Step 5: Deploy
```bash
git push heroku main
```

---

## Environment Variables Explained

| Variable | Purpose | Example |
|----------|---------|---------|
| `SECRET_KEY` | Flask session encryption | `abcd1234efgh5678...` |
| `MONGO_URI` | MongoDB Atlas connection | `mongodb+srv://user:pass@cluster.mongodb.net/db` |
| `DATABASE_URL` | PostgreSQL/MySQL (optional) | `postgresql://user:pass@host/db` |
| `FLASK_ENV` | Environment mode | `production` |
| `FLASK_DEBUG` | Debug mode (always False in prod) | `False` |

---

## File Structure for Deployment

The following files are essential:

```
Placement_Prediction_Using_Machine-Learning/
├── app.py                    ✓ Flask app entry point
├── requirements.txt          ✓ Python dependencies
├── render.yaml              ✓ Render configuration
├── Procfile                 ✓ Alternative deploy config
├── runtime.txt              ✓ Python version
├── .env.example             ✓ Template for env vars
├── .gitignore               ✓ Ignore local files
├── config.py                ✓ App configuration
├── retrain_models.py        ✓ Model training script
├── Placement_Prediction_data.csv
└── Salary_prediction_data.csv
```

**Note:** `model.pkl` and `model1.pkl` are **NOT** committed. They are generated during the build step by `retrain_models.py`.

---

## Monitoring & Troubleshooting

### View Logs on Render
```
Render Dashboard > Your App > Logs
```

### Check Build Status
Look at the "Deploy Log" in Render dashboard to see real-time build output.

### Common Issues

**1. Build fails: "ModuleNotFoundError"**
- Solution: Ensure all packages are in `requirements.txt`
- Run locally: `pip install -r requirements.txt`

**2. App crashes after deploy: "model.pkl not found"**
- Solution: The build command failed to train models
- Check the Deploy Log for errors from `retrain_models.py`

**3. "SECRET_KEY not set"**
- Solution: Add `SECRET_KEY` in Render Environment Variables

**4. MongoDB connection error**
- Solution: Verify `MONGO_URI` is correct and your IP is whitelisted in MongoDB Atlas

---

## Local Testing Before Deploy

Run these commands locally to ensure everything works:

```bash
# Install dependencies
pip install -r requirements.txt

# Train models
python retrain_models.py

# Verify models
python verify_models.py

# Start app with gunicorn (like Render will)
gunicorn app:app
```

Then visit `http://127.0.0.1:8000` in your browser.

---

## Database Persistence

### Using SQLite (Default)
- Data is stored in `placement_users.db`
- Works but data is lost if the app restarts
- Fine for testing/development

### Using PostgreSQL (Recommended for Production)
1. Create a PostgreSQL database on Render or AWS RDS
2. Set `DATABASE_URL` environment variable
3. App automatically migrates tables on startup

---

## Model Training

The `retrain_models.py` script:
- Loads `Placement_Prediction_data.csv` and `Salary_prediction_data.csv`
- Trains placement and salary prediction models
- Saves as `model.pkl` and `model1.pkl`
- Takes ~30 seconds on standard hardware

This runs automatically:
- During Render build (via `buildCommand`)
- During Heroku deploy (via `Procfile` release phase)
- Locally: `python retrain_models.py`

---

## Next Steps

1. ✅ Commit all changes: `git add . && git commit -m "Add deployment files"`
2. ✅ Push to GitHub: `git push origin main`
3. ✅ Connect to Render and deploy
4. ✅ Set environment variables
5. ✅ Test the deployed app

**Your app will be live at:** `https://placement-prediction-ml.onrender.com`

---

## Support

For issues:
- Check the **Deploy Log** in Render dashboard
- Verify environment variables are set
- Ensure data files (CSVs) are in the repository
- Test locally with: `gunicorn app:app`
