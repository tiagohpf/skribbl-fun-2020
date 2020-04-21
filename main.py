import sys, os
from file_manager import FileManager

def main():
    dir = 'data'
    if len(sys.argv) > 1:
        dir = sys.argv[1]

    if os.path.exists(dir):
        file_manager = FileManager(dir)
        file_manager.read_txt_files()
        file_manager.write_txt_files()
    else:
        print('Directory not found!')


if __name__ == '__main__':
    main()