"""List general purpose S3 buckets for the authenticated AWS account."""

from __future__ import annotations

import sys

import boto3
from botocore.exceptions import BotoCoreError, ClientError


def list_bucket_names(s3_client) -> list[str]:
    """Return bucket names, following the ListBuckets continuation token."""
    bucket_names: list[str] = []
    request: dict[str, object] = {"MaxBuckets": 1000}

    while True:
        response = s3_client.list_buckets(**request)
        bucket_names.extend(
            bucket["Name"] for bucket in response.get("Buckets", [])
        )

        continuation_token = response.get("ContinuationToken")
        if not continuation_token:
            break

        request["ContinuationToken"] = continuation_token

    return bucket_names


def main() -> int:
    s3 = boto3.client("s3")

    try:
        bucket_names = list_bucket_names(s3)
    except ClientError as exc:
        error = exc.response.get("Error", {})
        code = error.get("Code", "Unknown")
        message = error.get("Message", "The S3 request failed.")
        print(f"AWS service error ({code}): {message}", file=sys.stderr)
        return 1
    except BotoCoreError as exc:
        print(f"AWS SDK error: {exc}", file=sys.stderr)
        return 1

    if not bucket_names:
        print("No general purpose buckets were returned.")
        return 0

    for bucket_name in bucket_names:
        print(bucket_name)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
