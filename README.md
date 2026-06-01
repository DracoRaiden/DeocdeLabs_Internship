# Rule-Based AI Chatbot

**DecodeLabs | Artificial Intelligence - Project 1**

## Overview
This project is a foundational "White Box" logic engine designed to act as a deterministic guardrail for AI systems. Before introducing the probabilistic nature of Large Language Models (LLMs), this chatbot establishes strict control flow and logic through explicit programmatic decision-making.

## Architecture
The chatbot operates on the **IPO (Input-Process-Output)** model:
1. **Input & Sanitization:** Captures raw user input and normalizes it (handling casing and whitespace) to ensure reliable data flow.
2. **Process (The Logic Skeleton):** Utilizes an O(1) Hash Map (Dictionary) for intent matching, completely avoiding the technical debt of linear `if-elif` ladders.
3. **Output:** Returns the exact hardcoded response or cleanly falls back to a default message using atomic operations (`.get()`).

## Features
* **Infinite Heartbeat:** Runs in a continuous cycle until a strict kill command (`exit`) is issued.
* **Deterministic Guardrails:** Zero hallucination risk; 100% hardcoded, rule-based responses ensuring safety and traceability.
* **Algorithmic Efficiency:** Employs key-value pair dictionaries for instant lookups regardless of rulebase scale.
* **Atomic Fallback:** Gracefully handles unknown inputs without system failure or cascading logic errors.

## Usage
Run the script via your Python environment:
