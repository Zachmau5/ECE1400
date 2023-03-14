#!/usr/bin/python3

import scanf as scanf

class Resistor:

    def __init__(self, string):

        self.name = None
        self.positiveNode = None
        self.negativeNode = None
        self.value = None
        self.read(string)


    def current(self, floatvoltage):
        return floatvoltage/self.value

    def read(self, s):

        if s is None or not s[0].isalpha() or s[0].lower() != "r":
            raise ValueError(f"Resistor must start with an R: {s}")


        s = s.split(" ")
        if len(s) != 4: # check if its always 4
            raise ValueError(f"Resistor requires at least 4 values: {s}")

        self.name = s[0]
        self.positiveNode = s[1]
        self.negativeNode = s[2]
        self.value = decodeValue(s[3])

    def print(self):
        print(f"{self.name}\t{self.positiveNode}\t{self.negativeNode}\t{self.value:.2e}")
def decodeValue(string):
    string=string.lower()
    suffix = {'t': 1e12, 'g': 1e9, 'meg': 1e6, 'x': 1e6, 'k': 1e3, 'm': 1e-3, 'u': 1e-6, 'n': 1e-9, 'p': 1e-12, 'f': 1e-15, 'a': 1e-18}
    val,suf = scanf.scanf("%f%s", string)

    if suf in suffix:
        try:
            return float(val) * suffix[suf]
        except:
            raise ValueError(f"Invalid Value: {string}")

    try:
        return float(string)
    except:
        raise ValueError(f"Invalid Value: {string}")
