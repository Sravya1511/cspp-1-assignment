"""assignment"""
def paying_debt_off_in_year(balance_1, annual_interest_rate, monthly_payment_rate):
    """A"""
    for i in range(1,13):
        monthly_intrest_rate = annual_interest_rate/12.0
        minimum_monthly_payment = monthly_payment_rate * balance_1
        monthly_unpaid_balance = balance_1 - minimum_monthly_payment
        updated_balance_each_month =  monthly_unpaid_balance + monthly_intrest_rate*monthly_unpaid_balance
        balance_1 = updated_balance_each_month
    return round (balance_1, 2)
def main():
    """a"""
    data = input()
    data = data.split(' ')
    data = list(map(float, data))
    print("Remaining balance:",paying_debt_off_in_year(data[0],data[1],data[2]))
if __name__ == "__main__":
    main()
