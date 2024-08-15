from django.contrib import admin
from django.urls import include, path
from users import views

urlpatterns = [
    # path("polls/", include("polls.urls")),
    # path("admin/", admin.site.urls),
    path("",include('users.urls')),
    path("addNew/",include('users.urls')),
    path("insertUser/",views.insertUser,name="insertUser"),
    path("deleteUser/<int:id>",views.deleteUser,name="deleteUser"),
    path("editUser/<int:id>",views.editUser,name="editUser"),
    path("updateUser/<int:id>",views.updateUser,name="updateUser")
]