from django.shortcuts import render, redirect
from .forms import URLForm
from .utils import get_short_url
from .models import Url
import pyperclip


def redirect_page(request, tk):
    long_url = Url.objects.filter(short_url=tk).first()
    return redirect(long_url.long_url)


def main(request):
    if request.method == "POST":
        form = URLForm(request.POST or None)
        if form.is_valid():
            data = form.data
            dom = request.headers['Host']
            long_url = data.get('long_url')
            short_url = get_short_url()
            s_url = Url(long_url=long_url, short_url=short_url)
            s_url.save()
            pyperclip.copy(dom + '/' + short_url)
            context = {'long_form': form, 'short_form': dom + '/' + short_url}
            return render(request, 'shortlink/short.html', context)
    context = {'long_form': URLForm()}
    return render(request, 'shortlink/main.html', context)
