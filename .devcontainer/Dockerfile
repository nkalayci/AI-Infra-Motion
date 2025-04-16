FROM mcr.microsoft.com/azure-cli:2.58.0

RUN apt-get update && \
    apt-get install -y python3-pip && \
    pip3 install torch fastapi uvicorn kubernetes