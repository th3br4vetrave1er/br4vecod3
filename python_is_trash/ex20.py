import webbrowser

def open_google_query(query):
    # URL для поиска в Google
    url = f"https://www.google.com/search?q={query}"
    # Открываем URL в браузере по умолчанию
    webbrowser.open(url)

def main():
    while True:
        # Запрос к пользователю на ввод поискового запроса
        query = input("Введите ваш запрос для поиска в Google (или 'exit' для выхода): ")
        if query.lower() == 'exit':
            print("Выход из программы.")
            break
        else:
            # Открываем результат поиска в браузере
            open_google_query(query)

if __name__ == "__main__":
    main()
