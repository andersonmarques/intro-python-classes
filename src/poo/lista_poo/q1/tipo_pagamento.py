from enum import Enum

class Tipo_Pagamento(Enum):
    DEBITO = "Cartao de Debito"
    CREDITO = "Cartao de Credito"
    PIX = "Pix"
    CHEQUE = "Cheque"
    DINHEIRO = "Dinheiro"
