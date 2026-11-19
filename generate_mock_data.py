import csv
import os
import random
from datetime import datetime

HEADER_STR = "ALERT_ID,ALERTNAME,ALERT,PATIENT_ID,CODE_DESCRIPTION,NPI,FIRSTNAME,MIDDLENAME,LASTNAME,HCPSPECIALTY1,HCPSPECIALTY2,HCPADDRESS,HCO_NAME,CITY,STATE,ZIP,EMAIL,PHONE,PAYERNAME,PAYERTYPE,YEAR,WEEK,DATE_1,DATE_KIDNEY_TRANSPLANT,DATE_THROMBOCYTOPENIA,DATE_HEMOLYSIS,DATE_BMT,DATE_DIALYSIS,DATE_PLASMA_EXCHANGE,DATE_SOL_ULT,DATE_9,DATE_10,DATE_11,DATE_TMA_ENCOUNTER,ADULT,TOTAL_DIALYSIS_ENCOUNTERS,TOTAL_RENALDYSFUNCTIONS_ENCOUNTERS,TMA_ENCOUNTERS_R12M,LUPUS_NEPHRITIS,QUEST_LOCAL_RESULT_NAME,ADAMTS13_LAB_RESULT,QUEST_RESULT_UNIT,QUEST_REFERENCE_RANGE_LOW,QUEST_REFERENCE_RANGE_HIGH,QUEST_REFERENCE_RANGE_ALPHA,QUEST_REFERENCE_INTERPRETATION,QUEST_COMMENTS,INDICATION_MAPPING,ON_LABEL_USAGE,DATE_LAST_ENCOUNTER,LAST_CLAIM_DATE,INSIGHTS_TEXT,SEGMENT_US__C,FILE_DATE,DIAGNOSED_AHUS,TERRITORY_NAME,DATE_OF_MOST_RECENT_EVENT,WHAT_WAS_THE_LAST_TRIGGER,HEMATOLOGIST,NEPHROLOGIST,RHEUMATOLOGIST,CKD_STAGE,PATIENT_TYPE,ALERT_TYPE_DETAIL"
COLUMNS = HEADER_STR.split(",")

def generate_csv(file_date_str, fail_dq=False, fail_header=False):
    os.makedirs("data/source", exist_ok=True)
    tag = "_BAD_DQ" if fail_dq else ("_BAD_HDR" if fail_header else "")
    filepath = f"data/source/AHUS_PRESCRIPTIVE_INTERNAL_{file_date_str}{tag}.csv"

    cols = COLUMNS.copy()
    if fail_header:
        cols[3] = "WRONG_PATIENT_COL"

    rows = []
    for i in range(1, 6):
        row = {col: "" for col in COLUMNS}
        row.update({
            "ALERT_ID": f"ALT_{file_date_str}_{i}",
            "ALERTNAME": "aHUS Prescriptive Alert",
            "ALERT": "TMA_TRIGGER",
            "PATIENT_ID": "" if (fail_dq and i == 2) else f"PT_{random.randint(100000, 999999)}",
            "CODE_DESCRIPTION": "Atypical hemolytic uremic syndrome",
            "NPI": f"123456789{i}",
            "FIRSTNAME": "Jane",
            "LASTNAME": f"Smith_{i}",
            "HCPSPECIALTY1": "NEPHROLOGY",
            "STATE": "NY",
            "YEAR": "2026",
            "WEEK": "46",
            "ADULT": "Y",
            "FILE_DATE": file_date_str,
            "DIAGNOSED_AHUS": "Y",
            "TERRITORY_NAME": "NORTHEAST_01",
            "NEPHROLOGIST": "Y",
            "PATIENT_TYPE": "NEW"
        })
        rows.append([row[c] for c in COLUMNS])

    with open(filepath, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(cols)
        writer.writerows(rows)
    print(f"Created {filepath}")

if __name__ == "__main__":
    today = datetime.now().strftime("%Y%m%d")
    generate_csv(today, fail_dq=False, fail_header=False)