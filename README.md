**Описание задачи**

Разработать инструмент командной строки для визуализации графа зависимостей, включая транзитивные зависимости. Сторонние средства для получения зависимостей использовать нельзя.

Зависимости определяются для git-репозитория. Для описания графа зависимостей используется представление Mermaid. Визуализатор должен выводить результат в виде сообщения об успешном выполнении и сохранять граф в файле формата png.

Построить граф зависимостей для коммитов, в узлах которого находятся списки файлов и папок.

Ключами командной строки задаются:
- Путь к программе для визуализации графов.
- Путь к анализируемому репозиторию.
- Путь к файлу с изображением графа зависимостей.

Все функции визуализатора зависимостей должны быть покрыты тестами.

**Описание работы**

Запуск может быть произведён из консоли. После ввода всех необходимых данных программа сгенерирует граф зависимостей коммитов и разместит его по указанному пути. 

Для работы необходим визуализатор графов mermaid-cli. Запуск производится из консоли, указываются 3 аргумента: -r (путь к репозиторию), -o (путь к выходному файлу), --vis (путь к mmdc.cmd файлу визуализатора). 

Для установки рекомендуется git clone, после чего необходимо запустить файл configur2.py из консоли с вышеописанными аргуметами.

ПРЕДУПРЕЖДЕНИЕ:
Не рекомендуется генерировать граф в формате png при большом количестве файлов в репозитории и при большом количестве коммитов. Используйте pdf.

**Пример работы программы**

![image](https://github.com/user-attachments/assets/ec2dc78a-6280-4b88-8c1c-609ff1627c7e)

**Тестирование**

![image](https://github.com/user-attachments/assets/251a9eba-3699-4318-825e-ee3694921a3f)

repo url: https://github.com/EverlastingN1ghtfall/configur2
