import boto3
import os
from utils import vfy_cft_link

nginx_def_index="Welcome to nginx"
stack_name=os.environ['STACK_NAME']

#Verify the basic functionality of NAP
try:
  vfy_status=vfy_cft_link(stack_name,nginx_def_index)
  if vfy_status:
    print("NGINX APP PROTECT BASIC PAGE VERIFICATION IS COMPLETED SUCESSFULLY...")
  else:
    print("Error: NGINX APP PROTECT BASIC PAGE VERIFICATION IS Failed...")
except Exception as e:
  print("Exception raised with error:",e)
