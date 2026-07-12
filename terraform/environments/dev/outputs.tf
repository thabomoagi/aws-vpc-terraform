output "vpc_id" {
  description = "The ID of the VPC"
  value       = module.development_network.vpc_id
}

output "public_subnet_id" {
  description = "The ID of the public subnet"
  value       = module.development_network.public_subnet_id
}

output "private_subnet_id" {
  description = "The ID of the private subnet"
  value       = module.development_network.private_subnet_id
}