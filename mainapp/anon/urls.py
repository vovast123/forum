from django.urls import path
from . import views


urlpatterns = [
    path('', views.Index.as_view(),name ='base'),
    path('logout/', views.logoutUser,name ='logout'),
    path('login', views.Login.as_view(),name ='login'),
    path('register', views.Reg.as_view(),name ='reg'),
    path('create', views.Create.as_view(),name ='create'),
    path('info/<int:post_id>', views.Info.as_view(),name ='info'),
    path('all', views.AllPost.as_view(),name ='all'),
    path('info/<int:post_id>/like/', views.AddLike.as_view(), name='add-like'),
    path('all/like/<int:post_id>', views.AddLike2.as_view(), name='add-likee'),
    path('info/likeart/<int:art_id>/', views.AddLikeArt.as_view(), name='add-likeart'),
    path('profile', views.Profile.as_view(), name='prof'),
    path('profile/posts', views.AllProfPost.as_view(), name='profall'),
    path('profile/dellpost', views.AllProfPostDell.as_view(), name='profalld'),
    path('profile/dellpost/<int:post_id>', views.AllProfPostDellId.as_view(), name='profalldell'),
    path('profile/comments/', views.AllProfCom.as_view(), name='comment'),
    path('profile/comments/<int:art_id>/', views.AddLikeArt2.as_view(), name='add-likeartt'),
    path('profile/comments/delete/', views.AllProfArtToDel.as_view(), name='delart'),
    path('profile/comments/delete/<int:art_id>/', views.AllProfArtDellId.as_view(), name='delartt'),
]