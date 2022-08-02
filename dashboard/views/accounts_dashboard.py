from django.shortcuts import render


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username") or None
        password = request.POST.get("password") or None

    return render(request, "accounts/login.html")
