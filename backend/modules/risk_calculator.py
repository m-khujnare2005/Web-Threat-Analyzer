def calculate_risk(ssl_result, headers_result):

    score = 0

    if ssl_result.get("status") == "Valid":
        score += 30

    if headers_result.get("Content-Security-Policy") == "Present":
        score += 20

    if headers_result.get("Strict-Transport-Security") == "Present":
        score += 20

    if headers_result.get("X-Frame-Options") == "Present":
        score += 15

    if headers_result.get("X-Content-Type-Options") == "Present":
        score += 15

    if score >= 80:
        risk_level = "LOW RISK"
    elif score >= 50:
        risk_level = "MEDIUM RISK"
    else:
        risk_level = "HIGH RISK"

    return {
        "score": score,
        "risk_level": risk_level
    }