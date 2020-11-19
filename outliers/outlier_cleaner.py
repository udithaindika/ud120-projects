#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """

    cleaned_data = []

    ### your code goes here

    temp_data = []
    for i in range(len(predictions)):
        pred_net_worth = predictions[i][0]
        age = ages[i][0]
        net_worth = net_worths[i][0]
        error = abs(pred_net_worth - net_worth)
        temp_data.append((age, pred_net_worth, net_worth, error))

    temp_data = sorted(temp_data, key=lambda x: x[3])
    temp_data = temp_data[0:len(predictions) * 90 / 100]

    for tup in temp_data:
        cleaned_data.append((tup[0], tup[2], tup[3]))

    return cleaned_data
