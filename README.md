# 🚑 Rapid Route: Smart Emergency Traffic Clearance System

## 📌 Overview

Rapid Route is an AI-driven traffic management system designed to reduce ambulance response time by dynamically clearing traffic using intelligent signal control and route optimization.

The system is implemented using **SUMO (Simulation of Urban Mobility)** and Python (TraCI), demonstrating how emergency vehicles can be prioritized in real-time traffic scenarios.

---

## 🎯 Problem Statement

Traffic congestion delays emergency vehicles, increasing mortality risk. Even a few minutes delay can significantly impact survival rates.

---

## 💡 Solution

Our system introduces:

- 🚦 Dynamic Traffic Signal Control (Green Wave)
- 🧠 Rolling Horizon Optimization
- 🚑 Emergency Vehicle Priority Routing
- 📊 Performance Evaluation using Simulation

---

## ⚙️ Features

- 🚗 Simulated traffic with multiple vehicles
- 🚑 High-priority ambulance vehicle
- 🚦 Automatic signal switching when ambulance approaches
- 🔄 Real-time decision making (Rolling Horizon)
- 📈 Travel time and waiting time comparison

---

## 🧰 Tech Stack

- **SUMO** – Traffic simulation
- **Python (TraCI)** – Simulation control
- **NumPy** – Computation
- **Matplotlib** – Visualization

---

## 📁 Project Structure




---

## 🚀 How It Works

### Step 1: Simulation Setup
- Load network and vehicle routes in SUMO

### Step 2: Ambulance Detection
- Identify ambulance using unique ID (`ambulance1`)

### Step 3: Dynamic Bubble Logic
- If ambulance is within a certain radius of a signal:
  - Signal turns green for ambulance direction
  - Other directions are blocked

### Step 4: Rolling Horizon Optimization
- System recalculates decisions every few seconds
- Adapts to real-time traffic changes

---

## 🧠 Optimization Techniques (Simplified)

### 🔹 Rolling Horizon
- Continuously re-optimizes signal control in short intervals

### 🔹 Route Selection (ACO-inspired)
- Chooses fastest route based on traffic conditions

### 🔹 Signal Timing Optimization (PSO-inspired)
- Adjusts signal timings to minimize ambulance delay

---

## 📊 Evaluation

We compare two scenarios:

| Metric              | Normal Traffic | Optimized System |
|--------------------|--------------|-----------------|
| Travel Time        | High         | Reduced         |
| Waiting Time       | High         | Low             |
| Signal Delay       | Significant  | Minimal         |

---

## ▶️ How to Run

### 1️⃣ Install Dependencies

```bash
pip install traci numpy matplotlib
sumo-gui -c simulation.sumocfg
python main.py
