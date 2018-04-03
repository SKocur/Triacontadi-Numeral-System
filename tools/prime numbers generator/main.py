def convert_decimal_to_triacontadi(decimal):
    result = ""

    while True:
        num = str(decimal // 32)
        num_left = decimal - int(num) * 32

        if num_left < 10:
            result += str(num_left)
        else:
            result += chr(num_left + 55)

        if int(num) < 32:
            if int(num) < 10:
                result += num
            else:
                result += chr(int(num) + 55)
            break

        decimal = int(num)

    return result[::-1]

def is_prime(n):
    if (n == 1):
        return False
    elif (n == 2):
        return True;
    else:
        for x in range(2,n):
            if(n % x == 0):
                return False
        return True

file = open("prime_numbers_1000.txt", "w")
i = 1
prime_counter = 0
while True:
    if is_prime(i):
        file.write(str(i) + " " + convert_decimal_to_triacontadi(i) + "\n")
        prime_counter += 1
    if prime_counter == 1000:
        break
    i += 1
file.close()

file = open("prime_numbers_10000.txt", "w")
i = 1
prime_counter = 0
while True:
    if is_prime(i):
        file.write(str(i) + " " + convert_decimal_to_triacontadi(i) + "\n")
        prime_counter += 1
    if prime_counter == 10000:
        break
    i += 1
file.close()