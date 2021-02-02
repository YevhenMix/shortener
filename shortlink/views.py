from django.shortcuts import render
from .forms import URLForm


def main(request):
    if request.method == "POST":
        form = URLForm(request.POST or None)
        if form.is_valid():
            data = form.data
            long_url = data.get('long_url')
            short_url = "https://django.fun/docs/django/"
            context = {'long_form': form, 'short_form': short_url}
            return render(request, 'shortlink/main.html', context)
    context = {'long_form': URLForm()}
    return render(request, 'shortlink/main.html', context)
