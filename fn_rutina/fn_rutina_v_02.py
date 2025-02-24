#fn_rutina_v_02.py

import pyttsx3
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import speech_recognition as sr

# Configuración de SQLAlchemy
Base = declarative_base()

class Rutina(Base):
    __tablename__ = "rutinas"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String, nullable=False)
    tipo = Column(String, nullable=False)
    pasos = Column(String, nullable=False)

class BasicVoiceBot:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.recognizer = sr.Recognizer()

    def hablar(self, mensaje):
        print(mensaje)
        self.engine.say(mensaje)
        self.engine.runAndWait()

    def escuchar(self):
        with sr.Microphone() as source:  # Crear una nueva instancia de micrófono en cada llamada
            self.hablar("Estoy escuchando...")
            try:
                self.recognizer.adjust_for_ambient_noise(source)
                audio = self.recognizer.listen(source)
                texto = self.recognizer.recognize_google(audio, language="es-ES")
                self.hablar(f"Entendido: {texto}")
                return texto
            except sr.UnknownValueError:
                self.hablar("No entendí lo que dijiste. Intenta nuevamente.")
                return self.escuchar()
            except sr.RequestError:
                self.hablar("Error con el servicio de reconocimiento de voz.")
                return ""

class GestorRutinas:
    def __init__(self):
        # Configuración de la base de datos
        self.engine = create_engine("sqlite:///rutina2025.sqlite")
        Base.metadata.create_all(self.engine)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()
        self.bot = BasicVoiceBot()

    def crear_rutina(self):
        self.bot.hablar("Vamos a crear una nueva rutina.")
        self.bot.hablar("Dime el nombre de la rutina.")
        nombre = self.bot.escuchar()
        
        self.bot.hablar(f"¿Cuál es el tipo de rutina para {nombre}?")
        tipo = self.bot.escuchar()

        pasos = {}
        index = 1

        while True:
            self.bot.hablar(f"Dime el paso número {index}.")
            paso = self.bot.escuchar()
            pasos[index] = paso
            index += 1

            #self.bot.hablar("¿Está lista la rutina? Responde sí o no.")
            #lista = self.bot.escuchar().strip().lower()
            if paso in ["salir", "terminar", "listo", "está listo"]:
                break

        # Guardar la rutina en la base de datos
        nueva_rutina = Rutina(
            nombre=nombre,
            tipo=tipo,
            pasos=str(pasos)
        )
        self.session.add(nueva_rutina)
        self.session.commit()
        self.bot.hablar(f"La rutina {nombre} de tipo {tipo} se ha guardado correctamente.")

    def menu_principal(self):
        while True:
            self.bot.hablar("¿Qué deseas hacer? Crear una rutina o salir.")
            opcion = self.bot.escuchar().strip().lower()
            if opcion == "crear":
                self.crear_rutina()
            elif opcion in ["salir", "terminar", "listo", "está listo"]:
                self.bot.hablar("Adiós. Nos vemos pronto.")
                break
            else:
                self.bot.hablar("Opción no válida. Inténtalo de nuevo.")

if __name__ == "__main__":
    gestor = GestorRutinas()
    gestor.menu_principal()
