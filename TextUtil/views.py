 # I have created this file - Gaurav
 # code vedio 6
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return  render(request,'index.html')

def analyze(request):
    # get the text
    djtext=(request.POST.get('text','default'))


    #checkbox value
    removepunc=(request.POST.get('removepunc','off'))
    fullcaps=(request.POST.get('fullcaps','off'))
    newlineremover=(request.POST.get('newlineremover','off'))
    extraspaceremover=(request.POST.get('extraspaceremover','off'))
    charcount=(request.POST.get('charcount','off'))

    #check with check box is on
    if removepunc=="on":
        punctuations='''!()-[]{};:'"\,<>.??@!#$%^*_~'''
        analyzed=""
        for char in djtext:
            if char not in punctuations:
                analyzed=analyzed+char
        params={'purpose':'Removed Punctuation','analyzed_text':analyzed}
        djtext=analyzed

    if(fullcaps=="on"):
        analyzed=""
        for char in djtext:
            analyzed=analyzed+char.upper()
        params = {'purpose': 'Chanaged to uppercase ', 'analyzed_text': analyzed}
        djtext=analyzed

    if(newlineremover=="on"):
        analyzed = ""
        for char in djtext:
            if char !="\n" and char!="\r":
                analyzed = analyzed + char
        params = {'purpose': 'Removed new lines ', 'analyzed_text': analyzed}
        djtext=analyzed
        # analyze the text

    if (extraspaceremover == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index+1]==" "):

                analyzed = analyzed + char
        params = {'purpose': 'extraspaceremover ', 'analyzed_text': analyzed}
        djtext=analyzed
        # analyze the text

    if (charcount == "on"):
        analyzed = len(djtext)

        params = {'purpose': 'charcount ', 'analyzed_text': analyzed}

    if(removepunc !="on" and newlineremover !="on" and extraspaceremover !="on" and fullcaps !="on" and charcount !="on"):
        return HttpResponse("Please select any operation and try again")

    return render(request, 'analyze.html', params)

