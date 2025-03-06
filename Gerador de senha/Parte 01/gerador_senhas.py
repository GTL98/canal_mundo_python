# --- Importar a função de escolha --- #
from random import choices

# --- Importar o módulo com os caracteres --- #
from caracteres import CARACTERES


def gerador_senhas(quantidade: int) -> str:
    """
    Função é responsável pela geração de uma senha aleatória.
    :param quantidade: Quantidade de caracteres na senha.
    :return: Uma string com a senha aleatória de tamanho n.
    """
    # --- Criar a senha baseada na quantidade de caracteres desejados --- #
    senha = choices(
        population=CARACTERES,
        k=quantidade
    )

    return ''.join(senha)


if __name__ == '__main__':
    senha = gerador_senha(20)
    print(senha)
