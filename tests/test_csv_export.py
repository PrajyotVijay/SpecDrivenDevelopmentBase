"""Tests for GET /reports/export (add-csv-export change)."""

from __future__ import annotations

import csv
import io

from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_export_reports_default_pagination() -> None:
    r = client.get("/reports/export")
    assert r.status_code == 200
    assert r.headers["content-type"].startswith("text/csv")
    assert 'filename="reports.csv"' in r.headers["content-disposition"]

    rows = list(csv.DictReader(io.StringIO(r.text)))
    assert len(rows) == 20
    assert set(rows[0].keys()) == {"id", "title", "status", "owner", "amount", "created_at"}


def test_export_reports_matches_list_page() -> None:
    params = {"status": "approved", "limit": 5, "offset": 10, "sort": "id", "descending": False}
    listed = client.get("/reports", params=params).json()
    exported = list(csv.DictReader(io.StringIO(client.get("/reports/export", params=params).text)))
    assert [int(row["id"]) for row in exported] == [item["id"] for item in listed["items"]]


def test_export_reports_escapes_special_characters_in_title() -> None:
    r = client.get("/reports/export", params={"limit": 200})
    rows = list(csv.DictReader(io.StringIO(r.text)))
    tricky = next(row for row in rows if "quotes" in row["title"])
    assert "commas" in tricky["title"]
    assert "\n" in tricky["title"]


def test_export_reports_omits_internal_fields() -> None:
    r = client.get("/reports/export", params={"limit": 200})
    assert r.status_code == 200
    assert "internal_id" not in r.text
    assert "owner_email" not in r.text


def test_export_reports_rejects_bad_sort_field() -> None:
    r = client.get("/reports/export", params={"sort": "owner_email"})
    assert r.status_code == 400
