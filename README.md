# athome

An API Zillow Listings built using DRF.

## How to run

### Docker
- Pull docker container `addauda/athome:latest` from docker hub registry
- Run container with the following command `docker run --rm -it -p 8000:8000/tcp addauda/athome:latest`
- Send requests to API as per [API documentation](documentation.md)

### Local

#### Tested on Python 3.7.4
- Run db migration with the following command `python manage.py makemigrations zillowchallenge && python manage.py migrate`
- Run custom django command to import zillow data `python manage.py import_zillow ./data/output`
- Start webserver using `python manage.py runserver`
- Send requests to API as per [API documentation](documentation.md)

# Approach to Challenge
