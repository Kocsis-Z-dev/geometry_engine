"""
Point Filter Service
--------------------
Reussable Python script for Filtering and validating 3D (XYZ) point data.
Supports CSV imput and CSV output.
"""
from typing import List, Tuple
import csv
from pathlib import Path
Point3D = Tuple[float, float, float]
Points = List[Point3D]
FILTER_CONFIG = {"min_x": 2.0, "max_x": 8.0, "min_y": 2.0, "max_y": 8.0, "min_z": 4.0, "max_z":9.0}
def load_points_from_csv(csv_path: str) -> Points:
    """
    Load 3D points from a csv file with columns:x,y,z
    """
    path = Path(csv_path)
    points: Points = []
    with path.open("r", newline="", encoding="utf-8") as f:
        reader =csv.reader(f)
        for row in reader:
            if not row:
                continue
            if row[0].strip().lower() in {"x", "x_coord", "xcoordinate"}:
                continue
            x =float( row[0])
            y =float( row[1])
            z =float( row[2])
            points.append((x, y, z))
        return points
def load_points() -> Points:
    """
    Load or define input point data.
    Replace this with file loading if needed.
    """
    points = [(1.0, 2.0, 3.0), (4.0, 5.0, 6.0), (7.0, 8.0, 9.0),]
    return points
def filter_points(points: Points, min_x: float, max_x: float, min_y: float, max_y: float, min_z: float, max_z: float,) -> Points:
    """s
    Apply filtering rules to point data.
    """
    filtered = []
    for x, y, z in points:
        if (min_x <= x <= max_x and min_y <= y <= max_y and min_z <= max_z):
            filtered.append((x, y, z))
    return filtered
def save_points_to_csv(points: Points, csv_path: str) -> None:
    """
    Save filtered 3D points to a CSV file.
    """
    path = Path(csv_path)
    with path.open("w", newline="", encoding="utf-8") as f:
        writer =csv.writer(f)
        writer.writerow(["x", "y", "z"])
        for x, y, z in points:
            writer.writerow([x, y, z])
def summarize(input_points: Points, output_points: Points) -> None:
    """
    Print input vs output summary.
    """
    print(f"Input points: {len(input_points)}")
    print(f"Output points: {len(output_points)}")
    if len(input_points) > 0:
        ratio = (len(output_points) / len(input_points))* 100
        print(f"Kept: {ratio:.1f}%")
def main() -> None:
    input_csv = "input_points.csv"
    if Path(input_csv).exists():
        points = load_points_from_csv(input_csv)
        print(f"Loaded from CSV: {input_csv}")
    else:
        points = load_points()
        print("Loaded from built-in sample data")
    filtered = filter_points(points, **FILTER_CONFIG)
    summarize(points, filtered)
    output_csv = "filtered_points.csv"
    save_points_to_csv(filtered, output_csv)
    print(f"Saved filtered points to: {output_csv}")
if __name__ == "__main__":
    main()   