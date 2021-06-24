__copyright__ = "Copyright (c) 2020-2021 Jina AI Limited. All rights reserved."
__license__ = "Apache-2.0"

import os

from PIL import Image
from jina import Flow, Document, DocumentArray
from jinahub.crafter.pdf_crafter import PDFCrafter


def doc_generator(uri, buffer):
    if uri:
        doc = DocumentArray([Document(uri=uri, mime_type='application/pdf')])
    else:
        doc = DocumentArray([Document(buffer=buffer, mime_type='application/pdf')])
    return doc


def test_flow(test_dir, input_pdf, expected_text):
    flow = Flow().add(uses=PDFCrafter)
    for uri, buffer in input_pdf['img_text']:
        doc = doc_generator(uri, buffer)
        with flow:
            results = flow.post(
                on='/test',
                inputs=doc,
                return_results=True
            )

            assert len(results[0].docs) == 1
            chunks = results[0].docs[0].chunks
            assert len(chunks) == 3
            for idx, c in enumerate(chunks[:2]):
                with Image.open(os.path.join(test_dir, f'data/test_img_{idx}.jpg')) as img:
                    blob = chunks[idx].blob
                    assert chunks[idx].mime_type == 'image/*'
                    assert blob.shape[1], blob.shape[0] == img.size
                    if idx == 0:
                        assert blob.shape == (660, 1024, 3)
                    if idx == 1:
                        assert blob.shape == (626, 1191, 3)

                # Check text
                assert chunks[2].text == expected_text
                assert chunks[2].mime_type == 'text/plain'
