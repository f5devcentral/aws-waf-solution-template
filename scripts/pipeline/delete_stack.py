import boto3
import os
from utils import *

stack_name=os.environ['STACK_NAME']
cfn = boto3.resource('cloudformation')
stack = cfn.Stack(stack_name)
status=stack.delete()
print(status)
