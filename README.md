# AI-Powered Fake Review Detection System

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![Flask](https://img.shields.io/badge/Flask-%E2%98%AB%EF%B8%8F-brightgreen.svg)](https://flask.palletsprojects.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/MuthukumarD2003/Ai--Fake-Review-System/graphs/commit-activity)

This project implements an AI-powered system to detect fake reviews of Android applications listed on the Google Play Store. It leverages the power of a large language model (LLM), specifically the Llama family of models accessed via an API, to analyze the content of user reviews and identify potentially inauthentic ones.

## Overview

The system consists of a Flask web application that allows users to input a Google Play Store app URL and specify the number of reviews they want to analyze. The backend then fetches these reviews, utilizes the Llama LLM to assess their authenticity, and presents a summary of the analysis, including the total number of reviews, the count of likely fake reviews, and the count of likely genuine reviews. Individual review analysis results are also provided.

## Key Features

* **Easy-to-use Web Interface:** A simple web form allows users to easily submit app URLs for analysis.
* **Google Play Store Integration:** Fetches reviews directly from the provided Google Play Store URL.
* **Llama LLM Powered Analysis:** Employs a Llama large language model (via API) to intelligently identify patterns indicative of fake reviews.
* **Detailed Analysis:** Provides a breakdown of the total reviews, the number of likely fake reviews, and the number of likely genuine reviews.
* **Individual Review Assessment:** Shows the LLM's analysis result (fake or genuine) for each reviewed comment, along with a brief explanation.
* **Adjustable Review Count:** Users can specify the number of reviews to analyze (up to a reasonable limit).

## Technologies Used

* **Python:** The primary programming language.
* **Flask:** A micro web framework for building the user interface and API endpoints.
* **`google-play-scraper`:** A library to scrape app information and reviews from the Google Play Store.
* **`requests`:** A library for making HTTP requests to interact with the LLM API.
* **Beautiful Soup (`bs4`):** Used for basic HTML parsing (though primarily for extracting the app ID).
* **Llama Large Language Model (via API):** The core AI model for analyzing review text.

## Setup and Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/MuthukumarD2003/Ai--Fake-Review-System.git](https://github.com/MuthukumarD2003/Ai--Fake-Review-System.git)
    cd Ai--Fake-Review-System
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Set the Llama API Key:**
    This project utilizes an API to access the Llama large language model. You need to obtain an API key from a provider that offers access to Llama models (e.g., Groq). Once you have the key, set it as an environment variable named `GROQ_API_KEY`.

    On Linux/macOS:
    ```bash
    export GROQ_API_KEY="your_llama_api_key_here"
    ```

    On Windows (Command Prompt):
    ```bash
    set GROQ_API_KEY="your_llama_api_key_here"
    ```

    On Windows (PowerShell):
    ```powershell
    $env:GROQ_API_KEY = "your_llama_api_key_here"
    ```

4.  **Run the Flask application:**
    ```bash
    python app.py
    ```

    This will start the development server, usually accessible at `http://127.0.0.1:5000/`.

## Usage

1.  Open your web browser and navigate to `http://127.0.0.1:5000/`.
2.  In the form, paste the URL of the Google Play Store app you want to analyze.
3.  Enter the number of reviews you want to analyze (default is 20, maximum is 100).
4.  Click the "Analyze" button.
5.  The results will be displayed on the page, showing the total reviews analyzed, the count of likely fake reviews, the count of likely genuine reviews, and the analysis for each individual review.

## Project Structure
Ai--Fake-Review-System/
├── static/
│   └── style.css         # Basic CSS for styling the web page
├── templates/
│   └── index.html        # HTML template for the main page
├── app.py                # Flask application code
├── review_analyzer.py    # Functions for fetching and analyzing reviews
├── requirements.txt      # List of Python dependencies
└── README.md             # This README file

## Disclaimer

The accuracy of fake review detection depends on the capabilities of the underlying Llama large language model and the quality of the reviews. This system provides an analysis based on patterns and indicators, but it may not be definitive.

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).

## Contributing

Contributions to this project are welcome. Please feel free to submit pull requests or open issues for any bugs or feature requests.

## Author

[MuthukumarD2003](https://github.com/MuthukumarD2003)
