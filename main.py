import pyperclip as pc

def readClipboard():
    return pc.paste();

def writeClipboard(text):
    pc.copy(text);

def main():
    print("Hello World!");

if __name__ == "__main__":
    main();