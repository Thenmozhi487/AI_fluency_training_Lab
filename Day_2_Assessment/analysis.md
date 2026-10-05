# Day 2 Assessment
## Reasoning and Acting: Comparing Direct Prompting, Chain-of-Thought, and ReAct

## 1. Scenario

The scenario compares the cost of two course options using different scholarship percentages.

The course fees are:

- CS101 = ₹12,000
- AI202 = ₹18,000
- DS303 = ₹15,000

The first question is:

Which is cheaper?

1. CS101 and AI202 with a 10% scholarship
2. All three courses with a 25% scholarship

The second reasoning question used for self-consistency is:

If a 15% scholarship is applied to the total cost of all three courses and the remaining amount is paid in 4 equal instalments, how much is each instalment?

---

## 2. Direct Prompting

Direct prompting asks the model to answer the question directly using its available knowledge.

In this experiment, the model received the course fees and calculated both scholarship options without using any external tool.

The result was:

- CS101 + AI202 with 10% scholarship = ₹27,000
- All three courses with 25% scholarship = ₹33,750
- Difference = ₹6,750

Therefore, the first option is cheaper by ₹6,750.

Direct prompting is simple and fast. It is suitable when all required information is already available in the prompt and the problem does not require external information or tools.

---

## 3. Chain-of-Thought

Chain-of-Thought prompting asks the model to solve a problem through multiple reasoning steps.

For the scholarship problem, the model calculated:

CS101 + AI202:

₹12,000 + ₹18,000 = ₹30,000

After 10% scholarship:

₹30,000 - ₹3,000 = ₹27,000

All three courses:

₹12,000 + ₹18,000 + ₹15,000 = ₹45,000

After 25% scholarship:

₹45,000 - ₹11,250 = ₹33,750

Difference:

₹33,750 - ₹27,000 = ₹6,750

The result was correct.

Chain-of-Thought is useful for multi-step reasoning because it makes the important calculation steps easier to understand. However, it cannot obtain information that is not available to the model unless an external tool is provided.

---

## 4. ReAct

ReAct combines reasoning with actions and observations.

The ReAct experiment used two tools:

- `get_course_fee()` to retrieve course fees
- `calculate_discount()` to calculate discounted prices

The process followed the cycle:

**Thought → Action → Observation → Thought → Action → Observation → Final Answer**

First, the agent identified that it needed the fees of CS101, AI202 and DS303.

It then used the course-fee tool and observed:

- CS101 = ₹12,000
- AI202 = ₹18,000
- DS303 = ₹15,000

Next, it calculated the two scholarship options.

The results were:

- Option 1 = ₹27,000
- Option 2 = ₹33,750

The final difference was ₹6,750.

ReAct is useful when a problem requires external information or tools. It can interact with tools, observe their results, and continue reasoning based on those observations.

---

## 5. Comparison

| Aspect | Direct Prompting | Chain-of-Thought | ReAct |
|---|---|---|---|
| Reasoning depth | Low | Higher for multi-step problems | Higher with iterative reasoning |
| Tool usage | No | No | Yes |
| Reliability on multi-step questions | Moderate | Better for multi-step calculations | Better when external information is required |
| Transparency | Simple answer | Shows important reasoning steps | Shows Thought, Action and Observation |
| Speed/cost | Fast and low cost | More reasoning, so potentially slower | More steps and tool calls, so potentially slower |
| Consistency across repeated runs | Usually consistent for simple problems | Can vary with non-zero temperature | Depends on reasoning and tool results |

---

## 6. Self-Consistency

A reasoning question was run five times using a non-zero temperature of 0.7.

The question was:

Three courses cost ₹12,000, ₹18,000 and ₹15,000. If a 15% scholarship is applied to the total cost and the remaining amount is paid in 4 equal instalments, how much is each instalment?

All five runs produced the same answer:

**₹9,562.50**

The majority answer was therefore:

**₹9,562.50**

This answer was correct.

The same question was then run with temperature 0. The result was also:

**₹9,562.50**

This experiment showed that the model was consistent for this particular calculation even when the temperature was increased to 0.7.

---

## 7. Suitability of Each Approach

Direct prompting is suitable for simple questions where all the required information is already provided and only a direct answer is needed.

Chain-of-Thought is suitable for problems that require multiple reasoning or calculation steps. It can make the important steps easier to understand.

ReAct is more suitable when the problem requires external information, tools, or repeated interaction with an environment. The agent can retrieve information through tools and use the observations to continue solving the problem.

For the selected scenario, Direct Prompting and Chain-of-Thought were sufficient because the course fees were already provided. ReAct demonstrated an additional advantage because it retrieved the course fees through tools before performing the calculations.

---

## 8. Conclusion

Different approaches are useful for different types of problems.

Direct prompting is appropriate for simple questions that can be answered directly from the information provided.

Chain-of-Thought is useful for multi-step reasoning and calculation problems.

ReAct is useful when reasoning must be combined with external information or tools.

Therefore, the best approach depends on the problem requirements. If no external information is required, direct prompting or Chain-of-Thought may be sufficient. If tools or external information are required, ReAct is more suitable.