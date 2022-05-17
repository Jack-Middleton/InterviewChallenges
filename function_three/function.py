low_range = [0]
# have the low end steps be input and however many price-bands wanted
# generate the high-end from that
high_range = []
cumulative_premium_band = []

# update so that the high range entered via user input, generating the low range, and then initial cumulative premium is calculated
def base_premium_calc(gross_revenue):
    incremental_rate = 5
    # generate the initial premium that the cumulative premium is calculated from
    cumulative_premium = high_range[0] * incremental_rate/100
    cumulative_premium_band.append(cumulative_premium)
    low_index = - 1
    high_index = - 1
    try:
        gross_revenue = int(gross_revenue)
    except:
        return "Please enter gross revenue as an integer"
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
    print(f" Gross Revenue: {gross_revenue} \n Exposure Band: {exposure_band} \n Cumulative Premium Below Band: {cum_premium_below_band}\
        \n Max Exposure Below Band: {max_exposure} \n Rate in band: {incremental_rate}%")
    return round(cum_premium_below_band + (gross_revenue - max_exposure) * incremental_rate/100, 2)


while True:
    try:
        bracket_diff = int(input("How much would you like the income bracket difference to be? eg; 3000000, 5000000: \n"))
        steps = int(input("How many income bands would you like? \n")) - 1
    except:
        print("Please enter a valid integer")
        continue
    # append the initial high end value
    high_range.append(0 + bracket_diff)
    # generate the high and low end
    for i in range (steps):
        low_range.append(low_range[i] + bracket_diff)
        high_range.append(low_range[i] + bracket_diff * 2)
    # add one to each value in the low end after 0
    for i in range (1, steps + 1):
        low_range[i] += 1

    print(low_range, high_range)
    revenue = input("Enter gross revenue: \n")
    if revenue == "":
        continue
    print(f" Base Premium: {base_premium_calc(revenue)}")
    if input("e to exit: \n").lower() == "e": 
        break