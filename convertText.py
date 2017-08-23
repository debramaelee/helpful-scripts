# enter original string here between triple quotes
str0 = """CARR_CD	STRING	NULLABLE	
Describe this field...
CARR_PRO_NBR	STRING	NULLABLE	
Describe this field...
CRT_TS	TIMESTAMP	NULLABLE	
Describe this field...
PRTNR_ID	STRING	NULLABLE	
Describe this field...
FRT_BILL_NBR	STRING	NULLABLE	
"""
 
# remove all unwanted strings and values
nullVals = ["INTEGER", "STRING", "FLOAT", "NULLABLE", "TIMESTAMP", "BOOLEAN", "Describe this field...", " ", "	"]
for i in nullVals:
    str0 = str0.replace(i, "")
 
# replace all paragraph breaks with commas
newStr = str0. replace("\n", ",")
newStr1 = newStr. replace(",,", ", ")
 
# change all values to uppercase
finalStr = newStr1.upper()
print '------------------------------------------------------------'
print finalStr
 
# removes last 2 characters (space and last comma)
print '------------------------------------------------------------'
print finalStr[:-2]
 
# result
# CUST_ORD_ID, LAST_UPD_SNSH_ID, TOT_ORD_RETL_AMT
