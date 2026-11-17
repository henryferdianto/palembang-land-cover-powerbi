from src.analyze import built_up_share, top_growth_regions, yoy_growth
from src.sample_data import make


def test_built_up_share_in_range():
    share = built_up_share(make())
    assert share["built_up_share"].between(0, 1).all()


def test_yoy_has_growth_column():
    assert "yoy_growth_pct" in yoy_growth(make()).columns


def test_top_regions_limit():
    assert len(top_growth_regions(make(), top=2)) == 2
