from django.db import models
from django.utils import timezone
from libgravatar import Gravatar


# Create your models here.
class Event(models.Model):
    """Classe contendo o evento propriamente dito, sua data, descrição
    e também prioridade."""

    priorities_list = (
        ('0', 'Sem prioridade'),
        ('1', 'Normal'),
        ('2', 'Urgente'),
        ('3', 'Muito Urgente'),
    )

    date = models.DateField()
    event = models.CharField(max_length=80)
    priority = models.CharField(max_length=1, choices=priorities_list)

    class Meta:
        ordering = ('-date', '-priority', 'event',)

    def number_of_comments(self):
        """Retorna a quantidade de comentários dentro de um evento."""
        return self.comment_event.count()

    def __str__(self):
        return self.event


class Comment(models.Model):
    """Comentários efetuados em um determinado evento."""

    author = models.CharField(max_length=80)
    email = models.EmailField()
    text = models.CharField(max_length=160)
    commented = models.DateTimeField(default=timezone.now)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='comment_event')

    def avatar(self):
        """Retorna a partir do endereço de e-mail, um avatar
        configurado no Gravatar ou um dos avatares padrão deles."""
        g = Gravatar(self.email)
        return g.get_image(default='identicon')

    def __str__(self):
        return "{} commentou em {:%c}".format(self.author, self.commented)

class Cadastro(models.Model):
    """Classe contendo o evento propriamente dito, sua data, descrição
    e também prioridade."""

    sexo_list = (
        ('0', 'masculino'),
        ('1', 'feminino'),
        ('2', 'outro'),
        
    )

    raca_list= (
        ('0', 'afro'),
        ('1', 'branco'),
        ('2', 'pardo'),

    )

    nome = models.CharField(max_length=80)
    idade = models.CharField(max_length=80) 
    nacionalidade = models.CharField(max_length=80)
    pebom = models.CharField(max_length=80)
    posicao = models.CharField(max_length=80)
    sexo = models.CharField(max_length=1, choices=sexo_list)
    raca = models.CharField(max_length=1, choices=raca_list)



    def __str__(self):
        return self.nome