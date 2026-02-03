import os
from pathlib import Path

# Get .env path
BASE_DIR = Path(__file__).resolve().parent.parent
ENV_PATH = BASE_DIR / '.env'

# Manual .env parser (handles BOM)
def load_env_manually(env_path):
    env_vars = {}
    if env_path.exists():
        with open(env_path, 'r', encoding='utf-8-sig') as f:  # utf-8-sig removes BOM
            for line in f:
                line = line.strip()
                if line and not line.startswith('#') and '=' in line:
                    key, value = line.split('=', 1)
                    key = key.strip().lstrip('\ufeff')  # Extra BOM removal
                    env_vars[key] = value.strip()
    return env_vars

# Load environment variables
env_vars = load_env_manually(ENV_PATH)

TELEGRAM_TOKEN = env_vars.get('TELEGRAM_BOT_TOKEN', '').strip()
GEMINI_API_KEY = env_vars.get('GEMINI_API_KEY', '').strip()

# Validation
print(f'📂 .env path: {ENV_PATH}')
print(f'✅ .env exists: {ENV_PATH.exists()}')
print(f'📄 Keys found: {list(env_vars.keys())}')

if not TELEGRAM_TOKEN:
    print('❌ TELEGRAM_BOT_TOKEN is empty!')
    raise ValueError('TELEGRAM_BOT_TOKEN not found in .env file')

print(f'🔑 Token loaded: {TELEGRAM_TOKEN[:20]}...')
print(f'🤖 Gemini key loaded: {bool(GEMINI_API_KEY)}')

SUPPORTED_LANGUAGES = {
    'en': 'English',
    'ur': 'Urdu',
    'ar': 'Arabic'
}

DEFAULT_LANGUAGE = 'en'
