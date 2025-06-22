# Deployment Guide for Wikipedia Outline API

## Quick Solution: Using ngrok (Temporary Public URL)

Since you already have the server running locally, you can make it publicly accessible using ngrok:

1. **In a new terminal window, run:**
   ```bash
   ngrok http 8000
   ```

2. **Copy the public URL** that ngrok provides (e.g., `https://abc123.ngrok.io`)

3. **Your API endpoint will be:**
   ```
   https://abc123.ngrok.io/api/outline?country=CountryName
   ```

## Permanent Deployment Options

### Option 1: Render.com (Recommended - Free)

1. Go to [render.com](https://render.com) and create a free account
2. Connect your GitHub repository
3. Create a new Web Service with these settings:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `uvicorn Assignment4:app --host 0.0.0.0 --port $PORT`
   - Environment: Python 3.9

### Option 2: Railway.app (Alternative - Free)

1. Go to [railway.app](https://railway.app) and create a free account
2. Connect your GitHub repository
3. Deploy automatically

### Option 3: Heroku (Free tier discontinued, but still works)

1. Install Heroku CLI
2. Run: `heroku create your-app-name`
3. Run: `git push heroku main`

## For Assignment Submission

Use the ngrok URL for immediate submission, or deploy to Render/Railway for a permanent solution.

**Example API calls:**
- `https://your-ngrok-url.ngrok.io/api/outline?country=Vanuatu`
- `https://your-ngrok-url.ngrok.io/api/outline?country=Canada`
- `https://your-ngrok-url.ngrok.io/api/outline?country=Japan` 