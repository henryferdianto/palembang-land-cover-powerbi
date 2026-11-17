"""Reproduce the dashboard KPIs in Python."""
from pathlib import Path

import pandas as pd


def built_up_share(df: pd.DataFrame) -> pd.DataFrame:
    pivot = df.pivot_table(index=["year", "region"], columns="class",
                           values="area_ha", aggfunc="sum").fillna(0)
    pivot["total"] = pivot.sum(axis=1)
    pivot["built_up_share"] = pivot["Built-up"] / pivot["total"]
    return pivot.reset_index()


def yoy_growth(df: pd.DataFrame) -> pd.DataFrame:
    by_year = df[df["class"] == "Built-up"].groupby("year")["area_ha"].sum().reset_index()
    by_year["yoy_growth_pct"] = by_year["area_ha"].pct_change() * 100
    return by_year


def top_growth_regions(df: pd.DataFrame, top: int = 3) -> pd.DataFrame:
    by_region = df[df["class"] == "Built-up"].groupby("region")["area_ha"].agg(["min", "max"])
    by_region["absolute_growth"] = by_region["max"] - by_region["min"]
    return by_region.sort_values("absolute_growth", ascending=False).head(top)


def report(input_csv: str = "data/raw/land_cover.csv") -> dict:
    df = pd.read_csv(input_csv)
    return {
        "built_up": built_up_share(df),
        "yoy": yoy_growth(df),
        "top_regions": top_growth_regions(df),
    }


def main():
    frames = report()
    out = Path("reports")
    out.mkdir(exist_ok=True)
    for name, frame in frames.items():
        frame.to_csv(out / f"{name}.csv", index=False)
        print(f"--- {name} ---")
        print(frame.to_string(index=False))


if __name__ == "__main__":
    main()
