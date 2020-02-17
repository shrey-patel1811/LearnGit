#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 03:12:55 2019

@author: shrpatel
"""

import boto3
import json
ec2=boto3.client('ec2', region_name='us-east-1', aws_access_key_id='ASIAYUWGSFUXRHMWM55L', aws_secret_access_key='0idgX8M4tMNoM6NvMwCSjiXtDFXntUMhz3Q4sn85', aws_session_token='FQoGZXIvYXdzEJP//////////wEaDG+eW9hfWnR2hYgNxSKpAlohr56qqn8P8vsdi3TfjeGzqDnVeq8spkQ7wDEnI2D+Wwmj6wBhr4KwOX6Un7MajgEkhBwL+IKoEQchqtv8pH3h8AUSMwDGGwtFvf4Sj40JTP9PyGz9nFTzOxaMAW2ZZAjqCqXtQESf43l339CLoOhG7XXhwb3Z50j5b9Jy4CUuURrWyUgBw+HcpwyCxYxqK+/mfpwTqPuI+iMgS0YlXjlGW0/MEjml5f/cVBSeyJ3QQVcfwiGgQGO/2lEhKfkNLWY3V56BWf97Zrw04sEmTjbaAt68KoRhsPEbwU7mMZHn4Hm5EXjSMvd0D3Hy/hWe8QzTnj4w6X77GO1UFCmVwWBe2glFp6h0Ke+zrlG3VFHyKpL2O/gNx5HM+U3PczDbczOt+uMNm8bRHyiq8PnrBQ==')
#ec2.describe_instances(InstanceIds=['i-0dd4f6cc57041493f'])['Reservations'][0]['Instances'][0]['PrivateDnsName']

response1 = ec2.describe_instance_attribute(
    Attribute='instanceType',   
    InstanceId='i-0a14d6d8a76ad847d',
)
#print (response)

print (response1['InstanceType']['Value'])
print (response1['InstanceId'])


for key,val in response.items():
    if key == 'InstanceType':
        print(val)

#json_data = json.dumps(response)




