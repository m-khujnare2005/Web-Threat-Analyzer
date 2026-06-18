import requests

def check_headers(url):

    try:

        response = requests.get(url, timeout=10)

        headers = response.headers

        return {

            "Content-Security-Policy":
                "Present" if headers.get("Content-Security-Policy") else "Missing",

            "Strict-Transport-Security":
                "Present" if headers.get("Strict-Transport-Security") else "Missing",

            "X-Frame-Options":
                "Present" if headers.get("X-Frame-Options") else "Missing",

            "X-Content-Type-Options":
                "Present" if headers.get("X-Content-Type-Options") else "Missing"

        }

    except Exception as e:

        return {
            "error": str(e)
        }