FROM python:3.9

WORKDIR /app

COPY calc.py ./

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["python","calc.py"]
