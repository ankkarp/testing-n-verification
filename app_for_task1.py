import re
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('input', help='Проверяемая строка')
parser.add_argument('-e', '--email', action='store_true', help='Проверить может ли быть адресом электронной почты')
parser.add_argument('-c', '--cello', action='store_true', help='Проверить может ли быть мобильным номером')
parser.add_argument('-f', '--file', action='store_true', help='Проверить может ли быть именем файла')
parser.add_argument('--host', action='store_true', help='Получить адрес хоста электронной почты')
parser.add_argument('-n', '--cellnum', action='store_true',
                    help='Получить получить номер как число (с удалением скобок и тире)')
args = parser.parse_args()


def validate_email(inp):
    return bool(re.fullmatch(r"[\w~!$%^&*_=+}{'?\-.]+@][a-z]+\.[a-z]+", inp.strip()))


def validate_mobile_number(inp):
    return bool(re.fullmatch(r"\d-?\(?\d{3}\)?-?\d{3}-?\d{2}-?\d{2}", inp))


def validate_filename(inp):
    return bool(re.fullmatch(r"[\w\-. ]+", inp.strip()))


def numerize_phone_number(inp):
    return re.sub(r"\D+", "", inp.strip())


def get_email_host(inp):
    return inp[:inp.find("@")]


if args.email:
    print(args.input, " " if validate_email(args.input) else " не ", "может быть электронной почтой", sep="")
if args.cello:
    print(args.input, " " if validate_mobile_number(args.input) else " не ", "может быть номером телефона", sep="")
if args.cellnum:
    phone_number = numerize_phone_number(args.input)
    if phone_number:
        print(f"{args.input} в числовом формате: {phone_number}")
    else:
        print(f"{args.input} не может быть номером телефона")
if args.host:
    host = get_email_host(args.input)
    if host:
        print(f"Адрес хоста почты {args.input}: {host}")
    else:
        print(f"{args.input} не может быть адресом электронной почты")
if args.file:
    print(args.input, "не" if validate_mobile_number(args.input) else "", "может быть названием файла", sep="")

