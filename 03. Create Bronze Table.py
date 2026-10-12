# Databricks notebook source
# /// script
# [tool.databricks.environment]
# environment_version = "6"
# dependencies = [
#   "openpyxl",
# ]
# ///
# MAGIC %md
# MAGIC Install Openpyxl

# COMMAND ----------

# MAGIC %pip install openpyxl

# COMMAND ----------

# MAGIC %md
# MAGIC Restart Python

# COMMAND ----------

dbutils.library.restartPython()

# COMMAND ----------

import pandas as pd

FILE_PATH = "/Volumes/hms_arya/bronze/hcls/HCLS.xlsx"

excel = pd.ExcelFile(
FILE_PATH,
engine="openpyxl"
)

for sheet in excel.sheet_names:

    print(f"Processing {sheet}")

    pdf = pd.read_excel(
    FILE_PATH,
    sheet_name=sheet,
    engine="openpyxl"
    )
    try:
        #sdf = spark.createDataFrame(pdf)
       
        if sheet == "Hierarchy":
           
            pdf["entity_id"] = pdf["entity_id"].astype(str)
            pdf["hospital_id"] = pdf["hospital_id"].astype(str)
            #sdf = spark.createDataFrame(pdf)
        
        elif sheet == "Referrals":
            
            pdf["referred_doctor_id"] = pdf["referred_doctor_id"].astype(str)
            pdf["patient_id"] = pdf["patient_id"].astype(str)
            
           
        elif sheet == "Patients":
           
            pdf["patient_id"] = pdf["patient_id"].astype(str)
            #sdf = spark.createDataFrame(pdf)
        sdf = spark.createDataFrame(pdf)
    except Exception as e:

        print(f"Problem sheet = {sheet}")
        print(e)
        raise

    table_name = (
    sheet.lower()
    .replace(" ", "_")
    )

    sdf.write \
    .format("delta") \
    .mode("overwrite") \
    .option("overwriteSchema", "true") \
    .saveAsTable(
    f"hms_arya.bronze.{table_name}"
    )

print(f"Created {table_name}")

# COMMAND ----------

# MAGIC %sql
# MAGIC --select * from hms_arya.silver.patient
# MAGIC --select count(*) from hms_arya.silver.patient
# MAGIC DESCRIBE EXTENDED hms_arya.silver.patient;

# COMMAND ----------

# MAGIC %sql
# MAGIC select count(*) from hms_arya.silver.patient where first_name is null

# COMMAND ----------

# MAGIC %sql
# MAGIC --select count(*) from hms_arya.silver.admission
# MAGIC --select count(*) from hms_arya.bronze.admissions
# MAGIC
# MAGIC select count(*) from hms_arya.bronze.patients p 
# MAGIC inner join hms_arya.bronze.billing b on p.patient_id = b.patient_id
# MAGIC