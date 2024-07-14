from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('venues/', views.venue_list, name='venue_list'),
    path('venues/<int:category_id>/', views.venue_list, name='venue_list_by_category'),
    path('venue/<int:venue_id>/', views.venue_detail, name='venue_detail'),
    path('search/', views.search_venues, name='search_venues'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('venue/create/', views.VenueCreateView.as_view(), name='create_venue'),
    path('venue/<int:pk>/update/', views.VenueUpdateView.as_view(), name='update_venue'),
    path('venue/<int:pk>/delete/', views.VenueDeleteView.as_view(), name='delete_venue'),
    path('venue/<int:venue_id>/review/', views.add_review, name='add_review'),
    path('venue/<int:venue_id>/book/', views.book_venue, name='book_venue'),
    path('contact/', views.contact, name='contact'),
]