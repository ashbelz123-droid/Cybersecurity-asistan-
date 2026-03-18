import requests

def basic_scan(target):
    try:
        response = requests.get(f"http://{target}", timeout=5)

        headers = response.headers
        issues = []

        if "X-Frame-Options" not in headers:
            issues.append("Missing X-Frame-Options header")

        if "Content-Security-Policy" not in headers:
            issues.append("Missing CSP header")

        return {
            "status": response.status_code,
            "issues": issues
        }

    except Exception as e:
        return {"error": str(e)}
