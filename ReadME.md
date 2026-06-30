# AWS Landing Zone & Compliance Automation

A Terraform-based AWS infrastructure project that demonstrates an enterprise-style landing zone with reusable networking modules, automated compliance checks, and CI/CD validation.

The project focuses on Infrastructure as Code (IaC), AWS networking, governance, and automation using Terraform, Python, GitHub Actions, and Boto3.

## Features

- **Reusable VPC Module** – Multi-subnet VPC architecture for the `af-south-1` (Cape Town) region.
- **Infrastructure as Code** – Modular Terraform configuration for consistent deployments.
- **Compliance Automation** – Python (`boto3`) script that audits AWS resource tags (`environment`, `owner`, `project`).
- **CI/CD Validation** – GitHub Actions workflow that runs Terraform formatting and validation before changes are merged.

## Project Structure

```text
aws-enterprise-platform/
├── .github/
│   └── workflows/
│       └── iac-pipeline.yml
├── scripts/
│   └── tag_enforcer.py
└── terraform/
    ├── environments/
    │   └── dev/
    └── modules/
        └── vpc/
```

## Architecture

- Multi-subnet VPC deployed in the **AWS Africa (Cape Town)** (`af-south-1`) region.
- Separation of public and private subnets.
- Modular Terraform design for reuse across environments.
- Python-based compliance auditing using the AWS SDK (`boto3`).

## Security Principles

- **Least Privilege** – Infrastructure is designed to support IAM least-privilege access.
- **No Hardcoded Secrets** – Credentials are supplied through environment variables or AWS credential providers.
- **Idempotent Infrastructure** – Terraform modules are designed for repeatable deployments with predictable state management.

## Technologies

- Terraform
- AWS
- Python
- Boto3
- GitHub Actions

## Future Improvements

- Remote Terraform state using S3 and DynamoDB
- AWS Config compliance rules
- CloudTrail and GuardDuty integration
- Automated security scanning with tfsec or Checkov
- Multi-environment deployment (dev, staging, production)

## License

This project is licensed under the MIT License.
