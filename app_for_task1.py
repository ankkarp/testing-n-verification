import re
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('email', help='Потенциальный имэйл')
args = parser.parse_args()

print(bool(re.fullmatch(r"\w+@\w+\.\w+", args.email)))