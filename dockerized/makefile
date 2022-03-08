build:
	docker build -t flask-cors-webserver:latest .

bash:
	docker run --rm -it \
           -p 60050:60050 \
           -v /data/dockerizedFlask:/app \
           --entrypoint /bin/bash \
           flask-cors-webserver:latest

run:
	docker run --rm -dit \
          -p 60050:60050 \
          -v /data/dockerizedFlask:/app \
          --restart always \
          --entrypoint /app/runDockerizedFlaskWebServerForStaticGenomeFiles.sh \
          flask-cors-webserver:latest 


ps:
	docker ps | grep "app/runDockerized" | awk '{print $$1}'

stop:
	docker stop `docker ps | grep "app/runDockerized" | awk '{print $$1}'`

