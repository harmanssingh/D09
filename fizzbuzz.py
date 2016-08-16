def fizzbuzz():
    for n in range(1,101):
        msg=''
        if n % 3 == 0:
            msg+="Fizz"
        if n % 5 == 0:
            msg+="Buzz"
        print(msg or n)

fizzbuzz()
