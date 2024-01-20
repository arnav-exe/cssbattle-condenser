import pyperclip as pc
import time # USE time.perf_counter() TO MEASURE PROGRAM PERFORMANCE (WILL DEPLOY AS AWS LAMBDA FUNC  SO SHOULD REMAIN IN FREE TIER PERFORMANCE ALLOCATION)
from bs4 import BeautifulSoup as bs

def readClipboard():
    return pc.paste();

def writeClipboard(text):
    pc.copy(text);

def optimizer(text):
    punc = ".,:;%#/"
    text = text.split("\n");

    text = map(str.strip, text)  # removes whitespace from each element (if element is purely whitespace, it becomes an empty string)
    text = list(filter(lambda x: x != "", text)); # removes empty strings

    i = 0;
    while (i < len(text)):
        """TODO:
        1. remove all elements that are comments [DONE]
        2. remove last set of lines:
            a. final closing curly bracket "}" [DONE]
            b. closing style tag "</style>" [DONE]
        3. remove last semicolon inside each class [DONE]
        4. remove all whitespaces in between valid punctuation
        5. remove units for width and height (EG: width: 100px -> width: 100)
        6. remove all newlines"""

        if ("<!--" in text[i]): # removing comments
            text.pop(i);
            i -= 1; # since idx will be offset by +1
        
        # removing last semicolon in each class:
        if (text[i] == "}"):
            text[i-1] = text[i-1][:-1]; # remove last character
        
        if (text[i] == "</style>"): # slice list from before this element
            text = text[:i-1];


        i += 1;

    return text;

def main():
    text = readClipboard();
    while(text == ""):
        text = readClipboard();
    
    print(optimizer(text));


if __name__ == "__main__":
    main();
