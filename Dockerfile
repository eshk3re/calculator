FROM python:3.9

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

ENV PATH="/root/.local/bin:${PATH}"

EXPOSE 5000

CMD ["python","app.py"]
