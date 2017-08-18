from django import forms


class SpotifySearchForm(forms.Form):
    """Searching form"""
    KIND_CHOICES = (
        ('album', 'album'),
        ('artist', 'artist'),
        ('track', 'track'),
        ('playlist', 'playlist')
    )

    text = forms.CharField(label='Search text', max_length=200, required=True)
    kind = forms.ChoiceField(label='Type', choices=KIND_CHOICES, required=True)
    limit = forms.IntegerField(label='Number of results', min_value=1, max_value=50, required=True)