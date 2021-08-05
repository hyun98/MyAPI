FROM python:3.9.0

RUN echo "test1"

COPY ./ /home/ubuntu/MyAPI

WORKDIR /home/ubuntu/MyAPI/

RUN apt-get upgrade && pip3 install --upgrade pip

RUN pip install -r requirements.txt

RUN pip install gunicorn

EXPOSE 8000

CMD ["bash", "-c", \
     "python manage.py collectstatic --noinput --settings=config.settings.prod&& \ 
      python manage.py makemigrations --settings=config.settings.prod&& \
      python manage.py migrate --settings=config.settings.prod&& \
      gunicorn config.wsgi --bind 0.0.0.0:8000 --workers=3 --thread=3 --timeout=150 \
      --env DJANGO_SETTINGS_MODULE=config.settings.prod"]
