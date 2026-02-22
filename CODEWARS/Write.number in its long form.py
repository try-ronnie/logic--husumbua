# Write Number in Expanded Form
# You will be given a number and you will need to return it as a string in Expanded Form. For example:

#    12 --> "10 + 2"
#    45 --> "40 + 5"
# 70304 --> "70000 + 300 + 4"
# NOTE: All numbers will be whole numbers greater than 0.

# If you liked this kata, check out part 2!!
#note input is in the form of an interger 



#sol
    # try create a dict 
    # a dict since for the places of the numbers we can scave their positional numbers
    #but we need a way to relate them with thier values ...
    #
def expanded_form (num):
    place_values = {}