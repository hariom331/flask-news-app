from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

# NewsAPI endpoint and API key
NEWS_API_URL = 'https://newsapi.org/v2/top-headlines'
NEWS_API_KEY = 'ea3a77e818534ec091313f173ecaed45'

# CORS middleware to allow cross-origin requests (if needed)
@app.after_request
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = 'Origin, X-Requested-With, Content-Type, Accept'
    return response

# Proxy endpoint to fetch news from NewsAPI
@app.route('/api/news')
def get_news():
    try:
        # Extract query parameters from the client request (you can customize this based on your needs)
        country = request.args.get('country', 'in')
        category = request.args.get('category', 'general')
        page = request.args.get('page', '1')
        pageSize = request.args.get('pageSize', '5')

        # Construct the NewsAPI URL with the query parameters and API key
        url = f"{NEWS_API_URL}?country={country}&category={category}&apiKey={NEWS_API_KEY}&page={page}&pageSize={pageSize}"
        print(url)

        # Fetch data from NewsAPI
        response = requests.get(url)
        data = response.json()

        # Send the NewsAPI response back to the client
        return jsonify(data), 200
    except Exception as e:
        print('Error fetching news:', e)
        return jsonify({'error': 'Server Error'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
