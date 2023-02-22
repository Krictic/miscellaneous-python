# For numbers 1 through 100,
#
# if the number is divisible by 3 print Fizz;
# if the number is divisible by 5 print Buzz;
# if the number is divisible by 3 and 5 (15) print FizzBuzz;
# else, print the number.
def fizzbuzz():
    n = 101
    for i in range(1, n):

        fizz = i % 3 == 0
        buzz = i % 5 == 0
        fizzbuzz = i % 15 == 0
    
        if fizz and not buzz:
            print("fizz")
        elif buzz and not fizz:
            print("buzz")
        elif fizzbuzz:
            print("fizzbuzz")
        else:
            print(i)


def main():

    fizzbuzz()


if __name__ == "__main__":
    main()
