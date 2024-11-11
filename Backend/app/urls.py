from . import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, IndexView, ContactView, CreatePostView, PostsByUser, PostDetailView
#from .views import PostCreateView
from django.conf import settings
from django.conf.urls.static import static

router = DefaultRouter()
router.register(r'posts', PostViewSet)

urlpatterns = [
    # web
    path('', IndexView.as_view(), name="home"),
    #path('new/post/', PostCreateView.as_view(), name="create_post"),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('contact/', ContactView.as_view(), name="contact"),


    # mobile
    path('user/posts/<int:user_id>/', PostsByUser.as_view(), name="user-posts"),
    path('', include(router.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
