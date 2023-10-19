import sys


def factorize(number):
    p = 2
    while p * p <= number:
        if number % p == 0:
            q = number // p
            return p, q
        p += 1
    return None, None


if len(sys.argv) != 2:
    print("Usage: factors <file>")
    sys.exit(1)

input_file = sys.argv[1]

try:
    with open(input_file, 'r') as file:
        lines = file.readlines()
        for line in lines:
            number = int(line.strip())
            p, q = factorize(number)
            if p is not None and q is not None:
                print("{} = {} * {}".format(number, p, q))

except IOError:
    print("File '{}' not found.".format(input_file))
    sys.exit(1)
except ValueError:
    print("Invalid. All lines shld contain valid natural nmbrs greater than 1")
    sys.exit(1)
