yearly_salary = float(input('Yearly Salary:')) 
portion_saved = float(input('portion of salary you want to be Saved :')) 
cost_of_dream_home = float(input('Cost of dream Home:')) 

#initial phase
portion_down_payment = cost_of_dream_home*0.25
amount_saved = 0
month = 0

while (amount_saved < portion_down_payment) :
    intrest = amount_saved*(0.05/12)
    monthly_saving = (yearly_salary/12)*portion_saved
    amount_saved += intrest + monthly_saving
    month+=1
    
print('TOTAL MONTH NEED' , month)    
    
