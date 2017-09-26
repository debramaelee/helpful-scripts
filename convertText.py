# enter original string here between triple quotes
str0 = """ORD_ID	STRING	NULLABLE	
Describe this field...
CHUB_ORD_LINE_NBR	STRING	NULLABLE	
Describe this field...
CHUB_ORD_TRANS_TS	DATETIME	NULLABLE	
Describe this field...
CHUB_ORD_TRANS_TYP_IND	STRING	NULLABLE	
Describe this field...
CHUB_ORD_TRANS_QTY	FLOAT	NULLABLE	
Describe this field...
SHPMT_TRKG_NBR	STRING	NULLABLE	
Describe this field...
INVC_DT	DATE	NULLABLE	
Describe this field...
INVC_SHPG_AMT	FLOAT	NULLABLE	
Describe this field...
INVC_NBR_VAL	STRING	NULLABLE	
Describe this field...
INVC_CR_ADJ_AMT	FLOAT	NULLABLE	
Describe this field...
INVC_UNT_COST_AMT	FLOAT	NULLABLE	
Describe this field...
INVC_TAX_AMT	FLOAT	NULLABLE	
Describe this field...
INVC_TOT_COST_AMT	FLOAT	NULLABLE	
Describe this field...
CHUB_SRC_TRANS_ID	STRING	NULLABLE	
Describe this field...
SHP_FR_CITY_NM	STRING	NULLABLE	
Describe this field...
SHP_FR_ST_CD_VAL	STRING	NULLABLE	
Describe this field...
SHP_FR_PSTL_CD_VAL	STRING	NULLABLE	
Describe this field...
LAST_UPD_TS	DATETIME	NULLABLE	
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
# ORD_ID, CHUB_ORD_LINE_NBR, CHUB_ORD_TRANS_TS, CHUB_ORD_TRANS_TYP_IND, CHUB_ORD_TRANS_QTY, SHPMT_TRKG_NBR, INVC_DT, INVC_SHPG_AMT, INVC_NBR_VAL, INVC_CR_ADJ_AMT, INVC_UNT_COST_AMT, INVC_TAX_AMT, INVC_TOT_COST_AMT, CHUB_SRC_TRANS_ID, SHP_FR_CITY_NM, SHP_FR_ST_CD_VAL, SHP_FR_PSTL_CD_VAL, LAST_UPD_TS
# ------------------------------------------------------------