# quiz_app/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.contrib import messages
from .models import Question, Choice, QuizResult, UserAnswer
import random


def home(request):
    """Page d'accueil du quiz"""
    return render(request, 'quiz_app/home.html')


#@login_required
def quiz_view(request):
    """Affiche le quiz avec les questions"""
    if request.method == 'POST':
        return submit_quiz(request)

    # Récupérer 5 questions aléatoires
    questions = list(Question.objects.all())
    if len(questions) >= 5:
        selected_questions = random.sample(questions, 5)
    else:
        selected_questions = questions

    context = {
        'questions': selected_questions,
        'total_questions': len(selected_questions),
    }
    return render(request, 'quiz_app/quiz.html', context)


def submit_quiz(request):
    """Soumet le quiz et calcule le score"""
    if request.method != 'POST':
        return redirect('quiz')

    questions = Question.objects.all()
    score = 0
    total_questions = len(questions)

    # Stocker les réponses de l'utilisateur
    for question in questions:
        selected_choice_id = request.POST.get(f'question_{question.id}')
        if selected_choice_id:
            try:
                selected_choice = Choice.objects.get(id=selected_choice_id)
                is_correct = selected_choice.is_correct

                # Enregistrer la réponse utilisateur
                UserAnswer.objects.create(
                    user=request.user,
                    question=question,
                    selected_choice=selected_choice,
                    is_correct=is_correct
                )

                if is_correct:
                    score += 1

            except Choice.DoesNotExist:
                pass

    # Enregistrer le résultat final
    QuizResult.objects.create(
        user=request.user,
        score=score,
        total_questions=total_questions
    )

    messages.success(request, f'Quiz terminé ! Votre score : {score}/{total_questions}')
    return redirect('results')


#@login_required
def results_view(request):
    """Affiche les résultats"""
    results = QuizResult.objects.filter(user=request.user).order_by('-completed_at')
    context = {
        'results': results,
    }
    return render(request, 'quiz_app/results.html', context)


def create_sample_data():
    """Crée des données d'exemple (à exécuter une fois)"""
    # Créer des questions et réponses
    if not Question.objects.exists():
        questions_data = [
            {
                'text': "Quelle est la capitale de la France ?",
                'choices': [
                    ("Paris", True),
                    ("Lyon", False),
                    ("Marseille", False),
                    ("Toulouse", False)
                ]
            },
            {
                'text': "Quel est le plus grand océan du monde ?",
                'choices': [
                    ("Océan Atlantique", False),
                    ("Océan Pacifique", True),
                    ("Océan Indien", False),
                    ("Océan Arctique", False)
                ]
            },
            {
                'text': "Qui a peint la Joconde ?",
                'choices': [
                    ("Michel-Ange", False),
                    ("Raphaël", False),
                    ("Léonard de Vinci", True),
                    ("Donatello", False)
                ]
            },
            {
                'text': "Quelle est la plus grande planète du système solaire ?",
                'choices': [
                    ("Mars", False),
                    ("Jupiter", True),
                    ("Saturne", False),
                    ("Vénus", False)
                ]
            },
            {
                'text': "Combien de côtés a un triangle ?",
                'choices': [
                    ("3", True),
                    ("4", False),
                    ("5", False),
                    ("6", False)
                ]
            }
        ]

        for q_data in questions_data:
            question = Question.objects.create(question_text=q_data['text'])
            for choice_text, is_correct in q_data['choices']:
                Choice.objects.create(
                    question=question,
                    choice_text=choice_text,
                    is_correct=is_correct
                )


# Vue pour créer des données d'exemple (à utiliser une fois)
def create_sample_questions(request):
    """Crée des questions d'exemple"""
    create_sample_data()
    return JsonResponse({'status': 'success', 'message': 'Questions créées avec succès'})
