FROM python:3.9.16-alpine3.17

WORKDIR /app

COPY app.py ./

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

ENTRYPOINT ["python"]

CMD ["app.py"]
