FROM python:3.10

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

WORKDIR /app/to-do-app

EXPOSE 8008

RUN chmod +x /app/app.sh