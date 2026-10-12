# Databricks notebook source
# /// script
# [tool.databricks.environment]
# environment_version = "6"
# dependencies = [
#   "openpyxl",
# ]
# ///
# MAGIC %pip install openpyxl 

# COMMAND ----------

dbutils.library.restartPython()

# COMMAND ----------

import pandas as pd

file_path = "/Volumes/hms_arya/bronze/hcls/HCLS.xlsx"

excel = pd.ExcelFile(file_path)

print(excel.sheet_names)