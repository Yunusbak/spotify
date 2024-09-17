
# ----- URL для APIVIEW ----------#

# from django.conf import settings
# from django.conf.urls.static import static
# from django.urls import path
# from .views import AlbumView, ArtistView, SongView, ArtistDetailView, AlbumDetailView, SongDetailView
#
# urlpatterns = [
#     # artist
#     path('artist/', ArtistView.as_view(), name='artist'),
#     path('artist/<int:id>/', ArtistDetailView.as_view(), name='artist-detail'),
#     # album
#     path('album/', AlbumView.as_view(), name='album'),
#     path('album/<int:id>/', AlbumDetailView.as_view(), name='album-detail'),
#     # song
#     path('song/', SongView.as_view(), name='song'),
#     path('song/<int:id>/', SongDetailView.as_view(), name='song-detail'),
# ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



# ------ URL для ModelViewSet ------ #

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ArtistViewSet, AlbumViewSet, SongViewSet


router = DefaultRouter()
router.register(r'artist', ArtistViewSet, basename='artist')
router.register(r'album', AlbumViewSet, basename='album')
router.register(r'song', SongViewSet, basename='song')


urlpatterns = [
    path('', include(router.urls)),
]
