from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from modules.url_validators import validate_url
from modules.ssl_checker import check_ssl
from modules.header_checker import check_headers
from modules.whois_checker import get_whois_info
from modules.risk_calculator import calculate_risk
from modules.database import scans_collection
from datetime import datetime

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "Backend Running Successfully"

@app.route("/scan", methods=["POST"])
def scan():

    data = request.get_json()

    url = data.get("url")

    if not validate_url(url):
        return jsonify({
            "success": False,
            "message": "Invalid URL"
        })

    ssl_result = check_ssl(url)
    print(ssl_result)
    
    headers_result = check_headers(url)
    
    whois_result = get_whois_info(url)
    
    risk_result = calculate_risk(
        ssl_result,
        headers_result
    )
    
    print(risk_result)
    scan_record = {

        "url": url,

        "ssl_status": ssl_result.get("status"),

        "threat_score": risk_result.get("score"),

        "risk_level": risk_result.get("risk_level"),

        "scan_date": datetime.now()
    }

    scans_collection.insert_one(scan_record)

    return jsonify({
        "success": True,
        "message": "URL Valid",
        "url": url,
        "ssl": ssl_result,
        "headers": headers_result,
        "whois": whois_result,
        "risk": risk_result
    })
    
@app.route("/history", methods=["GET"])
def history():

    records = list(
        scans_collection.find({}, {"_id": 0})
    )

    return jsonify(records)

if __name__ == "__main__":
    app.run(debug=True)