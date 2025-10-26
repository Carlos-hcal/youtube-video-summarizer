<p align="center">
  <img src="cover_summarizer.png" alt="YouTube Video Summarizer" width="600">
</p>

# YouTube Video Summarizer

[![Python](https://img.shields.io/badge/Python-3.12%2B-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

🎬 Uma aplicação Python que **transcreve e resume vídeos do YouTube** usando **Whisper local**, sem depender de créditos da OpenAI. Ideal para estudo, pesquisa ou consumo rápido de conteúdo de vídeos longos.

---

## Funcionalidades

- Baixa vídeos do YouTube (apenas áudio) usando **pytubefix**
- Converte o áudio para MP3 usando **ffmpeg**
- Transcreve o áudio em texto com **Whisper local**
- Gera resumo do vídeo (ou transcrição completa, dependendo da versão do script)
- Salva o resultado automaticamente em **`resumo.txt`** ou **`transcricao.txt`**
- Funciona **offline**, sem limites de API

---

## Tecnologias Utilizadas

- **Python 3.12+**
- **pytubefix**: para baixar vídeos do YouTube
- **ffmpeg**: para conversão de áudio
- **Whisper (OpenAI)**: para transcrição de áudio
- **requests** (opcional, para integração com APIs de resumo)

---

## Requisitos

- Python 3.12+
- **ffmpeg** instalado no sistema (https://ffmpeg.org/)
- Bibliotecas Python:

```bash
pip install pytubefix ffmpeg-python git+https://github.com/openai/whisper.git
```

## Requisitos

### Clone o repositório:

```bash
git clone https://github.com/SEU_USUARIO/youtube-video-summarizer.git
```

### Entre na pasta do projeto:

```bash
cd youtube-video-summarizer
```

### Instale as dependências:

```bash
pip install -r requirements.txt
```

**(ou instale manualmente conforme listado nos requisitos)**

## Como Usar

**1°** Abra o terminal na pasta do projeto.

**2°** Rode o script com a URL do vídeo do YouTube:

```bash
python youtube_summarizer_whisper.py <URL_DO_VIDEO>
```

### Exemplo:

```bash
python youtube_summarizer_whisper.py https://www.youtube.com/watch?v=RvrDGKW31qQ
```

### Resultado:

A transcrição ou resumo é exibido no terminal.

Um arquivo **resumo.txt** ou **transcricao.txt** é salvo na pasta.

#### Exemplo de Saída:

Resumo do vídeo:
Oi pessoal, eu sou o Dólinho, seu amiguinho, vamos cantar!

### Modelos do Whisper:

**"tiny"** → rápido, menor precisão

**"base"** → equilíbrio entre velocidade e precisão

**"small"** → mais preciso, mais lento

**"medium"** / **"large"** → alta qualidade, uso intensivo de memória

### Observações:

Vídeos longos podem levar alguns minutos para processar

Funciona em Windows, macOS e Linux

### Autor

Carlos Henrique

💻 GitHub
| 📧 (https://github.com/Carlos-hcal)

Licença

Este projeto está licenciado sob a licença MIT - veja o arquivo LICENSE
para detalhes.
