variable "aws_region" {
  type        = string
  description = "AWS region to deploy into"
  default     = "af-south-1"
}

variable "environment" {
  type        = string
  description = "Deployment environment name"
  default     = "dev"
}

variable "vpc_cidr" {
  type        = string
  description = "CIDR block for the VPC"
  default     = "10.0.0.0/16"
}

variable "public_subnet_cidr" {
  type        = string
  description = "CIDR block for the public subnet"
  default     = "10.0.1.0/24"
}

variable "private_subnet_cidr" {
  type        = string
  description = "CIDR block for the private subnet"
  default     = "10.0.2.0/24"
}

variable "availability_zone" {
  type        = string
  description = "Availability zone for subnets"
  default     = "af-south-1a"
}