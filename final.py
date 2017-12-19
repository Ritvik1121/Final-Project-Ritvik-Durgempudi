#CaeserCipher Decoder/Encoder by Ritvik Durgempudi

def mode():
    mode = raw_input(" Please enter 'e' for encoder or 'd' for decoder:")
    if mode == "e":
        print("Encrypter")
    elif mode == 'd':
        print("Decoder")
    else:
        print("Enter either 'e' or 'd' ")
    return mode

def key():
    key = 0
    key = int(raw_input("Enter your key number(1-26):"))
    if key >= 1 and key <= 26:
        return key
    else:
        print("Please chose a number within parameter.")

def encoder_decoder(mode, phrase, key):
    alphabet = ["a", "b", "c", "d", "e", "f","g", "h","i", "j", "k", "l", "m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    capital_alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    encoded = ""
    decoded = ""
    if mode == "e":
        for i in range(0, len(phrase)):
            if phrase[i] in capital_alphabet:
                encoded = encoded + capital_alphabet[capital_alphabet.index(phrase[i])-(len(capital_alphabet)-key)]
            elif phrase[i] in alphabet:
                encoded = encoded + alphabet[alphabet.index(phrase[i])-(len(alphabet)-key)]
            elif phrase[i] not in alphabet:
                encoded = encoded + phrase[i]
        return "Your new message is:", encoded, "With a key of:", key
    if mode == "d":
        for i in range(0, len(phrase)):
            if phrase[i] in capital_alphabet:
                decoded = decoded + capital_alphabet[capital_alphabet.index(phrase[i]) - key]
            elif phrase[i] in alphabet:
                decoded = decoded + alphabet[alphabet.index(phrase[i]) - key]
            elif phrase[i] not in alphabet:
                decoded = decoded + phrase[i]
        return "Your new message is:", decoded,"With a key of:", key

mode = mode()
phrase = raw_input("Please enter your message:")
key = key()

print encoder_decoder(mode, phrase, key)
