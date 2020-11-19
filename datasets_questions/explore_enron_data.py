#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "rb"))

count = 0
for name in enron_data.keys():
    if enron_data[name]['poi']:
        count += 1

poi_count = 0
for line in open("../final_project/poi_names.txt", "r"):
    if line.startswith("(y)") or line.startswith("(n)"):
        poi_count += 1

print poi_count

people_with_salary = 0
known_emails = set()
total_people = len(enron_data.keys())
people_with_nan_salary = 0;
total_poi = 0
total_poi_non_salary = 0

for name in enron_data.keys():
    if enron_data[name]['poi']:
        total_poi += 1
        if enron_data[name]['total_payments'] == 'NaN':
            total_poi_non_salary += 1

    if enron_data[name]['salary'] != 'NaN':
        people_with_salary += 1

    if enron_data[name]['total_payments'] == 'NaN':
        people_with_nan_salary += 1

    if enron_data[name]['email_address'] != 'NaN':
        known_emails.add(enron_data[name]['email_address'])

    if name.upper() == 'Prentice James'.upper():
        print enron_data[name]['total_stock_value']
    elif name.upper() == 'Colwell Wesley'.upper():
        print "Corlwell Messages :", enron_data[name]['from_this_person_to_poi']
    elif name.upper() == 'Skilling Jeffrey K'.upper():
        print "Skilling Jeffrey K Excersized Stock Options :", enron_data[name]['exercised_stock_options']

print "Total People:" , total_people
print "People With Salary ", people_with_salary
print "Known Email ", len(known_emails)
print "Percentage missing salary ", float(people_with_nan_salary)/total_people * 100
print "Percentage missing salary New ", people_with_nan_salary+10
print "Percentage missing POI salary ", float(total_poi_non_salary)/total_poi * 100
print "Total new POI" , total_poi + 10

# {'salary': 365788, 'to_messages': 807, 'deferral_payments': 'NaN', 'total_payments': 1061827, 'exercised_stock_options': 'NaN', 'bonus': 600000, 'restricted_stock': 585062, 'shared_receipt_with_poi': 702, 'restricted_stock_deferred': 'NaN', 'total_stock_value': 585062, 'expenses': 94299, 'loan_advances': 'NaN', 'from_messages': 29, 'other': 1740, 'from_this_person_to_poi': 1, 'poi': False, 'director_fees': 'NaN', 'deferred_income': 'NaN', 'long_term_incentive': 'NaN', 'email_address': 'mark.metts@enron.com', 'from_poi_to_this_person': 38}
