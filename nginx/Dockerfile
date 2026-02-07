# using ubuntu
FROM ubuntu:latest

# install nginx and clean cache to keep image small
RUN apt-get update && apt-get install -y nginx && \
    rm -rf /var/lib/apt/lists/*

# apply custom config and html page
COPY nginx.conf /etc/nginx/nginx.conf
COPY index.html /usr/share/nginx/html/index.html

# server listens on two ports
EXPOSE 80 81

# Start Nginx
CMD ["nginx", "-g", "daemon off;"]
