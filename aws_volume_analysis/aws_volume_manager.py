import boto3


class AWSVolumeManager:
    def __init__(self, region_name='us-east-1', profile_name=None):
        self.session = boto3.Session(profile_name=profile_name)
        self.ec2 = self.session.client('ec2', region_name=region_name)

    def get_all_volumes(self) -> list:
        volumes = []
        paginator = self.ec2.get_paginator('describe_volumes')
        for page in paginator.paginate():
            volumes.extend(page['Volumes'])
        return volumes

    def get_node_volumes(self) -> list:
        '''Returns a list of EBS volumes attached to a node'''
        paginator = self.ec2.get_paginator('describe_volumes')
        volumes = []
        for page in paginator.paginate(
                Filters=[{'Name': 'tag-key', 'Values': ['Platform']}]):
            volumes.extend(page['Volumes'])
        return volumes
