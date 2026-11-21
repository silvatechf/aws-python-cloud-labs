# Lesson 02 — IAM for Application Developers and DVA-C03

## Purpose

This lesson turns the IAM concepts introduced in Lesson 01 and the course review questions into an exam-oriented study guide for the AWS Certified Developer – Associate (DVA-C03).

The course quiz is useful as a foundation check. This guide preserves its core topics but adds the distinctions, decision-making, and application-development context needed for the current exam.

**Scope note:** The DVA-C03 guide states that administering IAM users and groups is outside the target candidate's expected job tasks. Developers must still understand IAM identities and be able to configure programmatic access, make authenticated service calls, define permissions, and assume roles.

## Official DVA-C03 alignment

Content Domain 2 — Security represents 26% of scored content.

| Official task | Relevant skills | What this lesson covers |
|---|---|---|
| 2.1 — Implement authentication and authorization mechanisms for applications and AWS services | 2.1.1–2.1.7 | Federation, access control, MFA, programmatic access, authenticated calls, IAM permissions, role assumption |
| 2.2 — Implement encryption and manage sensitive data by using AWS services | 2.2.1–2.2.7 | Introduced as the next security learning block; not completed by IAM study |
| 2.3 — Identify and mitigate security risks associated with using and integrating AI services into application development | 2.3.1–2.3.5 | Separate future study block; not covered by the IAM quiz |

Official source: [AWS Certified Developer – Associate (DVA-C03) Exam Guide](https://docs.aws.amazon.com/pdfs/aws-certification/latest/developer-associate-03/developer-associate-03.pdf), Content Domain 2, pages 6–7.

## 1. IAM identity building blocks

### IAM user

An IAM user is an identity in one AWS account. Depending on how it is configured, it can have console credentials, programmatic credentials, or both.

Important points:

- An IAM user is not the same thing as the AWS account root user.
- An IAM user uses its own credentials, not root credentials.
- A user can exist without belonging to any group.
- A user can belong to multiple groups.
- Permissions can be granted through attached managed policies, inline policies, group membership, and other applicable policy mechanisms.

For workforce access, prefer federation and IAM Identity Center where appropriate. For workloads running on AWS, prefer roles over long-term IAM user access keys.

### IAM group

An IAM group is a collection of IAM users used to manage shared permissions.

- Groups contain users only; groups cannot contain other groups.
- A user can belong to multiple groups.
- A group is not an identity that applications or AWS services assume.
- Group membership is one way that a user can receive permissions.

For DVA-C03, understand the model, but do not spend disproportionate time learning administrative workflows for managing users and groups.

### IAM role

An IAM role is an assumable IAM identity with a set of permissions. A trusted principal assumes the role and receives temporary security credentials for a role session.

Typical role users include:

- An AWS service, such as an EC2 instance or Lambda function.
- A federated human identity.
- An application or external workload using a supported federation mechanism.
- A principal in another AWS account.

A role is not simply a group of users and does not require a permanent username/password pair or long-term access key for each consumer.

### IAM policy

An IAM policy is a JSON document that defines permissions or, in the case of a role trust policy, the principals allowed to assume a role.

Permissions policies can be attached to IAM users, groups, and roles. Resource-based policies are attached to supported AWS resources.

## 2. IAM role: trust versus permissions

This distinction is essential.

| Policy | Question answered | Example |
|---|---|---|
| Trust policy | Who can assume this role? | Allow the EC2 service principal to assume an instance role |
| Permissions policy | What can the role session do? | Allow read access to a specific S3 bucket |

A trust policy does not grant access to S3 objects, DynamoDB tables, or other application resources. It establishes the role's trust relationship.

A permissions policy does not, by itself, establish who may assume the role.

### Example: EC2 instance role

1. A role has a trust policy that trusts the EC2 service.
2. An EC2 instance is associated with an instance profile containing that role.
3. The instance receives temporary credentials through the EC2 role credential mechanism.
4. Application code on the instance uses the AWS SDK credential provider chain.
5. The role's permissions policies determine which AWS API actions are allowed.

This is safer than placing static access keys in an EC2 environment, source code, or an application configuration file.

## 3. IAM policy structure

A policy document can contain one or more statements.

Illustrative identity-based permissions policy:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "ReadOneBucket",
      "Effect": "Allow",
      "Action": [
        "s3:ListBucket"
      ],
      "Resource": "arn:aws:s3:::example-training-bucket"
    },
    {
      "Sid": "ReadObjectsInOneBucket",
      "Effect": "Allow",
      "Action": [
        "s3:GetObject"
      ],
      "Resource": "arn:aws:s3:::example-training-bucket/*"
    }
  ]
}
```

| Element | Meaning |
|---|---|
| `Version` | Policy language version; commonly `2012-10-17` |
| `Statement` | Array of policy statements |
| `Sid` | Optional statement identifier |
| `Effect` | `Allow` or `Deny` |
| `Action` | API actions covered by the statement |
| `Resource` | Resources to which the statement applies |
| `Condition` | Optional conditions evaluated in the request context |
| `Principal` | Identifies the principal in policy types that specify one, such as resource-based policies and role trust policies |

**Important correction for exam reasoning:** `Principal` is not a required element in every IAM policy statement. Identity-based policies specify permissions for the identity to which they are attached and do not use a `Principal` element. Resource-based policies and trust policies use `Principal` to identify who is granted access or allowed to assume a role.

### Resource ARN precision

- `s3:ListBucket` is a bucket-level action and uses the bucket ARN.
- `s3:GetObject` is an object-level action and uses object ARNs, commonly ending in `/*`.
- The action and resource must match the service's authorization model.
- Avoid `Resource: "*"` when the action supports narrower resource scoping.

## 4. Policy types and permission evaluation

Know the purpose of these policy categories:

| Policy type | Purpose |
|---|---|
| Identity-based policy | Grants or denies permissions to an IAM identity |
| Resource-based policy | Specifies principals that can access a supported resource |
| Permissions boundary | Sets the maximum permissions an identity-based policy can grant to a user or role |
| Session policy | Restricts permissions for a role session or federated session |
| AWS Organizations SCP | Sets the maximum available permissions for principals in member accounts; it does not grant permissions |
| Role trust policy | Defines which principals can assume a role |

Core evaluation rules:

1. Requests are implicitly denied by default.
2. An applicable explicit Allow can grant access.
3. An applicable explicit Deny overrides an Allow.
4. Boundaries, session policies, Organizations policies, resource policies, and cross-account rules can affect the final decision.

Do not assume that any Allow anywhere automatically means access is granted. Identify the principal, action, resource, applicable conditions, account relationship, and limiting policies.

For cross-account role access, both sides matter: the role trust policy must trust the calling principal, and the caller must be allowed to call `sts:AssumeRole`. The resulting role session is then governed by the role's permissions and applicable session restrictions.

## 5. Authentication, authorization, and programmatic access

- **Authentication:** establishes which principal is making a request.
- **Authorization:** evaluates whether that principal may perform the requested action on the requested resource.

A successful `aws sts get-caller-identity` identifies the caller. It does not prove that the caller can invoke an arbitrary service API.

For programmatic access, understand the difference between:

- Long-term IAM user access keys.
- Temporary credentials issued through AWS STS.
- Federated access.
- Credentials supplied by an AWS compute service role.
- Credentials discovered by an SDK provider chain.

For applications running on EC2, Lambda, and other AWS compute services, prefer the service's role-based temporary credentials over static access keys.

## 6. Least privilege

Grant only the actions, resources, and conditions required for the task.

A practical least-privilege workflow:

1. Identify the exact application operation.
2. Map it to the required AWS API actions.
3. Scope each action to the narrowest supported resource ARN.
4. Add conditions when they provide meaningful restrictions.
5. Test the application with the intended role.
6. Review denied actions and add only justified permissions.
7. Reassess permissions as the application changes.

Avoid attaching broad administrative policies to application roles. Do not solve an `AccessDenied` error by reflexively granting `*`.

## 7. IAM security tools from the course

The course summary names two useful IAM visibility tools:

- **IAM Credential Report:** account-level report about IAM users and the status of their credentials. It supports credential hygiene reviews; it does not replace authorization analysis.
- **IAM Access Advisor:** shows service permissions information and last-accessed data for an IAM entity. It can help identify permissions that may be unnecessary, but last-accessed information must be interpreted carefully.

These are useful IAM administration and audit concepts. For DVA-C03, prioritize the developer tasks in the official exam guide rather than memorizing console navigation for every IAM report.

## 8. Root user and shared responsibility

### Root user

The root user is the original identity for an AWS account and has extensive privileges. Do not use it for routine development or application access.

Security practices include:

- Protect root credentials.
- Enable MFA for the root user.
- Do not create root access keys for routine programmatic access.
- Use appropriately scoped identities for everyday work.
- Keep root access for tasks that specifically require it.

The course slide's suggestion to use root to create the first IAM user is an oversimplification for modern workforce access. Prefer a federated administrative identity through IAM Identity Center where available, and follow current AWS account bootstrap guidance.

### Shared Responsibility Model

AWS is responsible for security **of** the cloud, including the physical infrastructure and underlying facilities.

Customers are responsible for security **in** the cloud, with responsibilities varying by service and deployment model. Customer responsibilities include identity configuration, credentials, data, application code, and the permissions they grant.

For example, AWS secures the physical infrastructure; the customer must protect IAM credentials and avoid granting excessive permissions.

## 9. Course review: what to retain and what to deepen

| Course review topic | Keep from the course | Required deeper understanding |
|---|---|---|
| Definition of an IAM role | Role is an IAM identity with permissions used by trusted entities | Trust policy, permissions policy, temporary credentials, EC2 instance roles |
| IAM security tools | Credential Report | What it reports and what it does not prove |
| IAM users | Own credentials; not root credentials | User vs role, federation, programmatic access |
| IAM best practice | Avoid root for daily work | MFA, federation, temporary credentials, least privilege |
| IAM policies | JSON permissions documents | Policy types, resource ARNs, conditions, evaluation |
| Least privilege | Grant only required permissions | Derive, test, and refine action/resource scope |
| User groups | Contain users only | Understand the model without overemphasizing administration |
| Policy statement fields | Effect, Action, Resource, optional fields | Principal is policy-type dependent; Version belongs to the policy document |
| Shared responsibility | AWS secures underlying infrastructure | Customer responsibility for identities, credentials, application and data |

## 10. Exam-style scenario practice

Answer before opening the explanations. These are original practice questions based on the official DVA-C03 objectives and the course topics; they are not copied exam questions.

### Question 1 — EC2 application credentials

An application running on an EC2 instance must read objects from one S3 bucket. The developer currently plans to store an IAM user's access key and secret key in an environment file on the instance.

What is the best approach?

A. Keep the access keys in the environment file and rotate them monthly.  
B. Attach an IAM role to the EC2 instance with narrowly scoped S3 read permissions.  
C. Use the AWS account root credentials because EC2 is an AWS service.  
D. Create a separate IAM user for every application process.

### Question 2 — Role trust

A role has a permissions policy allowing `s3:GetObject`, but an external AWS account cannot assume it.

Which role configuration must be examined first?

A. The S3 bucket lifecycle policy.  
B. The role trust policy and the caller's permission to invoke `sts:AssumeRole`.  
C. The IAM Credential Report.  
D. The EC2 security group.

### Question 3 — Explicit deny

A principal has an applicable Allow for an S3 action. Another applicable policy explicitly denies the same action on the requested object.

What is the expected result?

A. Allow, because an Allow exists.  
B. Allow, if the request uses the AWS CLI.  
C. Deny, because an applicable explicit Deny overrides an Allow.  
D. It depends only on the user's group membership.

### Question 4 — Policy document

Which statement about the `Principal` element is correct?

A. Every identity-based policy must include Principal.  
B. Principal is used in policy types that identify who receives access, such as resource-based policies and role trust policies.  
C. Principal defines the AWS Region.  
D. Principal is another name for Resource.

### Question 5 — Identity versus permission

A developer runs `aws sts get-caller-identity` successfully but receives `AccessDenied` when calling an AWS service API.

What does this indicate?

A. Authentication succeeded, but authorization for the service request was denied.  
B. The AWS CLI installation is necessarily corrupted.  
C. The account has been deleted.  
D. STS automatically grants access to all AWS services.

### Question 6 — Least privilege

A Lambda function needs to read records from one DynamoDB table. Which policy design best follows least privilege?

A. `dynamodb:*` on all resources.  
B. `*` on all AWS services.  
C. Only the required DynamoDB read actions on the specific table ARN.  
D. Attach AdministratorAccess and rely on application validation.

### Question 7 — Shared responsibility

Which item is AWS's responsibility under the Shared Responsibility Model?

A. Choosing the IAM permissions for the customer's application.  
B. Rotating the customer's IAM user access keys.  
C. Securing the physical infrastructure of AWS data centers.  
D. Deciding which employees should have access to customer data.

### Question 8 — Temporary credentials

Why are role-based temporary credentials preferred for applications running on AWS compute services?

A. They never expire.  
B. They remove the need to authorize API calls.  
C. They avoid embedding long-term access keys in the application and are delivered through the service's role credential mechanism.  
D. They grant administrator permissions automatically.

## Answer key and explanations

Do not read this section until you have attempted all questions.

1. **B** — An EC2 instance role supplies temporary credentials to the application. Scope the role to the required S3 actions and bucket/object ARNs.
2. **B** — The trust policy controls who can assume the role. Cross-account use also requires the caller to be authorized for `sts:AssumeRole`.
3. **C** — An applicable explicit Deny overrides an Allow.
4. **B** — Principal is not required in identity-based policies; it appears in policy types that specify the accessing principal.
5. **A** — STS identity confirmation is not proof of service authorization.
6. **C** — Restrict actions and resource scope to the application's actual needs.
7. **C** — AWS secures the physical infrastructure; customers secure their use of AWS.
8. **C** — Temporary role credentials reduce dependence on long-term static secrets. They still require appropriate permissions.

## Completion criteria

Do not mark this lesson complete until you can:

- Explain the difference between an IAM user, group, and role.
- Explain trust policy versus permissions policy without mixing their purposes.
- Read an IAM permissions policy and identify its actions, resources, and conditions.
- Explain implicit deny and explicit deny.
- Distinguish identity-based and resource-based policies.
- Explain why an EC2 application should use an instance role instead of embedded access keys.
- Diagnose why successful authentication can still lead to `AccessDenied`.
- Score at least 7 out of 8 on a fresh scenario quiz and explain why the distractors are wrong.

## Not covered by this lesson

This lesson does not complete the entire Security domain. Separate study is still required for:

- Presigned URLs.
- Encryption at rest and in transit, KMS, and certificates.
- Secrets Manager and sensitive-data handling.
- Security risks when integrating AI services.
- Practical STS role assumption and a least-privilege role lab.

## References

- [AWS DVA-C03 Exam Guide — official PDF](https://docs.aws.amazon.com/pdfs/aws-certification/latest/developer-associate-03/developer-associate-03.pdf)
- [AWS IAM User Guide](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html)
- [IAM best practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html)
- [IAM roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html)
- [Shared Responsibility Model](https://aws.amazon.com/compliance/shared-responsibility-model/)
