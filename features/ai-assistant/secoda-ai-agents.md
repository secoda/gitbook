---
description: >-
  Turn your most valuable AI conversations into scheduled insights. Convert
  useful Secoda AI prompts into agents that run automatically and deliver
  results directly to your inbox.
---

# Secoda AI Agents

### Overview

Agents let you schedule recurring runs of your most useful Secoda AI conversations. When you have a productive chat with Secoda AI and get valuable insights, you can convert that specific prompt into an agent that runs on your preferred schedule - daily, weekly, or with custom cron timing. They leverage Secoda's full multi-agent system and tools under the hood, giving you the same powerful analysis capabilities on autopilot.

You can access agents in the Secoda AI chat interface by selecting the Agents tab.

<figure><img src="https://secoda-public-media-assets.s3.amazonaws.com/adb1f36b-2ecf-445a-9f86-db6cec6a9e26.png" alt=""><figcaption></figcaption></figure>

### How It Works

#### 1. **Create Your Agent**

Start by creating an agent in one of two ways:

* **Custom Agent**: Build from scratch with complete flexibility
* **Template**: Choose from pre-built templates for common use cases

<figure><img src="https://secoda-public-media-assets.s3.amazonaws.com/897d93bb-f0ef-4cd1-8cff-9a0b6b9a76f9.png" alt=""><figcaption></figcaption></figure>

#### 2. **Configure Your Agent**

Set up your agent with:

* **Agent name**: A descriptive title for your agent
* **Persona**: Choose from available AI personas&#x20;
* **Prompt**: Write the specific analysis or task you want automated
* **Schedule**: Set cron-based scheduling (minimum 1-hour intervals)
* **Web search**: Enable external documentation research when relevant

<figure><img src="https://secoda-public-media-assets.s3.amazonaws.com/190fbf09-ea46-459c-b2a5-a009182ecde3.png" alt=""><figcaption></figcaption></figure>

#### 3. **Schedule & Monitor**

Your agent runs automatically according to your schedule. View execution history, run status, and manually trigger runs when needed.&#x20;

<figure><img src="https://secoda-public-media-assets.s3.amazonaws.com/5af816f4-d889-4120-92be-ecb20da54298.png" alt=""><figcaption></figcaption></figure>

#### 4. **Get Results**

Each agent run creates a new conversation with the results. Access completed runs through the agent's run history or your AI chat history.

### What Agents Can Do

Agents can automate any analysis or task that Secoda AI currently handles in conversations, powered by the same multi-agent system including:

#### **Data Discovery & Analysis**

* Search across tables, columns, charts, dashboards, and documentation
* Analyze data quality patterns and identify issues
* Track resource usage and access patterns
* Monitor schema changes and data freshness

#### **Query Analysis & Performance**

* Analyze SQL query execution history and performance
* Identify slow or expensive queries
* Track query usage patterns and optimization opportunities
* Monitor database performance trends

#### **Automation & Monitoring Insights**

* Review automation configurations and effectiveness
* Analyze automation triggers and actions
* Monitor automation run patterns and success rates
* Identify opportunities for process improvement

#### **Policy & Governance**

* Track policy compliance and coverage
* Monitor data access patterns
* Identify governance gaps and recommendations
* Analyze policy effectiveness and usage

#### **Documentation & Knowledge**

* Find resources missing descriptions or ownership
* Track documentation coverage and quality
* Suggest improvements to resource discoverability
* Identify knowledge sharing opportunities

_Note: Agents execute the same AI analysis you'd get in a live conversation, leveraging Secoda's specialized agents for search, query analysis, automation monitoring, and policy review._

#### **Example Use Cases**

**Weekly Data Quality Check**

```
Agent: "Data Quality Monitor"
Persona: Data Steward
Prompt: "Show me all tables that haven't been updated in the last week and identify any that might have data quality issues. Focus on tables in our production schema."
Schedule: 0 9 * * 1 (Every Monday at 9 AM)
```

**Daily Query Performance Review**

```
Agent: "Query Performance Monitor" 
Persona: Data Engineer
Prompt: "Identify the top 10 slowest queries from yesterday and analyze any performance bottlenecks or optimization opportunities."
Schedule: 0 8 * * * (Daily at 8 AM)
```

**Monthly Governance Audit**

```
Agent: "Governance Compliance Check"
Persona: Data Steward  
Prompt: "Find tables containing potential PII that don't have proper governance tags or ownership assigned."
Schedule: 0 9 1 * * (First day of month at 9 AM)
```

**Automation Health Check**

```
Agent: "Automation Monitor"
Persona: Data Engineer
Prompt: "Review all automation runs from the past week and identify any that are failing consistently or need attention."
Schedule: 0 17 * * 5 (Friday at 5 PM)
```

### Frequently Asked Questions

**Q: How often can agents run?** A: Minimum interval is 1 hour. You can schedule daily, weekly, monthly, or any custom interval using cron expressions.

**Q: What happens if an agent fails?** A: Failed runs appear in the run history with error status. The agent continues with its next scheduled run as normal.

**Q: Can I share agent results with my team?** A: Agent results are AI conversations that can be shared like any other chat conversation in Secoda.

**Q: Do agents count against my AI usage?** A: Yes, agent executions use AI credits the same as interactive conversations.

**Q: Can agents create or modify data?** A: No, agents are read-only. They can only analyze and report on existing data and metadata.

**Q: What's the difference between agents and automations?** A: Agents perform AI analysis and create reports. Automations make changes to metadata like tags, descriptions, and assignments.

