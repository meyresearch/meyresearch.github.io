---
name: update-publications
description: Check the group's Google Scholar profile for papers missing from the website and draft new publication entries. Use when the user asks to update the publications list, sync publications from Google Scholar, or check for missing papers.
---

# Update publications from Google Scholar

Finds papers on the Mey group's Google Scholar profile that are not yet in
`_data/publist.yml` / `_data/prelist.yml` and drafts YAML entries for them.
Drafts are shown to the user for review; nothing is written or committed
without approval.

## Important caveats (tell the user if relevant)

- Google Scholar has no official API and blocks scrapers. Run this **locally**
  (residential IP), not from a cloud agent. It can still be throttled/CAPTCHA'd;
  if so, wait and retry, or rerun with `--no-fill`.
- Scholar does not provide the site's `description`, `image`, or DOIs. Drafts
  therefore contain `TODO:` placeholders and a best-effort author reformat to
  the site's `A.S.J.S. Mey` initials style. Every draft needs a human check.

## Steps

1. **Ensure `scholarly` is installed** (PyYAML is already available):
   ```bash
   python3 -c "import scholarly" 2>/dev/null || pip3 install scholarly
   ```

2. **Run the diff** from the repo root:
   ```bash
   python3 .claude/skills/update-publications/scholar_diff.py --repo .
   ```
   Useful flags: `--max N` (scan only the N most-recent papers, faster),
   `--no-fill` (fewer requests if Scholar is blocking), `--profile ID`
   (defaults to the group profile `_NNNlvMAAAAJ`).

3. **Review the drafts with the user.** The script prints draft YAML blocks for
   each missing paper on stdout. For each one, confirm with the user:
   - the `authors` string (fix the initials formatting; ensure `A.S.J.S. Mey`
     is present and ordering matches the paper),
   - a real one-line `description` (replace the `TODO:`),
   - the `link.url` (prefer a DOI: `https://doi.org/...`) and `link.display`
     (e.g. `J. Chem. Inf. Model., 65, 12279 (2025)`),
   - whether it is a **preprint** (bioRxiv/arXiv/ChemRxiv → `prelist.yml`) or a
     **published** paper (`publist.yml`),
   - `highlight: 1` only if the user wants it featured.

4. **On approval, add the entries** to the top of the correct file
   (`_data/publist.yml` for published, `_data/prelist.yml` for preprints),
   matching the existing entry format exactly. Do not commit unless asked.

## Notes

- Matching is by normalised + fuzzy title, so papers already listed (even with
  minor title differences) are skipped. If a paper is wrongly flagged as
  missing, it is likely a title-wording mismatch; check `publist.yml` by hand.
- Keep British English and the house style in any `description` you write.
