import os
import sys
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from bioLOLPython.bio.sequence import BioSeq


def test_gc_content_mixed_case():
    seq = BioSeq("aTgC")
    result = seq.gc_content()
    assert "50.00%" in result


def test_gc_content_empty_sequence():
    seq = BioSeq("")
    result = seq.gc_content()
    assert "0.00%" in result
