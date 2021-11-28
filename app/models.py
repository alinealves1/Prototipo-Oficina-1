from django.db import models

# Create your models here.
class Cliente(models.Model):
    nome = models.CharField('Nome', max_length=150)
    cpf = models.CharField('CPF', max_length=20)
    rg = models.CharField('RG', max_length=15)
    data_nasc = models.DateField('Data de Nascimento')
    telefone = models.CharField('Telefone', max_length=15)
    email = models.CharField('Email', max_length=50, null=True, blank=True)
    rua = models.CharField('Rua', max_length=150)
    numero = models.CharField('Numero', max_length=10)
    complemento = models.CharField('Complemento', max_length=120, null=True,blank=True)
    bairro = models.CharField('Bairro', max_length=100)
    cidade = models.CharField('Cidade', default='Itapevi', max_length=50)


class Agendamento(models.Model):
    HORARIO_CHOICES = [
        (8, '8:00'),
        (9, '9:00'),
        (10, '10:00'),
        (11, '11:00'),
        (12, '12:00'),
        (13, '13:00'),
        (14, '14:00'),
        (15, '15:00'),
        (16, '16:00'),
        (17, '17:00'),
        (18, '18:00'),
    ]
    #cpf_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    cliente = models.OneToOneField(Cliente, on_delete=models.CASCADE)
    modelo = models.CharField(max_length=30)
    marca = models.CharField(max_length=30)
    ano = models.IntegerField()
    placa = models.CharField(max_length=8)
    data_insp = models.DateField('Data da Inspeção')
    horario = models.IntegerField('Horario da Inspeção', choices=HORARIO_CHOICES)
    descricao = models.TextField('Descrição do Problema')
    def __str__(self):
        return self.cliente

class Orcamento(models.Model):
    SERVICOS_CHOICES = [
        (1, 'Manutenção da Embreagem'),
        (2, 'Revisão dos componentes de freio'),
        (3, 'Revisão do Sistema de Arrefecimento'),
        (4, 'Troca de óleo do motor'),
        (5, 'Troca de óleo do câmbio automático'),
        (6, 'Troca de filtros'),
        (7, 'Troca de lâmpadas'),
        (8, 'Alinhamento e Balanceamento'),

    ]
    cliente = models.OneToOneField(Cliente, on_delete=models.CASCADE)
    modelo = models.CharField('Modelo do Veículo:', max_length=30)
    marca = models.CharField('Meca do Veículo:', max_length=30)
    ano = models.IntegerField('Ano do Veículo:')
    tipo =models.IntegerField('Tipo de Serviços:', choices=SERVICOS_CHOICES)
    tempo_conserto = models.IntegerField('Tempo de Conserto:')
    valor = models.CharField('Valor do Serviço: R$', max_length=9)
    def __str__(self):
        return self.valor
