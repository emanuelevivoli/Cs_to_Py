import sys

def reverse(input):
    return input [::-1]

iter = int(sys.argv[1])

for i in range(iter):
    input = sys.stdin.readline()
    print(reverse(input))
    sys.stdout.flush()