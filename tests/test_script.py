import requests
import time

def test_ports():
    # Check if ports 80 and 81 are responding
    for port in [80, 81]:
        try:
            resp = requests.get(f"http://nginx_server:{port}", timeout=5)
            if resp.status_code != 200:
                print(f"Port {port} failed: {resp.status_code}")
                return False
        except Exception as e:
            print(f"Connection error on port {port}: {e}")
            return False
    return True

def test_rate_limiting():
    # Trigger the 5r/s limit with 10 fast requests
    status_codes = []
    for _ in range(10):
        try:
            resp = requests.get("http://nginx_server:80")
            status_codes.append(resp.status_code)
        except:
            pass
    
    # Validation: Look for 429 or 503 error codes
    is_limited = any(code in [429, 503] for code in status_codes)
    if is_limited:
        print("Rate limit confirmed.")
    return is_limited

if __name__ == "__main__":
    # Run all tests and exit with correct code for CI
    if test_ports() and test_rate_limiting():
        print("All tests passed successfully!")
        exit(0)
    else:
        print("Testing failed!")
        exit(1)
