# Lab 01 — List S3 Buckets with Boto3

## Objective

Call the Amazon S3 `ListBuckets` API using Boto3 and display the general purpose buckets owned by the authenticated AWS account.

This is a read-only lab. It does not create, modify, upload, or delete AWS resources.

## Prerequisites

- Python 3.10 or later.
- AWS CLI v2 or another supported AWS credential provider.
- Boto3 installed in an isolated virtual environment.
- An AWS identity configured for the target environment.
- Permission to call `s3:ListAllMyBuckets`.

For EC2 workloads, use an instance role. For local development, use an approved local profile or federation flow. Do not copy access keys into this repository or hardcode them in Python.

## Setup

From this directory:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

On macOS or Linux, activate the environment with:

```bash
source .venv/bin/activate
python -m pip install -r requirements.txt
```

## Verify the caller first

```bash
aws sts get-caller-identity
aws configure list
```

Confirm that the returned account and principal are the intended lab identity. Do not publish the output if it contains account or identity information you do not want to disclose.

## Run the lab

```bash
python list_buckets.py
```

The script uses Boto3's standard credential provider chain. It does not accept credentials as command-line arguments or read secrets from source files.

## Required permission

The `ListBuckets` API operation requires:

- Action: `s3:ListAllMyBuckets`

This permission allows listing buckets owned by the authenticated sender. It does not grant permission to list objects in a bucket or read object contents.

For accounts with a general purpose bucket quota above 10,000, S3 requires paginated `ListBuckets` requests. The sample explicitly follows the continuation token.

## Expected behavior

If the identity is authorized, the script prints each bucket name returned by S3. If the identity is not authorized, it prints a concise AWS error code and exits with a non-zero status.

An empty bucket list is a valid result when the account has no general purpose buckets visible to the caller.

## Tests

Install the development dependency and run:

```bash
python -m pip install -r requirements-dev.txt
python -m pytest -q
```

Unit tests use a mocked S3 client. They do not make AWS API calls.

## Validation status

**Documentation and code added; AWS execution not yet validated.**

Record the date, caller identity type (without publishing account identifiers), region/configuration, command result, and any permission errors after running the lab in the intended AWS environment.

## Security and cost notes

- The operation is read-only and does not create billable S3 storage.
- Bucket names can reveal internal naming conventions; treat output as operational information.
- Never commit credentials, session tokens, or unredacted identity output.
- Do not add broad S3 permissions merely to make the lab pass.
- Do not make a bucket public as a troubleshooting shortcut.

## Exam connection

This lab practices authenticated SDK calls and the distinction between `s3:ListAllMyBuckets` and bucket/object permissions. It supports the DVA-C03 development and security learning path but does not, by itself, complete an exam objective.

## References

- [Boto3 credentials](https://docs.aws.amazon.com/boto3/latest/guide/credentials.html)
- [Boto3 S3 ListBuckets](https://docs.aws.amazon.com/boto3/latest/reference/services/s3/client/list_buckets.html)
- [S3 ListBuckets API permissions](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListBuckets.html)
