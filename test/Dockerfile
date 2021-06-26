FROM python:3.8

COPY requirements.txt /test/
RUN pip install -r /test/requirements.txt

WORKDIR /test

ENV FLASK_APP=app
ENV FLASK_DEBUG=1

CMD ["flask", " run", "--host", "0.0.0.0", "--port", "5000"]