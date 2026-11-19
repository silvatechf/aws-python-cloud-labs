# AWS Python Cloud Labs

A hands-on learning repository for AWS application development with Python, aligned with the **AWS Certified Developer – Associate (DVA-C03)** exam and practical backend engineering.

The repository will grow alongside the Stephane Maarek Udemy course. Each lab should connect a course concept to an implementation, a reproducible validation step, and the relevant exam objectives.

## Learning goals

- Understand AWS services used to build and operate cloud applications.
- Develop with Python, AWS SDK for Python (Boto3), and AWS service APIs.
- Apply secure development practices, especially IAM least privilege and secrets handling.
- Test, deploy, troubleshoot, and optimize application workloads.
- Build practical evidence relevant to Python Backend, Application Security, and DevSecOps roles.

## Exam alignment

The DVA-C03 exam guide defines four domains:

| Domain | Weight |
|---|---:|
| Development with AWS Services | 30% |
| Security | 26% |
| Testing and Deployment | 22% |
| Troubleshooting and Optimization | 22% |

Always use the [official DVA-C03 exam guide](https://docs.aws.amazon.com/aws-certification/latest/developer-associate-03/developer-associate-03.html) as the source of truth. Exam objectives and in-scope services can change.

## Repository structure

    docs/                  Study roadmap, exam mapping, and glossary
    01-cloud-fundamentals/ AWS global infrastructure and core cloud concepts
    02-iam-security/       IAM, credentials, encryption, and secure access
    03-python-sdk/         Boto3 and AWS API integration with Python
    04-aws-services/       Application services, storage, and databases
    05-serverless/         Lambda, API Gateway, and event-driven patterns
    06-testing-deployment/ Testing, packaging, and deployment workflows
    07-monitoring/         Logging, monitoring, troubleshooting, optimization
    08-practice-exams/     Original practice questions and revision notes

Directories will be populated incrementally as topics are studied and validated.

## Lab quality standard

Every substantive lab should include:

1. **Objective** — the problem and expected outcome.
2. **Concepts** — service behavior, important limits, and trade-offs.
3. **Implementation** — small, readable Python code or configuration.
4. **Execution** — prerequisites and reproducible commands.
5. **Validation** — tests or observable evidence that the lab works.
6. **Security and cost** — permissions, data exposure, cleanup, and cost considerations.
7. **Exam connection** — relevant DVA-C03 domain and scenario patterns.

## Safety rules

- Never commit AWS access keys, session tokens, private keys, passwords, or real secrets.
- Prefer IAM roles and temporary credentials over long-lived access keys.
- Apply least privilege; do not use broad permissions as a shortcut.
- Use isolated resources and budgets/alerts for hands-on AWS work.
- Document resource cleanup. Verify that billable resources are removed after each lab.
- Do not treat educational examples as production-ready designs.

## Suggested local setup

Use a dedicated virtual environment and install only the dependencies required by each lab. Do not install AWS credentials or secrets as project dependencies.

    python -m venv .venv

Activate it, then install the dependencies specified by the relevant lab. AWS CLI configuration should use a secure local profile or an approved identity provider; never store credentials in this repository.

## Study workflow

1. Follow the course lesson.
2. Record the topic and any questions.
3. Implement or extend the corresponding lab.
4. Run the documented validation.
5. Explain the design and security choices in your own words.
6. Review the related DVA-C03 exam objectives.

## Status

This is an evolving study and portfolio repository. A topic is considered complete only after its implementation (where applicable), validation, and documentation have been reviewed.

## References

- [AWS Certified Developer – Associate (DVA-C03) exam guide](https://docs.aws.amazon.com/aws-certification/latest/developer-associate-03/developer-associate-03.html)
- [Boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)
- [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html)
