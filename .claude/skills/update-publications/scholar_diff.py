#!/usr/bin/env python3
"""Compare a Google Scholar profile against the site's publication YAML and
emit draft entries for any papers that are missing.

Only produces *drafts* on stdout; it never edits the YAML files itself. The
skill workflow shows the drafts to the user before anything is written.

Usage:
    python3 scholar_diff.py [--profile ID] [--repo PATH] [--max N] [--no-fill]

Requires `scholarly` (pip install scholarly) and PyYAML.
"""
import argparse
import re
import sys
from difflib import SequenceMatcher
from pathlib import Path

try:
    import yaml
except ImportError:
    sys.exit("PyYAML is required: pip install pyyaml")

# The group's Scholar profile, taken from the site footer / publications page.
DEFAULT_PROFILE = "_NNNlvMAAAAJ"

# Titles that normalise to the same string are treated as already present.
# Below this fuzzy ratio a Scholar paper is considered missing.
MATCH_THRESHOLD = 0.90


def norm(title: str) -> str:
    """Lowercase, strip punctuation, collapse whitespace for title matching."""
    return re.sub(r"\s+", " ", re.sub(r"[^a-z0-9 ]", " ", title.lower())).strip()


def load_titles(path: Path) -> list[str]:
    if not path.exists():
        return []
    data = yaml.safe_load(path.read_text()) or []
    return [norm(e["title"]) for e in data if isinstance(e, dict) and e.get("title")]


def is_present(title: str, existing: list[str]) -> bool:
    n = norm(title)
    if n in existing:
        return True
    return any(SequenceMatcher(None, n, e).ratio() >= MATCH_THRESHOLD for e in existing)


def to_initials(name: str) -> str:
    """'Aryo Pradipta Gema' -> 'A.P. Gema'. Best effort; review by hand."""
    parts = name.replace(".", "").split()
    if len(parts) < 2:
        return name
    initials = "".join(f"{p[0].upper()}." for p in parts[:-1] if p)
    return f"{initials} {parts[-1]}"


def format_authors(raw) -> str:
    """Scholar returns authors as 'A and B and C'; convert to the site's
    'A. Author, B. Author' initials style."""
    if not raw:
        return "TODO: authors"
    names = raw.split(" and ") if isinstance(raw, str) else list(raw)
    return ", ".join(to_initials(n.strip()) for n in names if n.strip())


# Venue / title fragments that mark items the site intentionally omits:
# conference abstracts, supporting-info duplicates, theses, tutorials, grants.
NOISE_MARKERS = (
    "abstracts of papers", "european biophysics journal", "supporting information",
    "tutorial", "documentation", "principal supervisor", "eastbio",
    "bound method", "organization:",
)


def clean_str(value) -> str:
    """Coerce a bib field to a sane string, dropping scholarly repr leakage."""
    if not isinstance(value, str):
        return ""
    text = value.strip()
    return "" if any(m in text.lower() for m in ("bound method", "organization:")) else text


def venue_of(bib: dict) -> str:
    return clean_str(bib.get("journal")) or clean_str(bib.get("venue")) or \
        clean_str(bib.get("citation"))


def looks_like_noise(bib: dict) -> bool:
    """True for items the site normally excludes (abstracts, SI, theses...)."""
    haystack = f"{bib.get('title', '')} {venue_of(bib)}".lower()
    if any(m in haystack for m in NOISE_MARKERS):
        return True
    # A thesis typically lists a university as the venue with no journal.
    return "university of" in venue_of(bib).lower() and not bib.get("journal")


def draft_entry(bib: dict) -> str:
    title = bib.get("title", "TODO: title").replace('"', "'")
    venue = venue_of(bib)
    year = bib.get("pub_year") or bib.get("year") or ""
    display = f"{venue} ({year})".strip() if year else (venue or "TODO: venue")
    url = bib.get("pub_url") or bib.get("eprint_url") or ""
    return (
        f'- title: "{title}"\n'
        f"  image: xx.png\n"
        f"  description: TODO: one-line summary\n"
        f"  authors: {format_authors(bib.get('author'))}\n"
        f"  link:\n"
        f"    url: {url}\n"
        f"    display: {display}\n"
        f"  highlight: 0\n"
        f"  news2:\n"
    )


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--profile", default=DEFAULT_PROFILE)
    ap.add_argument("--repo", default=".", help="path to the website repo root")
    ap.add_argument("--max", type=int, default=0, help="limit Scholar papers scanned (0 = all)")
    ap.add_argument("--no-fill", action="store_true",
                    help="skip per-paper fill (fewer requests, less blocking, thinner data)")
    args = ap.parse_args()

    try:
        from scholarly import scholarly
    except ImportError:
        sys.exit("scholarly is not installed. Run: pip install scholarly")

    repo = Path(args.repo)
    existing = load_titles(repo / "_data" / "publist.yml") + \
        load_titles(repo / "_data" / "prelist.yml")
    print(f"[info] {len(existing)} existing titles loaded from repo", file=sys.stderr)

    print(f"[info] fetching Scholar profile {args.profile} ...", file=sys.stderr)
    author = scholarly.search_author_id(args.profile)
    author = scholarly.fill(author, sections=["publications"])
    pubs = author.get("publications", [])
    if args.max:
        pubs = pubs[: args.max]
    print(f"[info] {len(pubs)} publications on Scholar profile", file=sys.stderr)

    likely, skip = [], []
    for pub in pubs:
        bib = pub.get("bib", {})
        title = bib.get("title", "")
        if not title or is_present(title, existing):
            continue
        if not args.no_fill:
            try:
                pub = scholarly.fill(pub)
                bib = pub.get("bib", bib)
            except Exception as exc:  # blocked / transient: keep thin data
                print(f"[warn] could not fill '{title[:50]}': {exc}", file=sys.stderr)
        (skip if looks_like_noise(bib) else likely).append(bib)

    print(f"[info] {len(likely)} likely-new, {len(skip)} probably-skip\n", file=sys.stderr)
    if not likely and not skip:
        print("# No missing publications. The site is up to date.")
        return 0

    if likely:
        print("# ==== LIKELY NEW publications (review, then add) ====\n")
        for bib in likely:
            print(draft_entry(bib))
    if skip:
        print("# ==== PROBABLY SKIP: abstracts / SI / theses / grants / etc. ====")
        print("# (Listed for awareness only; add manually if any genuinely belong.)\n")
        for bib in skip:
            yr = bib.get("pub_year") or bib.get("year") or "?"
            print(f"#   - {bib.get('title', '')[:80]}  ({venue_of(bib)[:40]}, {yr})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
