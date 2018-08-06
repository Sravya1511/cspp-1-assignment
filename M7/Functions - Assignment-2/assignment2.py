# Assignment-2 - Paying Debt off in a Year
def payingDebtOffInAYear(balance_1, annual_interest_rate):
	mfmp_ = 10
	temp_bal = balance_1
	year_count = 1
	while balance_1 > 0:
		balance_1 = temp_bal
		# print(mfmp_,year_count)
		for i in range(1, 13):
			m_intrest_rate = annual_interest_rate/12.0
			monthly_unpaid_balance = balance_1 - mfmp_
			updated_balance_each_month = monthly_unpaid_balance + m_intrest_rate*monthly_unpaid_balance
			balance_1 = updated_balance_each_month
			# print (i,balance_1)
		# if balance_1 <=0.5:
		#     break
		mfmp_ += 10
		year_count += 1
	return mfmp_
def main():
	data = input()
	data = data.split(' ')
	data = list(map(float, data))
	print(payingDebtOffInAYear(data[0],data[1]))
	
if __name__ == "__main__":
	main()