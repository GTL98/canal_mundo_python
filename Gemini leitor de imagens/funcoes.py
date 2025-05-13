def resposta_gemini(modelo, imagem, prompt):
    """
    Função que recebe a imagem, o prompt e retorna o que o usuário pediu.
    :param modelo: Modelo Gemini.
    :param imagem: Imagem para analisar.
    :param prompt: Entrada do usuário.
    :return: Resposta do Gemini.
    """
    # --- Gerar a repsosta --- #
    resposta = modelo.generate_content([imagem[0], prompt])
    return resposta.text


def imagem2bytes(imagem_upload):
    """
    Função responsável por transformar a imagem em bytes.
    :param imagem_upload: Imagem carregada.
    :return: Informações da imagem.
    """
    # --- Verificar se a imagem foi carregada --- #
    if imagem_upload is not None:
        # --- Converter a imagem carregada em bytes --- #
        imagem_bytes = imagem_upload.getvalue()

        # --- Partes da imagem --- #
        partes_imagem = [
            {
                'mime_type': imagem_upload.type,
                'data': imagem_bytes
            }
        ]
        return partes_imagem

    else:
        # --- Informar que nenhuma imagem foi carregada --- #
        raise FileNotFoundError('Não foi feito o upload da imagem.')