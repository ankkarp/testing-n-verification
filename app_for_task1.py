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
    return bool(re.fullmatch(r"[a-zA-Z\d~!$%^&*_=+}{'?\-.]+@[a-zA-Z]+\.[a-zA-Z]+", inp))


def validate_mobile_number(inp):
    return bool(re.fullmatch(r"\d{1}-?\(?\d{3}\)?-?\d{3}-?\d{2}-?\d{2}", inp))


def validate_filename(inp):
    return bool(re.fullmatch(r"[^\\\/].\w", inp))


def numerize_phone_number(inp):
    return re.sub(r"\D+", "", inp)


def get_email_host(inp):
    if validate_email(inp):
        return inp[:inp.find("@")]
    return None


if args.email:
    print(args.input, "" if validate_email(args.input) else "не", "может быть электронной почтой")
if args.cello:
    print(args.input, "не" if validate_mobile_number(args.input) else "", "может быть номером телефона")
if args.cellnum:
    print(f"{args.input} в числовом формате: {numerize_phone_number(args.input)}")
if args.host:
    print(f"Адрес хоста почты {args.input}: {get_email_host(args.input)}")
if args.file:
    print(args.input, "" if validate_mobile_number(args.input) else "не", "может быть названием файла")
