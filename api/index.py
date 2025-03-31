from flask import Flask, request
import requests

app = Flask(__name__)
BASE_URL = "http://74.176.192.16:8000"

@app.route('/', defaults={'path': ''}, methods=["GET", "POST", "PUT", "DELETE", "PATCH"])
@app.route('/<path:path>', methods=["GET", "POST", "PUT", "DELETE", "PATCH"])
def proxy(path):
    url = f"{BASE_URL}/{path}"
    response = requests.request(
        method=request.method,
        url=url,
        headers={key: value for (key, value) in request.headers if key != 'Host'},
        data=request.get_data(),
        cookies=request.cookies,
        allow_redirects=False
    )
    return (response.content, response.status_code, response.headers.items())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

