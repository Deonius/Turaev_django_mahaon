from django .http import HttpResponse
 #create your files here.
def index(request) :
    return HttpResponse("hello world")

