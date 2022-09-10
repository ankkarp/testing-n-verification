# Тестирование и верификация програмного обеспечения

## Приложение для практики 1

### Введение

Скрипт может:

1. Получать адрес хоста электронной почты
2. Проверять может ли быть адресом электронной почты 
3. Проверять может ли быть мобильным номером (номер должен быть без знака +)
4. Проверять может ли быть именем файла
5. Преобразовать номер мобильного телефона (номер должен быть без знака +) в число  

### Комманды для запуска в консоли

Вводится строка на проверку и один или более из следующих аргументов.

|Аргумент | Значение |
| ------------- |:-------------:|
| --host | Получить адрес хоста электронной почты
| -e --email | Проверить может ли быть адресом электронной почты
| -c --cello | Проверить может ли быть мобильным номером (номер должен быть без знака +)
| -f --file | Проверить может ли быть именем файла
| -n --cellnum | Получить получить номер как число (номер должен быть без знака +)

#### Краткий обзор

Пример вызова:

    python app_for_task1.py email@email.com --host -e -f
      
Вывод программы:

    email@email.com не может быть номером телефона
    Адрес хоста почты email@email.com: email
    email@email.com не может быть названием файла

Пример вызова:

    python app_for_task1.py "8-(800)-555-35-35" -c -n
      
Вывод программы:

    python app_for_task1.py "8-(800)-555-35-35" -c -n
    8-(800)-555-35-35 может быть номером телефона
    8-(800)-555-35-35 в числовом формате: 88005553535
    
### Общее описание

Скрипт использует стандарную питоновскую библиотеку re для компиляции регулярных выражений и определения совпадения.

#### Характеристики пользователя

- Разработчики нуждающиеся в верификации форм, содержации поле почты
- Любой желающий изучить какие почты бывают

#### Ограничения

На компьютер должно быть установлено:

- Python 3.5+
- Любой Python IDE

#### Допущения и зависимости

Используются только стандарные библиотеки Python. Дополнительной установки не требуют.

#### Детальные требования

Требований к внешним интерфейсам и функциональных требований нет.
