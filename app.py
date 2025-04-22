
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/search', methods=['POST'])
def search():
    data = request.get_json()
    region = data.get('region', '')
    propertyType = data.get('propertyType', '')
    sample = {
        "type": propertyType,
        "contractArea": "40평",
        "actualArea": "38평",
        "salePrice": 65000,
        "rent": 250,
        "yield": round((250*12)/65000*100, 1),
        "pricePerPy": round(65000/38, 1),
        "floor": "2층/5층",
        "availableDate": "즉시",
        "agent": "샘플부동산",
        "mapLink": f"https://map.naver.com/v5/search/{region}"
    }
    return jsonify([sample])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
