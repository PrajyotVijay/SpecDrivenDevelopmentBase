## ADDED Requirements

### Requirement: Export reports as CSV
THE system SHALL expose `GET /reports/export` returning the current page of reports as RFC 4180 CSV.

#### Scenario: default pagination
- **WHEN** the user calls `GET /reports/export` with no query parameters
- **THEN** the response status SHALL be 200
- **AND** the CSV body SHALL contain a header row plus at most 20 data rows
- **AND** the columns SHALL be `id`, `title`, `status`, `owner`, `amount`, `created_at`

#### Scenario: filter and sort parity with list
- **WHEN** the user calls `GET /reports/export` with the same `status`, `date_from`, `date_to`, `sort`, and `descending` parameters as a `GET /reports` call
- **THEN** the exported row `id` values SHALL match the `items[].id` values from that list response for the same `offset` and `limit`

#### Scenario: pagination applies to export
- **WHEN** the user passes `offset` and `limit` to `GET /reports/export`
- **THEN** the CSV SHALL contain only the slice `rows[offset : offset + limit]` after filter and sort
- **AND** the row count SHALL NOT exceed `limit`

#### Scenario: download headers
- **WHEN** the user calls `GET /reports/export` successfully
- **THEN** the response `Content-Type` SHALL indicate CSV
- **AND** the response SHALL include `Content-Disposition` with `attachment` and filename `reports.csv`

#### Scenario: invalid sort field
- **WHEN** the user passes a `sort` value that is not a permitted sort field
- **THEN** the response status SHALL be HTTP 400

#### Scenario: internal fields omitted from CSV
- **WHEN** the user receives a CSV export
- **THEN** the file SHALL NOT contain `internal_id` or `owner_email` columns or values

#### Scenario: CSV escaping
- **WHEN** a report `title` contains commas, double quotes, or newline characters
- **THEN** the CSV SHALL encode that field per RFC 4180 so standard CSV parsers recover the original title
