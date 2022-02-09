# I have created this
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
   # params = {'name': 'kajal', 'place': 'delhi'} render vali line m last m params pass kre
    return render(request, "index2.html")
def analyze(request):
    #get the text
    djtext = (request.POST.get('text', 'default'))
    removepunc = (request.POST.get('removepunc','off'))
    fullcaps = (request.POST.get('fullcaps', 'off'))
 #analyze text
    if (removepunc == "on"):
          punctutions = '''!@#$%^&890:;'.[] _~`{}'''
          analyzed = ""
          for char in djtext:
            if char not in punctutions:
               analyzed = analyzed + char
          params = {'purpose': 'remove punc', 'analyzedtext': analyzed}
          djtext = analyzed
         # return render(request, "analyze2.html", params)
    if(fullcaps == "on"):
         analyzed = ""
         for char in djtext:
               analyzed = analyzed + char.upper()
         params = {'purpose':'uppercase', 'analyzedtext': analyzed}
         djtext = analyzed
         #return render(request, "analyze2.html", params)

    if(removepunc!= "on" and fullcaps != "on"):
        return HttpResponse("ERROR")
    return render(request,"analyze2.html",params)



# def capfirst(request):
#     return HttpResponse('''"capitalize" <a href= '/'> back''')
# def newlineremove(request):
#     return HttpResponse("newlineremove")
# def charcount(request):
#     return HttpResponse("charcount")
# def spaceremover(request):
#     return HttpResponse("spaceremover")