# Exercise 6 – Code Generation Prompting

## Objective

To understand how providing detailed instructions in a prompt helps a Large Language Model (LLM) generate well-structured code along with explanations and complexity analysis.

---

## LLM Used

**Google Gemini (Web Version)**

---

## Prompt

```text id="w82krb"
You are a senior Python developer.

Write a Python program to find the factorial of a number.

Explain every line.

Mention time complexity.

Mention space complexity.
```

---

## Response Summary

The model generated a clean and efficient Python program to calculate the factorial of a number using an iterative approach. It also explained each line of the code in detail, described why the iterative method was preferred over recursion, and included both time complexity and space complexity analysis.

---

## Prompt Engineering Technique Used

**Code Generation Prompting**

---

## Observation

* The model generated syntactically correct and executable Python code.
* It followed all the instructions provided in the prompt.
* Every line of the program was explained clearly.
* The response included both time complexity (**O(n)**) and space complexity (**O(1)**).
* The model also explained why the iterative approach is preferred over the recursive approach for larger inputs, making the response more informative.

---

## Key Learning

This exercise demonstrated that detailed prompts help an LLM generate high-quality code along with meaningful explanations. By specifying the role, programming language, explanation requirements, and complexity analysis, the response became more educational and suitable for learning, documentation, and interview preparation.

---

## Screenshot

![Exercise 6 Screenshot](screenshots/exercise_06_a.png and screenshots/exercise_06_b.png and screenshots/exercise_06_c.png )
