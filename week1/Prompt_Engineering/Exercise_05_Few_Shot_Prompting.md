# Exercise 5 – Few-Shot Prompting

## Objective

To understand how providing a few examples in a prompt helps a Large Language Model (LLM) identify patterns and generate consistent responses.

---

## LLM Used

**Google Gemini (Web Version)**

---

## Prompt

```text
English : Cat

Hindi : बिल्ली

English : Dog

Hindi : कुत्ता

English : Car

Hindi :
```

---

## Response Summary

The model identified the translation pattern from the given examples and correctly translated **"Car"** into Hindi as **"गाड़ी"** (or **"कार"**). It continued the same format without requiring additional instructions.

---

## Prompt Engineering Technique Used

**Few-Shot Prompting**

---

## Observation

* The model recognized the translation pattern from the provided examples.
* It continued the sequence in the same format without any extra guidance.
* The generated translation was accurate and contextually correct.
* The response remained consistent with the examples given in the prompt.
* Providing examples helped the model understand the expected task and output style.

---

## Key Learning

This exercise demonstrated that **Few-Shot Prompting** improves the model's ability to understand patterns by learning from a small number of examples. It is especially useful for tasks such as translation, text classification, sentiment analysis, data extraction, and maintaining consistent output formats.

---

## Screenshot

![Exercise 5 Screenshot](screenshots/exercise_05.png)
