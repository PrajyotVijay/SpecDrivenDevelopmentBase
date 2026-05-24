## Why

Users viewing a filtered, sorted, paginated reports list need to download that same view as a spreadsheet. JSON alone forces manual copy-paste or a custom client; a one-click CSV export matches how finance and ops teams already work with report data.

## What Changes

- Add `GET /reports/export` returning RFC 4180 CSV for the **current page** of results (same filters, sort, `offset`, and `limit` as `GET /reports`).
- CSV columns match the public JSON fields: `id`, `title`, `status`, `owner`, `amount`, `created_at`.
- Response uses `Content-Disposition: attachment` so browsers download `reports.csv`.
- Reuse the existing `query()` layer in `app/reports.py`; no change to internal field exposure rules.
- Add tests covering pagination parity, filter parity, CSV escaping, and invalid sort handling.

## Capabilities

### New Capabilities

_(none — export extends the existing reports capability)_

### Modified Capabilities

- `reports`: Add a CSV export requirement with filter/sort/pagination parity to `GET /reports`, and scenarios for download headers, column set, and escaping.

## Impact

- **API**: New endpoint `GET /reports/export` alongside existing `GET /reports`.
- **Code**: `app/main.py` (route), `app/reports.py` (`to_csv` helper), `tests/test_reports.py`.
- **Dependencies**: None (stdlib `csv` only).
- **Breaking changes**: None.
