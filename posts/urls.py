from  django.urls import path
from .views import PostDeleteView, PostListView, PostDetailView, PostCreateView, PostUpdateView



urlpatterns = [
    path("", PostListView.as_view(), name="list"),
    path("<int:pk>/", PostDetailView.as_view(), name="detail"),
    path("new/", PostCreateView.as_view(), name="create"),
    path("edit/<int:pk>/", PostUpdateView.as_view(), name="update"),
    path("delete/<int:pk>/", PostDeleteView.as_view(), name="delete"),
]