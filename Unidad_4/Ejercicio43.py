# -*- coding: utf-8 -*-

import sys
from pathlib import Path
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QMessageBox,
)


class RegistroAlumnos(QWidget):
    """Ventana principal de la aplicación."""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Registro de Alumnos")
        self.resize(350, 250)

        # ------------------ Widgets ------------------
        self.nombre_edit = QLineEdit(self)
        self.nombre_edit.setPlaceholderText("Ej.: Ana García")

        self.carrera_edit = QLineEdit(self)
        self.carrera_edit.setPlaceholderText("Ej.: Ingeniería Informática")
        
        # Nuevo campo para la Edad
        self.edad_edit = QLineEdit(self)
        self.edad_edit.setPlaceholderText("Ej.: 20")
        
        # Se puede forzar que solo se muestre el teclado numérico en ciertos contextos,
        # pero aquí permitimos cualquier entrada para validar en 'guardar_alumno'.

        self.guardar_btn = QPushButton("Guardar", self)
        self.guardar_btn.clicked.connect(self.guardar_alumno)

        self.limpiar_btn = QPushButton("Limpiar", self)
        self.limpiar_btn.clicked.connect(self.limpiar_campos)

        # ------------------ Layout -------------------
        form_layout = QVBoxLayout()

        # Nombre
        fila_nombre = QHBoxLayout()
        fila_nombre.addWidget(QLabel("Nombre:", self))
        fila_nombre.addWidget(self.nombre_edit)
        form_layout.addLayout(fila_nombre)

        # Carrera
        fila_carrera = QHBoxLayout()
        fila_carrera.addWidget(QLabel("Carrera:", self))
        fila_carrera.addWidget(self.carrera_edit)
        form_layout.addLayout(fila_carrera)
        
        # Edad (NUEVA FILA)
        fila_edad = QHBoxLayout()
        fila_edad.addWidget(QLabel("Edad:", self))
        fila_edad.addWidget(self.edad_edit)
        form_layout.addLayout(fila_edad)

        # Botones
        botones_layout = QHBoxLayout()
        botones_layout.addStretch()
        botones_layout.addWidget(self.guardar_btn)
        botones_layout.addWidget(self.limpiar_btn)
        form_layout.addLayout(botones_layout)

        self.setLayout(form_layout)

        # Ruta del archivo donde se guardarán los datos
        self.ruta_archivo = Path("alumnos.txt")

    # -------------------------------------------------
    def guardar_alumno(self):
        """
        Recupera los datos, valida la edad, verifica la mayoría de edad,
        y guarda el registro en el archivo.
        """
        nombre = self.nombre_edit.text().strip()
        carrera = self.carrera_edit.text().strip()
        edad_text = self.edad_edit.text().strip() # Obtener la edad como texto

        # 1. Validación de campos obligatorios
        if not nombre or not carrera or not edad_text:
            QMessageBox.warning(
                self,
                "Campos incompletos",
                "Debes rellenar el nombre, la carrera y la edad.",
            )
            return

        # 2. Validación de la edad como número entero
        try:
            edad = int(edad_text)
            if edad <= 0 or edad > 150:
                 # Si la edad es <= 0 o irreal (ej. > 150), lanzamos un error de valor
                 raise ValueError("Edad fuera del rango válido.")
        except ValueError:
            QMessageBox.critical(
                self,
                "Error de edad",
                "La edad debe ser un número entero válido (1-150).",
            )
            return

        # 3. Comprobación de mayoría de edad (Requisito)
        mensaje_edad = ""
        if edad >= 18:
            mensaje_edad = "\n¡El alumno es mayor de edad!"

        # Formato de la línea para el archivo
        linea = f"{nombre}, {carrera}, {edad}\n"

        # 4. Guardar en el archivo
        try:
            with self.ruta_archivo.open("a", encoding="utf-8") as f:
                f.write(linea)
        except OSError as e:
            QMessageBox.critical(
                self,
                "Error de escritura",
                f"No se pudo guardar el registro.\nDetalle: {e}",
            )
            return

        # 5. Mostrar confirmación
        final_message = f"Alumno guardado correctamente en '{self.ruta_archivo}'."
        
        QMessageBox.information(
            self,
            "Guardado",
            final_message + mensaje_edad, # Se añade el mensaje de edad al final
        )
        self.limpiar_campos()

    def limpiar_campos(self):
        """Limpia todos los campos de entrada de la interfaz."""
        self.nombre_edit.clear()
        self.carrera_edit.clear()
        self.edad_edit.clear() # Limpiar el nuevo campo de edad
        self.nombre_edit.setFocus()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = RegistroAlumnos()
    ventana.show()
    sys.exit(app.exec_())