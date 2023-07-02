from django import forms

class LoginForms(forms.Form):
    nome_login = forms.CharField(
        label="Nome de Usuario",
        required=True,
        max_length=100,
        widget= forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Nome de Usuario"
            }
        )
    )
    senha = forms.CharField(
        label="Senha",
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Senha"
            }
        )
    )


class CadastroForms(forms.Form):
    nome_cadastro = forms.CharField(
        label="Nome de Usuario",
        required=True,
        max_length=100,
        widget= forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Nome de Usuario"
            }
        )
    )
    email = forms.EmailField(
        label="Nome de Usuario",
        required=True,
        max_length=100,
        widget= forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": "Email "
            }
        )
    )
    senha = forms.CharField(
        label="Senha",
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Senha"
            }
        )
    )
    senha_2 = forms.CharField(
        label="Confirme Sua Senha",
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Repita Senha"
            }
        )
    )

    def clean_nome_cadastro(self):
        nome = self.cleaned_data.get("nome_cadastro")

        if nome:
            nome = nome.strip()

            if " " in nome:
                raise forms.ValidationError("Use apenas o primeiro nome sem espaços")
            else:
                return nome
