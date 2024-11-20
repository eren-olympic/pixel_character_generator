# Pixel Character Generator

A Python application that generates pixel art game characters using OpenAI's DALL-E API.

## Features
- Interactive character creation through user prompts
- OpenAI DALL-E integration for image generation
- Automatic pixel art conversion
- Configurable settings via environment variables

## Setup
1. Clone repository
2. Create `.env` file with required variables:
```
OPENAI_API_KEY=your-openai-api-key
PIXEL_SIZE=8
OUTPUT_DIR=output
DEFAULT_IMAGE_SIZE=1024
```
3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage
Run:
```bash
python main.py
```
Follow the prompts to specify character details.

## Project Structure
```
pixel_character_generator/
├── config/         # Configuration settings
├── src/           # Source code
│   ├── generator.py
│   ├── pixelate.py
│   └── prompts.py
└── main.py        # Entry point
```

## Requirements
- Python 3.8+
- OpenAI API key
- Dependencies listed in requirements.txt