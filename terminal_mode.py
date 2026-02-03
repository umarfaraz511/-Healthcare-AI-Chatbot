import asyncio
from datetime import datetime
from src.ai_handler import AIHandler
from src.language_handler import SUPPORTED_LANGUAGES

ai_handler = AIHandler()

async def terminal_chat():
    # Create log file
    log_file = f'chat_log_{datetime.now().strftime("%Y%m%d_%H%M%S")}.txt'
    
    print('🏥 Healthcare AI Chatbot (Terminal Mode)')
    print('=' * 50)
    print('Commands:')
    print('  /language - Change language')
    print('  /quit - Exit')
    print(f'📝 Conversation saved to: {log_file}')
    print('=' * 50)
    
    language = 'en'
    
    with open(log_file, 'w', encoding='utf-8') as log:
        log.write('Healthcare AI Chatbot - Conversation Log\n')
        log.write('=' * 50 + '\n\n')
        
        while True:
            user_input = input(f'\n[{language.upper()}] You: ').strip()
            
            if not user_input:
                continue
                
            if user_input.lower() == '/quit':
                print('👋 Goodbye!')
                log.write('\n[Session ended]\n')
                break
                
            if user_input.lower() == '/language':
                print('\nAvailable languages:')
                for code, name in SUPPORTED_LANGUAGES.items():
                    print(f'  {code} - {name}')
                lang_choice = input('Select (en/ur/ar): ').strip().lower()
                if lang_choice in SUPPORTED_LANGUAGES:
                    language = lang_choice
                    print(f'✅ Language changed to {SUPPORTED_LANGUAGES[language]}')
                    log.write(f'\n[Language changed to {SUPPORTED_LANGUAGES[language]}]\n')
                continue
            
            print('🔄 Processing...')
            log.write(f'[{language.upper()}] User: {user_input}\n')
            
            try:
                response = await ai_handler.get_response(user_input, language)
                print(f'\n🤖 Bot: {response}')
                log.write(f'Bot: {response}\n\n')
            except Exception as e:
                error_msg = f'❌ Error: {e}'
                print(f'\n{error_msg}')
                log.write(f'{error_msg}\n\n')

if __name__ == '__main__':
    print('🚀 Starting Healthcare AI Chatbot (Terminal Mode)...')
    print('✅ No internet restrictions - works offline!')
    print()
    asyncio.run(terminal_chat())
