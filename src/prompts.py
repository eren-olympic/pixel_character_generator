QUESTIONS = [
    "這個角色的職業是什麼? (例如:戰士、魔法師、弓箭手等)",
    "角色的主要特徵是什麼? (例如:長髮、盔甲、法杖等)",
    "角色的色彩風格? (例如:暗色系、明亮色系等)"
]

def get_dalle_prompt(answers):
    return f"""
    A pixel art style character:
    - Class: {answers['職業']}
    - Features: {answers['特徵']}
    - Color scheme: {answers['色彩']}
    Make it in a simple, clean pixel art style suitable for a 2D game.
    """