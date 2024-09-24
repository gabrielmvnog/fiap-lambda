resource "aws_cognito_user_pool" "user_pool" {
  name = "18burguer_pool"
}

resource "aws_cognito_resource_server" "resource_server" {
  name       = "resource_server"
  identifier = "https://example.com"

  user_pool_id = aws_cognito_user_pool.user_pool.id

  scope {
    scope_name        = "all"
    scope_description = "Get access to all API Gateway endpoints."
  }
}


resource "aws_cognito_user_pool_client" "client" {
  name = "client"
  user_pool_id                         = "${aws_cognito_user_pool.user_pool.id}"
  generate_secret                      = true
  allowed_oauth_flows                  = ["client_credentials"]
  supported_identity_providers         = ["COGNITO"]
  allowed_oauth_flows_user_pool_client = true
  allowed_oauth_scopes                 = ["${aws_cognito_resource_server.resource_server.scope_identifiers}"]
}
