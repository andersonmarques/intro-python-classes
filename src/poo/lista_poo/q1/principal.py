# pyuic6 -x gui.ui -o gui.py
import sys
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication, QMainWindow
from gui_qt_designer import Ui_MainWindow
from cliente import Cliente
from io_.gerente_arquivo import Gerente_Arquivos

class Principal(Ui_MainWindow, QMainWindow):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        super().setupUi(self)
        self.frame_msg.hide()
        self.lista_clientes = []
        self.gerente = Gerente_Arquivos()
        self.gerente.ler_todas_linhas_arquivo('arquivo.txt')
        self.cor_sucesso = "background-color: rgb(209, 255, 209);"
        self.cor_erro = "background-color: rgb(250, 185, 185);"

        #### acoes dos botoes ###
        self.pushButton_salvar_cliente.clicked.connect(
            self.salvar_cliente
            )
        self.pushButton_fechar_msg.clicked.connect(
            lambda: self.frame_msg.hide()
            )
        

    def salvar_cliente(self):
        nome = self.lineEdit_nome.text()
        cpf  = self.lineEdit_cpf.text()
        c = Cliente(nome, cpf)
        if not c.erro: # se erro estiver com texto entao VERDADE
            self.lista_clientes.append(c)
            self.gerente.escrever_arquivo(c)
            self.frame_msg.show()
            self.label_msg.setText("Cliente salvo.")
            self.label_msg.setStyleSheet(self.cor_sucesso)
        else:
            self.frame_msg.show()
            self.label_msg.setText(f"{c.erro}")
            self.label_msg.setStyleSheet(self.cor_erro)
    
    # Sobrescrevendo o evento de fechamento
    def closeEvent(self, event):
        print("\n--- Exibindo conteúdo da lista antes de fechar ---")
        for item in self.lista_clientes:
            print(item)
        print("--------------------------------------------------\n")
        
        # IMPORTANTE: Aceita o evento e permite que a janela feche
        event.accept()

if __name__ == "__main__":
    qt = QApplication(sys.argv)    
    principal = Principal()
    principal.show()
    qt.exec()