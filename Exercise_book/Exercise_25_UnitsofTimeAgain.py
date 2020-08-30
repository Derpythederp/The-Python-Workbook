#!~/anaconda3/bin/python
seconds = int(input("How many seconds: "))

secperday = 60*60*24
secperhour = 3600
secpermin = 60

days = seconds//secperday
remainsec = seconds%secperday

hours = remainsec//secperhour
remainsec = remainsec%secperhour

minutes = remainsec//secpermin
remainsec = remainsec%secpermin

print(f"Time in D:HH:MM:SS is {days}:{hours:02d}:{minutes:02d}:{remainsec:02d}.")


#Syntax: {[argument_index_or_keyword]:[padding_type][width][.precision][type]}
#You can ignore precision, width or type field
#padding type comes in terms of whitespace, 0, + and -. Zero padding is commonly used to fill whitespace. Defaults to whitespace
#example {value:012.5f} where value is 69.12093456
#Output: 000069.12093 
#Explanation: Zero padding up to min length of 12 characters(including decimals), precision of 5
#https://stackoverflow.com/questions/36543804/what-does-02d-mean-in-python