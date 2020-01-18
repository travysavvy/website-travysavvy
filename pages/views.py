from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

def contact(request):
    form = MessageForm()
    message_saved = False
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            m_obj = {
                "name" : form.cleaned_data["name"],
                "email" : form.cleaned_data["email"], 
                "subject" : form.cleaned_data["subject"],
                "message" : form.cleaned_data["message"],
                "ip" : get_client_ip(request),
                "host" : request.get_host()
            }
            message = Message(
                name=m_obj["name"],
                email=m_obj["email"], 
                subject=m_obj["subject"],
                message=m_obj["message"],
                ip=m_obj["ip"]
            )
            message.save()
            send_email_to_admin(m_obj)
            message_saved = True
    
    context = {
        "form" : form,
        "message_saved" : message_saved
    }
    return render(request, 'contact.html', context)