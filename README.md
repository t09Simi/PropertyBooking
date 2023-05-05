# Django Property Booking App
This application is built using Django that allows user to view property rooms and book them. The dataset for property can be found here https://www.kaggle.com/datasets/dgomonov/new-york-city-airbnb-open-data?page=2. Users can login and create booking of the property and it also has dashboard for admin who can only view the statistics related to the property.
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
The home.html page has the listings of all the property and price associated with it. To book the room there is another book_room.html which will check if the user is a guest or a member. The login.html page will be rendered when a user tries to book the room. There is a dashboard which can be only used by admin to see the charts associated with property.
### Views
The logic for filtering, sorting and searching the property has been written in general.py file. The booking.py file provides the logic for booking the room and checking if the user is a registered user or not. Upon successful login the user will be able to book the room and get the confirmation for the same as seen below:

        @login_required
        def book_room(request, id):
            property = get_object_or_404(Property, id=id)
            if request.method == 'POST':
    
            check_in = request.POST['check_in']
            check_out = request.POST['check_out']
            
            booking = Booking(user = request.user,property = property,check_in=check_in,check_out=check_out)
            booking.save()
            
        # Creating a session to store the booking details
            request.session['booking'] = {
                'property': booking.property.id,
                'check_in': booking.check_in,
                'check_out': booking.check_out,
            }
            messages.success(request, 'The room has been booked successfully.')
            return HttpResponseRedirect(reverse('booking_confirmation', args=[booking.id]))
### Browser testing using Behave
To install behave use this command: Create features folder and add the scenarios in plain English and provide the suitable tests in the steps folder inside the features folder.

    pip install behave
    pip install selenium

### User details
The admin can only login to the dashboard to see the charts so the details of the admin are: username: admin and password:admin123. Registered user details are username: JohnSwan & password:May@2023 ; username: JennyMitchell & password:April@2023

### Deployment
The application is deployed on render, a cloud hosting platform. Application URL:https://property-5ud6.onrender.com