# Databricks notebook source
# /// script
# [tool.databricks.environment]
# environment_version = "6"
# ///
# MAGIC %sql
# MAGIC CREATE CATALOG IF NOT EXISTS hms_arya;
# MAGIC
# MAGIC CREATE SCHEMA IF NOT EXISTS hms_arya.bronze;
# MAGIC CREATE SCHEMA IF NOT EXISTS hms_arya.silver;
# MAGIC CREATE SCHEMA IF NOT EXISTS hms_arya.gold;

# COMMAND ----------

# MAGIC %md
# MAGIC Create Volume
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE VOLUME IF NOT EXISTS hms_arya.bronze.hcls;

# COMMAND ----------

display(
    dbutils.fs.ls("/Volumes/hms_arya/bronze/hcls")
)