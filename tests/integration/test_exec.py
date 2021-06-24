__copyright__ = "Copyright (c) 2020-2021 Jina AI Limited. All rights reserved."
__license__ = "Apache-2.0"

from jina import Flow, Document
from jinahub.crafter.pdf_crafter import PDFCrafter


def test_exec():
    f = Flow().add(uses=MyDummyExecutor)
    with f:
        resp = f.post(on='/test', inputs=Document(), return_results=True)
        assert resp is not None
