## Context

The Reports API already exposes `GET /reports` with filter, sort, and offset/limit pagination over an in-memory dataset. The query layer (`app/reports.py`) is intentionally separate from HTTP so export can reuse the same logic. Public fields are defined on `ReportPublic`; internal fields (`internal_id`, `owner_email`) must never leak into user-facing output.

## Goals / Non-Goals

**Goals:**

- Add `GET /reports/export` that returns CSV for exactly the rows on the current list page.
- Mirror all `GET /reports` query parameters: `status`, `date_from`, `date_to`, `sort`, `descending`, `offset`, `limit`.
- Serialize via stdlib `csv` (RFC 4180), including proper escaping of commas, quotes, and newlines in `title`.
- Set `Content-Type: text/csv` and `Content-Disposition: attachment; filename="reports.csv"`.

**Non-Goals:**

- Exporting the full filtered dataset in one file (ignoring `offset`/`limit`).
- New columns beyond the existing public JSON shape.
- Streaming very large exports or row-cap / 413 handling (dataset is fixed at 120 rows).
- A frontend UI or export button (API-only workshop repo).

## Decisions

1. **Endpoint path: `GET /reports/export`** (not `/reports.csv`)
   - Keeps content negotiation clear and groups export with the reports resource.
   - Alternative considered: `/reports.csv` — rejected as it blurs REST resource naming.

2. **Pagination scope: current page only**
   - "Download what's currently showing" means apply `offset` and `limit` after filter/sort, same slice as `GET /reports`.
   - Alternative: export all matching rows — rejected; contradicts the PM ask and pagination UX.

3. **CSV builder location: `to_csv()` in `app/reports.py`**
   - Reuses the query layer separation already documented in that module.
   - Accepts `list[ReportPublic]` so mapping stays consistent with JSON responses.

4. **Column set and datetime format**
   - Headers: `id`, `title`, `status`, `owner`, `amount`, `created_at`.
   - `created_at` as ISO 8601 strings via `.isoformat()` for stable, parseable output.

5. **HTTP response type**
   - FastAPI `Response` with raw CSV body (not `StreamingResponse`) — dataset is small; simplicity wins.

## Risks / Trade-offs

- **[Risk] Clients expect full export** → Mitigation: document that `offset`/`limit` apply; same params as the list call.
- **[Risk] Excel locale quirks on `amount`** → Mitigation: out of scope; use plain numeric string from Python `csv`.
- **[Risk] Duplicate query logic in two routes** → Mitigation: both routes call shared `query()`; only serialization differs.
