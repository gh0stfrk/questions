"""parseInt_reloaded

In this kata we want to convert a string into an integer. The strings simply represent the numbers in words.

Examples:

"one" => 1
"twenty" => 20
"two hundred forty-six" => 246
"seven hundred eighty-three thousand nine hundred and nineteen" => 783919

Additional Notes:

The minimum number is "zero" (inclusively)
The maximum number, which must be supported is 1 million (inclusively)
The "and" in e.g. "one hundred and twenty-four" is optional, in some cases it's present and in others it's not
All tested numbers are valid, you don't need to validate them

"""


class ParseInt:
    def process_string(self, string):
        words = string.replace('-', ' ').split()
        if words.index('thousand'):
            idx = words.index('thousand')
            remiander = list(filter(lambda x : x != 'hundred', words[idx+1:]))
            new_words = words[:idx+1] + remiander
            return new_words
        return words


    def text_to_int(self, text):

        ones = {
            "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4,
            "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9
        }
        tens = {
            "ten": 10, "eleven": 11, "twelve": 12, "thirteen": 13, "fourteen": 14,"fifteen": 15, "sixteen": 16, "seventeen": 17, "eighteen": 18, "nineteen": 19 }

        tens_multiple = {
            "twenty": 20, "thirty": 30, "forty": 40, "fifty": 50, "sixty": 60,
            "seventy": 70, "eighty": 80, "ninety": 90
        }

        hundreds = {"hundred": 100,"thousand": 1000, "million": 100000}

        words = self.process_string(text)
        n = len(words)
        number = 0
        i = 0

        while i < n:
            word = words[i]

            if word in ones:
                number += ones[word]
            elif word in tens:
                number += tens[word]
            elif word in tens_multiple:
                number += tens_multiple[word]
                if i+1 < n and words[i+1] in ones:
                    number += ones[words[i+1]]
                    i += 1
            elif word in hundreds:
                number *= hundreds[word]
            i += 1

        return number



if __name__ == "__main__":
    parse_int = ParseInt()
    fucked_ups = [
        "eight hundred eighty-eight thousand eight hundred and eighty-eight",
        "three thousand five hundred fifty-three",
        "one thousand three hundred and thirty-seven"
    ]

    for x in fucked_ups:
        result = parse_int.text_to_int(x)
        print(result)



