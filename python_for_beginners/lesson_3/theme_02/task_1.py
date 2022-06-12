salary = float(input())
loan = float(input())

if salary * 200 >= loan:
    print(f'Your loan application for {loan} has been approved.')
else:
    print(f'Your loan application for {loan} has been rejected.')


