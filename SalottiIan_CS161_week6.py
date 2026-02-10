

def main():
    print("Which option would you like to choose?\n"
          "1. Sum of digit\n"
          "2. Palindrome check")
    choice = input()
    match choice:
        case "1":
            sum_of_digits(input('Enter a number:'), 0)
        case "2":
            check_palindrome(input("Enter a word: "), '')
        case _:
            print("Please enter either a 1 or 2")



def sum_of_digits(num, total):
    if len(num) == 0:
        print(f"The sum of this numbers digits is: {total}")
        return

    num = str(num)
    total += int(num[0])
    new_num = num[1:]
    sum_of_digits(new_num, total)



def check_palindrome(word, new_word):
    count = len(word) - len(new_word)
    if len(new_word) ==  count + len(word):
        if word == new_word:
            print(f'The word "{new_word}" is a palindrome')
        else:
            print(f'The word "{word}" is not a palindrome')
        return
    word = word.lower()
    new_word += word[count - 1]
    check_palindrome(word, new_word)




if __name__ == '__main__':
    main()