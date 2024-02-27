
# Create your views here.
from django.shortcuts import render
from .models import Ebook,Category,Customer
from django.shortcuts import HttpResponse

def index(request):
    books=None
    categories=Category.get_all_categories()
    categoryID=request.GET.get('category')
    if categoryID:
        books=Ebook.get_all_books_by_category_id(categoryID)
    else:
        books=Ebook.get_all_books();
    data={}
    data['books']=books
    data['categories']=categories
    return render(request, 'store/index.html',data)


def signup(request):
    if request.method=='GET':
      return render(request, 'store/signup.html')

    else:
        postData = request.POST
        firstname = postData.get('firstname')
        lastname = postData.get('lastname')
        phone = postData.get('phone')
        email = postData.get('email')
        password = postData.get('password')
        
        customer = Customer(firstname=firstname,
                            lastname=lastname,
                            phone=phone,
                            email=email,
                            password=password)
        customer.register()
        return HttpResponse("signup successfully")
    
    
    
    
    
    
