from django.contrib import admin

# Register your models here.
from main.models import Subcategory, Category, Image, Product, Order, OrderItem, ShippingAddress, Story, Blogs, BlogReview

admin.site.register(Subcategory)
admin.site.register(Category)

admin.site.register(Image)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)
admin.site.register(Story)
admin.site.register(Blogs)
admin.site.register(BlogReview)


