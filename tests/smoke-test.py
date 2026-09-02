# File generated from our OpenAPI spec by Scalar. See README.md for details.

# Smoke test: calls every generated operation once to confirm the SDK can reach each endpoint.
# Run it from this repo with `python tests/smoke-test.py`. The generator also runs this file
# against a mock server and reads the JSON report produced via SCALAR_SMOKE_REPORT.
from __future__ import annotations

import json
import os
import sys
import time
import traceback
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from typing import Any, Callable, TypedDict

from fathom_analytics import FathomAnalyticsAPI

# The shared smoke-test runner injects base URL and credentials through the same
# environment variables the generated client reads in normal use.
client = FathomAnalyticsAPI(max_retries=0, timeout=30)


class SmokeResult(TypedDict, total=False):
    operation: str
    method: str
    path: str
    label: str
    status: str
    durationMs: int
    error: str


class _SmokeCaseBase(TypedDict):
    operation: str
    method: str
    path: str
    run: Callable[[], Any]


# `label` says which of an operation's two calls this is — "required params" or "all params".
# It sits in a total=False extension because it is absent when the operation contributed a
# single case, while the fields above are always present.
class SmokeCase(_SmokeCaseBase, total=False):
    label: str


def _smoke_case_0() -> None:
    client.account.list()


def _smoke_case_1() -> None:
    client.account.list_token()


def _smoke_case_2() -> None:
    client.sites.list(
        limit=10,
    )


def _smoke_case_3() -> None:
    client.sites.list(
        limit=10,
        starting_after="starting_after",
        ending_before="ending_before",
    )


def _smoke_case_4() -> None:
    client.sites.create(
        name="Bugs Bunny Portfolio",
        sharing="none",
        multi_domain=False,
    )


def _smoke_case_5() -> None:
    client.sites.create(
        name="Bugs Bunny Portfolio",
        sharing="none",
        share_password="",
        timezone="",
        multi_domain=False,
        multi_domain_option="combined",
    )


def _smoke_case_6() -> None:
    client.sites.retrieve(
        site_id="CDBUGS",
    )


def _smoke_case_7() -> None:
    client.sites.update(
        site_id="CDBUGS",
    )


def _smoke_case_8() -> None:
    client.sites.update(
        site_id="CDBUGS",
        name="Acme Holdings Inc",
        sharing="none",
        share_password="",
        timezone="",
        multi_domain=False,
        multi_domain_option="combined",
    )


def _smoke_case_9() -> None:
    client.sites.delete(
        site_id="CDBUGS",
    )


def _smoke_case_10() -> None:
    client.sites.wipe(
        site_id="CDBUGS",
    )


def _smoke_case_11() -> None:
    client.events.list(
        site_id="CDBUGS",
        limit=10,
    )


def _smoke_case_12() -> None:
    client.events.list(
        site_id="CDBUGS",
        limit=10,
        starting_after="starting_after",
        ending_before="ending_before",
    )


def _smoke_case_13() -> None:
    client.events.delete_by_name(
        site_id="CDBUGS",
        name="Purchase early access",
    )


def _smoke_case_14() -> None:
    client.events.create(
        site_id="CDBUGS",
        name="Purchase early access",
        currency="dollar",
    )


def _smoke_case_15() -> None:
    client.events.set_currency(
        site_id="CDBUGS",
        name="Purchase early access",
        currency="pound",
    )


def _smoke_case_16() -> None:
    client.events.retrieve(
        site_id="CDBUGS",
        event_id="ABCDEFGH",
    )


def _smoke_case_17() -> None:
    client.events.update(
        site_id="CDBUGS",
        event_id="ABCDEFGH",
    )


def _smoke_case_18() -> None:
    client.events.update(
        site_id="CDBUGS",
        event_id="ABCDEFGH",
        name="Purchase early access (live)",
        currency="dollar",
    )


def _smoke_case_19() -> None:
    client.events.delete(
        site_id="CDBUGS",
        event_id="ABCDEFGH",
    )


def _smoke_case_20() -> None:
    client.events.wipe(
        site_id="CDBUGS",
        event_id="ABCDEFGH",
    )


def _smoke_case_21() -> None:
    client.milestones.list(
        site_id="CDBUGS",
        limit=10,
    )


def _smoke_case_22() -> None:
    client.milestones.list(
        site_id="CDBUGS",
        limit=10,
        starting_after="starting_after",
        ending_before="ending_before",
    )


def _smoke_case_23() -> None:
    client.milestones.create(
        site_id="CDBUGS",
        name="Website Redesign Launch",
        milestone_date="2024-01-15",
    )


def _smoke_case_24() -> None:
    client.milestones.retrieve(
        site_id="CDBUGS",
        milestone_id="ddc9cdff-ab83-41fa-96c6-dfb276a862e7",
    )


def _smoke_case_25() -> None:
    client.milestones.update(
        site_id="CDBUGS",
        milestone_id="ddc9cdff-ab83-41fa-96c6-dfb276a862e7",
        name="Website Redesign Launch v2",
        milestone_date="2024-01-20",
    )


def _smoke_case_26() -> None:
    client.milestones.delete(
        site_id="CDBUGS",
        milestone_id="ddc9cdff-ab83-41fa-96c6-dfb276a862e7",
    )


def _smoke_case_27() -> None:
    client.reports.aggregation(
        entity="pageview",
        aggregates="pageviews",
    )


def _smoke_case_28() -> None:
    client.reports.aggregation(
        entity="pageview",
        entity_id="CDBUGS",
        site_id="site_id",
        entity_name="entity_name",
        aggregates="pageviews",
        date_grouping="hour",
        field_grouping="field_grouping",
        sort_by="sort_by",
        date_from="date_from",
        date_to="date_to",
        timezone="timezone",
        limit=1,
        filters="filters",
    )


def _smoke_case_29() -> None:
    client.reports.current_visitors(
        site_id="CDBUGS",
        detailed=False,
    )


cases: list[SmokeCase] = [
    {
        "operation": "list",
        "method": "GET",
        "path": "/account",
        "run": _smoke_case_0,
    },
    {
        "operation": "listToken",
        "method": "GET",
        "path": "/token",
        "run": _smoke_case_1,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/sites",
        "label": "required params",
        "run": _smoke_case_2,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/sites",
        "label": "all params",
        "run": _smoke_case_3,
    },
    {
        "operation": "create",
        "method": "POST",
        "path": "/sites",
        "label": "required params",
        "run": _smoke_case_4,
    },
    {
        "operation": "create",
        "method": "POST",
        "path": "/sites",
        "label": "all params",
        "run": _smoke_case_5,
    },
    {
        "operation": "retrieve",
        "method": "GET",
        "path": "/sites/{site_id}",
        "run": _smoke_case_6,
    },
    {
        "operation": "update",
        "method": "POST",
        "path": "/sites/{site_id}",
        "label": "required params",
        "run": _smoke_case_7,
    },
    {
        "operation": "update",
        "method": "POST",
        "path": "/sites/{site_id}",
        "label": "all params",
        "run": _smoke_case_8,
    },
    {
        "operation": "delete",
        "method": "DELETE",
        "path": "/sites/{site_id}",
        "run": _smoke_case_9,
    },
    {
        "operation": "wipe",
        "method": "DELETE",
        "path": "/sites/{site_id}/data",
        "run": _smoke_case_10,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/sites/{site_id}/events",
        "label": "required params",
        "run": _smoke_case_11,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/sites/{site_id}/events",
        "label": "all params",
        "run": _smoke_case_12,
    },
    {
        "operation": "deleteByName",
        "method": "DELETE",
        "path": "/sites/{site_id}/events",
        "run": _smoke_case_13,
    },
    {
        "operation": "create",
        "method": "POST",
        "path": "/sites/{site_id}/events",
        "run": _smoke_case_14,
    },
    {
        "operation": "setCurrency",
        "method": "POST",
        "path": "/sites/{site_id}/events/currency",
        "run": _smoke_case_15,
    },
    {
        "operation": "retrieve",
        "method": "GET",
        "path": "/sites/{site_id}/events/{event_id}",
        "run": _smoke_case_16,
    },
    {
        "operation": "update",
        "method": "POST",
        "path": "/sites/{site_id}/events/{event_id}",
        "label": "required params",
        "run": _smoke_case_17,
    },
    {
        "operation": "update",
        "method": "POST",
        "path": "/sites/{site_id}/events/{event_id}",
        "label": "all params",
        "run": _smoke_case_18,
    },
    {
        "operation": "delete",
        "method": "DELETE",
        "path": "/sites/{site_id}/events/{event_id}",
        "run": _smoke_case_19,
    },
    {
        "operation": "wipe",
        "method": "DELETE",
        "path": "/sites/{site_id}/events/{event_id}/data",
        "run": _smoke_case_20,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/sites/{site_id}/milestones",
        "label": "required params",
        "run": _smoke_case_21,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/sites/{site_id}/milestones",
        "label": "all params",
        "run": _smoke_case_22,
    },
    {
        "operation": "create",
        "method": "POST",
        "path": "/sites/{site_id}/milestones",
        "run": _smoke_case_23,
    },
    {
        "operation": "retrieve",
        "method": "GET",
        "path": "/sites/{site_id}/milestones/{milestone_id}",
        "run": _smoke_case_24,
    },
    {
        "operation": "update",
        "method": "POST",
        "path": "/sites/{site_id}/milestones/{milestone_id}",
        "run": _smoke_case_25,
    },
    {
        "operation": "delete",
        "method": "DELETE",
        "path": "/sites/{site_id}/milestones/{milestone_id}",
        "run": _smoke_case_26,
    },
    {
        "operation": "aggregation",
        "method": "GET",
        "path": "/aggregations",
        "label": "required params",
        "run": _smoke_case_27,
    },
    {
        "operation": "aggregation",
        "method": "GET",
        "path": "/aggregations",
        "label": "all params",
        "run": _smoke_case_28,
    },
    {
        "operation": "currentVisitors",
        "method": "GET",
        "path": "/current_visitors",
        "run": _smoke_case_29,
    },
]

DEFAULT_SMOKE_CONCURRENCY = 32


def _selected_cases() -> list[SmokeCase]:
    filter_value = os.environ.get("SCALAR_SMOKE_FILTER")
    needles = [needle.strip() for needle in filter_value.split(",") if needle.strip()] if filter_value else []
    if not needles:
        return cases
    return [case for case in cases if any(needle in case["operation"] or needle in case["path"] for needle in needles)]


def _smoke_concurrency(case_count: int) -> int:
    override = os.environ.get("SCALAR_SMOKE_CONCURRENCY")
    if override:
        try:
            parsed = int(override)
            if parsed > 0:
                return min(parsed, case_count)
        except ValueError:
            pass
    return min(DEFAULT_SMOKE_CONCURRENCY, case_count)


def _case_identity(case: SmokeCase) -> SmokeResult:
    # `label` is carried through only when the operation contributed both of its calls, so a
    # single-case operation reports exactly as it did before there were two.
    identity: SmokeResult = {
        "operation": case["operation"],
        "method": case["method"],
        "path": case["path"],
    }
    label = case.get("label")
    if label:
        identity["label"] = label
    return identity


def _run_case(case: SmokeCase) -> SmokeResult:
    started_at = time.monotonic()
    identity = _case_identity(case)
    try:
        case["run"]()
        return {
            **identity,
            "status": "passed",
            "durationMs": int((time.monotonic() - started_at) * 1000),
        }
    except Exception:
        return {
            **identity,
            "status": "failed",
            "durationMs": int((time.monotonic() - started_at) * 1000),
            "error": traceback.format_exc(),
        }


def main() -> None:
    selected = _selected_cases()
    if selected:
        # Keep enough parallelism to catch generated SDK concurrency bugs without overwhelming
        # CI runners or the in-process mock server for large SDKs.
        with ThreadPoolExecutor(max_workers=_smoke_concurrency(len(selected))) as executor:
            results = list(executor.map(_run_case, selected))
    else:
        results = []
    failed = [result for result in results if result["status"] == "failed"]

    report_path = os.environ.get("SCALAR_SMOKE_REPORT")
    if report_path:
        Path(report_path).write_text(
            json.dumps({"total": len(results), "failed": len(failed), "results": results}), encoding="utf-8"
        )
    else:
        for result in results:
            suffix = f" [{result['label']}]" if result.get("label") else ""
            if result["status"] == "passed":
                print(
                    f"PASS {result['operation']}{suffix} ({result['method']} {result['path']}) {result['durationMs']}ms"
                )
            else:
                print(
                    f"FAIL {result['operation']}{suffix} ({result['method']} {result['path']})\n{result.get('error', '')}",
                    file=sys.stderr,
                )
        if not results:
            print("No code samples ran (empty SDK or a SCALAR_SMOKE_FILTER that matched nothing).", file=sys.stderr)
        else:
            print(f"\n{len(results) - len(failed)}/{len(results)} samples passed")

    if failed or not results:
        sys.exit(1)


if __name__ == "__main__":
    main()
