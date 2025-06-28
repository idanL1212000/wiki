import random
from django.shortcuts import render, redirect
import markdown

from . import util
from .util import get_entry


def index(request):
    query = request.GET.get('q')
    if query:
        entry = get_entry(query)
        if entry is not None:
            return redirect("entry", title=query)

        all_entries = util.list_entries()
        matches = [title for title in all_entries if query.lower() in title.lower()]
        return render(request, "encyclopedia/search.html", {
            "query": query,
            "matches": matches
        })

    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def visitPage(request, title):
    print(title)
    content_md = util.get_entry(title)
    if content_md is None:
        return render(request, "encyclopedia/notFound.html")
    content_html = markdown.markdown(content_md)
    return render(request, "encyclopedia/entry.html",{
        "title": title,
        "content": content_html
    })

def addPage(request):
    if request.method == "POST":
        title = request.POST.get("title").capitalize()
        content = request.POST.get("content")

        if util.get_entry(title):
            return render(request, "encyclopedia/newPage.html", {
                "error": "An entry with this title already exists.",
            })

        util.save_entry(title, content)
        return redirect("entry", title=title)

    return render(request, "encyclopedia/newPage.html")

def editPage(request,title):
    if request.method == "POST":
        content = request.POST.get("content")
        util.save_entry(title, content)
        return redirect("entry", title=title)

    return render(request, "encyclopedia/editPage.html",{
        "title": title,
        "body": util.get_entry(title)
    })


def randomPage(request):
    all_entries = util.list_entries()
    title = random.choice(all_entries)
    return  redirect("entry", title=title)