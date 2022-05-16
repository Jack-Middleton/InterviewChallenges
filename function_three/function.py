low_range = [0,5000001,10000001,15000001,20000001,25000001,30000001,35000001,40000001,45000001,50000001]
high_range = [5000000,10000000,15000000,20000000,25000000,30000000,35000000,40000000,45000000,50000000,999999999999999999999]
cumulative_premium_band = [250000]


def base_premium_calc(gross_revenue):
    incremental_rate = 5
    cumulative_premium = 250000
    cumulative_rate = 5
    low_index = - 1
    high_index = - 1
    try:
         int(gross_revenue)
    except:
        return "Please enter gross revenue as an integer"
    gross_revenue = int(gross_revenue)
    if gross_revenue < 0:
        return "Please enter a number greater than or equal to 0"
    if gross_revenue > high_range[-1]:
        return "Please enter gross revenue"

    # finds the correct price band and grabs the index in the list
    for i in range(len(low_range)):
        if gross_revenue > low_range[i]:
            if gross_revenue < high_range[i]:
                low_index = i
                high_index = i
                break

    for x in range(1, low_index + 1):
        # index + 1 because range is not inclusive
        incremental_rate *= 0.9
        cumulative_premium += incremental_rate/100 * (high_range[x] - high_range[x - 1])
        cumulative_premium_band.append(cumulative_premium)
    exposure_band = low_index + 1
    max_exposure = high_range[high_index - 1]
    cum_premium_below_band = cumulative_premium_band[low_index - 1]
    # calculate the base premium
    return cum_premium_below_band + (gross_revenue - max_exposure) * incremental_rate/100


while True:
    revenue = input("Enter gross revenue: \n")
    if revenue == "":
        continue
    print(base_premium_calc(revenue))
    if input("e to exit: \n").lower() == "e": 
        break