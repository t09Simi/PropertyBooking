# Django Property Booking App
This application is built using Django that allows user to view property rooms and book them. The dataset for property can be found here https://www.kaggle.com/datasets/dgomonov/new-york-city-airbnb-open-data?page=2. There is login and register page which allows to book the room.
### Database Tables
There are six tables used in this application and the data from csv is used for Property and Room table creation. There foreign key relationship is established between three tables(Property,Room and Booking). To create migrations use these two commands:

    python manage.py makemigrations
    python manage.py migrate
### Create SuperUser
This will allow you to use admin properties of Django. Create it using this command:

    python manage.py createsuperuser
We can create some random customers using Faker in parse_csv.py file. Access the http://127.0.0.1:8000/admin, the admin page by first running the server using this command:
    
    python manage.py runserver

### HTML Templates 
The home page has the listings of all the property and price associated with it. To book the room there is another book_room.html which will check if the user is a guest or a member. The login.html page will be rendered when a user tries to book the room.
### Views
The logic for filtering, sorting and searching the property has been written in general.py file. The booking.py file provides the logic for booking the room and checking if the user is a registered user or not. 
### Browser testing using Behave

### Deployment
