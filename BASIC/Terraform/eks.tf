resource "aws_eks_cluster" "example" {
  name     = "example"
  role_arn = "${aws_iam_role.example.arn}"

  vpc_config {
    subnet_ids = ["${aws_subnet.example1.id}", "${aws_subnet.example2.id}"]
  }
}

output "endpoint" {
  value = "${aws_eks_cluster.example.endpoint}"
}

output "kubeconfig-certificate-authority-data" {
  value = "${aws_eks_cluster.example.certificate_authority.0.data}"
}
