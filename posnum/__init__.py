from ast import literal_eval as leval
from string import ascii_letters

STANDARD_ALPHABETS = set(range(2, 63))
AVAILABLE_ALPHABETS = STANDARD_ALPHABETS | set([256])


def _alphabet_maker(length):
    if length in AVAILABLE_ALPHABETS:
        if length < 10:
            return {i: str(i) for i in range(length)}
        if length < 63:
            return dict({i: str(i) for i in range(10)}.items() +
                        {i + 10: ascii_letters[i]
                         for i in range(length - 10)}.items())
        if length == 256:
            with open(r"./data/base256.txt", 'r') as f:
                return {i: leval(e) for i, e in enumerate(f.readlines())}


class BaseChanger(object):
    def __init__(self, number, current_base,
                 current_delim="", current_alphabet=None):
        self.number = number
        self.current_base = current_base
        self.current_delim = current_delim
        self.alphabet = current_alphabet

    def _base_10_to_b(self, decimal, b, delim=""):
        """
        Changes the base of a decimal to b where b <= len(NUM_REPO.items())
        Parameters
        ----------
        decimal           int or long
        b                 int
        Returns
        -------
        new_num_string    str
        """
        new_num_string = ''
        current = decimal
        while current != 0:
            current, remainder = divmod(current, b)
            if 26 > remainder > 9:
                remainder_string = self.alphabet[remainder]
            else:
                remainder_string = str(remainder)
            new_num_string = remainder_string + new_num_string
        return new_num_string

    def _base_b_to_10(self, number, b, delim=""):
        """
        Changes the base of `number` from `b` to 10.
        Parameters
        ----------
        number:           str
        b:                int
        Returns
        -------
        result            int or long
        """
        result = 0
        if delim == "":
            number = list(str(number))
        else:
            number = str(number).split(delim)
        number.reverse()
        for i in range(len(number)):
            for j in self.alphabet:
                if number[i] == self.alphabet[j]:
                    result += int(j) * b ** int(i)
        return result

    def change(self, target_base, target_delim, target_alphabet):
        pass
