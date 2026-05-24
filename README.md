# 🤖 Vibe Coded — CSV Export Feature

## What is Vibe Coding?
Vibe coding is a term coined by Andrej Karpathy in February 2025. It means:
> "Prompt an AI, accept what it generates, run it, re-prompt if it breaks."

No planning. No spec. Just vibes. ✨

## What I Built
Added a **CSV Export** feature to the Reports API.

### New Endpoint
`GET /reports/export` — Downloads the current filtered reports as a CSV file.

### How it works
- Accepts the same query parameters as `GET /reports`
- Returns a downloadable `reports.csv` file
- Columns: `id, title, status, owner, amount, created_at`

## How I Built It (Vibe Coding Process)
1. Got a casual Slack message from PM:
   > *"hey can you add a CSV export button to the reports page? should download whats currently showing. thanks!"*
2. Pasted it directly into **Cursor Composer**
3. Accepted whatever Cursor generated
4. Tests passed ✅ — shipped it!

## What's Missing (The Vibe Coding Problem)
- ❌ No proper spec written
- ❌ No edge cases considered upfront
- ❌ No documentation of decisions
- ❌ Could have leaked internal fields
- ❌ No row cap for large datasets

## Tech Stack
- Python 3.13
- FastAPI
- Pydantic
- Pytest

## Tests
```bash
pytest -q
```
9 tests passing ✅