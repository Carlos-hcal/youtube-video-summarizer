<p align="center">
  <img src="cover_youtube-video_summarizer.png" alt="YouTube Video Summarizer" width="600">
</p>

# YouTube Video Summarizer

[![Python](https://img.shields.io/badge/Python-3.12%2B-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

🎬 Uma aplicação Python que cria **resumos de vídeos do YouTube** usando **Whisper local**, sem precisar de créditos da OpenAI.

---

## Funcionalidades

- Baixa vídeos do YouTube (apenas áudio) usando **pytubefix**
- Converte o áudio para MP3 usando **ffmpeg**
- Transcreve o áudio em texto com **Whisper local**
- Gera um **resumo simplificado** do vídeo
- Salva o resumo automaticamente em **`resumo.txt`**
- Funciona **offline**, sem depender de créditos ou limites da OpenAI

---

## Requisitos

- Python 3.12+
- **ffmpeg** instalado no sistema
- Bibliotecas Python:

```bash
pip install pytubefix ffmpeg-python git+https://github.com/openai/whisper.git
```
