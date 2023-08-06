from pathlib import Path
from typing import Union

from arrow_bpmn.parser.xml.xml_element import XMLElement

BpmnSource = Union[Path, str, bytes]
Element = Union[XMLElement, dict]
