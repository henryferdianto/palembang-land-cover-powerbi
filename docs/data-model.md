# Data Model

Star schema:

- **Fact: LandCover** — `area_ha`, `class_id`, `region_id`, `date_id`
- **Dim: Class** — land cover class (built-up, vegetation, water body, agriculture, ...)
- **Dim: Region** — district / sub-district with centroid coordinates
- **Dim: Date** — year, quarter, month

Relationships: `LandCover[*] -> Class[1]`, `Region[1]`, `Date[1]`.
