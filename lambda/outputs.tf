output "lambda_name" {
  description = "Name of the Lambda function."

  value = aws_lambda_function.fiap_lambda.function_name
}

output "lambda_invoke_arn" {
  value = aws_lambda_function.fiap_lambda.invoke_arn
}
