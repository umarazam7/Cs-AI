def interest_monthly( balance ,  annual_interest_rate):
	 
	interest = balance*(annual_interest_rate/1200)
	return interest


def future_investment_value(investment_amount, monthly_interest_rate,  number_of_years ):
	 futureVal = investment_amount *  (1+monthly_interest_rate )**number_of_years * 12
	 return futureVal  
		