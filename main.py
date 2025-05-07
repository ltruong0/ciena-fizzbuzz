
import sys

def fizz_buzz(input_number, a, b):
    print(f'number input {input_number}')
    for x in range(1,input_number +  1):
        # print(f'debug {x}')
        if x % 15 == 0 :
            print('fizzbuzz')
        elif x % a == 0:
            print('buzz')
        elif x % b == 0:
            print('fizz')
        else:
            print(x)

if __name__ == "__main__":

    input_number = int(sys.argv[1])

    fizz_buzz(input_number, 5, 3)