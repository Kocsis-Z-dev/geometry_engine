"""
Point Filter Service
--------------------
Simple, deterministic 3D (XYZ) point filtering service.
Supports CSV imput and CSV output.
"""
from typing import List, Tuple
from pathlib import Path
import csv
Point3D = Tuple[float, float, float]
Points = List[Point3D]
FILTER_CONFIG = {"min_x": 2.0, "max_x": 8.0, "min_y": 2.0, "max_y": 8.0, "min_z": 4.0, "max_z":9.0}
def load_samlpe_points() -> Points:
    return [(1.0, 2.0, 3.0), (4.0, 5.0, 6.0), (7.0, 8.0, 9.0), (10.0, 10.0, 10.0), (3.0, 3.0, 3.0),]
def load_points_from_csv(csv_path: str) -> Points:
    points: Points = []
    path = Path(csv_path)
    with path.open("r", newline="", encoding="utf-8") as file:
        reader = csv.reader(file)
        for row in reader:
            if not row:
                continue
            if row[0].strip().lower() == "x":
                continue
            x =float(row[0])
            y =float(row[1])
            z =float(row[2])
            points.append((x, y, z))
        return points
def filter_points(points: Points, min_x: float, max_x: float, min_y: float, max_y: float, min_z: float, max_z: float,) -> Points:
    filtered: Points = []
    for x, y, z in points:
        if (min_x <= x <= max_x and min_y <= y <= max_y and min_z <= max_z):
            filtered.append((x, y, z))
    return filtered
def save_points_to_csv(points: Points, csv_path: str) -> None:
    path = Path(csv_path)
    with path.open("w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["x", "y", "z"])
        for x, y, z in points:
            writer.writerow([x, y, z])
def summarize(label: str, points: Points) -> None:
    print(f"{label}: {len(points)}")
def main() -> None:
    input_csv = "input_points.csv"
    output_csv = "filtered_points.csv"
    if Path(input_csv).exists():
        input_points = load_points_from_csv(input_csv)
        print(f"Loaded INPUT from CSV: {input_csv}")
    else:
        input_points = load_samlpe_points()
        print("Loaded INPUT from built-in sample data")
    output_points = filter_points(input_points, **FILTER_CONFIG)
    print("\n=== DATA SUMMARY ===")
    summarize("Input points", input_points)
    summarize("Output_points", output_points)
    if len(input_points) > 0:
        ratio = (len(output_points) / len(input_points)) * 100
        print(f"Kept ratio: {ratio:.1f}%")
    save_points_to_csv(output_points, output_csv)
    print(f"\nSaved OUTPUT to file: {output_csv}")
if __name__ == "__main__":
    main()