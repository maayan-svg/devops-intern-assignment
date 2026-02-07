# lightweight python base
FROM python:3.9-slim

# set working directory
WORKDIR /app

# install dependencies
RUN pip install --no-cache-dir requests

# copy test script to workdir
COPY test_script.py .

# run the verification script
CMD ["python", "test_script.py"]
