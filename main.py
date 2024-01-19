import pyperclip as pc

def readClipboard():
    return pc.paste();

def writeClipboard(text):
    pc.copy(text);

def optimizer(text):
    punc = ".,:;%#/"
    text = text.split("\n");
    text = list(filter(lambda x: x != "", text)); # removes empty elements

    i = 0;
    while (i < len(text)):
        text[i] = text[i].strip();

        if (text[i].isspace()):
            text.pop(i);

        if ("<" in text[i] or ">" in text[i]): #if element is a html tag
            i += 1;

        else: # main optimization loop
            
            """TODO:
            1. remove all elements that are comments
            2. remove last set of lines:
                a. final class semicolon
                b. final closing curly bracket "}
                c. closing style tag "</style>"
                d. all comments below that [DONE]
            3. remove all whitespaces in between valid punctuation
            4. remove last semicolon inside each class
            5. remove all newlines"""

            if ("<!--" in text[i]) { # removing comments
                text.pop(i);
            }

        i += 1;   

    return text;

def main():
    text = readClipboard();
    while(text == ""):
        text = readClipboard();
    
    print(optimizer(text));


if __name__ == "__main__":
    main();