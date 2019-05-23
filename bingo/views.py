from django.shortcuts import render


def error_404(request, exception):
    return render(request, '404.html')


def error_500(request, exception):
    # todo log exception somewhere?
    return render(request, '500.html')
