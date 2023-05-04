from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from property.forms import BookingForm
from property.models import Booking, Property

@login_required
def book_room(request, id):
    property = get_object_or_404(Property, id=id)
    if request.method == 'POST':
        form = BookingForm(request.POST)

        if form.is_valid():
            check_in = form.cleaned_data.get('check_in')
            check_out = form.cleaned_data.get('check_out')
            if check_out < check_in:
                messages.error(request, 'Check-out date cannot be earlier than check-in date.')
                return redirect('book_room', id=property.id)
            if Booking.objects.filter(property=property, check_out__gt=check_in, check_in__lt=check_out).exists():
                messages.error(request, 'The room is not available for the selected dates.')
                return redirect('book_room', id=property.id)
            booking = form.save(commit=False)
            booking.property = property
            booking.user = request.user
            booking.save()
            messages.success(request, 'The room has been booked successfully.')


        # Creating a session to store the booking details
            request.session['booking'] = {
                'property': booking.property.id,
                'check_in': booking.check_in,
                'check_out': booking.check_out,
            }
            return redirect('my_bookings')
    else:
        form = BookingForm()
    context = {'form': form, 'property': property}
    return render(request, 'property/book_room.html', context)
