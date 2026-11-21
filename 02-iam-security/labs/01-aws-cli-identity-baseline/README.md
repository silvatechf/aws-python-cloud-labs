# Lab 01 — AWS CLI Identity Baseline

## Objective

Install or verify AWS CLI v2, identify the active credential profile, and confirm which AWS principal the CLI is using without creating IAM users, access keys, or billable resources.

## Safety boundary

- Do not use the AWS account root user for routine CLI work.
- Prefer IAM Identity Center or another approved federation method.
- Do not create long-lived access keys just to complete this lab.
- Never share access keys, session tokens, credential files, or unredacted debug logs.
- The commands in this lab are read-only. No AWS resources are created.

## 1. Verify AWS CLI

On Windows PowerShell:

```powershell
aws --version
Get-Command aws
```

The output should identify AWS CLI version 2. If the command is not found, follow the official [AWS CLI v2 installation guide](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html).

## 2. Inspect local CLI configuration safely

```powershell
aws configure list
aws configure list-profiles
```

These commands help identify the selected profile and configuration sources. Do not paste their output publicly without reviewing it first.

## 3. Authenticate with an approved profile

If your organization or training account provides IAM Identity Center, configure a named profile:

```powershell
aws configure sso --profile aws-learning
aws sso login --profile aws-learning
```

The wizard asks for the Identity Center start URL, its region, the AWS account, and an assigned role. These values must come from your actual Identity Center setup; do not guess them.

If you already have a configured profile, do not reconfigure it. Use that profile in the next step.

## 4. Confirm the active identity

```powershell
aws sts get-caller-identity --profile aws-learning
```

If your profile has a different name, replace `aws-learning`.

Record locally:

- AWS account ID (do not publish it unnecessarily).
- Returned ARN.
- Whether the principal is an assumed role or another identity type.
- Profile name used.

This operation identifies the caller. It does not test permissions for other AWS services.

## 5. Compare profile behavior

```powershell
aws sts get-caller-identity --profile aws-learning --output json
```

Then, if you have more than one approved profile, run the same command with the other profile and compare the returned ARN. Never assume that the default profile is the identity you intended to use.

## Expected evidence

- AWS CLI v2 is installed.
- The intended profile can authenticate.
- `get-caller-identity` returns the expected account and principal.
- No access keys or tokens were added to the repository.
- No AWS resources were created.

## Troubleshooting

| Symptom | Likely area to inspect |
|---|---|
| `aws` is not recognized | Installation or refreshed PowerShell PATH |
| Profile not found | Profile name and local AWS config |
| SSO token expired | Run `aws sso login --profile <profile>` again |
| `AccessDenied` on a service operation | Authentication may have succeeded; inspect authorization policies |
| Unexpected account or ARN | Explicitly select the intended `--profile` |

## Cleanup

No cloud resources are created. To end cached IAM Identity Center sessions when finished:

```powershell
aws sso logout
```

## Exam connection

This lab supports DVA-C03 Security Domain skills around programmatic access, authenticated AWS API calls, and IAM principals. It also reinforces the distinction between authentication and authorization.
