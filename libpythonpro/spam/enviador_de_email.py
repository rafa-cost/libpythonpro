class Enviador:
    def enviar(self, remetente, destinatario, assunto, corpo):
        if '@' not in remetente:
            raise EmailInvalido(f'Email de remetente inválido: {remetente}')
        return remetente

class EmailInvalido(Exception):
    pass
#classe enviador com seu metodo enviar e seus atributos, e a classe email invalido