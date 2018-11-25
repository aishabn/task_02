from django.shortcuts import render
from django.http import HttpResponse



def start_func (request):
	

	context = {

	'msg' : 'Hello World!',
}
	return render (request,'index.html', context)