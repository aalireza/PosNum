NUM_REPO = dict(
    dict({i: str(i) for i in range(10)}).items() +
    dict({10: 'a', 11: 'b', 12: 'c', 13: 'd',
          14: 'e', 15: 'f', 16: 'g'}).items()
)


class BaseChanger(object):
    def __init__(self, number, base, delim=""):
        pass

def base_change(number, origin_base, target_base, delim=""):

    def base_10_to_b(decimal, b, delim=""):
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
                remainder_string = NUM_REPO[remainder]
            else:
                remainder_string = str(remainder)
            new_num_string = remainder_string + new_num_string
        return new_num_string


    def base_b_to_10(number, b, delim=""):
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
            for j in NUM_REPO:
                if number[i] == NUM_REPO[j]:
                    result += int(j) * b ** int(i)
        return result

    return base_10_to_b(
        base_b_to_10(number, origin_base, delim), target_base, delim
    )
