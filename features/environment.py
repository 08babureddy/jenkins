import os
import sys
def before_all(context):
   xmlreport_dir_path="2024-08-01-11-49-19"
   print("*****************")
   print("*****************")
   print("Started Execution")
   print("*****************")
   print("*****************")
   print(f"TEST_REPORT_PATH={xmlreport_dir_path}")
def after_all(context):
   print("Test execution completed.")
