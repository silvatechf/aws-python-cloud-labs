# 02 — IAM and Security

Study identity, authentication, authorization, IAM policies and roles, temporary credentials, encryption, secrets management, and secure application access.

## Learning path

1. [Lesson 01 — IAM Fundamentals](lessons/01-iam-fundamentals.md)
2. [Lab 01 — AWS CLI Identity Baseline](labs/01-aws-cli-identity-baseline/README.md)
3. [Lab 02 — AWS CloudShell Baseline](labs/02-cloudshell-baseline/README.md)
4. Policy evaluation and IAM policy types.
5. IAM roles, trust policies, STS, and temporary credentials.
6. Application access patterns with Boto3 and role-based credentials.

## Security principles

- Prefer IAM Identity Center or federation for human access.
- Prefer IAM roles and temporary credentials for workloads.
- Apply least privilege and scope permissions to specific actions and resources.
- Separate role trust policies from role permissions policies.
- Never commit credentials or secrets.
- Validate policy behavior before relying on it.

## Status

**In progress — foundational IAM and AWS CLI/CloudShell exploration documented.**

Evidence completed:
- Local AWS CLI v2 identity and configuration inspection.
- Read-only IAM user, group, and policy inventory commands.
- AWS-managed versus customer-managed policy distinction.
- CloudShell identity, region, credential-source, and read-only EC2 API checks.
- Quiz practice on explicit deny, JMESPath filtering, pagination, and credential source versus principal.

Still required before marking IAM complete:
- Inspect a managed policy document with `get-policy-version`.
- Complete trust policy versus permissions policy scenarios.
- Practice IAM roles and STS role assumption.
- Build and validate a least-privilege role-based access lab.
- Review remaining IAM/security objectives against the official DVA-C03 exam guide.
