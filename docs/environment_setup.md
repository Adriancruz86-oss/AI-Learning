# Environment Setup

## Purpose

This document explains how the AI-Learning project environment was created and configured.

The goal is to maintain a clean, repeatable development environment while learning Python, machine learning, and neural networks from the ground up.

---

# System Setup

## Operating System

macOS

## Development Tools

- Terminal
- Git
- GitHub
- Python
- Virtual Environment

---

# Python Virtual Environment

A virtual environment keeps this project isolated from other Python projects on the computer.

This prevents package conflicts and allows the project dependencies to be managed separately.

Create the environment:


python3 -m venv ai-learning
Activate the environment:
source ai-learning/bin/activate
When activated, the terminal displays:
(ai-learning)
This indicates that Python commands are running inside the project environment.
Installing Packages
Packages are installed using Python's package manager, pip.
Example:
python -m pip install package-name
Current and future AI development libraries include:
NumPy - numerical computing
Matplotlib - visualization
PyTorch - neural networks and machine learning
Requirements File
The requirements file records the packages and versions used by the project.
Create the file:
python -m pip freeze > requirements.txt
A new environment can install the same dependencies using:
python -m pip install -r requirements.txt
Git Setup
Git is used to track project changes and maintain version history.
Initialize the repository:
git init
Connect the local project to GitHub:
git remote add origin repository-url
Create a commit:
git add .
git commit -m "commit message"
Push changes to GitHub:
git push
Project Workflow
The development process for this project:
Create an experiment
Test the code
Document what was learned
Commit changes
Continue improving the project
Learning Goals
This project is focused on understanding the foundations of artificial intelligence.
Topics will include:
Python programming
Machine learning fundamentals
Neural networks
Weights and biases
Loss functions
Optimization
Backpropagation
PyTorch
AI experimentation
The goal is not only to use AI tools, but to understand how they work.
