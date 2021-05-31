from django.urls import path, include

urlpatterns = [
    path('proxies/', include("apps.proxies.api.urls")),

]
