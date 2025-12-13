# Geometry Engine - Python 3d data Processing
This project is a lightweight Python geometry engine focused on **processing and filtering 3D (XYZ) point data** using clean, deterministic logic. 
The goal of the project is to demostrate how spatial rules (distance, containment, collision zone) can be implemented in a **clear, reusable, and testable way** - without unnecessary complexity.
---
## What problem does this solve?
Many systems work with 3D point data:
- simulations
- 3D modeling
- robotics
- measurement preprocessing
- AI input preparation
This engine provides simple building blocks to:
- check whether points fall inside a defined spatial region
- validate spatial constraints befor further processing or decision logic
---
## Project structure
-  `belul_fuggveny.py` - code geometry filtering logic
- `demo_filter.py` - example: filtering XYZ point data by distance
- `demo.py` - example: basic 3D collision checks
---
## Status
This project is internationally small and focused.
It serves as a clean reference implementation for geometry-based data filtering and validation  in Python. 