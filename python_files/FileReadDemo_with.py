import pdb

# sample_file = "./sample2.txt"
#
# with open(sample_file, 'r') as f:
#     print(f.read())
#

sample_file = "./list_of_countries_with_no_comma.txt"

with open(sample_file, 'r') as f:
    countries = f.read()
    
    # pdb.set_trace()
    # print(countries)

    country_list = countries.split()
    print(country_list)
