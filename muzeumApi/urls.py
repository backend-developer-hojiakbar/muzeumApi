from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers, urlpatterns

import accounts.views
from blog import views
router = routers.DefaultRouter()
router.register('search',
                views.ExponantSearchViewSet,
                basename='search-exponant')
router.register("", accounts.views.UserViewSet)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('blog.urls')),
    path('accounts/', include('accounts.urls')),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls'))
]
app_name = 'blog'
if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += router.urls