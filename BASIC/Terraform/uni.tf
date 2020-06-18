resource "null_resource" "populate_db_psql" {
  count = "${var.createPostgreSQL ? 1 : 0 }" 
  depends_on = ["null_resource.update_dockerfile_psql"]
  provisioner "local-exec" {
    working_dir = "./psql"
    command = <<EOC
      sed 's/postgres_password/${var.psql_adminpass}/g' pgsqlScriptInstall.sh.tpl > pgsqlScriptInstall.sh
      sed -i 's/postgres_address/${aws_db_instance.psql.fqdn}/g' pgsqlScriptInstall.sh
      sed -i 's/postgres_username/${var.psql_adminuser}@${aws_db_instance.psql.server_name}/g' pgsqlScriptInstall.sh
      sed -i 's/postgres_db/${var.psql_db}/g' pgsqlScriptInstall.sh
      bash -x pgsqlScriptInstall.sh
    EOC
  }
}