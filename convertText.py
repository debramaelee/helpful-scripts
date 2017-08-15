# enter original string here between triple quotes
str0 = """last_upd_snsh_id  INTEGER NULLABLE  
Describe this field...
last_upd_ts STRING  NULLABLE  
Describe this field...
loc_tot_area  FLOAT NULLABLE  
Describe this field...
"""

# replace all unwanted strings with a space
nullVals = ["INTEGER", "STRING", "FLOAT", "NULLABLE"]
for i in nullVals:
	str0 = str0.replace(i, " ")

# remove all "Describe this field..."
newStr1 = str0.replace("Describe this field...", "")

# replace all paragraph breaks with commas
newStr2 = newStr1. replace("\n", ",")

# remove all spaces
newStr3 = newStr2.replace(" ", "")

# remove all double commas
newStr4 = newStr3.replace(",,", ", ")

# change all values to uppercase
finalStr = newStr4.upper()

print finalStr

