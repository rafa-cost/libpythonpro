import pytest

from libpythonpro.spam.enviador_de_email import Enviador, EmailInvalido


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None

#aqui esta testanto o envio de email, remetente é quem esta enviando, e logo abaixo segue o destinatario, assunto e corpo
@pytest.mark.parametrize('remetente',['foo@bar.com.br', 'renzo@python.pro.br'])
def test_remetente(remetente):
    enviador = Enviador()
    resultado = enviador.enviar(
        remetente,
        'luciano@python.pro.br',
        'Cursos Python Pro',
        'Primeira turma Guido Von Rossum aberta'
    )
    assert remetente in resultado


#aqui é um teste de remetente invalido , um campo vazio e outro com um email inexistente
@pytest.mark.parametrize('remetente',['', 'renzo'])
def test_remetente_invalido(remetente):
    enviador = Enviador()
    with pytest.raises(EmailInvalido):
        enviador.enviar(
            remetente,
            'luciano@python.pro.br',
            'Cursos Python Pro',
            'Primeira turma Guido Von Rossum aberta'
        )

