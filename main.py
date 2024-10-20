
import sounddevice
from datetime import datetime
from scipy.io.wavfile import write


def second():
    while True:
        second = int(input('Entre la cantidad de segundos que desea grabar: '))
        try:
            if second > 0:
                print('Grabando... \n')
                return second
        except:
            print('Ingrese un numero mayor a 0')

def GuardarArchivos(fs, audio):
    carpeta = "grabaciones"

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")  # Formato: AñoMesDia_HoraMinutoSegundo
    filename = f"{carpeta}/grabacion_{timestamp}.wav"
    write(filename, fs, audio)
    print(f"Archivo guardado como: {filename}")

def main ():
    fs = 44100 #rate
    segundos = second()
    record_voice = sounddevice.rec(int(segundos*fs), samplerate=fs,channels=1)
    sounddevice.wait()
    GuardarArchivos(fs,record_voice)


main()


