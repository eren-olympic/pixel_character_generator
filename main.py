from config.settings import Settings
from src.generator import CharacterGenerator

def main():
    Settings.validate()
    generator = CharacterGenerator()
    output_path = generator.generate_character()
    print(f"角色圖片已生成: {output_path}")

if __name__ == "__main__":
    main()