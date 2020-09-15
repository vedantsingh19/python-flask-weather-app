
def prime_number_utility(day):
    if day > 1:

        for i in range(2, day):

            if (day % i) == 0:
                return False
                break
        else:
            return True

    else:
        return False

