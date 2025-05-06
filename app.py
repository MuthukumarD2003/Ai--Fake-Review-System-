from flask import Flask, render_template, request, jsonify
from review_analyzer import get_app_reviews, analyze_reviews
import os

app = Flask(__name__)

# Set the API key as an environment variable
os.environ["GROQ_API_KEY"] = "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"


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/analyze', methods=['POST'])
def analyze():
    app_url = request.form.get('app_url')
    review_count = int(request.form.get('review_count', 20))

    # Limit to a reasonable number
    if review_count > 100:
        review_count = 100

    # Get app reviews
    try:
        reviews = get_app_reviews(app_url, review_count)
    except Exception as e:
        return jsonify({
            'error': str(e),
            'message': 'Failed to retrieve reviews. Please check the URL and try again.'
        }), 400

    # Analyze the reviews
    analyzed_reviews = analyze_reviews(reviews)

    # Count fake and genuine reviews
    fake_count = sum(1 for review in analyzed_reviews if review['is_fake'])
    genuine_count = len(analyzed_reviews) - fake_count

    return jsonify({
        'total_reviews': len(analyzed_reviews),
        'fake_reviews': fake_count,
        'genuine_reviews': genuine_count,
        'reviews': analyzed_reviews
    })


if __name__ == '__main__':
    app.run(debug=True)