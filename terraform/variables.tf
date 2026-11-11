variable "aws_region" {
  description = "Região da AWS onde a infraestrutura será criada"
  type        = string
  default     = "us-east-1"
}

variable "instance_type" {
  description = "Tamanho do servidor"
  type        = string
  default     = "t3.micro"
}