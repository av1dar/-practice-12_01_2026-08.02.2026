import os
from dotenv import load_dotenv

loaded = load_dotenv()

if not loaded:
    print("⚠️ Увага: Файл .env не знайдено!")

database_url = os.getenv("DB_URL")
api_key = os.getenv("API_KEY")
debug_mode = os.getenv("DEBUG_MODE")

print("--- Конфігурація додатка ---")

if database_url:
    print(f"Підключення до БД: {database_url}")
else:
    print("Помилка: Не вказано DB_URL")

if api_key:
    # Ніколи не виводьте реальні ключі в консоль повністю!
    masked_key = api_key[:4] + "****" + api_key[-4:]
    print(f"API ключ завантажено: {masked_key}")
else:
    print("Помилка: Не вказано API_KEY")

print(f"Режим налагодження: {debug_mode}")