from django.forms import ModelForm
from app.models import Cliente, Agendamento, Orcamento

class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'cpf', 'rg', 'data_nasc', 'telefone', 'email', 'rua', 'numero', 'complemento', 'bairro', 'cidade']

class AgendamentoForm(ModelForm):
    class Meta:
        model = Agendamento
        fields = ['cliente', 'modelo', 'marca', 'ano', 'placa', 'data_insp', 'horario', 'descricao']


class OrcamentoForm(ModelForm):
    class Meta:
        model = Orcamento
        fields = ['cliente', 'modelo', 'marca', 'ano', 'tipo', 'tempo_conserto', 'valor']