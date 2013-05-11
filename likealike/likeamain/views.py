import json
import LikeALike

from django.http import HttpResponse
from django.template import Context, loader

def index(request):
	""" list all the things that the current user likes, """\
	""" grouped by category """

	# hard coded test data... lol!
	#categories = [
	#		{
	#			'id': '0',
	#			'display_name': 'Fruits/oranges',
	#			'members': [
	#				{
	#					'id': '1',
	#					'display_name': 'blood',
	#					'count': '23' # the number of friends that also like this
	#				},
	#				{
	#					'id': '2',
	#					'display_name': 'fancy italian one',
	#					'count': '3'
	#				}
	#			],
	#		},
	#		{
	#			'id': '3',
	#			'display_name': 'Fruits/apples',
	#			'members': [
	#				{
	#					'id': '4',
	#					'display_name': 'pink lady',
	#					'count': '5'
	#				},
	#				{
	#					'id': '5',
	#					'display_name': 'golden delicious',
	#					'count': '7'
	#				}
	#			]
	#		}
	#	]

	categories = LikeALike.getListOfDicOfIntersections()

	# TODO use a template to render LIST
	#return HttpResponse("index, listing categories.")
	template = loader.get_template('index.html')
	context = Context({
		#'categories': categories
		'categories': categories
	})
	return HttpResponse(template.render(context))


def show(request, fbID):
	""" display friends that also like the object fbID """
	# TODO LIST := get the list of friends that also like fbID

	likedThing = LikeALike.whoLikes(fbID)
	template = loader.get_template('show.html')
	context = Context({
		'likedThing': likedThing
	})
	return HttpResponse(template.render(context))


def show_contact(request, fbID):
	""" uses post data to show a form to contact """
	respString = "show_contact, fbID {0} with post data: {1}"
	return HttpResponse(respString.format(fbID, request.POST))


def uh_oh(request):
	""" 404 response """
	template = loader.get_template('404.html')
	context = Context({})
	return HttpResponse(template.render(context))

