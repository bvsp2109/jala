from django import forms
from JalaApp.models import JALAModel


class JalaForm(forms.ModelForm):
    First_Name=forms.CharField(label='First Name', widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    Last_Name=forms.CharField(label='Last Name', widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))
    Email_id=forms.CharField(label='Email id', widget=forms.EmailInput(attrs={'placeholder': 'Email Id'}))
    Location=forms.CharField(label='Location', widget=forms.TextInput(attrs={'placeholder': 'Location'}))
    Massage=forms.CharField(label='Massage', widget=forms.Textarea(attrs={'placeholder': 'Massage'}))



    class Meta:
        model = JALAModel
        fields = (
            'First_Name',
            'Last_Name',
            'Email_id',
            'Location',
            'Massage',


                  )

    def save(self, commit=True):
        user = super(JalaForm, self).save(commit=False)
        user.First_Name = self.cleaned_data['First_Name']
        user.Last_Name = self.cleaned_data['Last_Name']
        user.Email_id = self.cleaned_data['Email_id']
        user.Location = self.cleaned_data['Location']
        user.Massage = self.cleaned_data['Massage']



        if commit:
            user.save()
            return user