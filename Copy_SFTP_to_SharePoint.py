#import all the libraries

import shutil

directory_r = r"\\frlcork-storage.thefacebook.com\oresearch_cork_001\ExternalData\evg\incoming\SOAP_Bonding_Process_Tracker_Architecture_A 28.10.2020.xlsx"


directory_w = r"C:\Users\senguel\OneDrive - Facebook\Architecture A\Test\SOAP_Bonding_Process_Tracker_Architecture_A 28.10.2020.xlsx"

shutil.copyfile(directory_r, directory_w)
