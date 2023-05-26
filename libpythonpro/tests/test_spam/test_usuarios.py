from libpythonpro.spam.modelos import Usuario


def test_salvar_usuario(sessao):
    usuario = Usuario(nome='Renzo', email='renzo@python.pro.br')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)
#aqui é para salvar o email de cada usuario
def test_listar_usuarios(sessao):
    usuarios = [
        Usuario(nome='Renzo', email='renzo@python.pro.br'),
        Usuario(nome='Luciano', email='luciano@python.pro.br')
    ]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()
#aqui é a lista onde os usuarios serão salvos
