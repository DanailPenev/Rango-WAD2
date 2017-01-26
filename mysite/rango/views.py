from django.shortcuts import render
from django.http import HttpResponse
from rango.models import Category, Page


def index(request):

	# Query the database, sort, retrieve the top 5 entries and pass them to the template
	category_list = Category.objects.order_by('-likes')[:5]
	page_list = Page.objects.order_by('-views')[:5]
	context_dict = {'categories': category_list, 'pages': page_list}
	
	return render(request, 'rango/index.html', context_dict)

def about(request):
	context_dict = {'message': "This tutorial has been put together by Danail Penev"}
	return render(request, 'rango/about.html', context=context_dict)
	
def show_category(request, category_name_slug):
	context_dict = {}
	
	# Try and get the category with the required slug and return it and its pages
	# in the context_dictionary and the template
	
	try:
		category = Category.objects.get(slug=category_name_slug)
		
		pages = Page.objects.filter(category=category)
		
		context_dict['pages'] = pages
		context_dict['category'] = category
		
	except Category.DoesNotExist:
		
		context_dict['pages'] = None
		context_dict['category'] = None
		
	return render(request, 'rango/category.html', context_dict)