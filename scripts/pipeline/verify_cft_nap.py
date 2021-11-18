import boto3
import os
from utils import *
import sys

nginx_default_page="Welcome to nginx"
nginx_static_page="Hello World"
nginx_dynamic_page="Arcadia Finance"
stack_name= "nap-cft-stack"
page_type=sys.argv[1] 
if page_type == "static":
  page_type = nginx_static_page
elif page_type == "dynamic":
  page_type = nginx_dynamic_page
else:
  page_type = nginx_default_page
#Verify functionality of NAP
try:
  vfy_status=vfy_cft_link(stack_name,page_type)
  if vfy_status:
    print("NGINX APP PROTECT ", sys.argv[1].upper() , "PAGE VERIFICATION IS COMPLETED SUCESSFULLY...")
  else:
    print("Error: NGINX APP PROTECT ", sys.argv[1].upper() , " PAGE VERIFICATION IS Failed...")
except Exception as e:
  print("Exception raised with error:",e)