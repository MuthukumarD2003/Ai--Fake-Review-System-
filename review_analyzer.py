import requests
import re
import json
import os
from bs4 import BeautifulSoup
from google_play_scraper import app as app_scraper
from google_play_scraper import reviews as reviews_scraper


def get_app_reviews(app_url, count=20):
    """
    Extract reviews from a Google Play Store app URL
    """
    # Extract app ID from URL
    app_id_match = re.search(r'id=([^&]+)', app_url)
    if not app_id_match:
        raise ValueError('Invalid Google Play Store URL. Please provide a valid URL.')

    app_id = app_id_match.group(1)

    # Fetch basic app info
    app_info = app_scraper(app_id)

    # Fetch reviews
    result, continuation_token = reviews_scraper(
        app_id,
        lang='en',  # Language
        country='us',  # Country
        count=count  # Number of reviews to retrieve
    )

    # Format reviews for analysis
    formatted_reviews = []
    for review in result:
        formatted_reviews.append({
            'author': review.get('userName', 'Anonymous'),
            'text': review.get('content', ''),
            'rating': review.get('score', 0),
            'date': review.get('at', '')
        })

    return formatted_reviews


def analyze_reviews(reviews):
    """
    Analyze reviews using Llama 3.3B to detect fake reviews
    """
    api_key = os.environ.get("GROQ_API_KEY")
    if not api_key:
        raise ValueError("GROQ_API_KEY environment variable not set")

    analyzed_reviews = []

    for review in reviews:
        # Prepare the prompt for the LLM
        prompt = f"""
        You are an expert in detecting fake or suspicious reviews on app stores. 
        Analyze the following review and determine if it's likely fake or genuine.

        App review:
        Author: {review['author']}
        Rating: {review['rating']} stars
        Review: {review['text']}
        Date: {review['date']}

        Please consider the following indicators of fake reviews:
        1. Generic or vague language without specific details about the app
        2. Excessive praise without substantive feedback
        3. Unnatural language patterns or grammar issues unlike typical users
        4. Irrelevant content unrelated to app functionality
        5. Repetitive phrases or keywords that seem like SEO manipulation
        6. Extremely short reviews with 5-star ratings
        7. Patterns of posting (if this were one of many similar reviews)

        First, analyze the review considering each factor. Then, provide your conclusion on whether this review is likely fake or genuine with a brief explanation.

        Format your response as JSON with the following structure:
        {{
            "is_fake": true/false,
            "analysis": "Brief explanation (1-2 sentences) of why you think it's fake or genuine"
        }}

        Return only the JSON.
        """

        # Call the Groq API with Llama 3.3B model
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}"
        }

        payload = {
            "model": "llama-3.3-70b-versatile",
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.2
        }

        try:
            response = requests.post(
                "https://api.groq.com/openai/v1/chat/completions",
                headers=headers,
                json=payload
            )

            response_data = response.json()

            if 'choices' in response_data and len(response_data['choices']) > 0:
                llm_response = response_data['choices'][0]['message']['content']

                # Extract the JSON part from the response if needed
                json_match = re.search(r'({.*})', llm_response, re.DOTALL)
                if json_match:
                    llm_response = json_match.group(1)

                try:
                    analysis_result = json.loads(llm_response)
                    review.update(analysis_result)
                except json.JSONDecodeError:
                    # Fallback if JSON parsing fails
                    review.update({
                        "is_fake": False,
                        "analysis": "Unable to determine (analysis error). The review appears neutral."
                    })
            else:
                review.update({
                    "is_fake": False,
                    "analysis": "Unable to analyze this review due to API limitations."
                })

        except Exception as e:
            review.update({
                "is_fake": False,
                "analysis": f"Error analyzing review: {str(e)}"
            })

        analyzed_reviews.append(review)

    return analyzed_reviews