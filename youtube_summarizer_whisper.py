from pytubefix import YouTube
import subprocess
import os
import sys
import whisper


def criar_pastas():
    for pasta in ["audio", "transcricoes", "resumos"]:
        if not os.path.exists(pasta):
            os.makedirs(pasta)


def baixar_audio(url):
    yt = YouTube(url)
    titulo = yt.title.replace("/", "_")
    stream = yt.streams.filter(only_audio=True).first()
    caminho_audio = f"audio/{titulo}.mp4"
    caminho_mp3 = f"audio/{titulo}.mp3"

    stream.download(filename=caminho_audio)
    subprocess.run(
        ["ffmpeg", "-y", "-i", caminho_audio, "-vn", caminho_mp3],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )
    os.remove(caminho_audio)
    return caminho_mp3, titulo


def transcrever(audio_path):
    model = whisper.load_model("small")
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

    criar_pastas()
    audio_path, titulo = baixar_audio(sys.argv[1])
    texto = transcrever(audio_path)

    print("\nEscolha a opção:")
    print("1 - Apenas transcrição completa")
    print("2 - Apenas resumo (se maior que 500 caracteres)")
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
