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

resource "aws_s3_bucket" "my_bucket" {
  #bucket = "bucket-vishal-01082025"

  tags = {
    Name        = "BucketVishal"
    Environment = "Dev"
  }
}

