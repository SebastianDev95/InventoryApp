from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, get_user_model

User = get_user_model()

class RegisterForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=150,
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'FIRST NAME',
            'id': 'firstName'
        })
    )
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'placeholder': 'EMAIL ADDRESS',
            'id': 'email'
        })
    )
    password1 = forms.CharField(
        label="Password", # Añadido label para claridad
        widget=forms.PasswordInput(attrs={
            'placeholder': 'PASSWORD',
            'id': 'password'
        })
    )
    password2 = forms.CharField(
        label="Confirm Password", # Añadido label para claridad
        widget=forms.PasswordInput(attrs={
            'placeholder': 'CONFIRM PASSWORD',
            'id': 'password2'
        })
    )
    terms = forms.BooleanField(
        label="Acepto los términos y condiciones", # Añadido label
        required=True,
        widget=forms.CheckboxInput(attrs={'id': 'terms'})
    )
    
    class Meta:
        model = User
        # --- CORRECCIÓN CRÍTICA ---
        # 'fields' solo debe contener campos del *modelo* (User).
        # 'password1' y 'password2' son campos del *formulario*, no del modelo.
        fields = ['first_name', 'email']
    
    def clean_email(self):
        """
        Validación para asegurar que el email sea único.
        """
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Ya existe un usuario con este correo electrónico.")
        return email

    def save(self, commit=True):
        # super().save(commit=False) llamará a ModelForm.save(), 
        # que usará Meta.fields ('first_name', 'email') para poblar el objeto.
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.username = self.cleaned_data['email']  # Usar email como username
        user.first_name = self.cleaned_data['first_name']
        if commit:
            user.save()
        return user


class EmailLoginForm(forms.Form):
    email = forms.EmailField(
        label="Correo electrónico",
        widget=forms.EmailInput(attrs={'placeholder': 'EMAIL ADDRESS'})
    )
    password = forms.CharField(
        label="Contraseña",
        widget=forms.PasswordInput(attrs={'placeholder': 'PASSWORD'})
    )

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')

        if email and password:
            try:
                # Buscamos al usuario por su email
                user_obj = User.objects.get(email=email)
            except User.DoesNotExist:
                raise forms.ValidationError("Correo o contraseña incorrectos.")

            # Autenticamos usando el 'username' de ese usuario
            user = authenticate(username=user_obj.username, password=password)
            
            if not user:
                # La contraseña estaba incorrecta
                raise forms.ValidationError("Correo o contraseña incorrectos.")

            # --- MEJORA ---
            # Comprobamos si la cuenta está activa
            if not user.is_active:
                raise forms.ValidationError("Esta cuenta está inactiva.")

            cleaned_data['user'] = user
        
        return cleaned_data