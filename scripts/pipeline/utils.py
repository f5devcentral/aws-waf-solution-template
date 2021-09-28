import boto3
import re
import os
import requests

def vfy_cft_link(cft_name,exp_op):
  cf_client = boto3.client('cloudformation')
  response = cf_client.describe_stacks(StackName=cft_name)
  if not response["Stacks"][0]["Outputs"]:
      print("no results in output section")
      return False
  outputs = response["Stacks"][0]["Outputs"]
  print("output infor for the stack: ", outputs)
  try:
    for output in outputs:
      if output["OutputKey"] == "AppProtectLBDNSName":
        url="http://"+output["OutputValue"]
        chk_data = requests.get(url)
        if exp_op in chk_data.text:
          print(chk_data.text)
          return True
        else:
          print(chk_data.text)
          return False
  except Exception as e:
    print("Exception raised with error:",e)
#------------------------------------------------------------
#End of file
