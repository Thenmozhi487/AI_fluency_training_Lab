\# Day 3 – From Prompt to Action: Understanding LLMs, Tools, and Agents



\## 1. Scenario



For this task, I selected a course-fee lookup scenario. The LLM was asked questions about course fees and simple numerical comparison. A course-fee lookup tool was provided to retrieve the stored fee of a course.



The courses used in this scenario are:



\- CS101 – ₹12,000

\- AI202 – ₹18,000

\- DS303 – ₹15,000



The purpose was to compare a plain LLM with an LLM-supported tool and observe how a tool affects correctness and reliability.



\## 2. What is an LLM?



A Large Language Model (LLM) is an AI model that understands and generates natural language. It can answer questions using the knowledge and reasoning available to it.



An LLM can handle questions such as simple comparisons, explanations, summarization, and general reasoning from its own knowledge. However, it may not know specific information that is not available in its knowledge or context. In such cases, it may guess, ask for more information, or refuse to answer.



In this experiment, the plain LLM correctly answered the question “Which is cheaper: ₹12,000 or ₹18,000?” However, it could not provide the specific fees for CS101 and DS303.



\## 3. What is an Agent?



An AI agent is a system in which an LLM can use tools or take actions to achieve a goal. A plain chat system mainly generates an answer, while an agent can decide when an external tool is required, use that tool, receive its result, and then produce a final answer.



In this experiment, the tool-enabled program allowed the LLM workflow to use the course-fee lookup function when a specific course fee was required.



\## 4. What is a Tool and a Tool Call?



A tool is an external function or capability that an LLM can use to obtain information or perform an operation.



A tool call is the action of requesting that tool to perform its function.



The tool used in this project is:



`get\_course\_fee(course)`



It receives a course name as a parameter and returns the corresponding course fee.



A tool schema tells the model important information about the tool, such as its name, what it does, and the parameters it expects. This information is needed so that the model can understand when and how the tool should be used.



\## 5. One Tool-Call Flow



The tool-call process in this project is:



1\. The user asks a question.

2\. The model determines whether the question needs the course-fee tool.

3\. If required, the tool is called with the course name.

4\. The tool returns the course fee.

5\. The result is provided to the LLM.

6\. The LLM produces the final answer.



For example, for “What is the current fee of CS101?”, the tool is called with `CS101`, and it returns `12000`. The final answer is then generated using this result.



\## 6. Why Should a Tool Return a Result on Failure?



A tool should return a readable result even when it cannot find the requested information instead of immediately stopping the program with an error.



For example, returning “Course not found” allows the program or LLM to understand what happened and respond appropriately. This makes the workflow easier to continue and understand.



\## 7. Comparison: Plain LLM vs Tool-Enabled LLM



| Criteria | Plain LLM | Tool-Enabled LLM |

|---|---|---|

| Source of answer | Own knowledge and reasoning | LLM reasoning plus tool result |

| Can it fetch or compute outside memory? | No external lookup in this experiment | Yes, using the provided tool |

| Reliability on factual/numeric questions | Can be uncertain about specific information | More reliable when the tool provides the required data |

| Transparency | The source of specific information may not be clear | Tool call and tool result can be observed |

| Speed/cost | Simple and generally faster | Additional tool execution adds a small amount of processing |



\## 8. Observations



\### Question 1: What is the current fee of CS101?



The plain LLM did not know the specific course fee and asked for the institution or program details.



The tool-enabled run correctly called `get\_course\_fee('CS101')`. The tool returned `12000`, and the final answer correctly stated that the CS101 fee is ₹12,000.



\### Question 2: Which is cheaper: ₹12,000 or ₹18,000?



The plain LLM correctly answered that ₹12,000 is cheaper than ₹18,000.



The tool-enabled run did not need to call the course-fee tool because the question could be answered directly by comparing the two numbers.



\### Question 3: What is the fee of DS303?



The plain LLM did not know the specific fee and asked for additional context.



The tool-enabled run correctly called `get\_course\_fee('DS303')`. The tool returned `15000`, and the final answer correctly stated that the DS303 fee is ₹15,000.



\## 9. Suitability and Conclusion



A plain LLM is suitable when the question can be answered using general knowledge or simple reasoning available from the given context. For example, comparing ₹12,000 and ₹18,000 did not require an external tool.



A single tool becomes necessary when the question depends on specific information that the LLM does not reliably know. In this experiment, the course fees for CS101 and DS303 required the course-fee lookup tool.



The experiment shows that tools can improve the reliability of an LLM workflow for specific factual or numerical information. The LLM can decide when a tool is useful, the tool provides the required result, and the LLM can use that result to produce the final response.

