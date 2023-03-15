from django.db import models


# Create your models here.
class Cadastro(models.Model):
    nome = models.CharField(max_length=64, min_length=3, required=True)
    email = models.EmailField(required=True)
    idade = models.IntegerField()
    sexo = models.CharField(
        max_length=1,
        required=False,
        choices=[('M', 'Masculino'), ('F', 'Feminino'), ('O', 'Outros')]
    )
    hobbie = models.MultipleChoiceField(
        choices=(
            ('futebol', 'Futebol'),
            ('game', 'Games'),
            ('leitura', 'Leitura')
        ),
    )
