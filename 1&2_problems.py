equation = input("What is your equation?").split()




try:
    assert equation[0] in ['+', '-', '*', '/']
 


    if equation[0] == "+":
        answer = int(equation[1]) + int(equation[2])
    elif equation[0] == "-":
        answer = int(equation[1]) - int(equation[2])
    elif equation[0] == "*":
        answer = int(equation[1]) * int(equation[2])
    else:
        answer = int(equation[1]) / int(equation[2])
 


except ZeroDivisionError:
    print("Вы произвели деление на ноль, что является математической ошибкой. Попробуйте еще раз.")

except AssertionError:
    print("Вы допустили ошибку. В данной программе можно использовать только операции сложения, вычитания, умножения и деления. Попробуйте еще раз")

except IndexError:
    print("Вы ввели недостаточное количество аргументов для математической операции. Попробуйте еще раз.")

except ValueError:
    print("Вы ввели не число. Попробуйте еще раз.")
  

else:
    print("Ответ в данном примере: ", answer)


