# gha-matrix-cache-artifacts

A CI workflow showing the three features that make Actions fast and debuggable: a **build matrix**, **dependency caching**, and **artifacts**, with a **job summary** at the end.

## Flow

```
test x { ubuntu, windows } x { py3.12, py3.13 }   (4 jobs, in parallel)
   |  setup-python with cache: pip
   |  pytest --junitxml  -> upload artifact (even on failure)
   v
summary: download all JUnit files -> one Markdown table in the job summary
```

## What ran (2026-10-16)

- The first run **succeeded**: all 4 matrix jobs plus the summary.
- A **re-run of the same commit showed cache hits** in the logs (`Cache hit occurred on the primary key ... not saving cache`), so the pip cache is keyed and restored correctly. The first run populates it, the second uses it.

## Decisions

- **`fail-fast: false`** so one failing combination does not hide the others.
- **`if: always()` on the artifact upload**: results of a failed run are exactly the ones you need.
- **`concurrency` with `cancel-in-progress` only for pull requests**: stale PR runs are cancelled, runs on `main` never are.
- **`shell: bash` as the default**, so the same commands work on Windows runners.
- **Cache key comes from the hash of `requirements.txt`**, so changing a dependency invalidates it.
- **A final job merges per-job results** (`merge-multiple`), so a reader sees one table, not four logs.

## Honest limits

- The cache saved little here: one small dependency. The mechanism is what is shown, not a measured speed-up, and no timings are claimed.
- Windows minutes are billed at a higher rate on private repos (free for public ones).
- No `include` or `exclude` entries and no experimental-version job; no test sharding.

MIT licensed.
