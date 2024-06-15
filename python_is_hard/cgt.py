import openai

# Установка ключа API OpenAI
api_key = 'YOUR_OPENAI_API_KEY'
openai.api_key = api_key

class ChatBot:
    def generate_response(self, input_text):
        response = openai.Completion.create(
            engine="davinci",  # Используем модель Davinci (GPT-3.5)
            prompt=input_text,
            max_tokens=150  # Максимальное количество токенов в ответе
        )
        return response.choices[0].text.strip()

    def chat(self):
        print("Чат-бот готов. Поговорите с ним (для выхода введите 'exit').")
        while True:
            user_input = input("Вы: ")
            if user_input.lower() == 'exit':
                print("До свидания!")
                break
            response = self.generate_response(user_input)
            print("Бот:", response)

if __name__ == "__main__":
    bot = ChatBot()
    bot.chat()
