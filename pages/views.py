from django.shortcuts import render


def home(request):
    context = {
        "page_title": "Агентські послуги з організації та супроводу розрахунків",
        "meta_description": "Агентські послуги з організації та документального супроводу розрахунків між сторонами договорів в Україні.",
    }
    return render(request, "pages/home.html", context)

def documents(request):
    context = {
        "page_title": "Документи",
        "meta_description": "Публічна оферта, політика конфіденційності, згода на обробку персональних даних.",
    }
    return render(request, "pages/documents.html", context)
