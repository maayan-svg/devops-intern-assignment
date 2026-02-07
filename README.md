# devops-intern-assignment
This project sets up an Nginx server on Ubuntu with two ports and an automated CI pipeline.

**Project Structure**
* nginx/ - Dockerfile and configs for the web server (Ports 80 & 81)

* tests/ - Python script that checks if the server is up and responding

* docker-compose.yml - Connects the server and the test runner

* .github/workflows/ci.yml - Automation that runs everything on every push

**My Work & Challenges**
1. I used Ubuntu as the base image for Nginx as requested. During the setup, I had to fix a few things:

2. Docker Syntax: The CI failed at first because it didn't recognize docker-compose. I fixed it by using the docker compose command.

3. GitHub Actions Versions: I updated the workflow to use v4 for the checkout and artifact actions to avoid errors.

4. Custom Artifacts: I added logic to create a succeeded or failed file based on the test results.

**How to run it? **
If you have Docker installed, just run:
* docker compose up --build
