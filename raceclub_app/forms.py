from django import forms


class FeedbackForm(forms.Form):
    name = forms.CharField(label='Имя', max_length=10, min_length=3, error_messages={
        'max_length': 'Слишком много символов',
        'min_length': 'Слишком мало символов',
        'required': 'Нужно указать хотя бы три символа',
    })
    nickname = forms.CharField(label='Никнейм', max_length=10, min_length=3, error_messages={
        'max_length': 'Слишком много символов',
        'min_length': 'Слишком мало символов',
        'required': 'Нужно указать хотя бы три символа',
    })
    feedback = forms.CharField(label='Развернутый отзыв', widget=forms.Textarea(attrs={'rows': 4, 'cols': 25}), max_length=300, min_length=10,
                               error_messages={
        'max_length': 'Слишком много символов',
        'min_length': 'Слишком мало символов',
        'required': 'Нужно указать хотя бы три символа',
    })
    rating = forms.IntegerField(label='Оценка игры', max_value=5, min_value=1)