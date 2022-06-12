FROM python:3.10-slim

RUN mkdir -p /app/my_first_ml_app
COPY my_first_ml_app/ /app/my_first_ml_app
WORKDIR /app/my_first_ml_app/
RUN pip install -r requirements.txt

EXPOSE 3000
#CMD django-admin runserver 0.0.0.0:3000

CMD python manage.py runserver 0.0.0.0:3000