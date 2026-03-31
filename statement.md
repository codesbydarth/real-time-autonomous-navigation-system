# 📌 Project Statement

## 🧠 Problem Statement

In real-world delivery and navigation systems, finding the most efficient path is challenging due to dynamic conditions such as traffic, roadblocks, or moving obstacles. Traditional static pathfinding methods fail when the environment changes.

This project addresses the problem of **finding cost-efficient and time-efficient paths in a dynamic environment**, where obstacles may appear or move unpredictably.

---

## 🎯 Objective

The objective of this project is to design a system where an agent:

* Navigates from a start position to a goal
* Avoids both static and moving obstacles
* Dynamically replans its path when conditions change
* Compares different pathfinding strategies for efficiency

---

## 🛠️ Approach

### 1. Environment Modeling

A grid-based environment was created where:

* Each cell represents terrain
* Obstacles can block movement
* Some obstacles move dynamically

---

### 2. Pathfinding Algorithms

Three algorithms were implemented:

* **BFS** – Finds shortest path in terms of steps
* **UCS** – Finds least-cost path considering weights
* **A*** – Uses heuristics for efficient pathfinding

---

### 3. Dynamic Replanning

When a moving obstacle blocks the agent’s path:

* The system detects the blockage
* A new path is computed in real time
* The agent adapts without restarting

---

### 4. Performance Evaluation

Each algorithm is evaluated based on:

* Execution time
* Path cost
* Nodes expanded

---

### 5. Visualization

A Pygame-based interface was developed to:

* Display the grid environment
* Show agent movement
* Visualize paths and obstacles in real time

---

## ⚙️ Key Design Decisions

* Modular structure (Grid, Agent, Algorithms)
* Use of heuristics in A* for optimization
* Real-time simulation loop for dynamic behavior
* Separation of logic and visualization

---

## ⚠️ Challenges Faced

* Handling dynamic updates while maintaining correctness
* Ensuring efficient replanning without freezing the simulation
* Integrating visualization with algorithm logic
* Debugging synchronization between movement and rendering

---

## 📚 Learning Outcomes

* Deep understanding of search algorithms (BFS, UCS, A*)
* Experience with dynamic systems and real-time updates
* Improved problem-solving and debugging skills
* Exposure to simulation and visualization techniques

---

## 🚀 Conclusion

This project successfully demonstrates how classical pathfinding algorithms can be extended to handle dynamic environments. It highlights the importance of adaptability in real-world systems and provides a foundation for more advanced navigation systems.

---
