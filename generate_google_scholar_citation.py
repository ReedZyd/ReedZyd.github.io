import gsbg
from pathlib import Path

PROFILE_LINK = "https://scholar.google.com.hk/citations?user=SyMVOgMAAAAJ&hl=en&oi=ao"

out_dir = Path("assets") / "badges"
out_dir.mkdir(parents=True, exist_ok=True)

# 生成一个 SVG badge（文件名你可以改）
gsbg.gene_citation_badge_svg(
    link=PROFILE_LINK,
    link_type="profile",
    svg_name="scholar_citations.svg",
    path_to_save=str(out_dir),
)
