import os
import mido
import pretty_midi

def analyze_midi(file_path, nome):
    # Carregar o arquivo MIDI
    midi_data = pretty_midi.PrettyMIDI(file_path)

    # Detectar a tonalidade (key)
    key_signature_changes = midi_data.key_signature_changes
    if key_signature_changes:
        key = pretty_midi.key_number_to_key_name(key_signature_changes[0].key_number)
    else:
        key = 'Não detectado'

    # Detectar o tempo (BPM)
    tempo_changes = midi_data.get_tempo_changes()
    if len(tempo_changes[1]) > 0:
        tempo = tempo_changes[1][0]
    else:
        tempo = 'Não detectado'

    # Detectar o ritmo (time signature)
    time_signature_changes = midi_data.time_signature_changes
    if time_signature_changes:
        time_signature = f"{time_signature_changes[0].numerator}/{time_signature_changes[0].denominator}"
    else:
        time_signature = 'Não detectado'

    return {
        'Arquivo': nome,
        'Tonalidade': key,
        'Tempo (BPM)': tempo,
        'Ritmo (Signature)': time_signature
    }

# Exemplo de uso


def analyze(modelo,genre,folder,filename):
    # Pasta base onde os arquivos MIDI estão localizados
    base_folder = f'C:\\Users\\bruna\\fpcc2teste\\midis\\{genre}\\modelo {modelo}\\{folder}'

    # Lista de arquivos MIDI a serem analisados
    files_to_analyze = [
        (os.path.join(base_folder, f'{filename}.mid'), filename),
        (os.path.join(base_folder, '_Sample 5 (1).mid'), '_Sample 5 (1)'),
        (os.path.join(base_folder, '_Sample 4.mid'), '_Sample 4'),
        (os.path.join(base_folder, '_Sample 3.mid'), '_Sample 3'),
        (os.path.join(base_folder, '_Sample 2.mid'), '_Sample 2'),
        (os.path.join(base_folder, '_Sample 1.mid'), '_Sample 1'),
    ]

    # Analisar cada arquivo e armazenar os resultados em uma lista
    results = []
    for file_path, name in files_to_analyze:
        analysis = analyze_midi(file_path, name)
        results.append(analysis)

    # Caminho do arquivo de saída
    output_file = os.path.join(base_folder, 'analyze_midi_results.txt')

    # Gerar um arquivo txt com os resultados
    with open(output_file, 'w', encoding='utf-8') as f:
        for result in results:
            f.write(f"Arquivo: {result['Arquivo']}\n")
            f.write(f"Tonalidade: {result['Tonalidade']}\n")
            f.write(f"Tempo (BPM): {result['Tempo (BPM)']}\n")
            f.write(f"Ritmo (Signature): {result['Ritmo (Signature)']}\n")
            f.write("\n")

    print(f"Resultados salvos em {output_file}")

#analyze('1','electronic','1','Avicii - Fade Into Darkness (1)')
#analyze('1','electronic','2','Edward Maya - Stereo Love')
#analyze('1','electronic','3','EURYTHMICS.Sweet dreams K')
#analyze('1','electronic','4','haddaway-what_is_love')
#analyze('1','electronic','5','Yolanda Be Cool - We No Speak Americano')


#analyze('1','game','1','QUANTIZED Final Fantasy VIII - The Loser Game Over')
#analyze('1','game','2','Mario Bros. - Super Mario Bros. Theme')
#analyze('1','game','3','Donkey Kong Country 2 Diddys Kong Quest - Bonus')
#analyze('1','game','4','Tetris - Theme A Normal')
#analyze('1','game','5','QUANTIZED The Legend of Zelda - Zelda is Rescued Fanfare')


#analyze('1','classical','1','QUANTIZED Beethoven-Moonlight-Sonata')
#analyze('1','classical','2','QUANTIZED mozart-piano-concerto-21-2-elvira-madigan-piano-solo')

#analyze('1','classical','3','QUANTIZED Piano Sonata in Sonata in G, No.1, D894 - Molto moderato e cantabile')
#analyze('1','classical','4','QUANTIZED Piano Sonata n17 Tempestat')
#analyze('1','classical','5','QUANTIZED Piano Sonata n18 The Hunt')


#analyze('1','jazz','1','A-Foggy-Day-(Jazz-Gitaar-Trio)')
#analyze('1','jazz','2',"Alexander's-Ragtime-(Jazz-Gitaar-Trio)")
#analyze('1','jazz','3','As-Time-Goes-By-(Jazz-Gitaar-Trio)')
#analyze('1','jazz','4','Frank Sinatra - My Way')
#analyze('1','jazz','5','QUANTIZED Frank Sinatra - New York, New York')

#analyze('1','middleeastern','1','KHALED.Aicha K')
#analyze('1','middleeastern','2',"KHALED.Didi")
#analyze('1','middleeastern','3','KHALED.El Arbi')
analyze('1','middleeastern','4','KHALED.Fee nass')
analyze('1','middleeastern','5','KHALED.Wahshtny')
