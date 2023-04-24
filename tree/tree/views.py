from django.http import HttpResponse
from django.shortcuts import render
from api.models import *



list_categories = Category.objects.all()
list_categories_json = [category.to_json() for category in list_categories]

chosen_category: Category = Category.objects.none

def categories(request):

    context = {
        "categories" : list_categories_json
    }

    return render(request, 'templates/index.html', context)


def category(request, category_id = 0):
    global chosen_category

    current_category = Category.objects.get(id = category_id)
    chosen_category = current_category
    subcategories  = current_category.subcategories.all()
    subcategories_json = [subcategory.to_json() for subcategory in subcategories]

    context = {
        "categories" : list_categories_json,
        "subcategories" : subcategories_json,
        'category_id': category_id,
    }    
    
    return render(request, 'templates/subcategory.html', context)


def subcategory(request, category_id, subcategory_id):
    
    current_subcategory = chosen_category.subcategories.get(id=subcategory_id)
    subcategories = chosen_category.subcategories.all()
    subsubcategories = current_subcategory.subsubcategories.all()
    subcategories_json = [ subcategory.to_json() for subcategory in subcategories]
    subsubcategories_json = [subcategory.to_json() for subcategory in subsubcategories]

    current_subcategory.category
    context = {
        "categories" : list_categories_json,
        "subcategories" : subcategories_json,
        "subsubcategories": subsubcategories_json,
        "category_id": category_id,
    }

    return render(request, "templates/subsubcategory.html",context)




    
    
