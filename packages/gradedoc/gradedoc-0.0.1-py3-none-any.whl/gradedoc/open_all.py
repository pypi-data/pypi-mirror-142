"""Open all documents in preparation for grading."""

from __future__ import annotations

from typing import Optional

import docxrev
import fire
from win32com.client import constants

from gradedoc import shared
from gradedoc.shared import Path


def open_all(directory: Optional[Path] = None):
    """Open all documents in preparation for grading.

    Open all documents in `directory` as specified in :py:func:`shared.get_paths`.

    Parameters
    ----------
    directory
        The directory containing the documents.
    """

    (paths, _) = shared.get_paths(directory)
    for path in paths:
        document = docxrev.Document(path, save_on_exit=False, close_on_exit=False)
        with document:
            # Open the revisions pane.
            document.com.ActiveWindow.View.SplitSpecial = constants.wdPaneRevisions


if __name__ == "__main__":
    fire.Fire(open_all)
