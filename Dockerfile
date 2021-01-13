FROM python:3.7

WORKDIR /app

COPY . /app

RUN pip3 --no-cache-dir install -r requirements.txt

EXPOSE 8080

CMD ["gunicorn", "-w" , "2", "-b", ":8080", "flask_page:app"]

