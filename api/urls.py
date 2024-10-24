from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from api import views as api_views

urlpatterns = [
    path('user/token/',api_views.MyTokenObtainPairView.as_view()),
    path('user/token/refresh/',TokenRefreshView.as_view()),
    path('user/register/',api_views.RegisterView.as_view()),
    path('user/profile/<user_id>/',api_views.Profileview.as_view()),
    
    #post
    path('post/lists/',api_views.PostListAPIView.as_view()),
    path('post/lists/all/',api_views.PostListAllAPIView.as_view()),
    # path('post/details/<slug>/',api_views.PostDetailsAPIView.as_view()),
    path('post/details/<id>/',api_views.PostDetailsAPIView.as_view()),
    # path('post/delete/<id>/',api_views.PostDeleteAPIView.as_view()),
    path('post/featured/',api_views.PostFeaturedAPIView.as_view()),


    # path('author/dashboard/stats/<user_id>/',api_views.DashbordStas.as_view()),
    # path('author/dashboard/comment-list/<user_id>/',api_views.DashboardCommentLists.as_view()),
    # path('author/dashboard/noti-lit/<user_id>/',api_views.DashboardNotificationLists.as_view()),
    # path('author/dashboard/noti-mark-seen/<user_id>/',api_views.DashboardMarkNotificationSeen.as_view()),
    # path('author/dashboard/reply-comment/',api_views.DashbordReplyCommentAPIView.as_view()),
    
    # Gallery Ennpoints
    path("gallery/", api_views.GalleryAPIView.as_view()),
    # path("gallery/<id>/", api_views.GalleryAPIView.as_view()),
    path("auth/gallery/create/",api_views.GalleryCreate.as_view()),
    path('auth/gallery/<item_id>/', api_views.GalleryDeleteView.as_view(), name='gallery-delete'),
    #  path("gallery/create/", api_views.gallery_create, name="gallery-create"),

    #Post Create,Delete,Update
    path('author/dashboard/post-create/',api_views.DashboardPostCreateAPIView.as_view()),
    path('author/dashboard/post-details/<user_id>/<post_id>/',api_views.DashboardPostUpdateAPIView.as_view()),
    

    # Others
    path("quote/quote-view/",api_views.DashboardQuoteAPIView.as_view()),
    path("quote/create-quote/",api_views.QuoteCreate.as_view()),
]
