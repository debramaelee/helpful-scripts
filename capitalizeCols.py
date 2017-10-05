# enter original string here between triple quotes
str0 = """
[{"name":"transaction_id","description":"","type":"string","mode":"NULLABLE"},{"name":"load_dt","description":"","type":"date","mode":"NULLABLE"}]
"""

# add line breaks 
str1 = str0.replace("},","},\n")

# change all values to uppercase
str2 = str1.upper()

# all non column names back to lower case
backToLower = [""""NAME":""", """"DESCRIPTION":""", """"TYPE":"STRING""", """TYPE":"DATETIME""", """TYPE":"DATE""", """TYPE":"TIMESTAMP""", """TYPE":"BOOLEAN""", """MODE":"""]
for i in backToLower:
	str2 = str2.replace(i, i.lower())

print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
print str2
print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'

# output

# [{"name":"TRANSACTION_ID","description":"","type":"string","mode":"NULLABLE"},
# {"name":"LOAD_DT","description":"","type":"date","mode":"NULLABLE"}]