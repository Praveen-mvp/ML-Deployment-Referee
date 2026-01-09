# ML Deployment Referee

A **rule-based decision support tool** that helps engineers choose the
right **ML inference deployment strategy** by comparing multiple options
and clearly explaining their **trade-offs**.

This project is built as part of **AI for Bharat – Week 6: The Referee**.

---

## 🚩 Problem Statement

Selecting an ML inference deployment strategy is not straightforward.

Options like:

* PyTorch FP32
* Quantized PyTorch (INT8)
* ONNX Runtime
* TensorRT

all come with **different trade-offs** in terms of **latency, cost,
hardware dependency, and complexity**.

Most tutorials provide **one recommended solution**, but in reality:

> **There is no single best choice — the right decision depends on constraints.**

---

## 🎯 Solution: Referee-Based Approach

This project acts as a **referee**, not an opinionated advisor.

Instead of giving one answer, it:

* Compares **multiple deployment options**
* Explains **pros and cons**
* Highlights **trade-offs**
* Recommends the most suitable option **based on user inputs**

---

## 🧩 Deployment Options Compared

* **PyTorch FP32**
* **PyTorch INT8 (Quantized)**
* **ONNX Runtime**
* **TensorRT**

---

## 📝 User Inputs

The decision engine evaluates options based on:

* **Hardware**: CPU | GPU
* **Deployment Environment**: Cloud | Edge
* **Latency Priority**: Low | Medium | High
* **Cost Sensitivity**: Low | Medium | High

---

## ⚙️ Architecture Overview

* **Backend**: FastAPI (Python)
* **Decision Engine**: Rule-based logic
* **Frontend**: HTML + CSS + JavaScript
* **AI Assistance**: Kiro (used to design decision logic and trade-offs)

```
UI  →  FastAPI  →  Decision Engine  →  Comparison + Recommendation
```

---

## 🚀 How to Run Locally

### 1️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 2️⃣ Start the backend

```bash
uvicorn app.main:app
```

### 3️⃣ Open the UI

Open the following file in your browser:

```
ui/index.html
```

---

## 🎥 Demo Recording

A **screen recording** demonstrating:

* Kiro prompt and generated decision logic
* Backend API execution
* UI comparison results with recommendation

📁 Available in this repository:

```
screenshots/kiro-and-ui-demo.mp4
```

---

## 🤖 How Kiro Accelerated Development

Kiro played a key role in accelerating this project by:

* Generating structured **decision rules**
* Identifying **trade-offs** between inference runtimes
* Producing a clear comparison framework
* Reducing trial-and-error during design

The `.kiro` directory in this repository contains:

* Prompts used to generate the decision logic
* Kiro-generated analysis and outputs

This significantly reduced development time and improved clarity.

---

## ✅ Key Takeaway

There is **no one-size-fits-all ML deployment strategy**.

This tool helps engineers make **informed decisions**
by understanding **constraints, trade-offs, and outcomes** —
exactly what a *referee* is meant to do.

---

## 📌 Notes

* This project focuses on **decision-making**, not model training.
* All logic is intentionally **rule-based** for clarity and explainability.
* Designed for demonstration and learning purposes.
