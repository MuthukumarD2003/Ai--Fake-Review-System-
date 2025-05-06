document.addEventListener('DOMContentLoaded', function() {
    const analyzeForm = document.getElementById('analyzeForm');
    const loadingSection = document.getElementById('loadingSection');
    const resultsSection = document.getElementById('resultsSection');
    const totalReviews = document.getElementById('totalReviews');
    const fakeReviews = document.getElementById('fakeReviews');
    const genuineReviews = document.getElementById('genuineReviews');
    const reviewsList = document.getElementById('reviewsList');

    analyzeForm.addEventListener('submit', function(e) {
        e.preventDefault();
        
        // Show loading spinner
        loadingSection.style.display = 'block';
        resultsSection.style.display = 'none';
        
        // Get form data
        const formData = new FormData(analyzeForm);
        const appUrl = formData.get('app_url');
        const reviewCount = formData.get('review_count');
        
        // Send data to the backend
        fetch('/analyze', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
            },
            body: `app_url=${encodeURIComponent(appUrl)}&review_count=${reviewCount}`
        })
        .then(response => response.json())
        .then(data => {
            // Hide loading and show results
            loadingSection.style.display = 'none';
            resultsSection.style.display = 'block';
            
            // Update stats
            totalReviews.textContent = data.total_reviews;
            fakeReviews.textContent = data.fake_reviews;
            genuineReviews.textContent = data.genuine_reviews;
            
            // Display review analysis
            reviewsList.innerHTML = '';
            data.reviews.forEach(review => {
                const reviewDiv = document.createElement('div');
                reviewDiv.className = `review-item ${review.is_fake ? 'fake-review' : 'genuine-review'}`;
                
                reviewDiv.innerHTML = `
                    <div class="review-header">
                        <span class="review-author">${review.author}</span>
                        <span class="review-rating">Rating: ${review.rating}★</span>
                    </div>
                    <div class="review-text">${review.text}</div>
                    <div class="review-analysis">
                        <strong>${review.is_fake ? '⚠️ Potentially Fake' : '✅ Likely Genuine'}</strong>: 
                        ${review.analysis}
                    </div>
                `;
                
                reviewsList.appendChild(reviewDiv);
            });
        })
        .catch(error => {
            console.error('Error:', error);
            loadingSection.style.display = 'none';
            alert('An error occurred while analyzing the reviews. Please try again.');
        });
    });
});