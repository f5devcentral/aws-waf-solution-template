import boto3
import sys
import requests


def vfy_cft_link(cft_name,exp_op):
  """
  This method is to verify the cloud formation output link status.
  |  *cft_name*         | Name of the Stack                      |
  |  *exp_op*           | expected output for the output link    |
  |  *returns*          | True if outoput exists if not False    |
  """
  cf_client = boto3.client('cloudformation')
  response = cf_client.describe_stacks(StackName=cft_name)
  if not response["Stacks"][0]["Outputs"]:
    print("no results in output section")
    return False
  outputs = response["Stacks"][0]["Outputs"]
  print("Available Output Links: ")
  for key in outputs: print(key["OutputKey"],key["OutputValue"])
  try:
    for output in outputs:
      if output["OutputKey"] == "externalDnsName":
        url="http://"+output["OutputValue"]
        chk_data = requests.get(url)
        if exp_op in chk_data.text:
          return True
        else:
          return False
  except Exception as e:
    print("Exception raised with error:",e)

    
if __name__ == '__main__':
  
  stack_name= "nap-cft-stack"
  page_type=sys.argv[1] 
  if page_type == "static":
    page = "Hello World"
  elif page_type == "dynamic":
    page = "Arcadia Finance"
  else:
    page = "Welcome to nginx"
  try:
    vfy_status=vfy_cft_link(stack_name,page)
    if vfy_status:
      print("Status: NGINX APP PROTECT ", page_type.upper() , "PAGE VERIFICATION IS COMPLETED SUCESSFULLY...")
    else:
      print("Error: NGINX APP PROTECT ", page_type.upper() , " PAGE VERIFICATION IS Failed...")
  except Exception as e:
    print("Exception raised with error:",e)
