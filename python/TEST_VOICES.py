#TEST_VOICES.py

import win32com.client as wincl

# Inicializar el sintetizador de voz
speak = wincl.Dispatch("SAPI.SpVoice")

# El texto a convertir a voz
text = "Hola, ¿cómo estás?"

# Seleccionar el idioma
#voice = wincl.Dispatch("SAPI.SpObjectToken")
#voice.SetId("HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-MX_SABINA_11.0")
#speak.Voice = voice

# Generar el audio
speak.Speak(text)