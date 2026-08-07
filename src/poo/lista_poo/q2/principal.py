from PyQt6 import uic
from PyQt6.QtWidgets import QApplication

Form, Window = uic.loadUiType("gui.ui")

app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
window.show()
app.exec()

# Executar esse comando para converter o arquivo gui.ui para gui.py
# pyuic6 -x gui.ui -o gui.py