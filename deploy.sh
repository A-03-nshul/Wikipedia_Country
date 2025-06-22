#!/bin/bash

echo "🚀 Wikipedia Outline API Deployment Helper"
echo "=========================================="
echo ""

echo "📋 Files in your project:"
ls -la

echo ""
echo "🌐 Your API is currently running at:"
echo "   http://localhost:8000/api/outline?country=CountryName"
echo ""

echo "📝 For assignment submission, you need a public URL."
echo "   Choose one of these options:"
echo ""
echo "   1. Render.com (Recommended - Free):"
echo "      - Go to https://render.com"
echo "      - Sign up and create a new Web Service"
echo "      - Connect your GitHub repository"
echo "      - Build Command: pip install -r requirements.txt"
echo "      - Start Command: uvicorn Assignment4:app --host 0.0.0.0 --port \$PORT"
echo ""
echo "   2. Railway.app (Alternative - Free):"
echo "      - Go to https://railway.app"
echo "      - Sign up and create a new project"
echo "      - Connect your GitHub repository"
echo "      - Deploy automatically"
echo ""

echo "✅ Your API endpoint will be:"
echo "   https://your-app-name.onrender.com/api/outline?country=CountryName"
echo "   or"
echo "   https://your-app-name.railway.app/api/outline?country=CountryName"
echo ""

echo "🧪 Test your API with:"
echo "   curl 'https://your-app-name.onrender.com/api/outline?country=Vanuatu'" 