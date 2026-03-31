# 🚀 Real-Time Autonomous Navigation System

## 📌 Overview

This project simulates an autonomous delivery agent navigating a grid-based environment using pathfinding algorithms. The system incorporates both **static and dynamic obstacles**, allowing the agent to **adapt and replan its path in real time**.

The goal is to demonstrate how different search algorithms perform in realistic, changing environments.

---

## 🧠 Features

* 📍 Grid-based environment with customizable size
* 🚧 Static and dynamic (moving) obstacles
* 🤖 Agent capable of real-time path planning and replanning
* 🔍 Implementation of:

  * Breadth-First Search (BFS)
  * Uniform Cost Search (UCS)
  * A* Search (with heuristic)
* 📊 Performance comparison:

  * Execution time
  * Path cost
  * Nodes expanded
* 🎮 Interactive visualization using **Pygame**

---

## 🏗️ Project Structure

```
.
real-time-autonomous-navigation-system/
│
├── agent_pathfinding_env.py   # Core logic (grid, agent, algorithms)
├── pygame_ui.py               # Visualization (Pygame)
├── main.py                    # Runs experiments + simulation
│
├── README.md                  # Project explanation
├── statement.md               # Problem + approach
├── project-report.pdf         # Final report
│
├── requirements.txt           # Dependencies
└── requirements.md            # Dependencies
```
---

## ⚙️ Installation & Setup

### 1. Clone the repository

```
git clone <your-repo-link>
cd <repo-folder>
```

### 2. Install dependencies

```
pip install numpy pandas matplotlib seaborn pygame
```

### 3. Run the project

```
python main.py
```

---

## 🎮 How It Works

1. The system generates multiple maps (small, medium, large)
2. Each algorithm (BFS, UCS, A*) is tested on these maps
3. Performance metrics are recorded and visualized
4. A dynamic simulation runs where:

   * Obstacles move
   * The agent replans its path when blocked
5. A Pygame window shows real-time navigation

---

## 📊 Output

* Console logs for simulation steps
* Graphs comparing algorithm performance
* Real-time visualization of agent movement

---

## 🧪 Example Use Case

Simulating delivery routing where:

* Roads may be blocked
* Conditions change dynamically
* The system must adapt and find efficient paths

---

## 📚 Technologies Used

* Python 3
* NumPy
* Pandas
* Matplotlib
* Seaborn
* Pygame

---

## 🔮 Future Improvements

* Implement advanced algorithms like D* Lite
* Add multiple agents with collision avoidance
* Create a web-based dashboard
* Improve obstacle intelligence (AI-driven movement)

---

## 👨‍💻 Author

     Siddharth Sharma | 25BCE10977
     B. Tech CSE Core | First Year
     VIT Bhopal University
Developed as part of the **Bring Your Own Project (BYOP)**.


---
