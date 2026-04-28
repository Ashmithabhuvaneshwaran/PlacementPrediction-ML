@echo off
REM Quick Render Deployment Script for Windows
REM Run this after pushing to GitHub

echo =========================================
echo PLACEMENT PREDICTION ML - RENDER DEPLOY
echo =========================================
echo.
echo ^✅ Pre-deployment checklist:
echo.
echo 1. Git preparation:
echo    git add .
echo    git commit -m "Add Render deployment configuration"
echo    git push origin main
echo.
echo 2. Render setup:
echo    - Go to https://render.com
echo    - Click "New ^> Web Service"
echo    - Connect your GitHub repository
echo.
echo 3. Configure the service:
echo    Name: placement-prediction-ml
echo    Environment: Python 3
echo    Build Command: pip install -r requirements.txt && python retrain_models.py
echo    Start Command: gunicorn app:app
echo.
echo 4. Set environment variables:
echo    SECRET_KEY=^<run 'python -c "import secrets; print(secrets.token_hex(32))'^>
echo    MONGO_URI=^<your-mongodb-uri^>
echo    FLASK_ENV=production
echo.
echo 5. Click "Create Web Service" and wait 3-5 minutes
echo.
echo =========================================
echo App will be available at:
echo https://placement-prediction-ml.onrender.com
echo =========================================
pause
