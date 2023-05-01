FROM python:3.9

# Install supervisor
RUN apt-get update && apt-get install -y supervisor

RUN mkdir app

RUN cd app

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

ARG OPENAI_API_KEY
ENV OPENAI_API_KEY=${OPENAI_API_KEY}

ARG ELEVENLABS_API_KEY
ENV ELEVENLABS_API_KEY=${ELEVENLABS_API_KEY}

ARG CELERY_BROKER_URL
ENV CELERY_BROKER_URL=${CELERY_BROKER_URL}

ARG result_backend
ENV result_backend=${result_backend}

# RUN flask db upgrade

RUN python manage.py


EXPOSE 80

CMD bash -c "supervisord -c supervisord.conf"