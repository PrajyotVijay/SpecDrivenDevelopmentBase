# 📋 Spec Driven Development — CSV Export Feature

## What is Spec Driven Development (SDD)?
Spec Driven Development means writing a **detailed specification first**, then implementing code based on that spec. No guessing, no surprises.

> "The spec is the contract. The code is just the fulfillment."

## What I Built
Added a **CSV Export** feature to the Reports API using the full OpenSpec 1.3.1 workflow.

### New Endpoint
`GET /reports/export` — Downloads the current filtered reports as a CSV file.

### How it works
- Accepts the same query parameters as `GET /reports`
- Returns a downloadable `reports.csv` file
- Columns: `id, title, status, owner, amount, created_at`
- ✅ No internal fields leaked (`internal_id`, `owner_email` excluded)
- ✅ RFC 4180 compliant CSV (handles commas, quotes, newlines in data)
- ✅ Proper `Content-Disposition` download headers

## How I Built It (SDD Process with OpenSpec)

### Step 1 — Propose the change

/opsx:propose add-csv-export

OpenSpec created 4 artifacts:
- `proposal.md` — Why we need this feature
- `design.md` — Implementation approach
- `specs/reports/spec.md` — Detailed spec with scenarios
- `tasks.md` — 11 atomic tasks to implement

### Step 2 — Review the spec
Reviewed all artifacts before writing a single line of code.

### Step 3 — Implement based on spec

/opsx:apply add-csv-export

Cursor implemented all 11 tasks based on the spec. 11/11 tests passed ✅

### Step 4 — Archive the change

/opsx:archive add-csv-export
Spec merged into `openspec/specs/reports/spec.md` permanently.

## SDD vs Vibe Coding — The Difference

| | Vibe Coding | Spec Driven Development |
|---|---|---|
| Planning | ❌ None | ✅ Full spec first |
| Edge cases | ❌ Missed | ✅ Covered in spec |
| Internal field leak | ❌ Risk | ✅ Explicitly prevented |
| Audit trail | ❌ None | ✅ Full archive |
| Tests | ❌ Basic | ✅ Comprehensive |

## OpenSpec Files

```
openspec/
├── config.yaml
├── specs/reports/spec.md
└── changes/archive/
└── 2026-05-24-add-csv-export/
├── proposal.md
├── design.md
├── tasks.md
└── specs/reports/spec.md

```

## Tech Stack
- Python 3.13
- FastAPI
- Pydantic
- Pytest
- OpenSpec 1.3.1

## Tests
```bash
pytest -q
```
11 tests passing ✅
