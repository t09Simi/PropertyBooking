from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from property.models import Booking, Property

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
    else:
        return render(request, 'property/book_room.html',{'property':property})

def booking_confirmation(request, id):
    booking = get_object_or_404(Booking, id=id)
    return render(request, 'property/booking_confirmation.html', {'booking': booking})

