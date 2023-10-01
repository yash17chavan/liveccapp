from django.shortcuts import render, redirect
from requests import *

def home(request):
	if request.GET.get("amt"):
		amt = float(request.GET.get("amt"))
		url = "https://api.exchangerate-api.com/v4/latest/USD"
		res = get(url)
		data = res.json()
		dollar = data["rates"]["RUB"]
		air = amt * dollar
		msg = "\u20b9" + str(round(air,2))
		return render(request, "home.html", {"msg":msg})
	else:
		return render(request,"home.html")

def pnf(request, exception):
	return redirect("home")