# athome

An API Zillow Listings built using DRF.

## How to run
#### Tested on Python 3.7.4 and Postman

### Using Docker
- Pull docker container `addauda/athome:latest` from docker hub registry
- Run container with the following command `docker run --rm -it -p 8000:8000/tcp addauda/athome:latest`
- Send requests to API as per [API documentation](documentation.md)

### Using Local
- Run db migration with the following command `python manage.py makemigrations zillowchallenge && python manage.py migrate`
- Run custom django command to import zillow data `python manage.py import_zillow ./data/output`
- Start webserver using `python manage.py runserver`
- Send requests to API as per [API documentation](documentation.md)

# My Approach To Challenge

### Assumptions
- I sought to establish context for the data and decided on the data being a snapshot of third-party data. Data synchronization is one-way. Fields are not updated once ingested.
- Due to the number of columns with null data, I designated the id, address, price, zipcode, state, city as required fields and the rest as optional. 

### Task Breakdown
- Data Preparation - **2hrs**
  - Verifying data types for numerical fields
  - Converting price from humanized form to numerical
  - Data conversions
- Import Script (CSV to db) - **2hrs**
- DRF Model - **40min**
- API Creation - **40min**
- Testing - **1hr**
- Dockerizing - **30min**
- Documentation & Cleanup - **1hr**

### What I Found Most Challenging
I decided to use pandas to help with data preprocessing. However, I ran into some trouble dealing with null values when mapping `NaN` values in pandas to `None` values in Django models. I went around this by writing the pandas dataframe to csv, and then reading the csv in the import script.

### Eureka Moment :O
After running my tests multiple times and coming up with empty responses. I took a deep breath and started researching. I found out that model tests used a blank database and there was an option to preserve the databse between tests.