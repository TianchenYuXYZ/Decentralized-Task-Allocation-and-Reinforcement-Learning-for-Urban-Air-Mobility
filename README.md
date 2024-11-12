# Decentralized Task Allocation and Reinforcement Learning for Urban Air Mobility

This repository contains the code and simulations for a project focused on optimizing takeoff and landing operations in Urban Air Mobility (UAM) through decentralized task allocation and reinforcement learning techniques. The primary use case involves unmanned aerial vehicles (UAVs) like drone taxis, aimed at achieving efficient and autonomous operation in urban environments.

# Project Demo
<video src="demo.mp4" controls="controls" style="max-width: 100%; height: auto;">
    Your browser does not support the video tag.
</video>


## Project Overview

This project utilizes **Microsoft AirSim** with **Unreal Engine 4** to create a 3D simulation environment where UAVs perform landing, takeoff, and path optimization tasks. The following two approaches were implemented and evaluated:

- **Decentralized Task Allocation**: We explored and implemented algorithms, such as the **Consensus-Based Bundle Algorithm (CBBA)**, to assign tasks across UAVs. This approach improves coordination, minimizes travel distance, and prevents collisions by enabling each UAV to make task assignment decisions independently.

- **Reinforcement Learning**: Multiple reinforcement learning models, including **Deep Q-Network (DQN)**, **Logical Team Q-Learning (LTQL)**, and **Deep Deterministic Policy Gradient (DDPG)**, were trained to navigate complex scenarios, avoid obstacles, and optimize paths for takeoff and landing.

## Key Features

- **3D Simulation Environment**: Built using Microsoft AirSim and Unreal Engine 4.
- **Decentralized Algorithms**: Implemented and tested CBBA and other decentralized task allocation methods for multi-agent coordination.
- **Reinforcement Learning Models**: Developed and trained models for collision avoidance and optimal pathfinding.
- **Performance Optimization**: Focused on real-time operations in dynamic and unpredictable urban environments, supporting high UAV autonomy.

## Objective

This project aims to contribute to the development of safe and efficient UAM systems by combining decentralized task allocation techniques with adaptive reinforcement learning models, enabling UAVs to operate autonomously within complex urban airspace.
