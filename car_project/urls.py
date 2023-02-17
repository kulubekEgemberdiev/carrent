from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include
from car_project import settings
from django.conf.urls.i18n import i18n_patterns
from pages.views import SendFormEmail, HomeSendFormEmail

handler404 = 'pages.views.my_404'

urlpatterns = [
    path('admin/abai', admin.site.urls),

]
urlpatterns += i18n_patterns(
    path('cars/', include('cars.urls')),
    path('users/', include('users.urls')),
    path('charges/', include('charges.urls')),
    path('agreement/', include('agreement.urls')),
    path('', include('pages.urls')),
    path('reservations/', include('reservations.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('home-send-form-email/', HomeSendFormEmail.as_view(), name='home_send_email'),
    path('send-form-email/', SendFormEmail.as_view(), name='send_email'),
    path('i18n/', include('django.conf.urls.i18n')),

    #API

    path("api-v1/", include("api_v1.urls")),
    prefix_default_language=False,
)
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
    # urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
