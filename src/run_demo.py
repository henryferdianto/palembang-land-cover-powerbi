from src.analyze import report
from src.sample_data import main as make_sample
from pathlib import Path


def main():
    if not Path("data/raw/land_cover.csv").exists():
        make_sample()
    for name, frame in report().items():
        print(f"--- {name} ---")
        print(frame.to_string(index=False))


if __name__ == "__main__":
    main()
