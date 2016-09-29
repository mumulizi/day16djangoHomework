from django.shortcuts import render,HttpResponse
from app01 import models
# Create your views here.
#def index(request,user):
def index(request):
    #print("user request:",request.GET)
    # return HttpResponse("app01...index...ok...%s"%user)
    user_info = [
        {'username':'alex','name':'ALEX LI'},
        {'username':'2alex','name':'2ALEX LI'},
        {'username':'3alex','name':'3ALEX LI'},
        {'username':'4alex','name':'4ALEX LI'},
    ]
    #return render(request,"app01/index.html",{"user_obj":user_info})
    return render(request,"app01/index.html")
def pay_by_cash(request):
    return HttpResponse("CASH...CASH")
def year_archive(request,year,file_type,user):
    print("--->",year,file_type,user)
    return HttpResponse(year)
def pag01(request):
    return  render(request,"app01/pag01.html")
def book(request):
    # if request.method == "GET":
    #     books = models.Book.objects.all()
    #     publisers = models.Publisher.objects.all()
    #     author_list = models.Authon.objects.all()
    #     return render(request,'app01/book.html',{'books':books,
    #                                                 'publisers':publisers,
    #                                                 'authors':author_list
    #                                              })
    if request.method =='POST':
        print(request.POST)
    #return render(request,'app01/book.html',{'books':books})
        book_name = request.POST.get('name')
        publiser_id = request.POST.get('publiser_id')
        author_ids = request.POST.getlist('author_ids')
        print(book_name,publiser_id,author_ids)

        new_book = models.Book(
            name = book_name,
            publisher_id = publiser_id,
            publish_date = '2014-05-22'
        )
        new_book.save()
        new_book.authors.add(*author_ids)
    books = models.Book.objects.all()
    publisers = models.Publisher.objects.all()
    author_list = models.Authon.objects.all()
    return render(request,'app01/book.html',{'books':books,
                                                    'publisers':publisers,
                                                    'authors':author_list
                                                 })

