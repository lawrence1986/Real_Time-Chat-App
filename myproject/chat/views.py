from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from chat.models import Thread
from django.http import HttpResponse


@login_required
def messages_page(request):
    threads = Thread.objects.by_user(user=request.user).prefetch_related('chatmessage_thread').order_by('timestamp')
    context = {
        'Threads': threads
    }
    return render(request, 'messages.html', context)


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('messages')  # Redirect to the home page or any other desired page
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('login')

def handle_404(request):
    return render(request, '404.html', {})

def user_search(request):
    if 'q' in request.GET:
        query = request.GET['q']
        users = User.objects.filter(username__icontains=query)
        print(users)
    else:
        users = User.objects.all()

    context = {'users': users}
    return render(request, 'messages.html', context)

@login_required
def start_chat(request, user_id):
    # Get the other user based on user_id
    other_user = get_object_or_404(User, id=user_id)

    # Check if a thread already exists between the current user and the other user
    thread = Thread.objects.filter(
        participants=request.user
    ).filter(participants=other_user).first()

    if not thread:
        # If no thread exists, create a new thread
        thread = Thread.objects.create()
        thread.participants.add(request.user, other_user)
        thread.save()

    # Redirect the user to the chat page with the thread_id
    return redirect('chat_detail', thread_id=thread.id)

