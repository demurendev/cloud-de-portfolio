provider "aws" {
  region = "us-east-1"
}

resource "aws_s3_bucket" "portfolio_bucket" {
  bucket = "deborah-terraform-demo-2026"

  tags = {
    Name        = "Deborah Portfolio Demo"
    Environment = "Dev"
    ManagedBy   = "Terraform"
  }
}

output "bucket_name" {
  value = aws_s3_bucket.portfolio_bucket.bucket
}