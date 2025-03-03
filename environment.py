import os
def before_all(context):
   xmlreport_dir_path="results/xml/2024-08-01-11-49-19"
   os.environ["TEST_REPORT_PATH"] = xmlreport_dir_path
def after_all(context):
   print("Test execution completed.")
