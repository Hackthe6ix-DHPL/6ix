from uuid import UUID

from vellum_ee.workflows.display.editor import NodeDisplayData, NodeDisplayPosition
from vellum_ee.workflows.display.nodes import BaseInlinePromptNodeDisplay
from vellum_ee.workflows.display.nodes.types import NodeOutputDisplay, PortDisplayOverrides

from ...nodes.outline_creator import OutlineCreator


class OutlineCreatorDisplay(BaseInlinePromptNodeDisplay[OutlineCreator]):
    label = "Outline Creator"
    node_id = UUID("4c353599-c81e-45f5-ae5e-83ee93a122d5")
    output_id = UUID("a76b93ec-0d40-4af0-b4bd-1ac7e3296154")
    array_output_id = UUID("cbd2a674-8610-42fc-998d-d82a5776a9e6")
    target_handle_id = UUID("843a8727-2773-4022-98da-e7fc8133eea4")
    node_input_ids_by_name = {
        "prompt_inputs.audience": UUID("fbe54af0-619c-46c1-863f-e187c099d130"),
        "prompt_inputs.topics": UUID("a58d3ad9-6abb-49e5-882c-f29f6966362b"),
    }
    output_display = {
        OutlineCreator.Outputs.text: NodeOutputDisplay(id=UUID("a76b93ec-0d40-4af0-b4bd-1ac7e3296154"), name="text"),
        OutlineCreator.Outputs.results: NodeOutputDisplay(
            id=UUID("cbd2a674-8610-42fc-998d-d82a5776a9e6"), name="results"
        ),
        OutlineCreator.Outputs.json: NodeOutputDisplay(id=UUID("147ecd86-5d42-4c03-880f-e8978569a564"), name="json"),
    }
    port_displays = {
        OutlineCreator.Ports.default: PortDisplayOverrides(id=UUID("bbf79c3f-d0d8-4aa9-b359-5124e998871b"))
    }
    display_data = NodeDisplayData(position=NodeDisplayPosition(x=864, y=27), width=553, height=252)
