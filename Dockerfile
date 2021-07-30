FROM python:3.9.0

RUN echo "run"

COPY ./ /home/MyAPI/

WORKDIR /home/MyAPI/

RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["bash", "-c", "python manage.py runserver 0.0.0.0:8000"]
