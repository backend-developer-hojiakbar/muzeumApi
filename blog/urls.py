from django.urls import path
from .views import ExponantListApi, ExponantDetailApiView, \
    ExponantDeleteApiView, ExponantUpdateApiView,\
    ExponantCreateApiView, ExponantUpdateDeleteView, ExponantCommentListCreateView

urlpatterns = [
    path('exponant/', ExponantListApi.as_view(),name='exponant_list'),
    path('exponant/<int:pk>/', ExponantDetailApiView.as_view()),
    path('exponant/<int:pk>/update/', ExponantUpdateApiView.as_view()),
    path('exponant/<int:pk>/delete/', ExponantDeleteApiView.as_view()),
    path('exponant/create/', ExponantCreateApiView.as_view()),
    path('exponant/updatedelete/<int:pk>/', ExponantDeleteApiView.as_view()),
    path('exponant/comment/<int:exponant_id>/', ExponantCommentListCreateView.as_view()),
]