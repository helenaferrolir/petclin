class Usuario:
    def __init__(self, nome, telefone, email, cpf, endereco, data_cadastro):
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.cpf = cpf
        self.endereco = endereco
        self.data_cadastro = data_cadastro


class Funcionario(Usuario):
    def __init__(self, salario, funcao, horario, escala, login, senha):
        self.salario = salario
        self.funcao = funcao
        self.horario = horario
        self.escala = escala
        self.login = login
        self.senha = senha
        self.historico_ferias = []  # list<ferias>


class Cliente(Usuario):
    def __init__(self):
        self.pets = []  # list<animal>
        self.caixa_msgs = []  # list<string>


class Animal:
    def __init__(self, nome, idade, raca, porte):
        self.nome = nome
        self.idade = idade
        self.raca = raca
        self.porte = porte
        self.vacinas = []  # list<vacina>
        self.historico = []  # list<atendimento>


class Atendimento:
    def __init__(self, data: str, hora: str, animal: Animal, tutor: Cliente, motivo: str, tipo: str, pagamento: float):
        self.data = data
        self.hora = hora
        self.animal = animal
        self.tutor = tutor
        self.motivo = motivo
        self.tipo = tipo
        self.pagamento = pagamento  # classe pagamento
