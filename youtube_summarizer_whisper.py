# youtube_summarizer_whisper.py
from pytubefix import YouTube
import subprocess
import os
import sys
import whisper
import re


def criar_pastas():
    for pasta in ["audio", "transcricoes", "resumos"]:
        if not os.path.exists(pasta):
            os.makedirs(pasta)


def limpar_nome_arquivo(nome):
    # Remove caracteres inválidos no Windows
    return re.sub(r'[\\/*?:"<>|]', "_", nome)


def baixar_audio(url):
    criar_pastas()  # garante que a pasta audio/ exista
    try:
        yt = YouTube(url)
        titulo = limpar_nome_arquivo(yt.title)
        stream = yt.streams.filter(only_audio=True).first()
        if not stream:
            print("Erro: não foi encontrado stream de áudio disponível.")
            sys.exit(1)

        # Baixa para arquivo temporário simples
        tmp_file = "video_temp.mp4"
        stream.download(filename=tmp_file)

        caminho_mp3 = f"audio/{titulo}.mp3"

        # Converte para MP3 usando ffmpeg
        subprocess.run(
            ["ffmpeg", "-y", "-i", tmp_file, "-vn", caminho_mp3],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )

        # Remove arquivo temporário
        if os.path.exists(tmp_file):
            os.remove(tmp_file)

        # Verifica se MP3 foi criado
        if not os.path.exists(caminho_mp3):
            print("Erro: arquivo MP3 não foi gerado. Verifique se o vídeo é baixável.")
            sys.exit(1)

        return caminho_mp3, titulo

    except Exception as e:
        print(f"Erro ao baixar/converter o vídeo: {e}")
        sys.exit(1)


def transcrever(audio_path):
    model = whisper.load_model("small")  # "tiny" para mais rápido, "small" para mais preciso
    result = model.transcribe(audio_path)
    return result["text"]


def gerar_resumo(texto):
    if len(texto) > 500:
        return texto[:500] + "..."
    return texto


def salvar_arquivo(pasta, nome_arquivo, conteudo):
    caminho = f"{pasta}/{nome_arquivo}.txt"
    with open(caminho, "w", encoding="utf-8") as f:
        f.write(conteudo)
    return caminho


def main():
    if len(sys.argv) < 2:
        print("Uso: python youtube_summarizer_whisper.py <URL_DO_VIDEO>")
        return

    audio_path, titulo = baixar_audio(sys.argv[1])
    texto = transcrever(audio_path)

    # Pergunta ao usuário o que ele quer gerar
    print("\nEscolha a opção:")
    print("1 - Apenas transcrição completa")
    print("2 - Apenas resumo")
    print("3 - Ambos (transcrição e resumo)")
    opcao = input("Digite 1, 2 ou 3: ").strip()

    if opcao == "1":
        salvar_arquivo("transcricoes", titulo, texto)
        print("\nTranscrição completa salva ✅")
    elif opcao == "2":
        resumo = gerar_resumo(texto)
        salvar_arquivo("resumos", titulo, resumo)
        print("\nResumo salvo ✅")
    elif opcao == "3":
        resumo = gerar_resumo(texto)
        salvar_arquivo("transcricoes", titulo, texto)
        salvar_arquivo("resumos", titulo, resumo)
        print("\nTranscrição e resumo salvos ✅")
    else:
        print("Opção inválida. Nenhum arquivo foi salvo.")

    print(f"\nArquivos organizados nas pastas: audio/, transcricoes/, resumos/")

if __name__ == "__main__":
    main()
