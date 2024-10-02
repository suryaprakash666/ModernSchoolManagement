import re
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render

def evaluate_expression(expression):
    # Check if the expression contains only valid characters
    if re.match(r'^[0-9+\-*/.]+$', expression):
        try:
            # Safely evaluate the mathematical expression
            return eval(expression)
        except Exception:
            return 'Invalid Input'
    else:
        return 'Invalid Input'

@csrf_exempt
def gradingtabview(request):
    if request.method == 'POST':
        div1 = request.POST.get('div1') or request.session.get('div1mark', 0)
        div2 = request.POST.get('div2') or request.session.get('div2mark', 0)
        div3 = request.POST.get('div3') or request.session.get('div3mark', 0)
        div4 = request.POST.get('div4') or request.session.get('div4mark', 0)

        if request.POST.get('div1'):
            total_mark_in_div1 = evaluate_expression(div1)
            request.session['div1mark'] = total_mark_in_div1
        else:
            total_mark_in_div1 = request.session.get('div1mark', 0)

        if request.POST.get('div2'):
            total_mark_in_div2 = evaluate_expression(div2)
            request.session['div2mark'] = total_mark_in_div2
        else:
            total_mark_in_div2 = request.session.get('div2mark', 0)

        if request.POST.get('div3'):
            total_mark_in_div3 = evaluate_expression(div3)
            request.session['div3mark'] = total_mark_in_div3
        else:
            total_mark_in_div3 = request.session.get('div3mark', 0)

        if request.POST.get('div4'):
            total_mark_in_div4 = evaluate_expression(div4)
            request.session['div4mark'] = total_mark_in_div4
        else:
            total_mark_in_div4 = request.session.get('div4mark', 0)

        total_marks = total_mark_in_div1+total_mark_in_div2+total_mark_in_div3+total_mark_in_div4

        if total_marks >40 :
            status = "pass"
        else:
            status = "fail"
        return render(request, 'GradingTab.html', {
            'div1mark': total_mark_in_div1,
            'div2mark': total_mark_in_div2,
            'div3mark': total_mark_in_div3,
            'div4mark': total_mark_in_div4,
            'status':status
        })
    else:
        return render(request, 'GradingTab.html')
