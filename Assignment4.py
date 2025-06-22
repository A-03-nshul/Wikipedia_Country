from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import PlainTextResponse
import requests
from bs4 import BeautifulSoup
import re
from urllib.parse import quote

app = FastAPI(title="Wikipedia Outline Generator", description="Generate Markdown outlines from Wikipedia country pages")

# Enable CORS for all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_wikipedia_url(country_name):
    """Get the Wikipedia URL for a given country name"""
    # Search for the country page
    search_url = f"https://en.wikipedia.org/w/api.php"
    params = {
        "action": "query",
        "format": "json",
        "list": "search",
        "srsearch": country_name,
        "srlimit": 1
    }
    
    try:
        response = requests.get(search_url, params=params)
        response.raise_for_status()
        data = response.json()
        
        if data["query"]["search"]:
            page_title = data["query"]["search"][0]["title"]
            # Convert title to URL format
            url_title = quote(page_title.replace(" ", "_"))
            return f"https://en.wikipedia.org/wiki/{url_title}"
        else:
            return None
    except Exception as e:
        print(f"Error searching for country: {e}")
        return None

def extract_headings(html_content):
    """Extract all headings (H1-H6) from HTML content"""
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Find all headings
    headings = []
    for heading in soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6']):
        # Skip certain headings that are not part of the main content
        if heading.get('id') in ['mw-content-text', 'mw-navigation', 'mw-page-base']:
            continue
            
        # Skip navigation and table of contents elements
        if heading.get('id') in ['toc', 'mw-toc-heading']:
            continue
            
        # Skip headings that are part of navigation or sidebars
        parent = heading.parent
        while parent:
            if parent.get('id') in ['mw-navigation', 'mw-panel', 'mw-head', 'mw-footer']:
                continue
            if 'navigation' in parent.get('class', []) or 'sidebar' in parent.get('class', []):
                continue
            parent = parent.parent
            
        # Get the heading text
        text = heading.get_text(strip=True)
        if text:  # Only include non-empty headings
            # Skip common navigation and TOC headings
            skip_texts = ['Contents', 'Navigation menu', 'Tools', 'Languages', 'Print/export']
            if any(skip_text.lower() in text.lower() for skip_text in skip_texts):
                continue
                
            level = int(heading.name[1])  # Extract number from h1, h2, etc.
            headings.append((level, text))
    
    return headings

def generate_markdown_outline(headings, country_name):
    """Generate Markdown outline from headings"""
    if not headings:
        return f"## Contents\n\n# {country_name}\n\nNo headings found on the Wikipedia page."
    
    outline = "## Contents\n\n"
    outline += f"# {country_name}\n\n"
    
    for level, text in headings:
        # Skip the main title if it's already the country name
        if level == 1 and text.lower() == country_name.lower():
            continue
            
        # Skip empty or very short headings
        if len(text.strip()) < 2:
            continue
            
        # Skip "Contents" heading since we already have it
        if text.lower() == "contents":
            continue
            
        # Add appropriate number of # symbols
        outline += "#" * level + " " + text + "\n\n"
    
    return outline

@app.get("/api/outline")
async def get_outline(country: str):
    """
    Generate a Markdown outline from a Wikipedia country page
    
    Args:
        country (str): The name of the country to generate an outline for
        
    Returns:
        PlainTextResponse: Markdown-formatted outline
    """
    if not country or country.strip() == "":
        raise HTTPException(status_code=400, detail="Country parameter is required")
    
    country = country.strip()
    
    # Get Wikipedia URL
    wiki_url = get_wikipedia_url(country)
    if not wiki_url:
        raise HTTPException(status_code=404, detail=f"Could not find Wikipedia page for '{country}'")
    
    try:
        # Fetch the Wikipedia page
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(wiki_url, headers=headers)
        response.raise_for_status()
        
        # Extract headings
        headings = extract_headings(response.text)
        
        # Generate markdown outline
        outline = generate_markdown_outline(headings, country)
        
        return PlainTextResponse(content=outline, media_type="text/plain")
        
    except requests.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Error fetching Wikipedia page: {str(e)}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing page: {str(e)}")

@app.get("/")
async def root():
    """Root endpoint with usage instructions"""
    return {
        "message": "Wikipedia Outline Generator API",
        "usage": "GET /api/outline?country=CountryName",
        "example": "GET /api/outline?country=Vanuatu"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
