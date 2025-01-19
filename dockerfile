FROM python:3.12

WORKDIR /DjangoProject

COPY . .

RUN pip install django

EXPOSE 3000

CMD [ "python", "manage.py", "runserver", "0.0.0.0:3000" ]