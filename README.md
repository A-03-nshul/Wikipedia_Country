# Wikipedia Outline Generator API

A FastAPI web application that generates Markdown outlines from Wikipedia country pages by extracting all headings (H1-H6).

## Features

- Fetches Wikipedia pages for any country
- Extracts all headings (H1 to H6) from the page
- Generates a clean Markdown outline
- CORS enabled for cross-origin requests
- RESTful API design

## Installation

1. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application

1. Start the server:
```bash
python Assignment4.py
```

The application will start on `http://localhost:8000`

## API Usage

### Endpoint
- **URL**: `/api/outline`
- **Method**: GET
- **Query Parameter**: `country` (required)

### Example Usage

```bash
curl "http://localhost:8000/api/outline?country=Vanuatu"
```

### Example Response

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

## API Documentation

Once the server is running, you can access:
- Interactive API docs: `http://localhost:8000/docs`
- Alternative API docs: `http://localhost:8000/redoc`

## Error Handling

The API returns appropriate HTTP status codes:
- `400`: Missing or empty country parameter
- `404`: Wikipedia page not found for the country
- `500`: Server error during processing

## CORS Support

The application is configured to allow requests from any origin, making it suitable for web applications. 