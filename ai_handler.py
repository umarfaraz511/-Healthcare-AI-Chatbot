import google.generativeai as genai
from config.settings import GEMINI_API_KEY
from src.prompts import get_system_prompt

genai.configure(api_key=GEMINI_API_KEY)

class AIHandler:
    def __init__(self):
        # Use the latest Gemini 2.5 Flash model
        self.model = genai.GenerativeModel('gemini-2.5-flash')
        print('✅ Using model: gemini-2.5-flash')
        
    async def get_response(self, user_message: str, language: str = 'en') -> str:
        try:
            system_prompt = get_system_prompt(language)
            full_prompt = f"{system_prompt}\n\nUser: {user_message}\nAssistant:"
            
            response = self.model.generate_content(full_prompt)
            return response.text
        except Exception as e:
            return f"⚠️ Error: {str(e)}"
