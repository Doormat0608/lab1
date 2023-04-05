from parser import parse, wtf

def main():
    url = 'https://omgtu.ru/general_information/faculties/'
    faculties = parse(url)
    wtf(faculties, 'faculties.txt')
    print("Факультеты:")
    print(*faculties, sep="\n")

if __name__ == '__main__':
    main()
