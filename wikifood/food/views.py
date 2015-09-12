#encoding=utf-8
from django.shortcuts import render
from django.http import HttpResponse
from django.template.defaulttags import register
import List_of_cakes_dict
import List_of_rice_dishes_dict
import os
# Create your views here.

obtain = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) \
	+ '/obtain' 
List_of_cakes_file = open(obtain + '/List_of_cakes/rootall')
List_of_cakes_list = List_of_cakes_file.readlines()
List_of_rice_dishes_file = open(obtain + '/List_of_rice_dishes/rootall')
List_of_rice_dishes_list = List_of_rice_dishes_file.readlines()


@register.filter
def get_item(list, key):
    return list[key-1].replace(str(key), '').strip('_')

'''
	filter
'''

def goto(request):
	A = request.GET['A']
	B = request.GET['B']
	addr = "{dir}/{id}.html" .format(dir = A, id = B)
	return render(request, addr)
'''
	go to local html
'''

def home(request):
	return render(request, 'home.html')

'''
	home
'''

def indexSearch(request, index, page):
	riceList = []
	cakeList = []
	for item in index:	
		if (item in List_of_cakes_dict.dict):
			subcake = List_of_cakes_dict.dict[item]
			if (len(cakeList) == 0):
				cakeList = subcake
			else:
				cakeList = [val for val in subcake if val in cakeList]
		else:
			cakeList = []
			break
			
	'''
		intersect
	'''
	lencake = len(cakeList)
	if (lencake > 0):
		modv = lencake / 10 + (lencake % 10 > 0)
		first = page % modv * 10
		last = first + 10
		if (last > lencake):
			last = lencake
		cakeList = cakeList[first:last]
	'''
		search from cake
	'''	
	for item in index:
		if (item in List_of_rice_dishes_dict.dict):
			subrice = List_of_rice_dishes_dict.dict[item]
			if (len(riceList) == 0):
				riceList = subrice
			else:
				riceList = [val for val in subrice if val in riceList]
		else:
			riceList = []
			break
	'''
		intersect
	'''
	lenrice = len(riceList)
	if (lenrice > 0):
		modv = lenrice / 10 + (lenrice % 10 > 0)
		first = page % modv * 10
		last = first + 10
		if (last > lenrice):
			last = lenrice
		riceList = riceList[first:last]
	'''
		search from rice
	'''	
	index2str = ''
	for item in index:
		index2str = index2str + ' ' + item
	cakeWiki = [it.replace(' ','_') for it in List_of_cakes_list]
	riceWiki = [it.replace(' ','_') for it in List_of_rice_dishes_list]
	return render(request, 'food.html', {'cakeList':cakeList, 'chickenList':riceList, 'cakeFile': List_of_cakes_list, 'riceFile':List_of_rice_dishes_list,
	'lastpage':max(page-1, 0), 'nextpage':page+1, 'index':index2str, 'cakeWiki':cakeWiki, 'riceWiki':riceWiki})

	
def foodindex(request):
	if (request.method == 'POST'):
		index = request.POST['keywords'].strip()
		if (index == ''):
			return render(request, 'home.html')
		else:
			index = index.lower()
			index = index.split(' ')
			return indexSearch(request, index, 0)
	else:
		if (not request.GET.has_key('index')):
			return render(request, 'home.html')
		else:
			index = request.GET['index'].strip()
			index = index.lower()
			index = index.split(' ')
			return indexSearch(request, index, int(request.GET['page']))
'''
	index search
'''