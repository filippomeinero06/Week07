from time import sleep


def countdown_recursive(n):
    if n == 0:
        return
    else:
        print(n)
        n -= 1
        sleep(1)
        countdown_recursive(n)


countdown_recursive(10)