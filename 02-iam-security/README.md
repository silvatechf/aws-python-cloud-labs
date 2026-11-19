# 02 — IAM and Security

Study identity, authentication, authorization, IAM policies and roles, temporary credentials, encryption, secrets management, and secure application access.

## Learning path

1. [Lesson 01 — IAM Fundamentals](lessons/01-iam-fundamentals.md)
2. [Lab 01 — AWS CLI Identity Baseline](labs/01-aws-cli-identity-baseline/README.md)
3. Policy evaluation and IAM policy types.
4. IAM roles, trust policies, STS, and temporary credentials.
5. Application access patterns with Boto3 and role-based credentials.

## Security principles

- Prefer IAM Identity Center or federation for human access.
- Prefer IAM roles and temporary credentials for workloads.
- Apply least privilege and scope permissions to specific actions and resources.
- Separate role trust policies from role permissions policies.
- Never commit credentials or secrets.
- Validate policy behavior before relying on it.

## Status

In progress — foundational lesson and read-only CLI identity lab added. Completion requires learner answers and verified local CLI evidence.
