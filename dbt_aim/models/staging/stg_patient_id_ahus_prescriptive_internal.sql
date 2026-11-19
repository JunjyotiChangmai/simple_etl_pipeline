{{ config(materialized='table') }}

SELECT DISTINCT
    PATIENT_ID,
    MAX(FILE_DATE) AS LAST_ALERT_DATE
FROM {{ ref('ahus_prescriptive_alert_internal') }}
WHERE PATIENT_ID IS NOT NULL
GROUP BY PATIENT_ID