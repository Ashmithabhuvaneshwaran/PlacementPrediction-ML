# 🚀 Render Deployment Checklist

## Pre-Deployment (Local)

- [x] Flask app configured with environment variables
  - See: [app.py](app.py#L20-L43)
  
- [x] Removed hard-coded credentials from config
  - See: [config.py](config.py#L7)
  
- [x] Added Gunicorn to dependencies
  - See: [requirements.txt](requirements.txt) (line 17)
  
- [x] Models trained and verified
  - Run: `python retrain_models.py`
  
- [x] All deployment files created:
  - ✅ [render.yaml](render.yaml) — Render configuration
  - ✅ [Procfile](Procfile) — Heroku/alt platform support
  - ✅ [runtime.txt](runtime.txt) — Python version (3.10.13)
  - ✅ [.gitignore](.gitignore) — Ignore models, cache, .env
  - ✅ [.env.example](.env.example) — Environment template
  - ✅ [DEPLOYMENT.md](DEPLOYMENT.md) — Full deployment guide
  - ✅ [BUILD.md](BUILD.md) — Build & local setup

---

## Deployment Steps

### Step 1: Prepare GitHub Repository
```bash
cd "d:\placement prediction ml\Placement_Prediction_Using_Machine-Learning"
git add .
git commit -m "Add Render deployment configuration"
git push origin main
```

### Step 2: Connect to Render
1. Go to **https://render.com**
2. Sign up / Log in
3. Click **New > Web Service**
4. Select your GitHub repository
5. Click **Connect**

### Step 3: Configure Render Service

| Setting | Value |
|---------|-------|
| **Name** | `placement-prediction-ml` |
| **Environment** | `Python 3` |
| **Build Command** | `pip install -r requirements.txt && python retrain_models.py` |
| **Start Command** | `gunicorn app:app` |
| **Plan** | Free (recommended for testing) |

### Step 4: Add Environment Variables

In Render Dashboard → **Environment**:

```
SECRET_KEY=<run: python -c "import secrets; print(secrets.token_hex(32))">
MONGO_URI=<your-mongodb-atlas-connection-string>
FLASK_ENV=production
FLASK_DEBUG=False
```

**Optional:**
```
DATABASE_URL=<your-postgres-url>  # Leave empty for SQLite
```

### Step 5: Deploy
Click **Create Web Service** and wait for deployment.

---

## Files Changed/Created

```diff
Created:
  ✅ render.yaml              — Render deployment config
  ✅ Procfile                 — Heroku/alt deploy
  ✅ runtime.txt              — Python version
  ✅ .gitignore               — Git ignore rules
  ✅ .env.example             — Env template (safe to commit)
  ✅ DEPLOYMENT.md            — Detailed deployment guide
  ✅ BUILD.md                 — Build instructions

Modified:
  ✅ app.py                   — Environment-driven config
  ✅ config.py                — Removed hard-coded secrets
  ✅ requirements.txt         — Added gunicorn==21.2.0
  ✅ FINAL_README.md          — Added deployment section
```

---

## Expected Render Build Process

```
1. Clone repository from GitHub
2. Install Python 3.10.13 (from runtime.txt)
3. Install dependencies: pip install -r requirements.txt
4. Train models: python retrain_models.py
5. Start app: gunicorn app:app
6. Service available at: https://placement-prediction-ml.onrender.com
```

**Estimated build time:** 3-5 minutes (first deploy)

---

## Testing After Deploy

1. **Check Deploy Log**
   - Render Dashboard → Your App → Deploy Log
   - Look for: "Build successful" or errors

2. **Test the App**
   - Visit: `https://placement-prediction-ml.onrender.com`
   - Expected: Home page loads

3. **Test Prediction**
   - Click "Make Prediction"
   - Fill in sample data
   - Submit and verify results

4. **Monitor Logs**
   - Render Dashboard → Logs
   - Watch for errors

---

## Troubleshooting Quick Reference

| Problem | Solution |
|---------|----------|
| "Build failed" | Check Deploy Log for specific error |
| "model.pkl not found" | `retrain_models.py` failed — check logs |
| "SECRET_KEY not set" | Add `SECRET_KEY` in Render Environment |
| "MongoDBConnectionError" | Verify `MONGO_URI` and MongoDB IP whitelist |
| "Port already in use" | Render manages ports automatically |
| "404 Not Found" | Flask app didn't start — check Deploy Log |

---

## Environment Variables

### Required
- `SECRET_KEY` — Flask session encryption (generate new one)

### Optional
- `MONGO_URI` — MongoDB Atlas connection (skip if not using)
- `DATABASE_URL` — PostgreSQL URL (uses SQLite if not set)
- `FLASK_ENV` — `production` (default)
- `FLASK_DEBUG` — `False` (default)

---

## Important Notes

✅ **Models are NOT committed to GitHub**
- They are generated during Render build by `retrain_models.py`
- See `.gitignore` for excluded files

✅ **Credentials are NOT committed**
- `.env` is in `.gitignore`
- Set actual values in Render Environment

✅ **Database will be lost on restart**
- Default SQLite is in-memory on Render free tier
- Connect PostgreSQL for persistent data

✅ **First deploy takes 3-5 minutes**
- Render installs deps and trains ML models
- Subsequent deploys are faster

---

## Next Steps

- [ ] Commit all changes: `git add . && git commit -m "Add Render deployment"`
- [ ] Push to GitHub: `git push origin main`
- [ ] Go to https://render.com
- [ ] Create new Web Service
- [ ] Set environment variables
- [ ] Deploy
- [ ] Test app at deployed URL
- [ ] Monitor logs in Render dashboard

---

## Success! 🎉

Your app will be live at: **https://placement-prediction-ml.onrender.com**

(Replace "placement-prediction-ml" with your actual service name)

For detailed deployment help, see [DEPLOYMENT.md](DEPLOYMENT.md)
