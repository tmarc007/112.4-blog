from  django.urls import path
from posts import views



urlpatterns = [
    path("", views.PostListView.as_view(), name="list"), #homepage.com/posts/
    path("drafts/", views.DraftPostListView.as_view(), name="drafts"), #homepage.com/posts/drafts/
    path("<int:pk>/", views.PostDetailView.as_view(), name="detail"),
    path("new/", views.PostCreateView.as_view(), name="new"),
    path("edit/<int:pk>/", views.PostUpdateView.as_view(), name="update"), #homepage.com/posts/edit/4
    path("delete/<int:pk>/", views.PostDeleteView.as_view(), name="delete"),
    path("archived/", views.PostArchivedListView.as_view(), name="archived"),
]