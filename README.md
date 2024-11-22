MESSAGE SPLITTER

**DESCRIPTION:**
  Message Splitter is a Python utility designed to split large HTML messages into smaller fragments while maintaining the integrity and nesting of HTML tags. 
  This tool is particularly useful in situations where messages exceed platform character limits, ensuring the correct HTML structure in all fragments. 
  I implemented this functionality in two ways: first using Python's standard "batteries" html.parser, then using BeautifulSoup4. 
  After comparing their performance speeds, I found that my first solution is 4 times faster, so I propose it as the primary one for consideration.

**FEATURES:**
  `HTML Parsing`: Uses Python's standard html.parser and the BeautifulSoup4 library for processing HTML content.
  `Tag Preservation`: Ensures the correct opening and closing of all HTML tags in each fragment.
  `Nesting Support`: Maintains the correct nesting of HTML tags in all fragments.
  `Configurable Fragment Size`: Allows users to set the maximum length for each message fragment.
  `Command Line Interface`: Uses argparse for handling command-line arguments, providing a convenient interface for users.
  `Prerequisites`: Python 3.6 or higher must be installed on your computer. It can be downloaded from the official website.

**INSTALLATION:**
  First, create a folder and clone the repository to your local computer:
    command: `git clone https://github.com/<your_login>/test_msg_split.git .`
  Create and Activate a Virtual Environment (Recommended):
    command: `python -m venv venv`
  Activate the Virtual Environment:
    Windows:
      command: `venv\Scripts\activate`
    Unix or macOS:
      command: `source venv/bin/activate`
      
INSTALL DEPENDENCIES:
  Install all required packages listed in requirements.txt:
    command: `pip install -r requirements.txt`

**RUNNING AND USING:**
  To run the application, follow these steps:
    Prepare the HTML File
    Ensure you have an HTML file (source.html) that you want to split into fragments.

**EXECUTE THE SCRIPT:**
  Use the following command to run the message splitting:
    command: `python msg_split.py --max-len=<your_max_len> ./<path_to_html_file>`
  Command Line Arguments:
    --max-len: This is the maximum length for one message fragment.
    ./source.html: This is the path to the file with data for fragmentation.
EXAMPLE EXECUTION:
  Suppose you have an HTML file source.html that needs to be split into fragments no longer than 4396 characters:
  After entering the command: `python msg_split.py --max-len=4396 ./source.html`
  **Script Output:**
      [FIRST FRAGMENT]: ![image](https://github.com/user-attachments/assets/7b5084fb-4954-4523-b2ad-249b7c98b460)
      [SECOND FRAGMENT]: ![image](https://github.com/user-attachments/assets/ef1d908a-5410-49d5-a9b5-bc74f9240bea)

----------------------------------------------------------------------------------------------------------------------

`START`
Чтобы запустить приложение нужно:
Установить зависимости, с помощью команды:
command: `pip install -r requirements.txt`
запустить корневой файл `msg_split.py`, с помощью команды:
`python msg_split.py --max-len=3072 ./source.html`

`--max-len` - Это максимальная длина для одного сообщения 
`./source.html` - Это путь к файлу с данными для фрагментации 


MESSAGE SPLITTER
**ОПИСАНИЕ:**
  Message Splitter — это утилита на Python, предназначенная для разбиения больших HTML-сообщений на более мелкие фрагменты при сохранении целостности и вложенности HTML-тегов.
  Этот инструмент особенно полезен в ситуациях, когда сообщения превышают лимиты символов платформ, обеспечивая корректную структуру HTML во всех фрагментах.
  Этот функционал я реализовал двумя способами, первый я сделал через стандартные "батарейки" python `html.parser`, 
  после этого сделал задачу используя `BeautifullSoup4`, после этого сравнив их скорость работы пришел к тому, 
  что мое первое решение быстрее в 4 раза, поэтому предлагаю его основным для рассмотрения. 
  
**ОСОБЕННОСТИ:**
  `HTML Парсинг`: Использует стандартный парсер Python html.parser и библиотеку BeautifulSoup4 для обработки HTML-контента.
  `Сохранение Тегов`: Гарантирует правильное открытие и закрытие всех HTML-тегов в каждом фрагменте.
  `Поддержка Вложенности`: Сохраняет правильную вложенность HTML-тегов во всех фрагментах.
  `Настраиваемый Размер Фрагмента`: Позволяет пользователям задавать максимальную длину для каждого фрагмента сообщения.
  `Командная Строка`: Использует argparse для обработки аргументов командной строки, предоставляя удобный интерфейс для пользователей.
  `Предварительные Требования`: Python 3.6 или выше должен быть установлен на вашем компьютере. Скачать можно с официального сайта.

**УСТАНОВКА:**
  Сначала создайте папку и клонируйте репозиторий на ваш локальный компьютер:
  command: `git clone https://github.com/<your_login>/test_msg_split.git .`
  
  Создание и Активация Виртуального Окружения (Рекомендуется):
    command `python -m venv venv`
  Активация Виртуального Окружения:
    Windows:
      command: `venv\Scripts\activate`
    Unix или macOS:
      command: `source venv/bin/activate`

УСТАНОВКА ЗАВИСИМОСТЕЙ:
  Установите все необходимые пакеты, перечисленные в requirements.txt:
    command: `pip install -r requirements.txt`

**ЗАПУСК И ИСПОЛЬЗОВАНИЕ:**
  Чтобы запустить приложение, выполните следующие шаги:
    Подготовьте HTML Файл
    Убедитесь, что у вас есть HTML-файл (source.html), который вы хотите разбить на фрагменты.

ВЫПОЛНЕНИЕ СКРИПТА:
  Используйте следующую команду для запуска разделения сообщения:
    command: `python msg_split.py --max-len=<your_max_len> ./<path_to_html_file>`
  Аргументы Командной Строки:
    --max-len: Максимальная длина для одного фрагмента сообщения.
    ./source.html: Путь к файлу с данными для фрагментации.
    
Пример исполнения:
  Предположим, у вас есть HTML-файл source.html, который необходимо разбить на фрагменты длиной не более 4396 символов:
    После ввода команды: `python msg_split.py --max-len=4396 ./source.html`
    **Вывод скрипта:**
      ![image](https://github.com/user-attachments/assets/7b5084fb-4954-4523-b2ad-249b7c98b460)
      ![image](https://github.com/user-attachments/assets/ef1d908a-5410-49d5-a9b5-bc74f9240bea)

