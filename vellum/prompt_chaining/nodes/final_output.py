from vellum.workflows.nodes.displayable import FinalOutputNode
from vellum.workflows.state import BaseState

from .content_generator import ContentGenerator


class FinalOutput(FinalOutputNode[BaseState, str]):
    class Outputs(FinalOutputNode.Outputs):
        value = ContentGenerator.Outputs.text
