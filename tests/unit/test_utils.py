import pytest
from deepClassifier.utils import read_yaml
from pathlib import Path
import os
from box import ConfigBox

##Dummy files for testing
yaml_files=[
    "testsdata/empty.yaml",
    "testsdata/demo.yaml"
]

def test_read_yaml_empty():
    with pytest.raises(ValueError):
        read_yaml(Path(yaml_files[0]))