from kubernetes import client, config


class KubernetesManager:
    def __init__(self):
        config.load_kube_config()  # Assumes kubeconfig is set up
        self.v1 = client.CoreV1Api()

    def get_all_pv_ebs_volumes(self) -> dict:
        '''Returns a dictionary of EBS volumes used by PVCs'''
        pv_list = self.v1.list_persistent_volume().items
        ebs_volumes = []
        for pv in pv_list:
            if pv.spec.csi and pv.spec.csi.driver == "ebs.csi.aws.com" and not pv.spec.aws_elastic_block_store:
                volume_id = pv.spec.csi.volume_handle
                ebs_volumes.append(volume_id)
            elif pv.spec.aws_elastic_block_store and not pv.spec.csi:
                volume_id = pv.spec.aws_elastic_block_store.volume_id
                trim_volume_id = volume_id.split('/')[-1]
                ebs_volumes.append(trim_volume_id)
        return ebs_volumes
