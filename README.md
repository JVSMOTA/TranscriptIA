# TranscriptIA

TranscriptIA é um projeto que utiliza a API da **AssemblyAI** para transcrever arquivos de áudio e gerar legendas automaticamente no formato **.srt**.

## 🚀 Como iniciar o projeto

### 1️⃣ Clonar o repositório
```bash
git clone https://github.com/JVSMOTA/TranscriptIA.git
cd TranscriptIA
```

### 2️⃣ Criar um ambiente virtual e ativá-lo (Recomendado)
```bash
python3 -m venv venv
source venv/bin/activate  # No Windows use: venv\Scripts\activate
```

### 3️⃣ Instalar dependências
```bash
pip install assemblyai
```

### 4️⃣ Definir sua chave de API
Substitua a chave no código:
```python
aai.settings.api_key = "SUA_CHAVE_AQUI"
```
Para obter uma chave gratuita, cadastre-se em: [AssemblyAI](https://www.assemblyai.com/)

## 🎵 Como usar?

1️⃣ Coloque o arquivo **.mp3** que deseja transcrever na pasta do projeto.
2️⃣ No arquivo Python, altere o nome do arquivo no código:
```python
audio_file = "./seuarquivo.mp3"
```
3️⃣ Execute o script:
```bash
python main.py
```
4️⃣ O arquivo de legendas **subtitles.srt** será gerado na mesma pasta.

## 📌 Observação
Atualmente, a **AssemblyAI** suporta apenas transcrição em inglês. Se precisar de suporte para português, confira APIs como **Google Speech-to-Text, Azure Speech Service, Amazon Transcribe ou Whisper (OpenAI)**.

## 🛠 Contribuição
Sinta-se à vontade para abrir **issues** e **pull requests** no repositório!
