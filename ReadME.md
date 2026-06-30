# Enterprise AWS Landing Zone & Compliance Automation Platform

A production-ready infrastructure blueprint and governance platform designed to enforce cloud architecture best practices, automated compliance, and rigorous CI/CD safety controls within an enterprise environment.

This repository applies the theoretical frameworks validated by my **AWS Solutions Architect Associate (SAA-C03)** certification to programmatic Infrastructure as Code (IaC) and systems automation.

## Architecture Overview

- **Core Networking:** Multi-subnet, highly available Virtual Private Cloud (VPC) baseline designed across strict public and private isolation boundaries inside the Cape Town (`af-south-1`) region.
- **Automation & Compliance:** Programmatic resource tracking using Python (`boto3`) to enforce corporate metadata tagging policies (`environment`, `owner`, `project`).
- **CI/CD Guardrails:** Automated GitHub Actions pipeline executing rigorous format linting and code validation checks to prevent syntax anomalies before production promotion.

## Repository Structure

```text
aws-enterprise-platform/
├── .github/workflows/
│   └── iac-pipeline.yml   # Automated linting and validation pipeline
├── scripts/
│   └── tag_enforcer.py    # Python compliance audit engine (Boto3)
└── terraform/
    ├── environments/
    │   └── dev/           # Dedicated environment consumer configurations
    └── modules/
        └── vpc/           # Reusable parameterised networking module
```
