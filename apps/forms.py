import json
from django import forms


class JsonFormMixin():
    def as_json(self) -> json:
        data = {name: field.to_python(self[name].data) for name, field in self.fields.items()}
        return json.dumps(data)


class CadastroForm(JsonFormMixin, forms.Form):
    nome = forms.CharField(label='NoMe', max_length=64, min_length=3, required=True)
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Email'}), required=True)
    idade = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'Idade'}))
    sexo = forms.ChoiceField(
        required=False,
        choices=[('M', 'Masculino'), ('F', 'Feminino'), ('O', 'Outros')])
    hobbie = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple, 
        choices=(
            ('futebol', 'Futebol'),
            ('game', 'Games'),
            ('leitura', 'Leitura')
        ),
    )
