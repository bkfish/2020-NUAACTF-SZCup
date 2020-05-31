docker build -t web4-command-injection .
docker run -d -p 8092:80 web4-command-injection
