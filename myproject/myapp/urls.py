from django.urls import path
from .views import BookListView,BookDetailView

urlpatterns = [
    path('api/book/',BookListView.as_view(), name='book-list'),
    path('api/book/<int:book_id>/',BookDetailView.as_view(),name='book-detail')
]


