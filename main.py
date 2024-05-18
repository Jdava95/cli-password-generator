import argparse

from generator import password_generator


def main():
    parser = argparse.ArgumentParser(description='Пример использования argparse')
    subparser = parser.add_subparsers(dest='command')

    gen = subparser.add_parser("generate", help="Генерация пароля")
    gen.add_argument('-l','--length', help='Длина пароля (по умолчанию 10)', required=True, type=int)
    gen.add_argument('-c','--complication', help='Выберите сложность от 1 до 3',  required=False, type=int)
    gen.add_argument('-s','--save', help='Сохранить в буфер', action='store_true')


    args = parser.parse_args()

    if args.command == 'generate':
        if args.complication and args.length:
            password_generator(args.__dict__)

if __name__ == "__main__":
    main()