from django.urls import URLPattern, path
from . import views
# from views import api_home

urlpatterns = [
    # path('auth/', obtain_auth_token),
    # path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('', views.api_home), # localhost:8000/api/
    # path('products/', include('products.urls'))
]