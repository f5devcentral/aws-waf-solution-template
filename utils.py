#!/usr/bin/env python
import boto3
import re
import requests

#Variable Initialization
test_name="tCaT-nap-"

#Methods
#----------------------------------
def get_s3_bucket():
  get_list = []
  s3 = boto3.resource('s3')
  try:
    for bucket in s3.buckets.all():
      if bucket.name.startswith(test_name.lower()):
        get_list.append(bucket.name) 
  except Exception as e:
    print("Exception raised with error:",e)  
  return get_list
#-----------------------------------
def get_stack_name():
  m_lst = get_s3_bucket() 
  try:
    if not len(m_lst): 
      print("There is NO existing stack with TaskCat ");
      return False
    else:
      for bucket in m_lst:
        temp_lst= re.split("-",bucket)
        stack_name=test_name+temp_lst[2]
        return stack_name.strip()
  except Exception as e:
    print("Exception raised with error:",e)      
#--------------------------------------------------      
def vfy_cft_link(exp_op):
  cft_name=get_stack_name()  
  #print(cft_name)
  cf_client = boto3.client('cloudformation')
  response = cf_client.describe_stacks(StackName=cft_name)
  #print(response)
  try:
    if not response["Stacks"][0]["Outputs"]:
      print("no results in output section")
      return False
    for output in outputs:
      if output["OutputKey"] == "AppProtectLBDNSName":
        url="http://"+output["OutputValue"]
        chk_data = requests.get(url)
        if exp_op in chk_data.text:
          #print(chk_data.text)
          return True
        else:
          print(chk_data.text)
          return False
  except Exception as e:
    print("Exception raised with error:",e)
#------------------------------------------------------------
#End of file
