import os
def before_all(context):
   os.environ["TEST_REPORT_PATH"] = xmlreport_dir_path
