import json

from django.http import HttpResponse
from django.template import Context, loader

def index(request):
	""" list all the things that the current user likes, """\
	""" grouped by category """
	# TODO LIST := get the list of things the user likes, grouped by category
	# hard coded test data... lol!
	#categories = {
		#{
			#'id': '0',
			#'display_name': 'fruits/oranges',
			#'members': [
				#{
					#'id': '1',
					#'display_name': 'alice'
				#},
				#{
					#'id': '2',
					#'display_name': 'bob'
				#}
			#],
		#},
		#{
			#'id': '3',
			#'display_name': 'fruits/apples',
			#'members': [
				#{
					#'id': '4',
					#'display_name': 'charlie'
				#},
				#{
					#'id': '5',
					#'display_name': 'trudy'
				#}
			#]
		#}
	#}
	# TODO use a template to render LIST
	#return HttpResponse("index, listing categories.")
	template = loader.get_template('index.html')
	context = Context({
		#'categories': categories
		'categories': ['alice', 'bob', 'charlie', 'trudy']
	})
	return HttpResponse(template.render(context))


def show(request, fbID):
	""" display friends that also like the object fbID """
	# TODO LIST := get the list of friends that also like fbID
	# TODO use a template to render LIST and use fbIDs of friends as values
	#      posted to show_contact
	return HttpResponse("view, showing the liked object {0}".format(fbID))


def show_contact(request, fbID):
	""" uses post data to show a form to contact """
	respString = "show_contact, fbID {0} with post data: {1}"
	return HttpResponse(respString.format(fbID, request.POST))


def uh_oh(request):
	""" 404 response """
	return HttpResponse("uh oh... page not found! zOMG!!!1")

