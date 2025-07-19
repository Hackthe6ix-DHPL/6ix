from vellum.workflows import BaseWorkflow
from vellum.workflows.state import BaseState

from .inputs import Inputs
from .nodes.content_generator import ContentGenerator
from .nodes.final_output import FinalOutput
from .nodes.note import Note
from .nodes.outline_creator import OutlineCreator
from .nodes.topic_researcher import TopicResearcher


class Workflow(BaseWorkflow[Inputs, BaseState]):
    graph = TopicResearcher >> OutlineCreator >> ContentGenerator >> FinalOutput
    unused_graphs = {Note}

    class Outputs(BaseWorkflow.Outputs):
        final_output = FinalOutput.Outputs.value
