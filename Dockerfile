FROM python:3.13-slim

WORKDIR /app 

COPY app.py /app
COPY modelo.py /app
COPY run.py /app

COPY requirements.txt .
RUN pip install -r requirements.txt

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8001"]
