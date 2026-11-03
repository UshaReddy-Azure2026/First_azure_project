# Databricks notebook source
# /// script
# [tool.databricks.environment]
# environment_version = "6"
# ///
print("hello pipeline")

# COMMAND ----------

# MAGIC %sql
# MAGIC CReate catalog if not exists lakehouse;