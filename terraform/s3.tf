resource "random_pet" "lambda_bucket_name" {
  prefix = "fiap-lambda"
  length = 4
}

resource "aws_s3_bucket" "lambda_bucket" {
  bucket = random_pet.lambda_bucket_name.id
}

resource "aws_s3_bucket_ownership_controls" "lambda_bucket" {
  bucket = aws_s3_bucket.lambda_bucket.id
  rule {
    object_ownership = "BucketOwnerPreferred"
  }
}

resource "aws_s3_bucket_acl" "lambda_bucket" {
  depends_on = [aws_s3_bucket_ownership_controls.lambda_bucket]

  bucket = aws_s3_bucket.lambda_bucket.id
  acl    = "private"
}

data "archive_file" "fiap_lambda_archive" {
  type = "zip"

  source_dir  = "${path.module}/../src"
  output_path = "${path.module}/../src.zip"
}

resource "aws_s3_object" "fiap_lambda_archive" {
  bucket = aws_s3_bucket.lambda_bucket.id

  key    = "src.zip"
  source = data.archive_file.fiap_lambda_archive.output_path

  etag = filemd5(data.archive_file.fiap_lambda_archive.output_path)
}
