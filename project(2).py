import os

def file_name(filename): # нзавание файлов в папке или на диске
    if os.path.exists(filename):
        name = os.listdir(filename)
        print ('Список найденных файлов', name, 'по этому пути -', os.path.dirname(filename))
    else:
        print('Такого директория не существует')

def name_file(filename): # еазвание файлов в папке или на диске
    if os.path.exists(filename):
        tree = os.walk(filename)
        for files in tree:
            for file in files:
                    print (file)
    else:
        print('Такого директория не существует')
        
# который варинат удачнее? 

def file_number(filename): # количество файлов в папке или на диске
    if os.path.exists(filename):
        files_count = []
        tree = os.walk(filename)
        for roots, dirs, files in tree:
            for file in files:
                files_count.append(file)
        print('Количество файлов: ', len(files_count), 'по этому пути -', os.path.dirname(filename))
    else:
        print('Такого директория не существует')
        

def unique_duplicate(filename): # уникальные и потворяющиеся файлы в папке или на диске
    if os.path.exists(filename):
        unique_files = []
        duplicate_files = []
        tree = os.walk(filename)
        for roots, dirs, files in tree:
            for file in files:
                if file in unique_files:
                    duplicate_files.append(file)
                else:
                    unique_files.append(file)
        print('По данному пути -', os.path.dirname(filename))
        print('Были найдены уникальные файлы:', unique_files, 'количестов которых -', len(unique_files))
        print('Были найдены повторяющиеся файлы:', duplicate_files, 'количество которых -', len(duplicate_files))
    else:
        print('Такого директория не существует')

    
def exten(filename): # расширение файлов в папке или на диске / сильно странно?
    if os.path.exists(filename):
        name = os.listdir(filename)
        typ = '\n'.join(name)
        ext = typ.replace('.', ' - ')
        print(ext)
    else:
        print('Такого директория не существует')
