from django import forms
from django.contrib.auth import(
	authenticate,
	get_user_model,
	login,
	logout,
	)
from django.shortcuts import render, redirect
from .forms import UserLoginForm
from .classification import classify
from .models import zonal_tweets
# Create your views here.
def login_view(request):
	
	form = UserLoginForm(request.POST or None)
	if form.is_valid():
		username = form.cleaned_data.get("username")
		password = form.cleaned_data.get("password")
		user = authenticate(username=username,password=password)
		login(request,user)
		return redirect('/')
	return render(request,"login.html",{"form":form})

def home_page_view(request):
	'''
	data_dict = classify()
	for data in data_dict:
		z = zonal_tweets(tag=data,tweet=data_dict[data])
		z.save()
	'''
	return render(request,"home.html")

def feedback_view(request, zone):
	
	titledict = {
		"nr" : "Northern Railway",
		"ner" : "North Eastern Railway",
		"nfr" : "Northeast Frontier Railway",
		"er" : "Eastern Railway",
		"ser" : "South Eastern Railway",
		"sr" : "Southern Railway",
		"scr" : "South Central Railway",
		"cr" : "Central Railway",
		"wr" : "Western Railway",
		"swr" : "South Western Railway",
		"nwr" : "North Western Railway",
		"wcr" : "West Central Railway",
		"ncr" : "North Central Railway",
		"secr" : "South East Central Railway",
		"ecor" : "East Coast Railway",
		"ecr" : "East Cenrtal Railway",
		"ed" : "Engineering Department",
		"mepd" : "Mechanical Engineering & Power Department",
		"eed" : "Electrical Engineering Department",
		"sted" : "Signal & Telecommunication Engineering Deaprtment",
		"otd" : "Operating and Traffic Department",
		"cd" : "Commercial Department",
		"md" : "Medical Deparment",
		"sd" : "Safety Deparment",
		"std" : "Stores Deparment",
		"ad" : "Accounts Deparment",
		"pd" : "Personnel Deparment",
		"sed" : "Security Deparment"
	}
	if zone in titledict:
		title = titledict[zone]
		queryset = zonal_tweets.objects.filter(tag = zone)
	else:
		title = "None"
		queryset = []


	context = {
		"title"		  : title,
		"object_list" : queryset
		}
	return render(request,"feedback.html",context)

