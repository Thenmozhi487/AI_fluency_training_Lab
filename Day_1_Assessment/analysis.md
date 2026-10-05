# Comparing a Plain Chatbot, a Rule-Based Workflow, and an AI Agent

## 1. Scenario and Problem

The scenario chosen for this assessment is a Student Course and Fee Assistant. The assistant needs to answer questions about private student and course information.

The private data contains the student name, department, course fees, and scholarship information. The course fees are CS101 = ₹12,000, AI202 = ₹18,000, and DS303 = ₹15,000. The Merit Scholarship provides a 10% discount.

The question used for testing is: "What is my CS101 fee and what is the fee after my 10% merit scholarship?"

---

## 2. Plain Chatbot

The plain chatbot mainly uses an LLM to understand the user's question and generate a response. It does not have access to the private data file used in this scenario.

When the user asks for the CS101 fee and the discounted fee, the chatbot cannot provide the exact answer because the private course fee is not available to it. It asks the user to provide the original CS101 fee.

Therefore, a plain chatbot is useful for general conversations and explanations, but it is not suitable when the answer requires access to private data.

---

## 3. Rule-Based Workflow

The rule-based workflow follows predefined steps and conditions. It does not use an LLM to make decisions.

In this scenario, the workflow checks the question for predefined course names and conditions. When it detects CS101 and the 10% scholarship condition, it uses the predefined fee of ₹12,000 and calculates the discount.

The calculation is:

CS101 fee = ₹12,000

10% discount = ₹1,200

Final fee = ₹12,000 - ₹1,200 = ₹10,800

The rule-based workflow gives a reliable answer for the predefined case. However, it is less flexible because new types of questions require new rules to be added.

---

## 4. AI Agent

An AI agent combines an LLM, tools, and a loop. The agent can use a tool to access information and then use the returned information to continue processing the request.

In this scenario, the AI agent uses a private-data tool to read the private college data. It then observes the returned data and uses the LLM to generate the final answer.

The agent follows these steps:

1. Receive and understand the user's question.
2. Use the private-data tool.
3. Observe the private data returned by the tool.
4. Process the information and generate the answer.

For the given question, the CS101 fee is ₹12,000 and the fee after the 10% Merit Scholarship is ₹10,800.

This makes the AI agent more flexible for questions that require private data and multiple processing steps.

---

## 5. Comparison

| Feature | Plain Chatbot | Rule-Based Workflow | AI Agent |
|---|---|---|---|
| Flexibility | Medium | Low | High |
| Decision-making | Limited to language generation | Based on predefined conditions | Context-based |
| Tool usage | No tool usage | Uses predefined data/rules | Uses tools to obtain information |
| Private-data access | No | Yes | Yes through a tool |
| Multi-step task handling | Limited | Predefined steps only | Stronger multi-step handling |
| Automation | Low | High for fixed cases | High |
| Reliability | Moderate for general responses | High for covered cases | Depends on LLM and tools |

---

## 6. Suitability Analysis

For a simple and fixed fee calculation, the rule-based workflow is suitable because the conditions are known in advance and the result is predictable. It provides a reliable answer when the question matches the predefined rules.

The plain chatbot is not suitable for this scenario because it cannot access the private course data. It would require the user to provide the missing information.

The AI agent is more suitable when the student may ask different types of questions that require private data, multiple steps, or different tools. It provides more flexibility than a fixed rule-based workflow.

Therefore, the best approach depends on the complexity of the task. For a small fixed task, a rule-based workflow can be sufficient. For more varied and multi-step tasks, an AI agent is more suitable.

---

## 7. General Conclusion

A plain chatbot, a rule-based workflow, and an AI agent can solve problems in different ways. A plain chatbot mainly depends on an LLM and is useful for general conversations. A rule-based workflow follows predefined rules and is reliable for known cases. An AI agent combines an LLM with tools and a loop to handle tasks that require information access and multiple steps.

For the Student Course and Fee Assistant scenario, the rule-based workflow works well for the fixed fee calculation, while the AI agent provides greater flexibility for more complex student requests. The comparison shows that the choice of approach should depend on the required flexibility, private-data access, multi-step handling, automation, and reliability.