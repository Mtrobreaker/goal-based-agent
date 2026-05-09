# 🎯 Goal-Based AI Agent

A real-world inspired **Goal-Based AI Agent** built using Python.

This project demonstrates how an AI agent can:

* Understand goals
* Generate action plans
* Track progress
* Maintain memory/state
* Persist data using JSON

---

# 🧠 What is a Goal-Based Agent?

A Goal-Based Agent is an AI system that:

> Makes decisions based on achieving a specific goal.

Unlike reflex agents that react immediately, goal-based agents:

* Think about objectives
* Create plans
* Execute step-by-step actions

---

# 🏗️ Architecture

```text
                +-------------------+
                |      User         |
                +---------+---------+
                          |
                          v
                +-------------------+
                |     main.py       |
                |  User Interface   |
                +---------+---------+
                          |
                          v
                +-------------------+
                |     agent.py      |
                |  Main Orchestrator|
                +---------+---------+
                          |
      +-------------------+-------------------+
      |                   |                   |
      v                   v                   v
+-------------+   +---------------+   +---------------+
| planner.py  |   |  memory.py    |   |task_manager.py|
| Goal Plans  |   | Current State |   | Progress Save |
+------+------+   +-------+-------+   +-------+-------+
       |                    |                   |
       v                    |                   v
+--------------+            |         +------------------+
|  goals.py    |            |         | progress.json    |
| Goal Library |            |         | Persistent Memory|
+--------------+            |         +------------------+
```

---

# 🔄 Execution Flow

```text
User Input
    ↓
main.py
    ↓
agent.py
    ↓
planner.py
    ↓
goals.py
    ↓
task_manager.py
    ↓
progress.json
    ↓
Response to User
```

---

# 📂 Project Structure

```text
goal-based-agent/
│
├── agent/
│   ├── goals.py
│   ├── planner.py
│   ├── memory.py
│   ├── task_manager.py
│   ├── processor.py
│   └── agent.py
│
├── data/
│   └── progress.json
│
├── main.py
├── README.md
└── .gitignore
```

---

# ⚙️ Features

✅ Goal Planning
✅ Task Generation
✅ Persistent Memory
✅ Progress Tracking
✅ Modular Architecture
✅ JSON-Based Storage

---

# 🧠 Components Explained

## 📋 goals.py

Stores predefined goals and their action steps.

Example:

```python
"become ai engineer": [
    "Learn Python",
    "Learn Machine Learning",
    "Build AI Projects"
]
```

---

## 🧠 planner.py

Generates execution plans for goals.

---

## 💾 memory.py

Stores current active goal in memory.

---

## 📊 task_manager.py

Handles:

* saving progress
* loading progress
* persistence using JSON

---

## 🤖 agent.py

Main decision-making system.

Controls:

* planning
* memory
* task execution
* progress tracking

---

# 🚀 How to Run

## 1️⃣ Create Virtual Environment

```bash
python -m venv venv
```

---

## 2️⃣ Activate Environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / Mac

```bash
source venv/bin/activate
```

---

## 3️⃣ Run Agent

```bash
python main.py
```

---

# 🧪 Example Usage

## Set Goal

```text
goal: become ai engineer
```

---

## Check Progress

```text
progress
```

---

# 📁 Example progress.json

```json
{
    "become ai engineer": [
        "Learn Python",
        "Learn Data Structures"
    ]
}
```

---

# 🧠 Concepts Learned

This project teaches:

* Goal-Based AI Architecture
* State Management
* Planning Systems
* Persistent Memory
* Modular Software Design
* File-Based Data Storage

---

# 🔥 Real-World Relevance

This architecture is similar to concepts used in:

* AI Assistants
* Workflow Agents
* Autonomous Systems
* AI Task Planners
* Personal Productivity Agents

---

# ⚠️ Current Limitations

* Uses predefined goals
* No dynamic reasoning
* No LLM integration yet
* No API/tool usage

---

# 🚀 Future Improvements

* Add LLM integration
* Dynamic planning
* Vector database memory
* Tool usage
* Autonomous execution
* Multi-agent collaboration

---

# 👨‍💻 Author

Built while learning AI Agent Architectures step-by-step using Python.
