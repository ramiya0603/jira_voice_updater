# Jira Voice Updater

## Features
- Upload WAV voice note
- Convert speech to text using Vosk (offline)
- Create professional Jira update using rule-based formatting
- Optionally post comment to Jira

## Setup

1. Install requirements

pip install -r requirements.txt

2. Copy .env.example to .env

3. Download a Vosk model:

https://alphacephei.com/vosk/models

Recommended:
vosk-model-small-en-us-0.15

Extract as:

./model

4. Run

python app.py
