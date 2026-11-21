# 02 — IAM and Security

Study identity, authentication, authorization, IAM policies and roles, temporary credentials, encryption, secrets management, and secure application access.

## Learning path

1. [Lesson 01 — IAM Fundamentals](lessons/01-iam-fundamentals.md)
2. [Lesson 02 — IAM for Application Developers and DVA-C03](lessons/02-iam-dva-c03-study-guide.md)
3. [Lab 01 — AWS CLI Identity Baseline](labs/01-aws-cli-identity-baseline/README.md)
4. [Lab 02 — AWS CloudShell Baseline](labs/02-cloudshell-baseline/README.md)
5. Policy evaluation and IAM policy types.
6. IAM roles, trust policies, STS, and temporary credentials.
7. Application access patterns with Boto3 and role-based credentials.

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
- Course quiz topics expanded into an exam-oriented study guide with original scenario questions and explanations.
- Official DVA-C03 Security Domain 2 task/skill mapping.

Still required before marking IAM complete:
- Inspect a managed policy document with `get-policy-version`.
- Complete the scenario questions in [Lesson 02](lessons/02-iam-dva-c03-study-guide.md) and explain each distractor.
- Practice IAM roles and STS role assumption.
- Build and validate a least-privilege role-based access lab.
- Complete the practical role/STS exercise and review the remaining Domain 2 objectives (encryption, sensitive data, and AI security) in their own lessons.
