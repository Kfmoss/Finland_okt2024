import PyPDF2
import biblio


def main():
    print('insert a word. In case you want to close the program write quit')
    word = input('please insert a word \n')
    done = False
    while not done:
        if word == 'quit':
            done = True
            quit()
        else:
            print('exito')
            done = True
          

if __name__ == '__main__':
    main()