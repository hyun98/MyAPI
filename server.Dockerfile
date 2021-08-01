FROM python:3.9.0

RUN echo "run"

WORKDIR /home/ubuntu/

RUN git clone https://github.com/hyun98/MyAPI.git

WORKDIR /home/ubuntu/MyAPI/

RUN python -m pip install --upgrade pip

RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["bash", "-c", \
     "python manage.py collectstatic --noinput --settings=config.settings.prod&& \ 
      python manage.py migrate --settings=config.settings.prod&& \
      gunicorn config.wsgi --bind unix:/tmp/gunicorn.sock --workers=3 --timeout=300 \
      --env DJANGO_SETTINGS_MODULE=config.settings.prod"]
