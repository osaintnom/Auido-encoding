import torchaudio
import torch

# Ruta del archivo de audio
ruta_audio = "/Users/lucaspinera/Desktop/ditella_sexto_semestre/AI/segunda_parte_redes/tps/tp4_td6/musica_nueva_5sec/pop/pop.wav"

# Cargar el audio usando torchaudio
waveform, sample_rate = torchaudio.load(ruta_audio, normalize=True)

# Si el audio tiene 2 canales, reducir a 1 canal tomando la media
if waveform.size(0) == 2:
    waveform = waveform.mean(dim=0, keepdim=True)

# Guardar el audio modificados
torchaudio.save("/Users/lucaspinera/Desktop/ditella_sexto_semestre/AI/segunda_parte_redes/tps/tp4_td6/musica_nueva_5sec/pop/pop_1canal.wav", waveform, sample_rate)
