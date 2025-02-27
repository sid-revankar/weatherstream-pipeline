def tri_pattern(size):
    for each in range(size):
        if each < size:
            print('*' * (each + 1), each,end='\n' if each < size - 1 else '')

def revers_numb(num)-> int:
    rev = 0
    while num > 0:
        rev = rev * 10 + num % 10
        num //= 10
    return rev

def prime(number)->bool:
    if number <=1:
        return False
    for i in range(2, int(number**0.5)+1):
        if number % i == 0:
            return False
    return True

def sum_of_num():
    sum_num = list(map(sum(int(digit)for digit in str(num))))
    return sum_num

def main():
    # print(prime(int(input("Enter a number to check its prime or not: "))))
    print(sum_of_num())

if __name__=='__main__':
    main()