FROM python:3.9  

WORKDIR /app  # рабочая директория 

COPY app.py ./  # копирует файлы

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt  # запуск команды с установкой зависимостей из текстовика с флагом без кэша

EXPOSE 5000  # выставляем порт

CMD ["python","app.py"]  # запуск скрипта внутри внутри контейнера


