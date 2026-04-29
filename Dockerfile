FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ARG SECRET_KEY
ENV SECRET_KEY=$SECRET_KEY

RUN python manage.py collectstatic --noinput

EXPOSE 8000

CMD ["gunicorn", "oc_lettings_site.wsgi:application", "--bind", "0.0.0.0:8000"]
