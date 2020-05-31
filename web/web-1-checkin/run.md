docker build -t web1-checkin .
docker run -d -p 8086:80 web1-checkin
