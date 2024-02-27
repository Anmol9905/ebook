
# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    # You can add more fields like date_of_birth, nationality, etc.

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)
    
    @staticmethod
    def get_all_categories():
        return Category.objects.all()
    
    def __str__(self):
        return self.name

class Ebook(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    cover_image = models.ImageField(upload_to='ebook_covers/')
    published_date = models.DateField()

    def __str__(self):
        return self.title
    
    @staticmethod
    def get_all_books():
        return Ebook.objects.all
    
    @staticmethod
    def get_all_books_by_category_id(category_id):
        if category_id:
          return Ebook.objects.filter(category=category_id)
        else:
            return Ebook.get_all_books



class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ebooks = models.ManyToManyField(Ebook)
    ordered_date = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'Order {self.id} by {self.user.username}'


class Customer(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    password = models.CharField(max_length=500)

    def register(self):
        self.save()