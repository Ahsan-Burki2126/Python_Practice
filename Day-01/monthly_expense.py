#Your monthly expense list (from Jan to May) looks like this,
"""
Write a program that asks you to enter an expense amount and program should tell you in which month that expense occurred. If expense is not found then it should print that as well.
"""
expense_list = [2340, 2500, 2100, 3100, 2980]
months = ["january","Feburary","March","April","May"]


def find_expense(exp):
    expense_to_found = exp
    try:
        indexOfExpense=expense_list.index(expense_to_found)
        print(f"{expense_to_found} is the expense for {months[indexOfExpense]}")
    except ValueError:
        print(f"the value you entered {expense_to_found} is not in the list")    




find_expense(2980)



