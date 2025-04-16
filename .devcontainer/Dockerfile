FROM mcr.microsoft.com/devcontainers/python:3.11

RUN apt-get update && \
    apt-get install -y curl gnupg2 lsb-release apt-transport-https && \
    curl -sL https://aka.ms/InstallAzureCLIDeb | bash && \
    curl -fsSL https://deb.nodesource.com/setup_18.x | bash - && \
    apt-get install -y nodejs && \
    npm install -g azure-functions-core-tools@4 --unsafe-perm true

RUN pip install --upgrade pip && \
    pip install torch fastapi uvicorn azure-cli azure-identity azure-ai-ml kubernetes
