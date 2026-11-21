# DVA-C03 Exam Objectives

## Source of truth

Use the [official AWS Certified Developer – Associate (DVA-C03) exam guide](https://docs.aws.amazon.com/aws-certification/latest/developer-associate-03/developer-associate-03.html). This document is a working index, not a replacement for the official guide. Recheck the official guide before booking the exam and during final revision.

## Content domains

| Domain | Weight |
|---|---:|
| 1. Development with AWS Services | 30% |
| 2. Security | 26% |
| 3. Testing and Deployment | 22% |
| 4. Troubleshooting and Optimization | 22% |

## Security domain — current study focus

Domain 2 includes implementing authentication and authorization, implementing encryption and managing sensitive data, and identifying and mitigating security risks associated with AI service integration.

The IAM and CLI learning path currently maps to these official Domain 2 skills:

| Official skill | Focus | Repository evidence | Status |
|---|---|---|---|
| 2.1.3 | Configure programmatic access to AWS | [AWS CLI Identity Baseline](../02-iam-security/labs/01-aws-cli-identity-baseline/README.md) and [CloudShell Baseline](../02-iam-security/labs/02-cloudshell-baseline/README.md) | Practiced; validation in progress |
| 2.1.5 | Make authenticated calls to AWS services | CLI identity baseline and CloudShell read-only API checks | Practiced; validation in progress |
| 2.1.6 | Define permissions for IAM principals and resources | [IAM Fundamentals](../02-iam-security/lessons/01-iam-fundamentals.md) and [IAM DVA-C03 Study Guide](../02-iam-security/lessons/02-iam-dva-c03-study-guide.md) | In study |
| 2.1.7 | Assume an IAM role | Planned STS and role-assumption lab | Not started |

Also study skill 2.1.4 (presigned URLs) in the later S3/security section rather than forcing it into the first IAM lesson.

The course's IAM quiz topics (users, groups, roles, policy statements, least privilege, root-user protection, IAM Credential Report, and shared responsibility) are retained as foundational knowledge and expanded into scenario-based practice in the [IAM DVA-C03 Study Guide](../02-iam-security/lessons/02-iam-dva-c03-study-guide.md). The guide explicitly distinguishes core DVA-C03 developer skills from IAM administration tasks that the exam guide lists as out of scope.

## Study mapping

| Domain | Repository areas | Evidence to build |
|---|---|---|
| Development with AWS Services | 01, 03, 04, 05 | Python integrations, service usage, event-driven and serverless labs |
| Security | 02, 03, 04, 05 | IAM-aware code, temporary credentials, encryption and secrets handling |
| Testing and Deployment | 06 | Automated tests, packaging, deployment and release exercises |
| Troubleshooting and Optimization | 07 | Logs, metrics, diagnosis, performance and cost exercises |

## AI-related coverage

DVA-C03 includes AI-assisted development workflows and security tasks for integrating managed AI services. Study only the tasks and services specified by the official guide. Do not expand this repository into prompt engineering, RAG architecture, or model training unless a specific exam objective or practical lab justifies it.

## Tracking matrix

Update this table as each objective is studied and validated. Use links to concrete labs rather than marking topics complete based on video progress alone.

| Objective / skill | Studied | Practiced | Validated | Evidence |
|---|---|---|---|---|
| Domain 1 | No | No | No | — |
| Domain 2 | In progress | In progress | No | IAM Fundamentals; AWS CLI and CloudShell labs |
| Domain 3 | No | No | No | — |
| Domain 4 | No | No | No | — |

## Exam format and readiness

Confirm current exam duration, question format, scoring, language availability, and scheduling details directly in AWS Certification resources. Do not rely on third-party summaries for booking decisions.
