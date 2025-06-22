# Assignment 4 Submission - Wikipedia Outline API

## API Endpoint Information

**Current Local URL:** `http://localhost:8000/api/outline?country=CountryName`

**For Assignment Submission (Public URL):** 
You need to deploy to get a public URL. Choose one option below.

## Deployment Options for Public URL

### Option 1: Render.com (Recommended - 5 minutes)
1. Go to [render.com](https://render.com) and sign up
2. Click "New +" → "Web Service"
3. Connect your GitHub repository
4. Use these settings:
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `uvicorn Assignment4:app --host 0.0.0.0 --port $PORT`
   - **Environment:** Python 3.9

### Option 2: Railway.app (Alternative - 3 minutes)
1. Go to [railway.app](https://railway.app) and sign up
2. Click "New Project" → "Deploy from GitHub repo"
3. Select your repository
4. Railway will auto-detect it's a Python app

## Your API Endpoint URL (After Deployment)

After deploying, your API endpoint will be:
```
https://your-app-name.onrender.com/api/outline?country=CountryName
```
or
```
https://your-app-name.railway.app/api/outline?country=CountryName
```

## Example API Calls

- **Vanuatu:** `https://your-app-name.onrender.com/api/outline?country=Vanuatu`
- **Canada:** `https://your-app-name.onrender.com/api/outline?country=Canada`
- **Japan:** `https://your-app-name.onrender.com/api/outline?country=Japan`

## Features Implemented

✅ **FastAPI Web Framework** - Modern, fast web framework  
✅ **Wikipedia Content Fetching** - Fetches country pages from Wikipedia  
✅ **Heading Extraction** - Extracts all H1-H6 headings from pages  
✅ **Markdown Outline Generation** - Creates clean Markdown outlines  
✅ **CORS Support** - Allows requests from any origin  
✅ **Error Handling** - Proper HTTP status codes and error messages  
✅ **Query Parameter** - Uses `?country=` parameter as required  

## API Response Format

The API returns a Markdown-formatted outline like this:

```markdown
## Contents

# Vanuatu

## Etymology

## History

### Prehistory

### European contact

## Geography

### Climate

## Demographics

### Languages

## Economy

## Culture
```

## Testing Your API

1. **Local Testing:** `curl "http://localhost:8000/api/outline?country=Vanuatu"`
2. **Public Testing:** `curl "https://your-app-name.onrender.com/api/outline?country=Vanuatu"`

## Files Included

- `Assignment4.py` - Main FastAPI application
- `requirements.txt` - Python dependencies
- `README.md` - Detailed documentation
- `DEPLOYMENT.md` - Deployment instructions
- `render.yaml` - Render.com configuration
- `Procfile` - Heroku configuration
- `.gitignore` - Git ignore rules

## For Assignment Submission

**Submit this URL:** `https://your-app-name.onrender.com/api/outline?country=CountryName`

Replace `your-app-name` with the actual name from your deployment. 