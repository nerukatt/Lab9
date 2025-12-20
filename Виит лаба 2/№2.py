def write_new_file(filename, text):
    with open(filename, 'w') as f:
        f.write(text)
    return "Файл успешно создан"

def append_in_file(filename, text):
    with open(filename,'a') as f:
        f.write('\n'+text)
    return "Текст успешно добавлен"
    
wrt = int(input("Режим записи:(создание файла - 1; Добавление в файл - 2)"))
if wrt==1:
    filename = input("Введите название нового файла:")
    newtext = input("Введите текст:")
    write_new_file(filename, newtext)
elif wrt==2:
    while wrt==2:
        filename = input("Введите название нового файла:")
        text = input("Введите текст для добавления:")
        append_in_file(filename, text)
        wrt = int(input("Продолжить запись - 2:"))
        if wrt!=2:
            break
def append_in_file(filename):
    file1 = filename
    with open (file1,"a") as f:
        f.write('\n'+file1)

wrt = 0
wrt = int(input("Режим записи:(создание файла - 1; Добавление в файл - 2)"))
if wrt==1:
    usertext = input("Введите текст:")
    write_new_file(filename)
elif wrt==2:
    while wrt==2:
        text = input("Введите текст для добавления в файл:")
        append_in_file(file1.txt)
        wrt = int(input("Продолжить запись - 2:"))
        if wrt!=2:
            break