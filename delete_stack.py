#!/usr/bin/env python
import boto3
from utils import *

cfn = boto3.resource('cloudformation')
stack_name=get_stack_name()
stack = cfn.Stack(stack_name)
status=stack.delete()
print(status)
        
