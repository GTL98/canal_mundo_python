class Quadrado:
    def __init__(self, posicao_centro, tamanho=[200, 200]):
        self.posicao_centro = posicao_centro
        self.tamanho = tamanho

    def atualizar(self, cursor):
        cx, cy = self.posicao_centro
        a, l = self.tamanho

        if cx - l // 2 < cursor[0][0][1] < cx + l // 2 and cy - a // 2 < cursor[0][0][2] < cy + a // 2:
            self.posicao_centro[0] = cursor[0][0][1]
            self.posicao_centro[1] = cursor[0][0][2]