## Run

1. Should set `server.crt` and `server.key` in `docker-compose.yml` properly
2. `docker-compose up -d --build`
3. port open at 8443.



##	Description

你知道什么是 HTTP 吗？（你通过一般方式是打不开网站的）

Hint: The newest.



## Solution

1. Build curl with http3 - https://github.com/curl/curl/blob/master/docs/HTTP3.md
2. `./curl -v https://localhost:8443/check.php --http3 -d 'pass=1&newpass=1'`


## Flag
NUAACTF{WH4T_d0_y0u_kn0w_H334}