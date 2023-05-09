text = "The Python String split() method splits all the words in a string separated by a specified separator. This separator is a delimiter string, and can be a comma, full stop, space character or any other character used to separate strings. Usually, if multiple separators are grouped together, the method treats it as an empty string. But if the separator is not specified or is None, and the string consists of consecutive whitespaces, they are regarded as a single separator, and the result will contain no empty strings at the start or end if the string has leading or trailing whitespace. Consequently, splitting an empty string or a string consisting of just whitespace with a None separator results in an empty string."

def textFinder(text: str, size: int) -> str:
    punctuationMarks = ['.', ',', '(', ')']

    newText = ''
    for char in text:
        if char not in punctuationMarks:
            newText += char

    words = newText.split()
    for word in words:
        if len(word) == size:
            return word
    
    return ''


print(textFinder(text, 7))