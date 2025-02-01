from flask import Flask, jsonify, request
import requests
from urllib.parse import urlparse
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
@app.route('/bypass', methods=['GET'])
def get_unlock_url():
    try:
        # Lấy URL từ tham số 'url' trong query string
        url = request.args.get('url')
        if not url:
            return jsonify({"error": "Missing URL parameter"}), 400

        # Phân tích URL và trích xuất phần pathname
        parsed_url = urlparse(url)
        sPathname = parsed_url.path.strip('/')

        # Tạo URL cho API với sPathname đã trích xuất
        api_url = f"https://api.rekonise.com/social-unlocks/{sPathname}/unlock"

        # Gửi yêu cầu GET tới API
        response = requests.get(api_url)
        json_data = response.json()
        key = json_data.get("url")
        if response.status_code == 200:
            return jsonify({"result": key}), 200
        else:
            return jsonify({"error": "Failed to fetch unlock URL from API"}), 500

    except Exception as e:
        return jsonify({"error": "Ngu sai link"}), 500

if __name__ == '__main__':
     app.run(debug=False, host='0.0.0.0', port=9888)
