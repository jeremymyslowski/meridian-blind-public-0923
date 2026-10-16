"""QA fixture: TODO markers for code search (2026-10-16)."""

# TODO(qa): add pagination to task export
def export_tasks(tasks):
    # TODO(qa): include archived tasks behind a flag (see issue #7)
    return [t for t in tasks if not t.get("archived")]

# TODO(qa): replace fixed retry delay with exponential backoff (issue #11)
RETRY_DELAY_SECONDS = 5
