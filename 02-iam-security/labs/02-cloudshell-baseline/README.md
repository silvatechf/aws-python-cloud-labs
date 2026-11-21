# Lab 02 — AWS CloudShell Baseline

## Objective

Verify CloudShell authentication, region configuration, credential source, and working directory. Compare the CloudShell execution context with a local AWS CLI installation without copying long-term credentials into the browser-based environment.

## Safety boundary

- Use the intended AWS account and region.
- Do not copy local Access Keys, Secret Access Keys, session tokens, or credential files into CloudShell.
- Do not paste credentials into commands, scripts, shell history, or repository files.
- Review command output before sharing it; redact account IDs and principal identifiers where appropriate.
- This lab uses read-only AWS API operations and local shell commands. It does not create cloud resources.

## 1. Open CloudShell

1. Sign in to the AWS Management Console using the intended identity.
2. Select the intended AWS Region.
3. Open CloudShell from the console navigation.
4. Wait for the shell environment to become available.

## 2. Inspect the shell environment

Run:

```bash
pwd
echo "$HOME"
echo "$AWS_REGION"
echo "$AWS_DEFAULT_REGION"
aws --version
```

The region variables and CLI version are environment observations. Do not assume that every CloudShell session or region has identical values.

## 3. Inspect AWS CLI configuration sources

```bash
aws configure list
```

Review the `TYPE` and `LOCATION` columns. The output can show whether the region comes from environment variables and which credential provider supplied credentials.

Do not share unredacted credential identifiers or secret material.

## 4. Confirm the authenticated principal

```bash
aws sts get-caller-identity
```

Record locally:

- Account identifier.
- Returned ARN.
- Principal type indicated by the ARN.
- Region used by the CLI.

The STS response identifies the authenticated principal. It does not prove access to every AWS service.

## 5. Compare with IAM identity metadata

For an IAM user principal, this read-only command returns user metadata:

```bash
aws iam get-user
```

If the principal is not an IAM user, this command may not be applicable. Do not treat that outcome alone as an authentication failure. Use the STS ARN to identify the caller.

## 6. Check a read-only regional API

```bash
aws ec2 describe-regions \
  --query "Regions[].RegionName" \
  --output text
```

This command requires permission for the EC2 `DescribeRegions` API. A successful response demonstrates authorization for this specific operation, not general EC2 access.

## 7. Create a local study workspace

```bash
mkdir -p "$HOME/aws-dva-c03/cli-hands-on"
cd "$HOME/aws-dva-c03/cli-hands-on"
printf '%s\n' "AWS DVA-C03 - CloudShell Hands-on" > environment-check.txt
cat environment-check.txt
```

CloudShell provides persistent storage in the home directory, subject to AWS service limits and lifecycle rules. Do not use it as the only copy of important project files.

## Expected evidence

- CloudShell starts in the intended account and Region.
- `get-caller-identity` returns the expected principal.
- `aws configure list` reveals the effective configuration sources.
- The learner can explain the difference between credential source and authenticated principal.
- No long-term credentials were copied into CloudShell.
- No AWS resources were created.

## Troubleshooting

| Symptom | Area to inspect |
|---|---|
| Empty output from `aws configure get region` | The command reads profile configuration; inspect environment variables and `aws configure list` |
| Unexpected region | Console Region and `AWS_REGION` / `AWS_DEFAULT_REGION` |
| `AccessDenied` | Authentication may have succeeded; inspect authorization for the specific API |
| `iam get-user` is not applicable | Inspect the STS ARN; the caller may not be an IAM user |
| Different credential source from local CLI | Compare `aws configure list`; credential providers differ by environment |

## Cleanup

No AWS resources are created. Local files can remain in the CloudShell home directory for subsequent exercises. Keep a separate copy of any important study notes.

## Exam connection

This lab reinforces programmatic access, authenticated AWS API calls, credential provider behavior, principal identification, and the distinction between authentication and authorization.
