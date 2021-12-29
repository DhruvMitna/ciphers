action = input("Do you want to decode or encode?: ")
text = input("Enter the text: ").lower()


output = ""

if action in ["decode", "d"]:

    correspondence = {

    "0": " ",
    "1": "a",
    "2": "b",
    "3": "c",
    "4": "d",
    "5": "e",
    "6": "f",
    "7": "g",
    "8": "h",
    "9": "i",
    "10": "j",
    "11": "k",
    "12": "l",
    "13": "m",
    "14": "n",
    "15": "o",
    "16": "p",
    "17": "q",
    "18": "r",
    "19": "s",
    "20": "t",
    "21": "u",
    "22": "v",
    "23": "w",
    "24": "x",
    "25": "y",
    "26": "z"

}

    nums = text.split(";")

    for num in nums:

        try:

            output += correspondence[num]

        except KeyError:

            output += num

elif action in ["encode", "e"]:

    correspondence = {

        " ": "0",
        "a": "1",
        "b": "2",
        "c": "3",
        "d": "4",
        "e": "5",
        "f": "6",
        "g": "7",
        "h": "8",
        "i": "9",
        "j": "10",
        "k": "11",
        "l": "12",
        "m": "13",
        "n": "14",
        "o": "15",
        "p": "16",
        "q": "17",
        "r": "18",
        "s": "19",
        "t": "20",
        "u": "21",
        "v": "22",
        "w": "23",
        "x": "24",
        "y": "25",
        "z": "26"

    }

    for char in text:

        if text.index(char) != -1:

            try:

                output += correspondence[char]
                output += ";"

            except KeyError:

                output += char

print(output)