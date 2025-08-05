provider "aws" {
  region = "us-east-2"
}

terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }

  required_version = ">= 1.0"
}

# Intentional Error 1: Invalid bucket name (must be globally unique and follow naming rules)
resource "aws_s3_bucket" "my_bucket" {
  bucket = "bucket"  # This will fail because "bucket" is too generic and likely already exists

  tags = {
    Name        = "BucketVishal"
    Environment = "Dev"
  }
}

# Intentional Error 2: Referencing a non-existent variable
resource "aws_instance" "test" {
  ami           = var.non_existent_ami_id  # This variable is not defined
  instance_type = "t2.micro"

  tags = {
    Name = "TestInstance"
  }
}

# Intentional Error 3: Typo in block name (should be lifecycle, not life_cycle)
resource "aws_security_group" "sg_error" {
  name        = "bad-sg"
  description = "SG with intentional typo"

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  life_cycle {  # Incorrect spelling
    prevent_destroy = true
  }
}
