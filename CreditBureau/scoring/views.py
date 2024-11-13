from django.shortcuts import render, redirect
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth import authenticate, login, logout
from .models import Question, UserResponse
from .utils import calculate_credit_score
# from django.http import HttpResponse
# from django.contrib import messages


def question_view(request):
    if request.method == 'POST':
        responses = []
        for question_id, answer in request.POST.items():
            if question_id.startswith('question_'):
                question = Question.objects.get(id = question_id.split('_')[1])
                responses.append(UserResponse(question = question, answer = answer))
                responses[-1].save()
                
        score = calculate_credit_score(responses)
        return render(request, 'results.html', {'score': score})
    
    questions = Question.objects.all()
    return render(request, 'questions.html', {'questions': questions})











# def custom_login(request):
#     if request.method == "POST":
#         username  = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username = username, password= password)
#         if user is not None:
#             login(request, user)
#             return redirect('home')
        
#         else:
#             messages.error(request, "Invalid username or password.")
            
    # return render(request, 'scoring/login.html')


# def custom_logout(request):
#     logout(request)
#     return redirect('login')


        
        
        
        
        
        
def home_view(request):
#     print("Home view accessed")
#     return HttpResponse("Welcome to the Home Page")
    return render(request, 'home.html')



# @login_required
# def form_page(request):
#     questions = Question.objects.all()
#     if request.method == "POST":
#         for question in questions:
#             answer = request.POST.get(f'question_{question.id}')
#             UserResponse.objects.create(
#                 user=request.user,
#                 question=question,
#                 answer=answer
#             )
#         return redirect('results_page')
#     return render(request, 'form_page.html', {'questions': questions})

# @login_required
# def results_page(request):
#     responses = UserResponse.objects.filter(user=request.user)
#     credit_score = calculate_credit_score(responses)
#     return render(request, 'results_page.html', {'credit_score': credit_score})
