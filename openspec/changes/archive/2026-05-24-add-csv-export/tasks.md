## 1. CSV serialization

- [x] 1.1 Add `to_csv(items: list[ReportPublic]) -> str` in `app/reports.py` using stdlib `csv` with columns `id`, `title`, `status`, `owner`, `amount`, `created_at`
- [x] 1.2 Format `created_at` as ISO 8601; ensure RFC 4180 escaping for special characters in `title`

## 2. Export endpoint

- [x] 2.1 Add `GET /reports/export` in `app/main.py` accepting the same query parameters as `GET /reports`
- [x] 2.2 Reuse `query()` for filter/sort, slice with `offset`/`limit`, map through `ReportPublic.from_internal`
- [x] 2.3 Return `Response` with `media_type="text/csv"` and `Content-Disposition: attachment; filename="reports.csv"`
- [x] 2.4 Return HTTP 400 for invalid `sort` (same as list endpoint)

## 3. Tests

- [x] 3.1 Test default export returns 20 data rows, correct headers, and CSV content type
- [x] 3.2 Test export row IDs match `GET /reports` for the same query params (filter, sort, offset, limit)
- [x] 3.3 Test CSV correctly round-trips a title with commas, quotes, and newlines
- [x] 3.4 Test invalid `sort` on export returns 400
- [x] 3.5 Run `pytest -q` and confirm all tests pass
