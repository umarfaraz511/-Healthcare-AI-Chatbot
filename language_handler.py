from langdetect import detect
from config.settings import SUPPORTED_LANGUAGES, DEFAULT_LANGUAGE

TRANSLATIONS = {
    'welcome': {
        'en': '👋 Welcome to Healthcare AI Assistant!\n\nI can help with:\n✅ Medical information\n✅ Symptom analysis\n✅ Health tips\n✅ Disease prevention\n\nChoose language: /language',
        'ur': '👋 ہیلتھ کیئر AI اسسٹنٹ میں خوش آمدید!\n\nمیں مدد کر سکتا ہوں:\n✅ طبی معلومات\n✅ علامات کا تجزیہ\n✅ صحت کے نسخے\n✅ بیماری سے بچاؤ\n\nزبان منتخب کریں: /language',
        'ar': '👋 مرحبا بك في مساعد الرعاية الصحية AI!\n\nيمكنني المساعدة في:\n✅ معلومات طبية\n✅ تحليل الأعراض\n✅ نصائح صحية\n✅ الوقاية من الأمراض\n\nاختر اللغة: /language'
    },
    'lang_selected': {
        'en': '✅ Language set to English',
        'ur': '✅ زبان اردو میں تبدیل ہو گئی',
        'ar': '✅ تم تعيين اللغة إلى العربية'
    }
}

def get_text(key: str, language: str) -> str:
    return TRANSLATIONS.get(key, {}).get(language, TRANSLATIONS[key]['en'])

def detect_language(text: str) -> str:
    try:
        lang = detect(text)
        return lang if lang in SUPPORTED_LANGUAGES else DEFAULT_LANGUAGE
    except:
        return DEFAULT_LANGUAGE
