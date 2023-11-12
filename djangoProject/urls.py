
from graphene_django.views import GraphQLView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
urlpatterns = [
    path("admin/", admin.site.urls),
    path("graphql", GraphQLView.as_view(graphiql=True)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
