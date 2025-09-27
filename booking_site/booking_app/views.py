from django.contrib import messages
from django.contrib.auth.decorators import login_required   
from django.core.exceptions import PermissionDenied, ObjectDoesNotExist, ValidationError
from django.db import IntegrityError, transaction
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse 
from django.utils import timezone
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from .forms import BookingForm
from .models import Booking, BookingStatus, Room, RoomCategory

def room_list(request):
    rooms = Room.objects.select_related("category").order_by("number")
    
    q = request.GET.get("q", "").strip()
    cat = request.GET.get("cat", "").strip()
    
    if q:
        rooms = rooms.filter(number__icontains=q)
    if cat: 
        rooms = rooms.filter(category__id=cat)
    
    categories = RoomCategory.objects.filter(is_active=True).order_by("name")
    ctx = {
        "rooms": rooms,
        "categories": categories,   
        "q": q,
        "cat": cat, }
    return render(request, "booking_app/room_list.html", ctx)

def room_detail(request, pk):
    room = get_object_or_404(Room.objects.select_related("category"), pk=pk)
    
    if request.method == "POST":
        if not request.user.is_authenticated:
            messages.error(request, "You need to log in to book a room.")
            return redirect(reverse("booking_app:room_detail", args=[room.pk]))
        
        instance = Booking(room=room, user=request.user)
        form = BookingForm(request.POST, instance=instance)
        
        if form.is_valid():
            try:
                with transaction.atomic():
                    form.save()
            except (ValidationError, IntegrityError) as e:
                form.add_error(None, getattr(e, "message", str(e)))
            else:
                messages.success(request, "Booking successfully created.")
                return redirect(reverse("booking_app:my_bookings")) 
    else:
        form = BookingForm()
    
    last_bookings = (
        room.bookings.select_related("user").order_by("-created_at")[:5]     # type: ignore
        )
    ctx = {
        "room": room,
        "form": form,
        "last_bookings": last_bookings,
    }
    return render(request, "booking_app/room_detail.html", ctx)

@login_required
def my_bookings(request):
    bookings = (
        Booking.objects.select_related("room", "room__category")
        .filter(user=request.user)
        .order_by("-created_at")
    )
    return render(request, "booking_app/my_bookings.html", {"bookings": bookings})

@login_required
def booking_cancel(request, pk: int):    
    booking = get_object_or_404(Booking, pk=pk, user=request.user)
    if booking.status != BookingStatus.CANCELED:
        booking.status = BookingStatus.CANCELED
        booking.save()
        messages.info(request, "Booking canceled.")
    return redirect(reverse("booking_app:my_bookings"))

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect(reverse("booking_app:room_list"))
    else:
        form = UserCreationForm()
    return render(request, "booking_app/auth/register.html", {"form": form}) 