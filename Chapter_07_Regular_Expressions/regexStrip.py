import re

testText = '123abc123'

def regexStrip(text, characters = ' '):
    characters = re.escape(characters)
    textToStrip = re.compile(r'(' + characters + ')*')

    cleanText = re.sub(textToStrip, '', text)

    return cleanText

print("'" + regexStrip(testText, '123') + "'")