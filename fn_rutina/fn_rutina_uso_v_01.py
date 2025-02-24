from sqlalchemy import create_engine, Column, Integer, String, Text, func
from sqlalchemy.orm import sessionmaker, declarative_base
import json
import pyttsx3  # Para Text-to-Speech
import speech_recognition as sr  # Para Speech-to-Text

# Configuración de SQLAlchemy
DATABASE_URL = "sqlite:///rutina2025.sqlite"  # Ruta de la base de datos
engine = create_engine(DATABASE_URL, echo=False)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

# Configuración del modelo
class Rutina(Base):
    __tablename__ = "rutinas"
    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    tipo = Column(String, nullable=False)
    pasos = Column(Text, nullable=False)

    def obtener_pasos(self):
        """Convierte los pasos en un diccionario."""
        return json.loads(self.pasos)

# Configuración de BasicVoiceBot
class BasicVoiceBot:
    def __init__(self):
        self.running = True
        self.engine = pyttsx3.init()  # Inicializa el motor de TTS
        self.recognizer = sr.Recognizer()  # Inicializa el reconocimiento de voz

    def speak(self, message):
        """Convierte texto a voz y lo reproduce."""
        print(f"Bot: {message}")  # También muestra el mensaje en texto
        self.engine.say(message)
        self.engine.runAndWait()

    def listen(self):
        """Convierte voz a texto utilizando reconocimiento de voz."""
        with sr.Microphone() as source:
            self.speak("Estoy escuchando...")
            try:
                audio = self.recognizer.listen(source, timeout=5)
                response = self.recognizer.recognize_google(audio, language="es-ES")
                print(f"Tú: {response}")
                return response.lower()
            except sr.WaitTimeoutError:
                self.speak("No escuché nada. Por favor, inténtalo de nuevo.")
            except sr.UnknownValueError:
                self.speak("No entendí lo que dijiste. Por favor, repítelo.")
            except Exception as e:
                self.speak(f"Ocurrió un error: {str(e)}")
        return ""

    def exit(self):
        """Finaliza el bot."""
        self.running = False
        self.speak("¡Hasta luego!")

# Funciones principales
def listar_tipos_rutinas(bot):
    """Lista los tipos de rutinas y su conteo."""
    tipos = session.query(Rutina.tipo, func.count(Rutina.tipo)).group_by(Rutina.tipo).all()
    if not tipos:
        bot.speak("No hay rutinas disponibles en la base de datos.")
        return []
    bot.speak("Estos son los tipos de rutinas disponibles:")
    for i, (tipo, count) in enumerate(tipos, start=1):
        bot.speak(f"{i}. {tipo}, con {count} rutinas.")
    return [tipo for tipo, _ in tipos]

def listar_rutinas_por_tipo(tipo, bot):
    """Lista las rutinas disponibles para un tipo específico."""
    rutinas = session.query(Rutina).filter(Rutina.tipo == tipo).all()
    if not rutinas:
        bot.speak(f"No hay rutinas disponibles para el tipo '{tipo}'.")
        return []
    bot.speak(f"Rutinas disponibles para el tipo '{tipo}':")
    for rutina in rutinas:
        bot.speak(f"{rutina.nombre}")
    return rutinas

def seleccionar_rutina_por_nombre(rutinas, bot):
    """Permite seleccionar una rutina por nombre."""
    nombres_rutinas = [rutina.nombre.lower() for rutina in rutinas]
    bot.speak("Elige una rutina diciendo su nombre:")
    nombre_seleccionado = bot.listen()
    if nombre_seleccionado.lower() not in nombres_rutinas:
        bot.speak("El nombre ingresado no coincide con ninguna rutina.")
        return None
    rutina_seleccionada = next(rutina for rutina in rutinas if rutina.nombre.lower() == nombre_seleccionado.lower())
    return rutina_seleccionada

def mostrar_tareas_de_rutina(id_rutina, bot):
    """Muestra las tareas de una rutina específica."""
    rutina = session.query(Rutina).filter(Rutina.id == id_rutina).first()
    if not rutina:
        bot.speak("No se encontró la rutina seleccionada.")
        return
    bot.speak(f"Has seleccionado la rutina: {rutina.nombre}. Estas son las tareas:")
    pasos = rutina.obtener_pasos()
    for paso_num, paso_desc in pasos.items():
        bot.speak(f"Tarea {paso_num}: {paso_desc}")

# Programa principal con BasicVoiceBot
def main():
    bot = BasicVoiceBot()
    bot.speak("¡Hola! Soy tu asistente de rutinas.")

    while bot.running:
        tipos = listar_tipos_rutinas(bot)
        if not tipos:
            bot.exit()
            break

        bot.speak("Elige un tipo de rutina por nombre:")
        tipo_seleccionado = bot.listen()
        if tipo_seleccionado not in tipos:
            bot.speak("Ese tipo de rutina no es válido. Intenta nuevamente.")
            continue

        rutinas = listar_rutinas_por_tipo(tipo_seleccionado, bot)
        if not rutinas:
            continue

        rutina_seleccionada = seleccionar_rutina_por_nombre(rutinas, bot)
        if not rutina_seleccionada:
            bot.speak("No se pudo seleccionar una rutina válida. Intenta nuevamente.")
            continue

        mostrar_tareas_de_rutina(rutina_seleccionada.id, bot)
        bot.speak("¿Quieres seleccionar otra rutina? Di 'sí' o 'no':")
        respuesta = bot.listen()
        if respuesta != "sí":
            bot.exit()

if __name__ == "__main__":
    main()
