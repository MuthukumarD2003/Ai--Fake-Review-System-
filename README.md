```markdown
# AI Fake Review Detection System

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)

A web application that analyzes Google Play Store reviews using AI to detect potentially fake or suspicious reviews.

## Features

- Scrape reviews from any Google Play Store app
- Analyze reviews using Llama LLM
- Detect fake reviews based on multiple indicators
- Simple web interface with results visualization
- Configurable number of reviews to analyze

## How It Works

1. Extracts reviews from Google Play Store using `google-play-scraper`
2. Analyzes each review using Llama 3.3B model via Groq API
3. Checks for indicators of fake reviews:
   - Generic/vague language
   - Excessive praise without substance
   - Unnatural language patterns
   - Irrelevant content
   - SEO manipulation patterns
   - Extremely short 5-star reviews
4. Provides analysis results with explanations

## Installation

1. Clone the repository:
```bash
git clone https://github.com/your-username/Ai-Fake-Review-System.git
cd Ai-Fake-Review-System
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Run the Flask application:
```bash
python app.py
```

2. Open your browser to:
```
http://localhost:5000
```

3. Enter a Google Play Store app URL and number of reviews to analyze

4. View the analysis results showing genuine vs fake reviews

## Configuration

- Modify `review_count` in the web form to analyze more reviews (max 100)
- Adjust `temperature` parameter in `review_analyzer.py` for more/less strict analysis
- Change the model in `review_analyzer.py` if you want to use a different LLM

## File Structure

```
Ai-Fake-Review-System/
├── app.py                # Main Flask application
├── review_analyzer.py    # Review scraping and analysis logic
├── requirements.txt      # Python dependencies
├── static/               # Static files (CSS, JS)
│   └── ...
├── templates/            # HTML templates
│   └── index.html
└── README.md             # This file
```

## Dependencies

- Flask
- google-play-scraper
- requests
- beautifulsoup4
- python-dotenv

## Limitations

- Currently only supports Google Play Store apps
- Limited to 100 reviews per analysis
- API rate limits may apply with Groq
- Accuracy depends on the LLM's capability to detect fake reviews

## Contributing

Contributions are welcome! Please open an issue or pull request for any improvements.
