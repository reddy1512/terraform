provider "aws" {
  region     = "us-east-1"
}

resource "aws_vpc" "main" {
  cidr_block           = "10.0.0.0/16"
  enable_dns_support   = true
  enable_dns_hostnames = true

  tags = {
    Name = "my-vpc"
  }
}

resource "aws_subnet" "my_subnet" {
  vpc_id            = aws_vpc.main.id
  cidr_block        = "10.0.1.0/24"
  availability_zone = "us-east-1a"

  tags = {
    Name = "my-subnet"
  }
}

#resource "aws_security_group" "my_sg" {}

resource "aws_instance" "my_instance" {
  ami           = "ami-02dfbd4ff395f2a1b"
  instance_type = "t3.micro"
  subnet_id     = aws_subnet.my_subnet.id

  tags = {
    Name = "my-instance"
  }
}
