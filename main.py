
import sys

def fizzbuzz(input_number):
    print(f'number input {input_number}')
    for x in range(1,input_number +  1):
        # print(f'debug {x}')
        if x % 15 == 0 :
            print('fizzbuzz')
        elif x % 5 == 0:
            print('buzz')
        elif x % 3 == 0:
            print('fizz')
    else:
        print(x)

    return True

def test_fizzbuzz():
    assert fizzbuzz(100) == True

if __name__ == '__main__':

    input_number = int(sys.argv[1])
    fizzbuzz(input_number)