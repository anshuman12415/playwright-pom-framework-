FROM mcr.microsoft.com/playwright/python:v1.47.0-jammy

WORKDIR /app
COPY . /app

RUN apt-get update && apt-get install -y openjdk-11-jre wget unzip ffmpeg     && pip install --upgrade pip     && pip install -r requirements.txt     && wget https://github.com/allure-framework/allure2/releases/download/2.30.0/allure-2.30.0.zip     && unzip allure-2.30.0.zip -d /opt/     && ln -s /opt/allure-2.30.0/bin/allure /usr/bin/allure

CMD ["pytest", "-n", "auto", "--alluredir=reports/allure-results"]
