provider "aws" {
  region = var.aws_region
  profile = var.aws_profile
}

module "api-gateway" {
    source = "./api-gateway"

    lambda_invoke_arn = module.lambda.lambda_invoke_arn
    cognito_endpoint = module.cognito.cognito_endpoint
}

module "lambda" {
    source = "./lambda"
}

module "cognito" {
    source = "./cognito"
}
