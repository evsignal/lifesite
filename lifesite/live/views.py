from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpRequest


from django.shortcuts import Http404
from django.http import Http404
from django.views import generic
from django.template import loader
from django.core.urlresolvers import reverse
from django.utils import timezone
from . models import Article
"""
HttpResponseRedirect
from django.template import loader
from django.core.urlresolvers import reverse
from .models import Article
from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.views import generic
from django.utils import timezone
"""
# Create your views here.


class IndexView(generic.ListView):
    latest_article_list = Article.objects.order_by('-pub_date')[:5]
    context = {'latest_article_list': latest_article_list}
    template_name = 'live/index.html'
    context_object_name = 'latest_article_list'

    def get_queryset(self):
        """
        Return the latest 5 published articles (without including those set
        to be published in the future
        """
        return Article.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Article
    template_name = 'live/article.html'

    def get_queryset(self):
        """
        Excludes any article that aren't published yet.
        """
        return Article.objects.filter(pub_date__lte=timezone.now())


'''
def index(request):
    return HttpResponse("You are looking at index")


def detail(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    return render(request, 'live/article.html', {'article': article})
'''

