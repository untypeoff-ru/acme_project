from django import forms
from django.core.exceptions import ValidationError
from django.core.mail import send_mail

from .models import Birthday, Congratulation

BEATLES = {'Джон Леннон', 'Пол Маккартни', 'Джордж Харрисон', 'Ринго Старр'}


class BirthdayForm(forms.ModelForm):
    class Meta:
        model = Birthday
        exclude = ('author',)
        widgets = {
            'birthday': forms.DateInput(attrs={'type': 'date'})
        }

    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        return first_name.split()[0]

    def clean(self):
        super().clean()
        first_name = self.cleaned_data['first_name']
        last_name = self.cleaned_data['last_name']

        if f'{first_name} {last_name}' in BEATLES:
            send_mail(
                subject='Beatles',
                message=f'{first_name} {last_name} пытался зарегистрироваться',
                from_email='form@bd.net',
                recipient_list=['ant@ipov.ru'],
                fail_silently=True,
            )
            raise ValidationError('Имя не должно быть из битлз')


class CongratulationForm(forms.ModelForm):
    class Meta:
        model = Congratulation
        fields = ('text',)
