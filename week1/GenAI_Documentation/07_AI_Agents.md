# 07 – AI Agents

## What are AI Agents?

An **AI Agent** is an intelligent system that can understand a goal, make decisions, use external tools, and perform multiple steps to complete a task.

Unlike a traditional LLM, which only generates responses, an AI Agent can plan, take actions, observe results, and adjust its approach until the task is completed.

---

## How are AI Agents Different from LLMs?

| Large Language Model (LLM) | AI Agent                         |
| -------------------------- | -------------------------------- |
| Answers questions          | Completes tasks                  |
| Generates text             | Plans and takes actions          |
| Responds to prompts        | Can use external tools           |
| Limited to conversation    | Can perform multi-step workflows |

---

## How Does an AI Agent Work?

```text
User Goal
     │
     ▼
Reason & Plan
     │
     ▼
Use Tools (APIs, Search, Database, etc.)
     │
     ▼
Observe Results
     │
     ▼
Generate Final Response
```

---

## Example

Suppose a user asks:

> "Find the cheapest flight from Delhi to Mumbai and summarize the best options."

An AI Agent can:

1. Search flight websites.
2. Compare available options.
3. Identify the lowest fares.
4. Summarize the results for the user.

A traditional LLM alone cannot perform these actions without access to external tools.

---

## Components of an AI Agent

* **Goal:** The task to be completed.
* **Reasoning:** Plans how to solve the task.
* **Tools:** Uses external services such as APIs, databases, or web search.
* **Memory:** Stores relevant information during the workflow.
* **Response:** Generates the final answer after completing the required steps.

---

## Applications

* Personal AI Assistants
* Customer Support Automation
* Travel Planning
* Research Assistants
* Software Development
* Business Process Automation

---

## Popular AI Agent Frameworks

| Framework     | Purpose                                                    |
| ------------- | ---------------------------------------------------------- |
| **LangGraph** | Builds stateful AI agent workflows                         |
| **CrewAI**    | Enables multiple AI agents to collaborate on complex tasks |

---

## Advantages

* Automates multi-step tasks
* Uses external tools and APIs
* Can make decisions based on available information
* Improves productivity and efficiency

---

## Limitations

* Depends on the quality of available tools and data.
* More complex than traditional chatbot applications.
* May require additional safeguards for sensitive or high-risk tasks.

---

## Key Takeaways

* AI Agents go beyond answering questions by performing actions.
* They combine reasoning, planning, memory, and tool usage.
* Frameworks such as LangGraph and CrewAI simplify the development of AI Agents.
* AI Agents are widely used for automation and intelligent decision-making.

---

## Summary

AI Agents extend the capabilities of Large Language Models by enabling them to reason, plan, use external tools, and complete multi-step tasks. They are becoming an important component of modern AI applications, supporting automation across domains such as customer service, software development, research, and business operations.
