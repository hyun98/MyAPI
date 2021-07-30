FROM python:3.9.0

RUN echo "run"

WORKDIR /home/

RUN git clone https://github.com/hyun98/DRF.git

WORKDIR /home/DRF/

RUN pip install -r requirements.txt

RUN pip install gunicorn

EXPOSE 8000

CMD ["bash", "-c", "python manage.py collectstatic --noinput && \ 
                    python manage.py migrate && \
                    gunicorn config.wsgi --bind 0.0.0.0:8000"]
