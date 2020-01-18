from django import forms

class MessageForm(forms.Form):
    name = forms.CharField(
        max_length=60,
        widget=forms.TextInput(attrs={
            "class": "contact_input contact_input_name",
            "placeholder": "Name"
        })
    )
    email = forms.CharField(
        max_length=60,
        widget=forms.TextInput(attrs={
            "class": "contact_input contact_input_email",
            "placeholder": "Email"
        })
    )
    subject = forms.CharField(
        max_length=60,
        widget=forms.TextInput(attrs={
            "class": "contact_input contact_input_subject",
            "placeholder": "Subject"
        })
    )
    message = forms.CharField(widget=forms.Textarea(
        attrs={
            "class": "contact_message_input contact_input_message",
            "placeholder": "Message"
        })
    )