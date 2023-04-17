from django.urls import path
from knox import views as knox_views
from . import views

urlpatterns = [
    path('create-post/', views.create_post),
    path('list-posts/', views.list_posts),
    path('publish-post/<int:post_id>/', views.publish_post),
    path('unpublish-post/<int:post_id>/', views.un_publish_post),
    path('update-post/<int:pk>/', views.post_update_view),
    path('find-post/<int:pk>/', views.post_detail_view),
    path('delete-post/<int:pk>/', views.post_destory_view),
    ########################## Comment Public ###########################
    path('comment/', views.create_comment),
    path('comment/update/<int:pk>/', views.comment_update_view),
    path('comment/delete/<int:pk>/', views.comment_destory_view),
    ########################### NestedComment Public ##################################
    path('comment/create-nestedcomment/', views.create_nestedcomment),
    path('comment/nestedcomment/update/<int:pk>/',
         views.nestedcomment_update_view),
    path('comment/nestedcomment/delete/<int:pk>/',
         views.nestedcomment_destory_view),
    ############################# Public ########################################
    path('comment/fetch-comments-by-post-id/<int:post_id>/',
         views.fetch_comments_by_post_id),
    path('comment/fetch-nestedcomments-by-comment-id/<int:comment_id>/',
         views.fetch_nestedcomments_by_post_id),
    path('', views.fetch_posts),
    path('comments/', views.fetch_comments),
]
