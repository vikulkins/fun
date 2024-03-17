coffe = float(input()) * 1000
milk = float(input()) * 1000


def main(coffe:float, milk:float)-> int:
    visitors = 0
    for i in range(1, 10**10):
        if (i % 3 == 0) or (i % 15 == 0): #cappicino
            if milk >= 100:
                if coffe >= 7:
                    milk -= 100
                    coffe -= 7
                    visitors += 1
                else:
                    return visitors

            elif coffe >= 7:
                visitors += min(i % 5, i % 3)
                return visitors
            else:
                return visitors
        elif i % 5 == 0: #latte
            if milk >= 180:
                if coffe >= 7:
                    milk -= 180
                    coffe -= 7
                    visitors += 1
                else:
                    return visitors

            elif coffe >= 7:
                visitors += min(i % 5, i % 3)
                return visitors
            else:
                return visitors
        elif coffe >= 7:
            visitors += 1
            coffe -= 7

        else:
            return visitors
        print("coffe - ", coffe, "milk - ", milk)


print(main(coffe, milk))
