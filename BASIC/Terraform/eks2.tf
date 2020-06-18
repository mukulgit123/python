provider "helm" {
kubernetes {
config_path = "${path.module}/kubeconfig_axiom-eks-cluster-${var.environment}"
load_config_file = "${path.module}/kubeconfig_axiom-eks-cluster-${var.environment}" != "" ? true : false #local_file.kube_config.filename != "" ? true : false
}
service_account = "${kubernetes_service_account.tiller_service_account.metadata.0.name}"
}

provider "kubernetes" {
config_path = "${path.module}/kubeconfig_axiom-eks-cluster-${var.environment}" != "" ? true : false#"${local_file.kube_config.filename}"
load_config_file = "${path.module}/kubeconfig_axiom-eks-cluster-${var.environment}" != "" ? true : false#local_file.kube_config.filename != "" ? true : false
}${path.module}/kubeconfig_axiom-eks-cluster-${var.environment}