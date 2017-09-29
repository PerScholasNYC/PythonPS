# create a mmapping of state to abbreviation
#variable for the dictionary
states = {
#list of key pairs
    'Oregon' : 'OR'
    'Florida' : 'FL'
    'California' : 'CA'
    'New York' : 'NY'
    'Michigan' : 'MI'
    }

# create a basic set of states and some cities in them
#variable for the dictionary
cities = {
#list of key pairs
    'CA' : 'San Francisco',
    'MI' : 'Detroit',
    'FL' : 'Jacksonville'
}

# add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print out some cities
print('-' * 10)
print("NY State has: ", cities['NY'])
print("OR State has: ", cities['OR'])

# do it by using the state thedn cities dict
print('-' * 10)
