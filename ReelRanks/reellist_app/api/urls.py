from django.urls import path, include
from rest_framework.routers import DefaultRouter
# from reellist_app.api.views import movie_list, movie_details
from reellist_app.api.views import (ReviewList, ReviewDetail, ReviewCreate, WatchListAV, 
                                    WatchDetailAV, StreamPlatformAV, 
                                    StreamPlatformDetailAV, StreamPlatformVS)


router = DefaultRouter()
router.register('stream', StreamPlatformVS, basename='streamplatform')

urlpatterns = [
    # path('list/', movie_list, name = 'movie-list'),
    # path('<int:pk>', movie_details, name = 'movie-details'),
    path('list/', WatchListAV.as_view(), name = 'movie-list'),
    path('<int:pk>', WatchDetailAV.as_view(), name = 'movie-details'),
    
    path('', include(router.urls)),
    
    # path('stream/', StreamPlatformAV.as_view(), name = 'stream-list'),
    # path('stream/<int:pk>', StreamPlatformDetailAV.as_view(), name = 'stream-detail'),
    
    # path('review/<int:pk>', ReviewDetail.as_view(), name='review-detail'),
    # path('review/', ReviewList.as_view(),name ='review-list')
    path('stream/<int:pk>/review-create', ReviewCreate.as_view(), name='review-create'),
    path('stream/<int:pk>/review', ReviewList.as_view(), name='review-list'),
    path('stream/review/<int:pk>', ReviewDetail.as_view(), name='review-detail')

    
]
    
    
