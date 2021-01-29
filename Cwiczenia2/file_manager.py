class FileManager:
    file_name = 'testplik.txt'

    def __init__(self, file_name):
        self.file_name = file_name

    def read_file(self):
        uchwyt = open(FileManager.file_name, 'r', encoding='utf-8')

        for linia in uchwyt:
            print(linia)

        uchwyt.close()

    def update_file(self, text_data):
        uchwyt = open('testplik.txt', 'a', encoding='utf-8')
        uchwyt.write(text_data)
        uchwyt.close()
