from django.http import HttpResponse, JsonResponse
from django.template import loader

def chat(request):
    if request.method == 'POST':
        return JsonResponse({'bot_response': 'Hi POST'})
    else:
        template = loader.get_template('bot.html')
    
    return HttpResponse(template.render())