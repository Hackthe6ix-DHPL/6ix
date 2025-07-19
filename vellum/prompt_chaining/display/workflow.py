from uuid import UUID

from vellum_ee.workflows.display.base import (
    EdgeDisplay,
    EntrypointDisplay,
    WorkflowDisplayData,
    WorkflowDisplayDataViewport,
    WorkflowInputsDisplay,
    WorkflowMetaDisplay,
    WorkflowOutputDisplay,
)
from vellum_ee.workflows.display.editor import NodeDisplayData, NodeDisplayPosition
from vellum_ee.workflows.display.workflows import BaseWorkflowDisplay

from ..inputs import Inputs
from ..nodes.content_generator import ContentGenerator
from ..nodes.final_output import FinalOutput
from ..nodes.outline_creator import OutlineCreator
from ..nodes.topic_researcher import TopicResearcher
from ..workflow import Workflow


class WorkflowDisplay(BaseWorkflowDisplay[Workflow]):
    workflow_display = WorkflowMetaDisplay(
        entrypoint_node_id=UUID("ba17bf7b-d636-417a-927e-2021950b515a"),
        entrypoint_node_source_handle_id=UUID("be35a6be-86d7-4b34-97e5-0b1ee505fa63"),
        entrypoint_node_display=NodeDisplayData(position=NodeDisplayPosition(x=0, y=355), width=124, height=48),
        display_data=WorkflowDisplayData(
            viewport=WorkflowDisplayDataViewport(x=196.6060641381879, y=239.53574816998406, zoom=0.48577909614377934)
        ),
    )
    inputs_display = {
        Inputs.audience: WorkflowInputsDisplay(
            id=UUID("60540c9e-a9fb-491e-9cfa-537048f3f20b"), name="audience", color="pink"
        ),
        Inputs.industry: WorkflowInputsDisplay(
            id=UUID("1f2a7788-c9a8-4e01-98e8-cb5ad9ab7a54"), name="industry", color="pink"
        ),
    }
    entrypoint_displays = {
        TopicResearcher: EntrypointDisplay(
            id=UUID("ba17bf7b-d636-417a-927e-2021950b515a"),
            edge_display=EdgeDisplay(id=UUID("7c2e890d-fb51-47c2-b97b-15c0a9480ea4")),
        )
    }
    edge_displays = {
        (TopicResearcher.Ports.default, OutlineCreator): EdgeDisplay(id=UUID("bbf7a6ad-f41d-4254-9425-44d7b3880099")),
        (OutlineCreator.Ports.default, ContentGenerator): EdgeDisplay(id=UUID("82866bbb-a121-4f81-af65-a3b9219746d2")),
        (ContentGenerator.Ports.default, FinalOutput): EdgeDisplay(id=UUID("8d6fe77a-53ae-411f-a0a4-5910e6ca2fc1")),
    }
    output_displays = {
        Workflow.Outputs.final_output: WorkflowOutputDisplay(
            id=UUID("a9351c63-fc50-4657-a5d4-c87cf7fb4387"), name="final-output"
        )
    }
