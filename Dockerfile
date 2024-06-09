FROM python:3.9-slim-buster
LABEL authors="alysson"

WORKDIR /app

COPY requirements.txt .
RUN pip install pip --upgrade
RUN pip install -r requirements.txt

COPY . .
EXPOSE 8000
ENV API_URL=http://localhost:5000/make
CMD ["uvicorn", "wsgi:app", "--host", "0.0.0.0", "--port", "8000"]