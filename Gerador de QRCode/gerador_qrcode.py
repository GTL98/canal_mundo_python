# --- Importar a biblioteca do QRCode --- #
import qrcode

qr = qrcode.QRCode(
    box_size=10,
    border=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H
)

# --- Armazenar o valor do dado --- #
dado = 'WIFI:S:nome_da_rede;T:tipo_de_criptografia;P:senha;;'

# --- Definir o dado que será passado para o QRCode --- #
qr.add_data(dado)

# --- Criar o QRCode --- #
qr.make()

# --- Criar a imagem do QRCode --- #
imagem = qr.make_image(fill_color='black', bank_color='white')

# --- Salvar a imagem --- #
imagem.save('qrcode.png')