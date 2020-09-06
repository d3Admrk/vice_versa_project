from django.http import HttpResponse
from django.shortcuts import render


def home(request):
	return render(request, 'home.html')

def reverse(request):
	get_text = request.GET['usertext']
	num_of_word = len(get_text.split())
	reversed_text = get_text[::-1]
	return render(request, 'reverse.html', {'usertext': get_text, 
		'reversedtext' : reversed_text, 'num_of_word':num_of_word})