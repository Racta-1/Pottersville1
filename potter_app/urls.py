from django.urls import path
from potter_app import views, back_views

app_name = 'pottersville_app'

urlpatterns = [
    path("album/", views.gallery, name="gallery"),
    path("dashboard/", back_views.dashboard, name="dashboard"),
    path('login/', back_views.login_view, name='login'),
   	path('register/', back_views.register, name='register'),
   	path('activate/<uidb64>/<token>/', back_views.activate, name='activate'),

   	path('add-category/', back_views.AddCategory.as_view(), name='add-category'),
   	path('view-category/', back_views.ListCategory.as_view(), name='view-category'),
   	path('update-category/<int:pk>',
   	     back_views.UpdateCategory.as_view(), name='update-category'),
   	path('delete-category/<int:pk>',
   	     back_views.DeleteCategory.as_view(), name='delete-category'),

    
    path('add-album/', back_views.AddGallery.as_view(), name='add-album'),
   	path('view-album/', back_views.ListGallery.as_view(), name='view-album'),
   	path('update-album/<int:pk>',
   	     back_views.UpdateGallery.as_view(), name='update-album'),
   	path('delete-album/<int:pk>',
   	     back_views.DeleteGallery.as_view(), name='delete-album'),

    
    path('add-event/', back_views.AddEvent.as_view(), name='add-event'),
   	path('view-events/', back_views.ListEvent.as_view(), name='view-events'),
   	path('update-event/<int:pk>',
   	     back_views.UpdateEvent.as_view(), name='update-event'),
   	path('delete-event/<int:pk>',
   	     back_views.DeleteEvent.as_view(), name='delete-event'),

    path("edit-profile/", back_views.edit_form, name="edit-profile"),
   	path("page-logout/", back_views.logout, name="page-logout"),











    # path("logout/", back_views.logout, name="logout"),
    # path("reset-password/", back_views.reset_password, name="reset-password"),
    # path("add-album/", back_views.add_album, name="add-album"),
    # path("view-album/", back_views.view_album, name="view-album"),
    # path("add-category/", back_views.add_category, name="add-category"),
    # path("view-category/", back_views.view_category, name="view-category"),
    # path("add-event/", back_views.add_event, name="add-event"),
    # path("view-events/", back_views.view_events, name="view-events"),

    
]
