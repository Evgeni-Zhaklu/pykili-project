import os # импортируем os для использования некоторых функций, например, os.walk()
files_count = 0
unique_files = set() # set для создания пустого множества; set - набор, множестов, совокупность; set -  последовательность, в которую элеименты входят один раз
duplicate_files = set()
file_types = set()
start_path = '/Users/a1126183/Downloads/'
tree = os.walk(start_path) # start_path - то, где нам нужно покопаться
for path, dirs, files in tree:
    files_count += len(files) # считаем общее количество найденных файлов 
    for file in files:
        if file in unique_files:
            duplicate_files.add(file)
        else:
            unique_files.add(file)

        try:
            file_type = file.rsplit('.', 1)[1] # отделяем формат файла от названия по точке 
            file_types.add(file_type)
        except IndexError as error:
            error = 'index_error'
print('ПОВТОРЯЮЩИЕСЯ ФАЙЛЫ: ')
for files in duplicate_files:
    print(files, sep='\n') # sep='\n' - для переноса строки, красивенько должно же все быть 
print()
print('РАСШИРЕНИЕ ФАЙЛОВ: ')
for types in file_types:
    print(types, sep='\n') # sep='\n' - здесь тоже для переноса строки, красивенько должно быть везде
s = '''Количество всех файлов в '{root} ' - {files}'''.format(root=start_path,
                                                      files = files_count) 
# format - сделать строку, подставив в неё некоторые данные, полученные в процессе выполнения программы; подстановку данных можно сделать с помощью форматирования строк. Форматирование можно сделать с помощью оператора %, либо с помощью метода format.
s1 = '''Количество уникальных файлов - {unique}'''.format(unique = len(unique_files))
s2 = '''Количество повторяющихся файлов - {duplicate}'''.format(duplicate=len(duplicate_files))
print(s, s1, s2, sep = '\n')

# main problem - непонятно, сколько раз повторяется файл, поэтому мы можем не досчитаться

# сделать как функцию, с возможностю ввода необходимого диска или папки 

# os - библиотека, на которой построена вся работа 

# Модуль os позволяет взаимодействовать с операционной системой - узнавать/менять файловую структуру,
# переменные среды, узнавать имя и права пользователя и др.

# os.walk()

# Метод os.walk() дает нам возможность для итерации на корневом уровне пути. Это значит, что мы можем назначить путь к этой функции и получить доступ ко всем её подкаталогам и файлам.
