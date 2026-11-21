# Lesson 01 — IAM Fundamentals

## Learning objectives

By the end of this lesson, you should be able to:

- Distinguish authentication from authorization.
- Explain the purpose of IAM users, groups, roles, and policies.
- Read a basic IAM policy document.
- Explain implicit deny and explicit deny.
- Distinguish identity-based policies from resource-based policies.
- Explain why temporary credentials and least privilege matter to application developers.

## Why IAM exists

AWS must answer two separate questions for every protected request:

1. **Authentication:** Who or what is making the request?
2. **Authorization:** Is that principal allowed to perform this action on this resource under the current request context?

A principal can authenticate successfully and still receive `AccessDenied`. Valid credentials prove identity; they do not automatically grant permission.

## Core IAM building blocks

| Concept | Meaning | Typical use |
|---|---|---|
| User | An IAM identity with long-term credentials or console access | Legacy or specific human/service scenarios; avoid creating users by default for workloads |
| Group | A collection of IAM users to manage shared permissions | Assigning common permissions to multiple IAM users |
| Role | An assumable identity that provides temporary credentials | AWS services, federated humans, cross-account access, CI/CD |
| Policy | A JSON document defining permissions or trust | Granting, limiting, or delegating access |

A role has two distinct policy concerns:

- **Trust policy:** who is allowed to assume the role.
- **Permissions policy:** what the role session is allowed to do.

A trust policy does not grant S3, DynamoDB, Lambda, or other service permissions. It establishes who may assume the role.

## Authentication is not authorization

Example:

- The AWS CLI loads credentials for a developer.
- AWS validates those credentials and identifies the principal.
- The developer calls an AWS API.
- IAM evaluates the applicable policies.
- The request is allowed or denied.

Therefore, a successful `aws sts get-caller-identity` confirms which identity is being used. It does **not** prove that this identity can perform a particular service action.

## IAM policy anatomy

A permissions policy is a JSON document. The following example is intentionally illustrative and is not attached to an AWS identity.

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowListingOneBucket",
      "Effect": "Allow",
      "Action": "s3:ListBucket",
      "Resource": "arn:aws:s3:::example-training-bucket"
    }
  ]
}
```

| Element | Meaning |
|---|---|
| `Version` | Policy language version; use `2012-10-17` |
| `Statement` | One or more permission statements |
| `Sid` | Optional statement identifier |
| `Effect` | `Allow` or `Deny` |
| `Action` | API actions covered by the statement |
| `Resource` | Resource ARNs to which the statement applies |
| `Condition` | Optional request-context conditions |

Important distinctions:

- `s3:ListBucket` applies to a bucket ARN.
- `s3:GetObject` applies to object ARNs, usually ending in `/*`.
- An action name is not a resource ARN.
- `Resource: "*"` is sometimes required by an API, but should not be used as a shortcut when narrower resource scoping is supported.

## How policy evaluation works

For exam scenarios, start with these rules:

1. Requests are implicitly denied by default.
2. An applicable explicit `Allow` can grant access.
3. An applicable explicit `Deny` overrides an `Allow`.
4. Other policy types can limit the effective permissions, including permissions boundaries, session policies, and AWS Organizations SCPs/RCPs.

Do not reduce every IAM scenario to "Allow wins if any policy says Allow." The result depends on the principal, resource, account boundary, and applicable policy types.

For a common same-account case involving identity-based and resource-based permissions policies, an applicable Allow in either can grant access unless an applicable explicit Deny or another limiting policy changes the result. Cross-account access generally requires authorization on both sides.


## AWS CLI hands-on: identity and policy discovery

The following read-only commands were executed during the study. They do not create or modify AWS resources.

### Identify the caller

```powershell
aws sts get-caller-identity
```

This returns the caller's account and principal identifiers. It is an identity check, not a test of permissions on every AWS service.

### Inspect IAM users and groups

```powershell
aws iam list-users
aws iam list-groups-for-user --user-name <iam-user>
aws iam get-user --user-name <iam-user>
```

Observed in the study account: one IAM user was returned by `list-users`; `list-groups-for-user` returned an empty list for the tested user. This is an observation about that account at that time, not a general IAM rule.

### Understand policy scopes

```powershell
aws iam list-policies --scope Local --max-items 10
aws iam list-policies --scope AWS --only-attached
aws iam list-user-policies --user-name <iam-user>
aws iam list-attached-user-policies --user-name <iam-user>
```

- `--scope Local` lists customer-managed policies.
- `--scope AWS` lists AWS-managed policies.
- `--only-attached` restricts results to attached managed policies.
- `list-user-policies` lists inline policies for the user.
- `list-attached-user-policies` lists managed policies attached directly to the user.

An empty result from `--scope Local` does not mean the user has no policies: AWS-managed and inline policies are different categories.

### Inspect a managed policy

```powershell
aws iam get-policy --policy-arn <policy-arn>
aws iam get-policy-version --policy-arn <policy-arn> --version-id <version-id>
```

- `get-policy` returns metadata, including `DefaultVersionId`.
- `get-policy-version` returns the JSON policy document for the requested version.
- `DefaultVersionId` is not an account ID, CLI version, or attachment count.

### Filter and paginate CLI output

JMESPath can filter the response locally:

```powershell
aws iam list-users --query "Users[?Path=='/'].UserName" --output text
```

The filter selects users whose `Path` is `/`, then projects their `UserName` values. The query does not modify AWS data.

For paginated operations, `--max-items` limits the number of items returned to the CLI caller in one page. A continuation token may be returned for subsequent retrieval. Do not confuse pagination with merely truncating terminal output.

## CloudShell hands-on: credential source and principal

CloudShell is a browser-based shell integrated with the AWS Management Console. It uses credentials made available to the environment; do not copy local long-term access keys into CloudShell.

During this study, the following observations were verified:

- The shell home directory was `/home/cloudshell-user`.
- `AWS_REGION` and `AWS_DEFAULT_REGION` were both set to `us-east-1`.
- `aws configure list` reported the region source as environment variables.
- The credential source was reported by the CLI as `container-role`.
- `aws sts get-caller-identity` and `aws iam get-user` identified the same IAM user used by the local Windows CLI.

Important distinction:

- **Credential provider/source:** where the CLI obtains credentials.
- **Authenticated principal:** the identity represented by those credentials, identified through STS.

Do not infer the IAM principal type from the credential-source label alone. Use the STS ARN as evidence of the caller.

See [Lab 02 — CloudShell Baseline](../labs/02-cloudshell-baseline/README.md) for the reproducible command sequence.

## Credential strategy for developers

Prefer this order:

1. Federated human access through IAM Identity Center where available.
2. IAM roles and temporary credentials for workloads running on AWS.
3. Web identity federation or role assumption for supported external workloads and CI/CD.
4. Long-term IAM user access keys only for exceptional cases where a better federation or role-based option is unavailable, with strict controls and rotation.

Never commit credentials, paste access keys into chat, put secrets in source code, or store them in project configuration files.

## DVA-C03 connection

This lesson supports Security Domain skills including:

- Configure programmatic access to AWS.
- Make authenticated calls to AWS services.
- Define permissions for IAM principals and resources.
- Assume an IAM role.

See the official [DVA-C03 exam guide](https://docs.aws.amazon.com/aws-certification/latest/developer-associate-03/developer-associate-03.html). The exam guide remains the source of truth.

## Knowledge check

Answer these without looking back:

1. Can a caller be authenticated and still receive `AccessDenied`? Explain.
2. What is the difference between a role trust policy and a role permissions policy?
3. What is the default result when no applicable policy allows a request?
4. Which wins when an applicable Allow and explicit Deny both match?
5. Does `GetCallerIdentity` prove that the caller can list an S3 bucket?

Do not mark this lesson complete until you can explain each answer in your own words.
