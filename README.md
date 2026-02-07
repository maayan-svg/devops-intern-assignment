# devops-intern-assignment
This project sets up an Nginx server on Ubuntu with two ports and an automated CI pipeline.

**Project Structure**
* nginx/ - Dockerfile and configs for the web server (Ports 80 & 81)

* tests/ - Python script that checks if the server is up and responding

* docker-compose.yml - Connects the server and the test runner

* .github/workflows/ci.yml - Automation that runs everything on every push

**My Work & Challenges**
1. I used Ubuntu as the base image for Nginx as requested. During the setup, I had to fix a few things:

2. Docker Syntax: The CI failed at first because it didn't recognize docker-compose: I fixed it by using the docker compose command.

4. GitHub Actions Versions: I updated the workflow to use v4 for the checkout and artifact actions to avoid errors.

5. Custom Artifacts: I added logic to create a succeeded or failed file based on the test results.

**Advanced Functional Requirements**

**1. Rate Limiting:** I added a limit of 5 requests per second to the Nginx server to prevent overload.

* **How it works:** Nginx tracks the IP of each client. If a user sends more than 5 requests in one second, the server blocks the extra requests.

* **How to change it:** In nginx/nginx.conf, find this line and update the rate value ( change 5r/s to 10r/s): 

  limit_req_zone $binary_remote_addr zone=mylimit:10m rate=**5r/s**;

**2. Extended Testing:** I updated the Python test script to verify the rate limiting:

* The script sends 10 rapid requests to the server.

* It confirms the test passed if the server blocks the excess traffic with a 429 or 503 error code.

**How to run it?**

If you have Docker installed, just run:
* docker compose up --build

