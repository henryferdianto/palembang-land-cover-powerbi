"""Generate synthetic multi-temporal land cover data for the dashboard."""
from pathlib import Path

import numpy as np
import pandas as pd

CLASSES = ["Built-up", "Vegetation", "Water body", "Agriculture"]


def make(seed: int = 42) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    regions = ["Ilir Barat I", "Ilir Timur II", "Sukarami", "Kemuning", "Bukit Kecil"]
    rows = []
    for year in [2018, 2020, 2022, 2024]:
        for region in regions:
            base = rng.uniform(400, 1200)
            for cls in CLASSES:
                if cls == "Built-up":
                    area = base * (0.15 + 0.06 * (year - 2018) / 2)
                else:
                    area = base * rng.uniform(0.1, 0.4)
                rows.append({"year": year, "region": region, "class": cls,
                             "area_ha": round(area, 2)})
    df = pd.DataFrame(rows)
    centroids = pd.DataFrame({"region": regions,
                              "lat": [-2.98, -2.97, -2.93, -2.95, -2.99],
                              "lon": [104.74, 104.77, 104.75, 104.79, 104.73]})
    return df.merge(centroids, on="region")


def main() -> Path:
    out = Path("data/raw/land_cover.csv")
    out.parent.mkdir(parents=True, exist_ok=True)
    make().to_csv(out, index=False)
    print(f"wrote land cover data -> {out}")
    return out


if __name__ == "__main__":
    main()
