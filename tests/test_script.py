import requests
import sys

def run_tests():
    # Targets for the two Nginx servers 
    # 'nginx_service' is the name we will use in Docker Compose later
    targets = [
        {"url": "http://nginx_service:80", "expected_status": 200},
        {"url": "http://nginx_service:81", "expected_status": 500}
    ]

    for target in targets:
        try:
            print(f"Testing {target['url']}...")
            response = requests.get(target['url'])
            
            # Verify the response code [cite: 20]
            if response.status_code != target['expected_status']:
                print(f"FAILED: Expected {target['expected_status']}, got {response.status_code}")
                sys.exit(1) # Exit with non-zero code if test fails [cite: 22]
            
            print(f"SUCCESS: Received status {response.status_code}")
            
        except Exception as e:
            print(f"Connection Error: {e}")
            sys.exit(1) # Exit with non-zero code on failure [cite: 22]

    print("All tests passed!")
    sys.exit(0)

if __name__ == "__main__":
    run_tests()
