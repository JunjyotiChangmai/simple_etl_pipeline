{{ config(materialized='table') }}

SELECT
    ALERT_ID, PATIENT_ID, NPI,
    TRIM(FIRSTNAME || ' ' || LASTNAME) AS HCP_FULL_NAME,
    HCPSPECIALTY1, STATE, DIAGNOSED_AHUS, TERRITORY_NAME, FILE_DATE
FROM {{ ref('ahus_prescriptive_alert_internal') }}
WHERE FILE_DATE = (SELECT MAX(FILE_DATE) FROM {{ ref('ahus_prescriptive_alert_internal') }})