FROM python:3.9-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app/todo-api

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY start.sh /start.sh
RUN chmod +x /start.sh

COPY . .

EXPOSE 8000
ENTRYPOINT ["sh", "/start.sh" ]