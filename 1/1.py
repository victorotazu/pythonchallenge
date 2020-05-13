phrase = """
g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.
"""

alphabet = [chr(x) for x in range(97, 123)]
last_index = len(alphabet) - 1

for letter in phrase:
    if letter in alphabet:
        index = alphabet.index(letter)
        print(alphabet[-(last_index - (index + 1))], end="")
    else:
        print(letter, end="")



