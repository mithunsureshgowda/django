from django.shortcuts import render

def palindrome(request):
    res=""
    if(request.method=="POST"):
        x=request.POST.get('p')
        res=x[::-1]
    content={
        'pa':res
    }
    return render(request,'pal.html',content)
