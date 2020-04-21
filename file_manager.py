from string_parser import StringParser
import os


class FileManager:
    def __init__(self, dir):
        self.dir = dir
        self.files = [file for file in os.listdir(dir)]
        self.words = []

    def read_txt_files(self):
        for file in self.files:
            filename = '{}/{}'.format(self.dir, file)
            with open(filename, 'r', encoding='utf-8') as document:
                lines = document.readlines()
                for line in lines:
                    if len(line) > 0:
                        new_sentence = StringParser.refactor_sentence(line)
                        self.words.append(new_sentence)
            document.close()

    def write_txt_files(self):
        with open('skribbl_final.txt', 'w', encoding='utf-8') as document:
            for word in self.words:
                if word == self.words[-1]:
                    document.write('{}\n\n'.format(word))
                else:
                    document.write('{}, '.format(word))

            document.write('Size: {} words from {} files'.format(len(self.words), len(self.files)))
            document.close()
        print('Size: {} words from {} files'.format(len(self.words), len(self.files)))