# IAM Scenario Practice — Set 02

## Purpose

This set records the eight original IAM scenarios practiced during the guided DVA-C03 study session. It complements, rather than replaces, the broader [IAM study guide](../lessons/02-iam-dva-c03-study-guide.md).

These are original learning questions, not official AWS exam questions or copied exam content.

## How to use this set

1. Answer each question before reading its explanation.
2. Identify the principal, action, resource, and applicable policies.
3. Explain why every distractor is incorrect.
4. Practice the model answer aloud.
5. Complete the short English recall exercise.

---

## Question 1 — EC2 application credentials

An application running on an EC2 instance must read objects from one S3 bucket. The developer plans to store an IAM user's access keys in an environment file on the instance.

What is the best approach?

A. Keep the access keys in the environment file and rotate them monthly.  
B. Attach an IAM role to the EC2 instance with narrowly scoped S3 read permissions.  
C. Use the AWS account root credentials because EC2 is an AWS service.  
D. Create a separate IAM user for every application process.

**Correct answer: B**

- **A — Incorrect:** Environment variables or files do not turn long-term access keys into temporary credentials. They still require secure storage, rotation, and lifecycle management.
- **B — Correct:** An EC2 instance role provides temporary credentials through the instance role credential mechanism. Scope its permissions to the required S3 actions and resources.
- **C — Incorrect:** Root credentials must not be used for routine application access.
- **D — Incorrect:** Creating more IAM users increases the number of long-term credentials to manage and is not the preferred workload identity pattern.

**Model answer**

> I would choose B because an EC2 instance can use an IAM role to obtain temporary credentials. This avoids storing long-term access keys and follows the principle of least privilege.

**Recall practice**

- An EC2 instance can use an IAM ______.
- The application obtains ______ credentials.
- This avoids storing long-term access ______.

Answers: role / temporary / keys.

## Question 2 — Role trust policy

A role has a permissions policy allowing `s3:GetObject`, but an external AWS account cannot assume it.

Which configuration must be examined?

A. The S3 bucket lifecycle policy.  
B. The role trust policy and the caller's permission to invoke `sts:AssumeRole`.  
C. The IAM Credential Report.  
D. The EC2 security group.

**Correct answer: B**

- **A — Incorrect:** Lifecycle rules govern object transitions and expiration; they do not define who can assume an IAM role.
- **B — Correct:** The role trust policy defines which principals may assume the role. For cross-account access, the calling principal must also be authorized to call `sts:AssumeRole`.
- **C — Incorrect:** The Credential Report provides credential status information; it does not establish the role's trust relationship.
- **D — Incorrect:** Security groups control network traffic for supported resources, not IAM role assumption authorization.

**Model answer**

> I would choose B because the trust policy defines who can assume an IAM role. The external account must also have permission to call sts:AssumeRole.

**Recall practice**

- The trust policy defines ______ can assume a role.
- The caller also needs permission to call ______.

Answers: who / sts:AssumeRole.

## Question 3 — Explicit Deny

A principal has an applicable Allow for an S3 action. Another applicable policy explicitly denies the same action on the requested object.

What is the expected result?

A. Allow, because an Allow exists.  
B. Allow, if the request uses the AWS CLI.  
C. Deny, because an applicable explicit Deny overrides an Allow.  
D. It depends only on the user's group membership.

**Correct answer: C**

- **A — Incorrect:** An applicable explicit Deny takes precedence over an Allow.
- **B — Incorrect:** AWS CLI does not bypass IAM authorization. The request is evaluated using the caller's identity and applicable policies.
- **C — Correct:** An applicable explicit Deny overrides an applicable Allow.
- **D — Incorrect:** Group membership alone does not determine the final authorization decision; all applicable policy mechanisms and conditions matter.

**Model answer**

> I would choose C because an explicit Deny overrides an applicable Allow in AWS IAM policy evaluation. Therefore, the request is denied, even if another policy allows the action.

**Recall practice**

- An explicit ______ overrides an applicable Allow.
- Therefore, the request is ______.

Answers: Deny / denied.

## Question 4 — IAM policy document structure

Which element is defined at the top level of an IAM policy document, outside the `Statement` array?

A. `Effect`  
B. `Principal`  
C. `Version`  
D. `Action`

**Correct answer: C**

- **A — Incorrect:** `Effect` is an element of an individual statement.
- **B — Incorrect:** `Principal` can appear in statements of resource-based policies and role trust policies; it is not a universal top-level policy field.
- **C — Correct:** `Version` is a top-level policy document element, outside the `Statement` array.
- **D — Incorrect:** `Action` is an element of an individual statement.

**Model answer**

> I would choose C because Version is defined at the top level of an IAM policy document, outside the Statement array. Effect and Action are elements of individual policy statements.

**Recall practice**

- Version is defined at the ______ level.
- It is outside the ______ array.
- Effect and Action are policy ______.

Answers: top / Statement / statements.

## Question 5 — Authentication versus authorization

A developer successfully runs `aws sts get-caller-identity`, but receives `AccessDenied` when calling an AWS service API.

What does this indicate?

A. Authentication succeeded, but authorization for the service request was denied.  
B. The AWS CLI installation is necessarily corrupted.  
C. The AWS account has been deleted.  
D. STS automatically grants access to all AWS services.

**Correct answer: A**

- **A — Correct:** STS confirms the caller's identity. It does not grant permissions to invoke arbitrary AWS service APIs.
- **B — Incorrect:** A service-side `AccessDenied` response is not evidence of a corrupted CLI installation.
- **C — Incorrect:** A successful STS identity response shows that AWS recognized the caller for that request.
- **D — Incorrect:** STS provides identity and temporary-credential capabilities; it does not automatically authorize access to other services.

**Model answer**

> I would choose A because STS confirms the caller's identity, but it does not grant permissions to access other AWS services. The service request is denied because the principal does not have the required authorization.

**Recall practice**

- STS confirms the caller's ______.
- It does not grant service ______.
- The service request is ______.

Answers: identity / permissions / denied.

## Question 6 — Explicit Deny in a bucket policy

An EC2 application uses an IAM role. The role's identity-based policy allows `s3:GetObject` on all S3 buckets. However, the target bucket policy contains an applicable explicit Deny for that action.

What happens when the application tries to read an object from that bucket?

A. The request is allowed because the IAM role has an Allow policy.  
B. The request is allowed because EC2 roles have higher priority than bucket policies.  
C. The request is denied because an explicit Deny overrides an applicable Allow.  
D. The request is allowed if the application uses AWS CLI instead of Boto3.

**Correct answer: C**

- **A — Incorrect:** The identity-based Allow does not override an applicable explicit Deny.
- **B — Incorrect:** EC2 roles do not have a general priority over resource-based policies. Applicable explicit Deny statements take precedence.
- **C — Correct:** The explicit Deny applies to the request and overrides the Allow.
- **D — Incorrect:** Changing from Boto3 to AWS CLI does not bypass authorization.

**Model answer**

> I would choose C because an explicit Deny overrides an applicable Allow in AWS IAM policy evaluation. Therefore, the request is denied, even if the EC2 instance role allows the S3 action.

**Recall practice**

- An explicit ______ overrides an applicable Allow.
- The request is ______.
- The EC2 instance ______ does not bypass the bucket policy.

Answers: Deny / denied / role.

## Question 7 — Temporary credentials for EC2

A developer is building a Python application that runs on an EC2 instance. The application needs to access an S3 bucket. The developer wants to avoid storing long-term access keys in the application code.

Which solution should the developer implement?

A. Create an IAM user, generate access keys, and store them directly in the Python source code.  
B. Attach an IAM role with the required S3 permissions to the EC2 instance.  
C. Create an IAM user and store its access keys in environment variables permanently.  
D. Disable IAM authentication and allow public access to the S3 bucket.

**Correct answer: B**

- **A — Incorrect:** Source-code credentials can be exposed through version control, logs, or distribution artifacts.
- **B — Correct:** An EC2 instance role supplies temporary credentials to the application. The role should grant only the required S3 permissions.
- **C — Incorrect:** Environment variables are not a substitute for temporary workload credentials. The keys remain long-lived credentials.
- **D — Incorrect:** Public bucket access exposes data and removes necessary access controls.

**Model answer**

> I would choose B because an EC2 instance can use an IAM role to obtain temporary credentials. This avoids storing long-term access keys in the application code and follows the principle of least privilege.

**Recall practice**

- An EC2 instance can use an IAM ______.
- The application obtains ______ credentials.
- This avoids storing long-term access ______.
- This follows the principle of least ______.

Answers: role / temporary / keys / privilege.

## Question 8 — Permissions boundary

An IAM user has an identity-based policy that allows access to Amazon S3. The user also has a permissions boundary that allows only access to Amazon DynamoDB.

What happens when the user tries to access S3?

A. Access is allowed because the identity-based policy explicitly allows S3 access.  
B. Access is allowed because permissions boundaries apply only to IAM roles, not IAM users.  
C. Access is denied because the permissions boundary does not allow S3 access.  
D. Access is allowed if the user makes the request using AWS CLI.

**Correct answer: C**

- **A — Incorrect:** An identity-based Allow cannot exceed the permissions boundary.
- **B — Incorrect:** Permissions boundaries can be attached to IAM users and IAM roles.
- **C — Correct:** The boundary sets a maximum for permissions granted through identity-based policies. S3 is outside the stated boundary, so the identity-based Allow does not produce effective S3 access.
- **D — Incorrect:** AWS CLI does not bypass a permissions boundary.

**Model answer**

> I would choose C because a permissions boundary defines the maximum permissions an IAM identity can have. Even if the identity-based policy allows S3 access, the boundary does not permit that action. Therefore, access is denied.

**Recall practice**

- A permissions boundary defines the ______ permissions.
- The identity-based policy allows ______ access.
- The boundary does not ______ that action.
- Therefore, access is ______.

Answers: maximum / S3 / permit / denied.

---

## Review notes

The main misconceptions identified during this practice session were:

- Treating a new IAM user as safer than an EC2 role for an AWS workload.
- Confusing a role's trust policy with its permissions policy.
- Assuming an Allow always grants access even when an applicable explicit Deny exists.
- Confusing policy document-level fields with statement-level fields.
- Treating successful authentication as proof of authorization.
- Assuming CLI or SDK choice changes IAM authorization.
- Treating environment variables as temporary credentials.
- Assuming permissions boundaries apply only to roles.

Revisit these scenarios after completing the S3 and Boto3 labs.

## References

- [AWS IAM policy evaluation logic](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_evaluation-logic.html)
- [IAM roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html)
- [IAM best practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html)
- [AWS Security Token Service](https://docs.aws.amazon.com/STS/latest/APIReference/welcome.html)
