
import django
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from oscar.views import handler403, handler404, handler500
from django.conf.urls.static import static
from django.conf import settings
from django.apps import apps


# from cashondelivery.dashboard.app import application as cod_app





urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),  # > Django-2.0

    path('admin/', admin.site.urls),  # > Django-2.0

    path('', include(apps.get_app_config('oscar').urls[0])),

    # path('dashboard/cod/', include(cod_app.urls)),

]


# Prefix Oscar URLs with language codes
# urlpatterns += i18n_patterns(
#     path('', include(apps.get_app_config('oscar').urls[0])),
# )

if settings.DEBUG:
    import debug_toolbar

    # Server statics and uploaded media
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    # Allow error pages to be tested
    urlpatterns += [
        path('403', handler403, {'exception': Exception()}),
        path('404', handler404, {'exception': Exception()}),
        path('500', handler500),
        path('__debug__/', include(debug_toolbar.urls)),
    ]