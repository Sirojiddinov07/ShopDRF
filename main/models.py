from django.contrib.auth.models import User
from django.db import models

class Subcategory(models.Model):
    name = models.CharField(max_length=200)
    img = models.ImageField(upload_to='media/')




class Category(models.Model):
    name = models.CharField(max_length=200)
    img = models.ImageField(upload_to='media/')
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE)




class Image(models.Model):
    img = models.ImageField(upload_to='media/')


class Product(models.Model):
    name = models.CharField(max_length=200)
    color = models.CharField(max_length=200, null=True, blank=True)
    img = models.ManyToManyField(Image)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    discount_price = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    discount_in_percent = models.IntegerField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,)
    description = models.TextField(null=True, blank=True)
    extra_info = models.TextField(null=True, blank=True)
    rating = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    countInStock = models.IntegerField(null=True, blank=True, default=0)
    createdAt = models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return self.name



class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    rating = models.IntegerField(null=True, blank=True, default=0)
    comment = models.TextField(null=True, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)



class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    paymentMethod = models.CharField(max_length=200, null=True, blank=True)
    shippingPrice = models.DecimalField( max_digits=7, decimal_places=2, null=True, blank=True)
    totalPrice = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    isPaid = models.BooleanField(default=False)
    paidAt = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    isDelivered = models.BooleanField(default=False)
    deliveredAt = models.DateTimeField( auto_now_add=False, null=True, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return str(self.createdAt)







class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    qty = models.IntegerField(null=True, blank=True, default=0)


    def __str__(self):
        return str(self.name)




class ShippingAddress(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=200, null=True, blank=True)
    postalCode = models.CharField(max_length=200, null=True, blank=True)
    country = models.CharField(max_length=200, null=True, blank=True)
    shippingPrice = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return str(self.address)




class Story(models.Model):
    header = models.CharField(max_length=200)
    text = models.TextField()
    img = models.ImageField(upload_to='media/', null=True, blank=True)



class Blogs(models.Model):
    header = models.CharField(max_length=200)
    text = models.TextField()
    img = models.ManyToManyField(Image)
    createdAt = models.DateTimeField(auto_now_add=True)



class BlogReview(models.Model):
    blog = models.ForeignKey(Blogs, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    comment = models.TextField(null=True, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
