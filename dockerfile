FROM python:3.10

ENV PYTHONUNBUFFERED=1
RUN mkdir /app
WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . /app

EXPOSE 8000

CMD ["python" "manage.py" "runserver"]