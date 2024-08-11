from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

def game_view(request):
    user_id = request.GET.get('user_id', '')
    return render(request, 'index.html', {'user_id': user_id})

@csrf_exempt
def submit_score(request):
    if request.method == 'POST':
        score = request.POST['score']
        # Get user_id from the request data
        user_id = request.POST['user_id']  

        # Save the score to the database or handle it as needed
        if user_id:
            player_score, created = PlayerScore.objects.update_or_create(
                user_id=user_id,
                defaults={'score': score}
            )
            if not created:
                # If the record already exists, update the score
                player_score.score += score
                player_score.save()
        else:
            score = 0
            message = "User ID is required"
            context = {
                'score':score,
                'message':message
            }
            return render (request, 'score.html', context)

        context = {
            'score':score
        }
        return render (request, 'score.html', context)
