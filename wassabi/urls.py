from django.contrib import admin
from django.urls import path
from products.views import main_page_view, products_view, hashtags_view, product_detail_view
from django.conf.urls.static import static
from wassabi.settings import MEDIA_ROOT, MEDIA_URL

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_page_view),
    path('products/', products_view),
    path('products/<int:id>/', product_detail_view),
    path('hashtags/', hashtags_view)
]

urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
