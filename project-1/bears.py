
# Given integer n, returns True or False based on reachability of goal
# See write up for "rules" for bears
def bears(n: int) -> bool:
    """A True return calue means that it is possible to win 
    the bear game by starting with n bears. A False return value means 
    that it is not possible to win the bear game by starting with n 
    bears."""

    if n == 42:
        return True
    elif n < 42:
        return False
    else:

        # Divisible by 2, return n/2 bears
        if n % 2 == 0:
            if bears(n // 2):
                return True
        # Divisible by 3 or 4, return the multiple of the last two digits
        if (n % 3 == 0) or (n % 4 == 0):
            last1 = n % 10
            last2 = (n // 10) % 10
            if last1 * last2 != 0:
                if bears(n - last1 * last2):
                    return True
        # Divisible by 5, return 42 bears
        if n % 5 == 0:
            if bears(n - 42):
                return True
            
    return False
