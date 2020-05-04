FROM python:3.8

WORKDIR /app

COPY . .

ADD https://github.com/ufoscout/docker-compose-wait/releases/download/2.7.3/wait /wait
RUN chmod +x /wait

RUN pip install -U pip
RUN pip install -r requirements.txt

ENTRYPOINT /wait && pytest --alluredir allure-results
