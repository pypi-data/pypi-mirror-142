"""Public API for interacting with Sciagraph."""

from datetime import datetime, timezone
from typing import Optional
import logging

__all__ = ["ReportResult"]

_LOGGER = logging.getLogger("sciagraph")

_DOWNLOAD_INSTRUCTIONS = """\
Successfully uploaded the Sciagraph profiling report.

Job start time: {job_time}
Job ID: {job_id}

To see the resulting profiling report, run the following on
Linux/Windows/macOS, Python 3.7+:

pip install --user sciagraph-report
python -m sciagraph_report download {download_key} {decryption_key}
"""


class ReportResult:
    """
    Information about how to download uploaded profiling report.

    This will get logged by Sciagraph when profiling is finished.
    """

    def __init__(
        self, job_time: datetime, job_id: str, download_key: str, decryption_key: str
    ):
        self.job_time = job_time.isoformat()
        self.job_id = job_id
        self.download_key = download_key
        self.decryption_key = decryption_key

    def __str__(self):
        return _DOWNLOAD_INSTRUCTIONS.format(**self.__dict__)


def _log_result(
    job_secs_since_epoch: int,
    job_id: Optional[str],
    download_key: str,
    decryption_key: str,
):
    """Log a ``ReportResult``."""
    if job_id is None:
        job_id = "Unknown, see docs to learn how to set this"
    job_time = datetime.fromtimestamp(job_secs_since_epoch, timezone.utc)
    report = ReportResult(job_time, job_id, download_key, decryption_key)
    _LOGGER.warning(report)
