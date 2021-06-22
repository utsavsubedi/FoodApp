from django.urls import include, path
from . import views
import Users.views as user_views

app_name = 'food'
urlpatterns = [
    path('', views.IndexClassView.as_view(), name = 'index'),
    path('item/<int:pk>/', views.DetailClassView.as_view(), name = 'detail'),
    path( 'item/add', views.CreateItems.as_view(), name = 'add_items' ),
    path( 'item/update/<int:item_id>/', views.UpdateItems, name ='update_items' ),
    path( 'item/delete/<int:item_id>/', views.DeleteItems, name = 'delete_items' ),
    path( 'register/', user_views.UserLogin, name= 'register' ),

]