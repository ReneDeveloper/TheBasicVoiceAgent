import sounddevice as sd
import numpy as np
import pyqtgraph as pg

def note_from_frequency(frequency):
    A4 = 440
    C0 = A4 * np.power(2, -4.75)
    semitones = 12 * np.log2(frequency / C0)
    note = int(semitones) % 12
    notes = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
    return notes[note]

def audio_callback(indata, frames, time, status):
    global current_note, audio_data
    if status:
        print(status, file=sys.stderr)
    audio = indata[:, 0]
    audio_data = np.append(audio_data, audio)
    spectrum = np.abs(np.fft.rfft(audio))
    frequencies = np.fft.rfftfreq(audio.size, 1.0/samplerate)
    index = np.argmax(spectrum)
    frequency = frequencies[index]
    new_note = note_from_frequency(frequency)
    if new_note != current_note:
        current_note = new_note
        print("Current note:", current_note)
    plot.setData(audio_data)

samplerate = 44100
duration = 50  # seconds
current_note = None
audio_data = np.array([])

app = pg.QtWidgets.QApplication([])
plot = pg.PlotWidget()
plot.show()

with sd.InputStream(callback=audio_callback, samplerate=samplerate, channels=1):
    print("Recording. Press Ctrl+C to stop.")
    sd.sleep(duration * 1000)
