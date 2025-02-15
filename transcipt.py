import assemblyai as aai
import os

aai.settings.api_key = "SUA_CHAVE_AQUI"

transcriber = aai.Transcriber()

# You can use a local filepath:
audio_file = "./exemplo.mp3"

# Or use a publicly-accessible URL:
# audio_file = (
#     "https://assembly.ai/sports_injuries.mp3"
# )

config = aai.TranscriptionConfig(speaker_labels=True)

transcript = transcriber.transcribe(audio_file, config)

if transcript.status == aai.TranscriptStatus.error:
    print(f"Transcription failed: {transcript.error}")
    exit(1)

# Export Subtitles
subtitles = transcript.export_subtitles_srt()

# Save as a file
with open('subtitles.srt', 'w') as f:
    f.write(subtitles)