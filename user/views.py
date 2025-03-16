import os

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from .forms import BookingForm
from .models import Booking
from django.contrib.auth.decorators import login_required
from langchain.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_mistralai import ChatMistralAI

from dotenv import load_dotenv
load_dotenv(override=True)

def landing(request):
    context = {}
    if request.method == "POST":
        query = request.POST.get("user_query", "").strip()  # Fix here

        if query:  # Only proceed if the query is not empty
            # llm = ChatGoogleGenerativeAI(
            #     model="gemini-1.5-pro",
            #     temperature=0,
            #     max_tokens=None,
            #     timeout=None,
            #     max_retries=2,
            #     api_key=os.environ.get("GEMINI_API_KEY")
            # )

            llm = ChatMistralAI(
                model="mistral-large-latest",
                temperature=0,
                max_retries=2,
                api_key=os.environ.get("MISTRAL_API_KEY")
            )

            prompt_template = """You are a helpful AI assistant for El Carino, a company specializing in live streaming, media production, digital marketing, event management, and esports services. Your goal is to provide information, guide users through the website, and assist with inquiries.
            Based on the query: {query}. Make the response shorter in one or two sentences.
            """

            prompt = PromptTemplate(input_variables=["query"], template=prompt_template)
            chain = prompt | llm | StrOutputParser()
            ai_response = chain.invoke({"query": query})

            context["ai_response"] = ai_response

    return render(request, 'user/landing.html', context)


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username already taken!")
            elif User.objects.filter(email=email).exists():
                messages.error(request, "Email already registered!")
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                messages.success(request, "Registration successful! You can now log in.")
                return redirect('login')
        else:
            messages.error(request, "Passwords do not match!")

    return render(request, 'user/register.html')

def user_login(request):  # Renamed from login to user_login
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            auth_login(request, user)  # Use Django's built-in login function
            messages.success(request, "Logged in successfully!")
            return redirect('services')  # Redirecting to services page
        else:
            messages.error(request, "Invalid username or password.")

    return render(request, 'user/login.html')

def user_logout(request):  # Renamed from logout to user_logout
    auth_logout(request)  # Use Django's built-in logout function
    messages.success(request, "Logged out successfully!")
    return redirect('landing')

def services(request):
    return render(request, 'user/service.html')

def plan_view(request):
    return render(request, 'user/plan.html')

@login_required
def plan_view(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.name = request.user  # Assign logged-in user as the name
            booking.save()
            messages.success(request, "Booking request submitted successfully!")
            return redirect('plan')  # Redirect to the same page or another page after submission
        else:
            messages.error(request, "There was an error in your submission.")
    else:
        form = BookingForm()

    return render(request, 'user/plan.html', {'form': form})

def about(request):
    return render(request, 'user/about.html')

def blog(request):
    return render(request, 'user/blog.html')

def blog_detail(request):
    return render(request, 'user/blog_detail1.html')

def portfolio(request):
    return render(request, 'user/portfolio.html')

def wedding(request):
    return render(request, 'user/wedding.html')


def tedx(request):
    return render(request, 'user/tedx.html')

def mcd(request):
    return render(request, 'user/mcd.html')

def contactus(request):
    return render(request, 'user/contactus.html')