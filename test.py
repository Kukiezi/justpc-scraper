def removeRpmFromText(text):
    return text.replace("obr./min.", "")

def removeRpmTextStart(text):
    return text[3:len(text)]

def getRpm(text):
    if not text[0].isdigit():
        text = removeRpmTextStart(text)
    return removeRpmFromText(text)

def getNoise(text):
    return text.replace(",", ".")

def main(text):
    print(getRpm(text))

if __name__ == "__main__":
    print(getNoise("9,2 - 24,6 dB"))