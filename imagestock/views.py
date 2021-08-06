from django.views.generic import TemplateView


<<<<<<< HEAD
def index(request):
    return render(request, 'index.html')



    
=======
class IndexView(TemplateView):
    template_name = 'index.html'
>>>>>>> f5b9798c88a106fa2eed64637b3d4b982ec3b242
