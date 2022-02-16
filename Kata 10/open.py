""" def main():
    try:
        configuration = open('config.txt')
    except FileNotFoundError:
        print("Couldn't fin the config.txt file!")
if __name__ == '__main__':
    main() """

def main():
    open("/path/to/mars.jpg")

if __name__ == '__main__':
    main()