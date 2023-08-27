from django.shortcuts import render
from . import util
from markdown2 import Markdown
from random import choice

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })
def convert_markdown_to_html(title):
    content=util.get_entry(title)
    md=Markdown()
    if content == None:
        return None 
    else :
        return md.convert(content)
def entry(request,title):
    html_content= convert_markdown_to_html(title)
    if  html_content ==None:
        return render(request,"encyclopedia/error.html",{
           "message":"this page dose not exist"
        })
    else:
        return render(request,"encyclopedia/entry.html",{
            "title":title,
            'content': html_content
        })
def search(request):
    search_title=request.POST['q']
    HTML_CONTENT=convert_markdown_to_html(search_title)
    if util.get_entry(search_title) != None : 
        return render(request,"encyclopedia/entry.html",{
                "title":search_title,
                'content':HTML_CONTENT,
            })
    elif 'a'<= search_title <= 'z' or 'A'<= search_title <= 'Z':
        entry_search=util.list_entries()
        search_results=[]
        conter=0
        for i in entry_search:
            if search_title.lower() in i.lower():
                search_results.append(i)
                conter+=1
        if conter>0:
            return render(request,"encyclopedia/search.html",{
                'entries':search_results,})
        else:
            return render(request,"encyclopedia/error.html",{
                    'message':"page not found"
                     })
    else:
        return render(request, "encyclopedia/index.html", {
            "entries": util.list_entries()
         })

def random(request):
    random_choise=choice(util.list_entries())
    HTML_CONTENT=convert_markdown_to_html(random_choise)
    return render(request,"encyclopedia/entry.html",{
            "title":random_choise,
            'content':HTML_CONTENT,})
def Create_New_Page(request):
    if request.method == 'GET':
        return render(request,"encyclopedia/C_N_P.html")
    if request.method == 'POST':
        title=request.POST['title']
        content=request.POST['content']
        if title not in util.list_entries():
            util.save_entry(title,content)
            return render(request,"encyclopedia/entry.html",{
                'title':title,
                'content': content}) 
        else:
            return render(request,"encyclopedia/error.html",{
                'message':"page is already exists"})
def edit (request):
    if request.method == 'POST':
        title=request.POST['title']
        content=util.get_entry(title)
        return render(request,"encyclopedia/edit.html",{
            "title":title,
            'content': content})
def save_the_edit(request):
    if request.method == 'POST':
        title=request.POST['title']
        content=request.POST['content']
        util.save_entry(title,content)
        HTML_CONTENT=convert_markdown_to_html(title)
        return render(request,"encyclopedia/entry.html",{
            "title":title,
            'content': HTML_CONTENT})


        


    




