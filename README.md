# Geometry Engine – Python 3D Data Processing & Filtering
This project is a lightweight Python geometry engine focused on
**processing, filtering, and validating 3D (XYZ) point data**
using clean, deterministic logic.
It started as a geometry / collision demo project and evolved into
a **practical data-processing tool** for real-world use cases where
raw spatial data must be validated or filtered before further processing.
---
## Core idea
Many systems work with raw 3D data, but most problems do not require
full physics engines or complex frameworks.
This project demonstrates how:
- geometric rules
- spatial constraints
- simple collision or containment logic
can be implemented in a **clear, reusable, and testable way**
using plain Python.
---
## What problem does this solve?
Raw 3D point data often contains:
- unnecessary points
- out-of-range measurements
- invalid or noisy data
Before using the data in:
- simulations
- 3D modeling / scanning workflows
- robotics
- measurement preprocessing
- AI / ML pipeline
it must be **filtered and validated**.
This tool provides simple building blocks to:
- check whether points fall inside a defined region
- filter point sets based on geometric rules
- export clean datasets for further processing
---
## Project structure
- `point_filter_service.py`  
  Main service script:
  - loads CSV input
  - applies geometric filtering rules
  - prints a clear data summary
  - exports filtered CSV output
- `geometry.py` / `collision.py`  
  Reusable geometry helpers:
  - distance checks
  - containment logic
  - simple collision-style rules
- `demo.py`  
  Geometry / collision demo (sphere–sphere, box–box, etc.)
- `demo_filter.py`  
  Minimal example of point filtering usage
- `input_points.csv`  
  Example input dataset (XYZ points)
---
## How to run
### Option A – CSV-based point filtering
1) Place your input data in `input_points.csv`
2) Run:
```bash
python point_filter_service.py