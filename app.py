from flask import Flask, request, jsonify
from flask_cors import CORS
from crawler import get_estate_data  # 실제 크롤러 함수

app = Flask(__name__)
CORS(app)

@app.route('/api/search', methods=['POST'])
def search():
    data = request.get_json()
    region = data.get('region', '')
    propertyType = data.get('propertyType', '')
    results = get_estate_data(region, propertyType)
    return jsonify(results)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)