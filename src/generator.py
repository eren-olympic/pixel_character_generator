import os
from openai import OpenAI
import requests
from PIL import Image
import io
from config.settings import Settings
from .pixelate import pixelate
from .prompts import QUESTIONS, get_dalle_prompt

class CharacterGenerator:
    def __init__(self):
        self.client = OpenAI(api_key=Settings.OPENAI_API_KEY)
        
    def ask_questions(self):
        answers = {}
        for q in QUESTIONS:
            key = '職業' if '職業' in q else '特徵' if '特徵' in q else '色彩'
            answers[key] = input(f"{q}\n")
        return answers

    def generate_image(self, prompt):
        response = self.client.images.generate(
            model="dall-e-3",
            prompt=prompt,
            size=f"{Settings.DEFAULT_IMAGE_SIZE}x{Settings.DEFAULT_IMAGE_SIZE}",
            quality="standard",
            n=1,
        )
        return response.data[0].url

    def download_and_pixelate(self, image_url):
        response = requests.get(image_url)
        img = Image.open(io.BytesIO(response.content))
        pixelated = pixelate(img, Settings.PIXEL_SIZE)
        
        output_path = os.path.join(Settings.OUTPUT_DIR, "character.png")
        pixelated.save(output_path)
        return output_path

    def generate_character(self):
        answers = self.ask_questions()
        prompt = get_dalle_prompt(answers)
        image_url = self.generate_image(prompt)
        return self.download_and_pixelate(image_url)