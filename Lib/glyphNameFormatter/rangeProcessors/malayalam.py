

def process(self):
    # edits go here
    self.edit("MALAYALAM")

    self.edit("MARK")
    self.edit("VOWEL")

    self.edit("VOCALIC", "vocal")
    self.edit("SIGN", "sign")

    self.edit("CHILLU", "chillu")

    self.processAs("Helper Digit Names")

    self.edit("DIGIT")
    self.edit("NUMBER")
    self.edit("FRACTION")
    self.edit("LETTER")
    self.lower()
    self.compress()

if __name__ == "__main__":
    from glyphNameFormatter.test import printRange
    printRange("Malayalam")
