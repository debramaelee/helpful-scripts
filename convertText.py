# enter original string here between triple quotes
str0 = """ORD_ID	STRING	NULLABLE	
Describe this field...
CHUB_ORD_LINE_NBR	STRING	NULLABLE	
Describe this field...
"""
 
# remove all unwanted strings and values
nullVals = ["INTEGER	NULLABLE", "STRING	NULLABLE", "FLOAT	NULLABLE", "TIMESTAMP	NULLABLE", "BOOLEAN	NULLABLE", "DATE	NULLABLE", "DATETIME	NULLABLE", "Describe this field...", " ", "	"]
for i in nullVals:
    str0 = str0.replace(i, "")
 
# replace all paragraph breaks with commas
newStr = str0. replace("\n", ",")
newStr1 = newStr. replace(",,", ", ")
 
# change all values to uppercase
finalStr = newStr1.upper()

# removes last 2 characters (space and last comma)
print '------------------------------------------------------------'
print finalStr[:-2]
print '------------------------------------------------------------'

# OUTPUT
# ------------------------------------------------------------
# ORD_ID, CHUB_ORD_LINE_NBR
# ------------------------------------------------------------