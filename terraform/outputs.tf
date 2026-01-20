output "vpc_id" {
  description = "VPC ID"
  value       = module.vpc.vpc_id
}

output "alb_dns_name" {
  description = "Application Load Balancer DNS name"
  value       = module.alb.alb_dns_name
}

output "ecs_cluster_name" {
  description = "ECS Cluster name"
  value       = module.ecs.ecs_cluster_name
}

output "ecs_service_name" {
  description = "ECS Service name"
  value       = module.ecs.ecs_service_name
}

output "application_url" {
  description = "Application URL (HTTP)"
  value       = "http://${module.alb.alb_dns_name}"
}
