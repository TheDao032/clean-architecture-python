FROM python:3.11-slim

WORKDIR /app

COPY . .

ENV POETRY_VERSION 1.6.1

RUN apt-get update && apt-get install -y curl gcc && apt-get install -y cron && apt-get clean
RUN pip install --no-cache-dir --upgrade -r requirements.txt
RUN pip install "poetry==${POETRY_VERSION}"

RUN touch /var/log/activate_scheduler.log
RUN chmod 0744 crontabs/activate-dumpuser-cron
RUN crontab crontabs/activate-dumpuser-cron

CMD cron && tail -f /var/log/activate_scheduler.log
