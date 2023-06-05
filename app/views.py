from django.shortcuts import render

# Create your views here.
def operational_html(request):
    d={'name':'Sudhaanshu Pandey','age':23}
    return render(request,'operational_html.html',context=d)
