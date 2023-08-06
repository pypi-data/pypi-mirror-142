letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
           'W', 'X', 'Y', 'Z']


def in_digits():
    print("Enter your number:")
    a = int(input())
    print("Enter the number system into which you are going to translate this number:")
    n = int(input())
    ans = []
    while a > (n - 1):
        ans.append(a % n)
        a //= n
    ans.append(a)
    ans.reverse()
    answer = ""
    ok = True
    for i in range(len(ans)):
        if ans[i] < 10:
            answer += str(ans[i])
        elif (ans[i] >= 10) and (ans[i] <= 35):
            answer += str(letters[ans[i] - 10])
        else:
            answer = "Not enough knowledge to translate into this number system. Go into the program 2.hs. Sorry :("
            ok = False
            break
    if ok:
        print("Your answer:")
    print(answer)


def out_digits():
    print("Enter your number:")
    a = input()
    print("Enter the number system from which you are going to translate this number:")
    n = int(input())
    answer = 0
    for i in range(len(a)):
        if ('A' <= a[i]) and (a[i] <= 'Z'):
            f = letters.index(a[i])
            f += 10
        else:
            f = int(a[i])
        answer += n**((len(a) - 1) - i) * f
    print("Your answer:")
    print(answer)


def main_program(flag):
    if flag > 1:
        print('\n' + '\n')
    print("What are you want?")
    print("I - in (convert from a decimal system to another)")
    print("O - out (convert from an any number system to decimal)")
    ch = input()
    if ch == 'I' or ch == 'i':
        in_digits()
    elif ch == 'O' or ch == 'o':
        out_digits()
    else:
        print('\n' + "Ummmmm, you entered something wrong :(" + '\n' + "Lets's try asgain ;)" + '\n')
        main_program(1)

def main_converter():
    s = ''
    flag = 0
    while s != 'N' and s != 'n':
        flag += 1
        main_program(flag)
        print('\n' + "Do you want to use the program again?")
        print("Y - Yes")
        print("N - No")
        s = input()
    print("Bye! Have a nice day!")
