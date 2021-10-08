from django.views import generic


class IndexView(generic.ListView):
    template_name = 'mainapp/index.html'
    queryset = ''
