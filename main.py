def minifier(text):
    punc = ".,:;%#/])*" # str of all valid punctuation
    text = text.split("\n");

    text = map(str.strip, text)  # removes whitespace from each element (if element is purely whitespace, it becomes an empty string)
    text = list(filter(lambda x: x != "", text)); # removes empty strings

    i = 0;
    while (i < len(text)):
        # removing all comments
        if ("<!--" in text[i]):
            text.pop(i);
            i -= 1; # since idx will be offset by +1
        
        # removing last semicolon in each class:
        if (text[i] == "}" and text[i-1] == ";"):
            text[i-1] = text[i-1][:-1]; # remove last character
        
        # removing all whitespaces in between valid punctuation
        j = 0;
        while (j < len(text[i]) - 1):
            if (text[i][j] in punc and text[i][j+1] == " "):
                tempArr = list(text[i]);
                tempArr[j+1] = "";
                text[i] = "".join(tempArr);
            j += 1;
        
        # removing whitespace in between tag name and "{" (l solution)
        k = 0;
        while (k < len(text[i])):
            if(text[i][k] == "{" and text[i][k-1] == " "):
                tempArr = list(text[i]);
                tempArr[k-1] = "";
                text[i] = "".join(tempArr);
            k += 1;

        # removing px units for width and height
        if ("width" in text[i] or "height" in text[i]):
            text[i] = text[i].replace("px", "");
        
        # slice list from before this element
        if (text[i] == "</style>"):
           text = text[:i-1];

        i += 1;
    
    text = "".join(text).replace("\n", "");

    if (text[-1] == ";"):
        text = text[:-1];

    return text;