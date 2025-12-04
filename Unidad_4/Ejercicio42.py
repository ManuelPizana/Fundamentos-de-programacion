# -*- coding: utf-8 -*-
"""

Requisitos:
"""

#Comentar cuales son las librerias que se importan y para que funciona cada una 
#

import sys
# Es un módulo para acceder a parámetros y funciones específicas del sistema. 
# Se usa para la gestión de la aplicación (QApplication(sys.argv) y sys.exit()).
import platform
# Es un módulo para obtener información sobre el sistema operativo, lo cual es crucial para determinar los parámetros correctos del comando 'ping'.
import subprocess
# Es un módulo para ejecutar nuevos procesos/comandos del sistema operativo.
# Se utiliza para ejecutar el comando 'ping' y capturar su salida.
from PyQt5.QtCore import Qt # Módulo de constantes y tipos básicos.
from PyQt5.QtWidgets import (
    QApplication, # Gestiona el flujo de control y las configuraciones principales de la GUI.
    QWidget, # La clase base de todos los objetos de interfaz de usuario. Es nuestra ventana principal.
    QLabel, # Se usa para mostrar texto o imágenes estáticas.
    QLineEdit, # Un campo de entrada de texto de una sola línea.
    QPushButton, #Botón interactivo (para ejecutar el ping).
    QTextEdit, # Área de texto multi-línea (para mostrar la salida del ping).
    QVBoxLayout, # Distribuye los widgets verticalmente.
    QHBoxLayout, # Distribuye los widgets horizontalmente.
    QMessageBox, ## Clase para mostrar cuadros de diálogo de mensaje y advertencia.
)


class PingApp(QWidget):
    """Ventana principal de la aplicación."""

    def __init__(self):
        # Llama al constructor de la clase base QWidget
        super().__init__()
        self.setWindowTitle("Ping – PyQt5")
        self.resize(400, 300)

        # ---------- Widgets ----------
        # Entrada de host / IP
        self.host_input = QLineEdit(self)
        self.host_input.setPlaceholderText("Ejemplo: google.com o 8.8.8.8")

        # Botón de ejecutar ping
        self.ping_btn = QPushButton("Enviar ping", self)
        self.ping_btn.clicked.connect(self.ejecutar_ping)

        # Área de texto donde se mostrará la salida
        self.resultado = QTextEdit(self)
        self.resultado.setReadOnly(True)

        # ---------- Layout ----------
        # Layout horizontal para la etiqueta "Destino" y el campo de entrada.
        entrada_layout = QHBoxLayout()
        entrada_layout.addWidget(QLabel("Destino:", self))
        entrada_layout.addWidget(self.host_input)

        # Layout principal vertical que organiza todos los elementos
        main_layout = QVBoxLayout()
        main_layout.addLayout(entrada_layout)
        main_layout.addWidget(self.ping_btn)
        main_layout.addWidget(QLabel("Resultado:", self))
        main_layout.addWidget(self.resultado)

        self.setLayout(main_layout)

    # -----------------------------------------------------------------
    def ejecutar_ping(self):
        """Construye y ejecuta el comando ping, mostrando la salida."""
        host = self.host_input.text().strip()
        if not host:
            QMessageBox.warning(self, "Entrada vacía", "Introduce una dirección IP o nombre de host.")
            return

        # Determinar parámetros según SO
        sistema = platform.system().lower()
        if "windows" in sistema:
            cmd = ["ping", "-n", "4", host]         
        else:  # Linux, macOS, etc.
            cmd = ["ping", "-c", "4", host]       

        try:
            # Ejecutamos el comando y capturamos stdout + stderr
            proceso = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=10,            
            )
            salida = proceso.stdout if proceso.returncode == 0 else proceso.stderr
            self.resultado.setPlainText(salida)
        except subprocess.TimeoutExpired:
            self.resultado.setPlainText("Error: tiempo de espera agotado.")
        except Exception as e:
            self.resultado.setPlainText(f"Ocurrió un error inesperado:\n{e}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = PingApp()
    ventana.show()
    sys.exit(app.exec_())