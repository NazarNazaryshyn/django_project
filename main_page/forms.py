from django import forms
from .models import UserReservation, UserContacts


class UserReservationForm(forms.ModelForm):
    name = forms.CharField(max_length=50,widget=forms.TextInput(attrs={
                                       'type': "text",
                                       'name': "name",
                                       'class': "form-control",
                                       'id': "name",
                                       'placeholder': "Your Name",
                                       'data-rule': "minlen:4",
                                       'data-msg': "Please enter at least 4 chars"
                           }))
    phone = forms.CharField(max_length=15,widget=forms.TextInput(attrs={
                                        'type': 'text', 'name': 'phone', 'id': 'phone', 'class': 'form-control',
                                        'placeholder': 'Телефон', 'required': 'required',
                                        'data-rule': 'minlen:4', 'data-msg': 'Please enter at least 4 chars'}))
    persons = forms.IntegerField(widget=forms.NumberInput(attrs={
                                        'type': "number",
                                        'class': "form-control",
                                        'name': "people",
                                        'id': "people",
                                        'placeholder': "# of people",
                                        'data-rule': "minlen:1",
                                        'data-msg': "Please enter at least 1 chars"}))

    message = forms.CharField(max_length=400,widget=forms.Textarea(attrs={
                                        'type': 'message', 'name': 'message', 'class': 'form-control',
                                        'rows': '5', 'placeholder': 'Сообщение', 'required': 'required'}))


    class Meta:
        model = UserReservation
        fields = ('name', 'phone', 'persons', 'message')


class UserContactsForm(forms.ModelForm):

    name = forms.CharField(max_length=40, widget=forms.TextInput(attrs={
        'type':"text",
        'name ': "name",
        'class':"form-control",
        'id': "name",
        'placeholder':"Your Name",
        'required':'required'
    }))

    email = forms.EmailField(max_length=100, widget=forms.EmailInput(attrs={
        'type':"email",
        'class' :"form-control",
        'name' : "email",
        "id" : "email",
        'placeholder' : "Your Email",
        'required': 'required'

    }))

    subject = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'type': "text",
        'class': "form-control",
        'name': "subject",
        "id": "subject",
        'placeholder': "Subject"

    }))
    message = forms.CharField(max_length=500, widget=forms.Textarea(attrs={
        'class': "form-control",
        'name': "message",
        'rows': "5",
        'placeholder': "Message",
        'required': 'required'

    }))

    class Meta:
        model = UserContacts
        fields = ('name', 'email', 'subject', 'message')