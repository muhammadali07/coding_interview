FROM python:3.8

COPY requirements.txt /app/
RUN pip install -r /app/requirements.txt

WORKDIR /app

ENV FLASK_APP=app
ENV FLASK_DEBUG=1

CMD ["flask", "run", "--host", "0.0.0.0", "--port", "5000"]