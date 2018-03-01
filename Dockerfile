FROM python:3.6-alpine

# Download dependencies for building numpy/pandas
RUN apk add --update gcc g++

RUN adduser -D appuser
WORKDIR /home/appuser

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY manage.py config.py ./

ENV FLASK_APP manage.py

# The ./instance/uploads directory holds uploaded files
RUN mkdir -p ./instance/uploads

RUN chown -R appuser:appuser ./
USER appuser

CMD ["python", "manage.py"]
