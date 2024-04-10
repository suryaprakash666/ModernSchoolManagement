from datetime import date
from django.http import HttpResponse
from django.shortcuts import render 

from django.views.decorators.csrf import csrf_exempt
import pywhatkit

def staffhomeview(request):
    current_date = date.today()
    return render(request, 'Staffview.html',{'current_date': current_date})

def send_whatsapp_message(request):
    to_number = ""
    message_body = ""
    if request.method == 'POST':
        try:
            to_number = request.POST.get('StudentReference')  # Get recipient's number from POST data
            message_body = request.POST.get('Sendmessage')
            pywhatkit.sendwhatmsg_instantly(to_number, message_body)
            return render(request, 'Staffview.html')  # Return response_data in all cases
        # Too broad exception clause
        except ValueError:
            if not to_number or not message_body:
                return HttpResponse(request, "Enter a correct number")
