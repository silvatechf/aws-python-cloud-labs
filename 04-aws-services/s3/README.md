# Amazon S3 — Fundamentals for DVA-C03

## Purpose

Introduce the Amazon S3 object-storage model and the concepts required before implementing S3 access with the AWS CLI and Boto3.

This is an introductory lesson. It does not complete the S3 service coverage required for DVA-C03.

## 1. What is Amazon S3?

Amazon Simple Storage Service (Amazon S3) is an object storage service. It stores data as objects inside buckets.

Common application use cases include:

- Images, documents, and user uploads.
- JSON, CSV, and other application data files.
- Backups and exported reports.
- Application assets and static content.
- Logs and datasets used by downstream processing.

S3 is not a traditional hierarchical file system or a relational database.

## 2. Bucket, object, and key

| Concept | Meaning |
|---|---|
| Bucket | A container and namespace for objects. |
| Object | The stored data together with metadata. |
| Key | The object's name, used to identify it within a bucket. |

Example:

```text
Bucket: training-example-bucket
Object key: reports/2026/january.pdf
```

For general purpose buckets, S3 has a flat object structure. The slash-separated path is part of the object key; console folders are a presentation built from shared key prefixes.

An object is identified by its bucket and key. When versioning is enabled, a version ID can distinguish object versions.

## 3. S3 API actions and IAM permissions

Do not treat all S3 permissions as interchangeable.

| Application operation | IAM action | Resource scope |
|---|---|---|
| List all buckets owned by the caller | `s3:ListAllMyBuckets` | Account-level bucket listing permission |
| List objects in one bucket | `s3:ListBucket` | Bucket ARN, for example `arn:aws:s3:::example-bucket` |
| Read one object | `s3:GetObject` | Object ARN, for example `arn:aws:s3:::example-bucket/*` |
| Upload an object | `s3:PutObject` | Object ARN |
| Delete an object | `s3:DeleteObject` | Object ARN |

The action and resource ARN must match the S3 authorization model. A bucket-level action and an object-level action usually require different resource ARNs.

**Important:** `s3:ListAllMyBuckets` is not required merely to read an object when the application already knows the bucket and key. Grant only the actions the application actually needs.

## 4. Access path from Python

A Python application can use the AWS SDK for Python (Boto3) to call S3 APIs.

Typical flow:

1. The application creates an S3 client.
2. Boto3 resolves credentials using its credential provider chain.
3. The application calls an S3 API operation.
4. AWS evaluates the principal's applicable identity policies, resource policies, and other authorization controls.
5. The SDK returns the response or raises an exception.

For applications running on EC2, prefer an attached IAM role and temporary credentials rather than static access keys in source code or configuration files.

Boto3 also supports local development profiles and other credential providers. Do not hardcode credentials in the client constructor.

## 5. First read-only Boto3 exercise

The companion lab lists general purpose buckets visible to the authenticated AWS account.

The `ListBuckets` operation requires `s3:ListAllMyBuckets`. It does not prove that the principal can list objects in a bucket or read an object.

The lab uses paginated `ListBuckets` requests. It does not create, modify, or delete AWS resources.

See [Lab 01 — Boto3 S3 Basics](labs/01-boto3-s3-basics/README.md).

## 6. DVA-C03 study points

Be able to distinguish:

- Bucket versus object versus object key.
- Bucket-level actions versus object-level actions.
- `s3:ListBucket` versus `s3:GetObject`.
- `s3:ListAllMyBuckets` versus listing objects in a known bucket.
- Identity-based permissions versus a bucket policy.
- Authentication versus authorization.
- Static long-term credentials versus role-based temporary credentials.

## 7. Not covered yet

This introductory lesson does not yet cover:

- S3 storage classes and lifecycle configuration.
- Versioning and delete markers.
- Server-side encryption, SSE-S3, SSE-KMS, and encryption in transit.
- S3 Block Public Access and bucket ownership controls.
- Presigned URLs.
- Multipart uploads.
- Replication and event notifications.
- Object Lock and retention controls.
- S3 performance and cost optimization.

These topics will be added as separate lessons or labs when they are reached in the course and mapped to the official exam guide.

## References

- [What is Amazon S3?](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html)
- [Organizing objects using prefixes and folders](https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-folders.html)
- [Required permissions for S3 API operations](https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-with-s3-policy-actions.html)
- [Boto3 credentials](https://docs.aws.amazon.com/boto3/latest/guide/credentials.html)
- [Boto3 S3 ListBuckets reference](https://docs.aws.amazon.com/boto3/latest/reference/services/s3/client/list_buckets.html)
