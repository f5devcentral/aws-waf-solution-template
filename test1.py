#!/usr/bin/env python
import boto3
from utils import vfy_cft_link
nginx_def_index="Welcome to nginx"

vfy_status=vfy_cft_link(nginx_def_index)
if vfy_status:
  print("NGINX APP PROTECT BASIC PAGE VERIFICATION IS COMPLETED SUCESSFULLY...")
else:
  print("Error: NGINX APP PROTECT BASIC PAGE VERIFICATION IS Failed...")
