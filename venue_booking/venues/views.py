from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db.models import Q
from .models import Venue, Category, Review, Booking
from .forms import VenueForm, ReviewForm, BookingForm, ContactForm

def index(request):
    categories = Category.objects.all()
    return render(request, 'index.html', {'categories': categories})

def venue_list(request, category_id=None):
    if category_id:
        venues = Venue.objects.filter(category_id=category_id)
        category = get_object_or_404(Category, id=category_id)
    else:
        venues = Venue.objects.all()
        category = None
    return render(request, 'venue_list.html', {'venues': venues, 'category': category})

def venue_detail(request, venue_id):
    venue = get_object_or_404(Venue, id=venue_id)
    return render(request, 'venue_detail.html', {'venue': venue})

@login_required
def dashboard(request):
    user_venues = Venue.objects.filter(owner=request.user)
    return render(request, 'dashboard.html', {'user_venues': user_venues})

class VenueCreateView(LoginRequiredMixin, CreateView):
    model = Venue
    form_class = VenueForm
    template_name = 'venue_form.html'
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class VenueUpdateView(LoginRequiredMixin, UpdateView):
    model = Venue
    form_class = VenueForm
    template_name = 'venue_form.html'
    success_url = reverse_lazy('dashboard')

class VenueDeleteView(LoginRequiredMixin, DeleteView):
    model = Venue
    success_url = reverse_lazy('dashboard')
    template_name = 'venue_confirm_delete.html'

def add_review(request, venue_id):
    venue = get_object_or_404(Venue, id=venue_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.venue = venue
            review.user = request.user
            review.save()
            return redirect('venue_detail', venue_id=venue.id)
    else:
        form = ReviewForm()
    return render(request, 'add_review.html', {'form': form, 'venue': venue})

def book_venue(request, venue_id):
    venue = get_object_or_404(Venue, id=venue_id)
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.venue = venue
            booking.user = request.user
            booking.save()
            return redirect('booking_confirmation', booking_id=booking.id)
    else:
        form = BookingForm()
    return render(request, 'booking.html', {'form': form, 'venue': venue})

def search_venues(request):
    query = request.GET.get('q')
    venues = Venue.objects.filter(
        Q(name__icontains=query) |
        Q(description__icontains=query) |
        Q(category__name__icontains=query)
    ).distinct()
    return render(request, 'search_results.html', {'venues': venues, 'query': query})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process the form data (e.g., send email)
            return redirect('contact_success')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})