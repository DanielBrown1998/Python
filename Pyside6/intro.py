from PySide6.QtWidgets import QApplication, QPushButton
import sys

app = QApplication(sys.argv)
button = QPushButton(r'pressione')
button.setStyleSheet('font-size: 40px')
button.show() #  adiciona o widget na hieraruia e exibe a janela
app.exec() #  loop da applicação
