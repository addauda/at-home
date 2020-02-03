FROM python:3

WORKDIR /usr/src/app

COPY . .
RUN pip install --no-cache-dir -r requirements.txt

# Confirm that all files are copied
RUN ls -la ./*

EXPOSE 8000

# DB migrations
RUN python manage.py makemigrations zillowchallenge
RUN python manage.py migrate

# Zillow import
RUN python manage.py import_zillow ./data/output

# Start command
CMD ["/bin/bash", "-c", "python manage.py runserver 0.0.0.0:8000"]
