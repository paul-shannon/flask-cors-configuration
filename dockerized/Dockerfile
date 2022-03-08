FROM python
USER root
WORKDIR /app
RUN apt-get update && apt-get install -y ca-certificates
COPY serveStaticGenomeFiles.py ./
COPY requirements.txt ./
COPY runDockerizedFlaskWebServerForStaticGenomeFiles.sh /app/
ADD cert .
RUN pip install -r requirements.txt
ENTRYPOINT ["/bin/bash", "runDockerizedFlaskWebServerForStaticGenomeFiles.sh"]
