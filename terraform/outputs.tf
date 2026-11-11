output "id_do_servidor" {
  description = "ID da instância EC2"
  value       = aws_instance.app.id
}

output "ip_publico" {
  description = "IP público do servidor"
  value       = aws_instance.app.public_ip
}