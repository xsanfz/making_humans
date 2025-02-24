# Импорты
import file_operations
import os
import random
from faker import Faker

# Объявления глобальных констант
SKILLS = [
    'Стремительный прыжок',
    'Электрический выстрел',
    'Ледяной удар',
    'Стремительный удар',
    'Кислотный взгляд',
    'Тайный побег',
    'Ледяной выстрел',
    'Огненный заряд'
]

LETTERS_MAPPING = {
    'а': 'а͠', 'б': 'б̋', 'в': 'в͒͠',
    'г': 'г͒͠', 'д': 'д̋', 'е': 'е͠',
    'ё': 'ё͒͠', 'ж': 'ж͒', 'з': 'з̋̋͠',
    'и': 'и', 'й': 'й͒͠', 'к': 'к̋̋',
    'л': 'л̋͠', 'м': 'м͒͠', 'н': 'н͒',
    'о': 'о̋', 'п': 'п̋͠', 'р': 'р̋͠',
    'с': 'с͒', 'т': 'т͒', 'у': 'у͒͠',
    'ф': 'ф̋̋͠', 'х': 'х͒͠', 'ц': 'ц̋',
    'ч': 'ч̋͠', 'ш': 'ш͒͠', 'щ': 'щ̋',
    'ъ': 'ъ̋͠', 'ы': 'ы̋͠', 'ь': 'ь̋',
    'э': 'э͒͠͠', 'ю': 'ю̋͠', 'я': 'я̋',
    'А': 'А͠', 'Б': 'Б̋', 'В': 'В͒͠',
    'Г': 'Г͒͠', 'Д': 'Д̋', 'Е': 'Е',
    'Ё': 'Ё͒͠', 'Ж': 'Ж͒', 'З': 'З̋̋͠',
    'И': 'И', 'Й': 'Й͒͠', 'К': 'К̋̋',
    'Л': 'Л̋͠', 'М': 'М͒͠', 'Н': 'Н͒',
    'О': 'О̋', 'П': 'П̋͠', 'Р': 'Р̋͠',
    'С': 'С͒', 'Т': 'Т͒', 'У': 'У͒͠',
    'Ф': 'Ф̋̋͠', 'Х': 'Х͒͠', 'Ц': 'Ц̋',
    'Ч': 'Ч̋͠', 'Ш': 'Ш͒͠', 'Щ': 'Щ̋',
    'Ъ': 'Ъ̋͠', 'Ы': 'Ы̋͠', 'Ь': 'Ь̋',
    'Э': 'Э͒͠͠', 'Ю': 'Ю̋͠', 'Я': 'Я̋',
    ' ': ' '
}

OUTPUT_DIR = "../output"
TEMPLATE_PATH = "charsheet.svg"

# Объявления функций
def replace_font(text, mapping):
    """Заменяет символы в тексте согласно переданному mapping."""
    return ''.join([mapping.get(char, char) for char in text])


def read_file(filename):
    """Читает содержимое файла."""
    with open(filename, encoding='utf8') as file_:
        return file_.read()


def write_to_file(filename, content):
    """Записывает содержимое в файл."""
    with open(filename, 'w', encoding='utf8') as file_:
        return file_.write(content)


def render_template(template_path, output_path, context):
    """Заменяет подсказки в шаблоне на значения из context и сохраняет результат."""
    content = read_file(template_path)
    for key, value in context.items():
        content = content.replace('{%s}' % key, str(value))
    write_to_file(output_path, content)


def generate_character(fake, runic_skills):
    """Генерирует данные для одного персонажа."""
    selected_skills = random.sample(runic_skills, 3)
    return {
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "job": fake.job(),
        "town": fake.city(),
        "strength": random.randint(3, 18),
        "agility": random.randint(3, 18),
        "endurance": random.randint(3, 18),
        "intelligence": random.randint(3, 18),
        "luck": random.randint(3, 18),
        "skill_1": selected_skills[0],
        "skill_2": selected_skills[1],
        "skill_3": selected_skills[2]
    }


def main():
    """Основная функция программы."""
    fake = Faker("ru_RU")
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # Преобразуем навыки в стилизованный шрифт
    runic_skills = [replace_font(skill, LETTERS_MAPPING) for skill in SKILLS]

    # Генерация персонажей
    for i in range(1, 11):
        context = generate_character(fake, runic_skills)
        output_path = os.path.join(OUTPUT_DIR, f"result_{i}.svg")
        render_template(TEMPLATE_PATH, output_path, context)
        print(f"Сгенерирован файл: {output_path}")


# Остальной код
if __name__ == '__main__':
    main()