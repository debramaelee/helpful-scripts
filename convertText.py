# enter original string here between triple quotes
str0 = """cust_ord_id   STRING  NULLABLE
last_upd_snsh_id    INTEGER NULLABLE
tot_ord_retl_amt    FLOAT   NULLABLE
"""
 
# remove all unwanted strings and values
nullVals = ["INTEGER", "STRING", "FLOAT", "NULLABLE", "TIMESTAMP", "Describe this field...", " ", "	"]
for i in nullVals:
    str0 = str0.replace(i, "")
 
# replace all paragraph breaks with commas
newStr = str0. replace("\n", ", ")
 
# change all values to uppercase
finalStr = newStr.upper()
print '------------------------------------------------------------'
print finalStr
 
# removes last 2 characters (space and last comma)
print '------------------------------------------------------------'
print finalStr[:-2]
 
# result
# CUST_ORD_ID, LAST_UPD_SNSH_ID, TOT_ORD_RETL_AMT
