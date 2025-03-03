import os
import sys
def before_all(context):
   xmlreport_dir_path="2024-08-01-11-49-19"
   os.environ["TEST_REPORT_PATH"] = xmlreport_dir_path
   print("*****************")
   print("*****************")
   print("Started Execution")
   print("*****************")
   print("*****************")
   sys.stdout.flush()
def after_all(context):
   print("Test execution completed.")
