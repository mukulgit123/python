from aws_volume_manager import AWSVolumeManager
from kubernetes_manager import KubernetesManager
import logging

logging.basicConfig(level=logging.INFO)


class VolumeAnalyzer:
    def __init__(self):
        self.aws_manager = AWSVolumeManager(
            region_name='eu-west-1', profile_name='my-profile')
        self.k8s_manager = KubernetesManager()

    def analyze_volumes(self):
        aws_volumes = self.aws_manager.get_all_volumes()
        aws_node_volumes = self.aws_manager.get_node_volumes()
        k8s_ebs_volumes = set(self.k8s_manager.get_all_pv_ebs_volumes())

        # Extract volume IDs from aws_node_volumes
        aws_node_volume_ids = {v['VolumeId'] for v in aws_node_volumes}

        for vol in aws_volumes:
            volume_id = vol['VolumeId']
            if volume_id not in k8s_ebs_volumes and volume_id not in aws_node_volume_ids:
                logging.info(f"{volume_id}")

        total_volumes = len(aws_volumes)
        used_volumes = len(k8s_ebs_volumes) + len(aws_node_volume_ids)
        unused_volumes = total_volumes - used_volumes
        logging.info(f"Total volumes: {total_volumes}")
        logging.info(f"Total volumes used by PVCs: {len(k8s_ebs_volumes)}")
        logging.info(
            f"Total volumes attached to Nodes: {len(aws_node_volume_ids)}")
        logging.info(f"Total used volumes: {used_volumes}")
        logging.info(f"Total unused volumes: {unused_volumes}")


if __name__ == "__main__":
    analyzer = VolumeAnalyzer()
    analyzer.analyze_volumes()
