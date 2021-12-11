FROM python:3.8

ENV PYTHONBUFFERED 1

RUN mkdir /code

WORKDIR /code/
COPY . /code/

RUN pip install pipenv
RUN pipenv install --system

CMD ["gunicorn", "-c", "config/gunicorn/conf.py", "--bind", ":8000", "--chdir", "docker_django", "config.wsgi:application"]