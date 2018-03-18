FROM python:3.6-alpine

# Download dependencies for building numpy/pandas
RUN apk add --update gcc g++

RUN adduser -D appuser
WORKDIR /home/appuser

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN pip install gunicorn

COPY manage.py config.py boot.sh ./
RUN chmod +x boot.sh

# Mounting a volume has caused issues when hosting on a server because the files
# from the volume don't get the proper owner set after the image is created
COPY app/ ./app

ENV FLASK_APP manage.py

# The ./instance/uploads directory holds uploaded files
RUN mkdir -p ./instance/uploads

RUN chown -R appuser:appuser ./
USER appuser

CMD ["./boot.sh"]
