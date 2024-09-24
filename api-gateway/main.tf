#----------------------------------------
# API Gateway
#----------------------------------------

resource "aws_apigatewayv2_api" "fiap_api_gateway" {
  name          = "fiap_api_gateway"
  protocol_type = "HTTP"
}

#----------------------------------------
# Authorizer
#----------------------------------------

resource "aws_apigatewayv2_authorizer" "fiap_api_authorizer" {
  api_id                            = aws_apigatewayv2_api.fiap_api_gateway.id
  authorizer_type                   = "JWT"
  identity_sources                  = ["$request.header.Authorization"]
  name                              = "cognito-authorizer"
  authorizer_payload_format_version = "2.0"

  jwt_configuration  {
      issuer   = var.cognito_endpoint
  }
}

#----------------------------------------
# Lambda Integration
#----------------------------------------

resource "aws_apigatewayv2_integration" "fiap_lambda_integration" {
  api_id = aws_apigatewayv2_api.fiap_api_gateway.id

  integration_uri    = var.lambda_invoke_arn
  integration_type   = "AWS_PROXY"
  integration_method = "POST"
}
