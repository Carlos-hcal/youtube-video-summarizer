# youtube_summarizer_whisper.py
from pytubefix import YouTube
import subprocess
import os
import sys
import whisper


def baixar_audio(url):
    yt = YouTube(url)
    stream = yt.streams.filter(only_audio=True).first()
    out = stream.download(filename="video.mp4")
    subprocess.run(
        ["ffmpeg", "-y", "-i", out, "-vn", "audio.mp3"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )
    return "audio.mp3"


def transcrever_e_resumir(audio_path):
    model = whisper.load_model("small")
    result = model.transcribe(audio_path)
    texto = result["text"]
    resumo = texto[:500] + "..." if len(texto) > 500 else texto
    return resumo


def main():
    if len(sys.argv) < 2:
        print("Uso: python youtube_summarizer_whisper.py <URL>")
        return

    audio = baixar_audio(sys.argv[1])
    resumo = transcrever_e_resumir(audio)

    print("\nResumo do vídeo:\n", resumo)

    # Salva em arquivo resumo.txt
    with open("resumo.txt", "w", encoding="utf-8") as f:
        f.write(resumo)
    print("\nResumo salvo em resumo.txt ✅")

    os.remove(audio)


if __name__ == "__main__":
    main()
