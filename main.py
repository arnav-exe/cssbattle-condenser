import pyperclip as pc

def readClipboard():
    return pc.paste();

def writeClipboard(text):
    pc.copy(text);

def optimizer(text):
    punc = ".,:;%#/"
    text = text.split("\n");
    text = list(filter(lambda x: x != " " and x != "", text)); # remove whitespace and empty elements

    i = 0;
    while (i < len(text)):
        if "<" in text[i] or ">" in text[i]:
            i += 1;
        else:


    return text;

def main():
    text = readClipboard();
    while(text == ""):
        text = readClipboard();
    
    print(optimizer(text));


if __name__ == "__main__":
    main();