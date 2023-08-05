from math import e


def inv_norm_sigmoid(x: float, s: float = 0.3, t: float = 0.88, p: float = 3.3, adjust: bool = False) -> float:
    """ Approach a value to an inverse normalized sigmoid function which starts in 0 with a value of 1,
    and it is reducing until the limit 0 in the infinite. Its equation is:

        .. math::
           1-\\frac{t}{1+e^\\frac{p-|x|}{s}}

        You can test this function in `demos web page <https://www.desmos.com/calculator/mea58nqqwr>`_.

    :param x: The value to normalize.
    :param s: The velocity of decreasing function.
    :param t: The bottom limit velocity.
    :param p: The curve with.
    :return: A value between 0 and 1 with the value x normalized by an inverse sigmoid.
    """
    if adjust:
        return 1 - t / (1 + e ** ((p - abs(x)) / s)) if x != 0 else 1
    return 1 - t / (1 + e ** ((p - abs(x)) / s))
