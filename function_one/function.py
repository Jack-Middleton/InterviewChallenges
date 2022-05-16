effective_dates = []
percentage_value = []

def date_conversion(date):
    new_date = date.split("/")
    # returns the rough amount of days the input date is worth, not inc. specific months
    return int(new_date[0]) + int(new_date[1]) * 30 + int(new_date[2]) * 365.25


def Inflation_factor(From_date, To_date, Effective_Dates, Percentage_Values):
    from_index = -1
    to_index = -1
    # ^^ for error handling
    from_date_days = date_conversion(From_date) # converts user input from_date to equivalent number of days
    to_date_days = date_conversion(to_date) # same as above
    if from_date_days > to_date_days:
        return "Please make sure your from_date is after than your to_date"
    if to_date_days > date_conversion(Effective_Dates[-1]) + 365:
        return "Please enter a to_date that is before 2051"
    for i in range(len(Effective_Dates)):
        # for each item in the range 1 to length of effective dates
        # if the first effective date is less than the user inputted from_date & from_index is equal to -1 (ie; hasnt been overwritten by anything) 
        if date_conversion(Effective_Dates[i]) < from_date_days and from_index == -1:
            from_index = i
            # grabs the index of the correct from_date
            # and then it does the same again, without the and from_index, because it breaks after it is found (starts smaller number, then bigger number)
        if date_conversion(Effective_Dates[i]) < to_date_days:
            # grabs the index of the correct to_date
            to_index = i
            break
    
    
    if from_index == to_index: # ie; the same interest rate
        # just calculates per day at the one interest rate
        return (1+Percentage_Values[to_index]/100) ** ((to_date_days-from_date_days) /365.25)
    else:
        cumulative_interest = 1 # because its multiplication, essentially starting at 100%    
                                # calculates the first years interest           # make the 'to_date' equal to the next whole year
        cumulative_interest *= (1+Percentage_Values[from_index]/100) ** ((date_conversion(Effective_Dates[from_index + 1]) - from_date_days) /365.25) 
        # essentially, works out the cumulative interest up to the next whole year
        for i in range(from_index + 1, to_index):
            cumulative_interest *= (1+Percentage_Values[i]/100) ** ((date_conversion(Effective_Dates[i + 1]) - date_conversion(Effective_Dates[i])) /365.25) 
            # then works out the cumulative interest for the days between the date i and i + 1 where i is the dates index previously calculated
        cumulative_interest *= (1+Percentage_Values[to_index]/100) ** (to_date_days - date_conversion(Effective_Dates[to_index]) /365.25) 
        # and calculates the final fraction of the years interest
        return cumulative_interest

while True:
    date = input("Enter a date in dd/mm/yyyy format: \n")
    value = float(input("Enter a percentage value: \n "))
    effective_dates.append(date)
    percentage_value.append(value)
    if input("e to finish entering values: \n").lower():
        break

print("Dates: ", ", ".join(effective_dates))
print("Percentage Values: ", percentage_value)

while True:
    from_date = input("enter from_date: \n")
    to_date = input("enter to_date: \n")
    if from_date == "" or to_date == "":
        continue
    print(Inflation_factor(from_date, to_date, effective_dates, percentage_value))
    if input("e to exit: \n").lower() == "e": 
        break