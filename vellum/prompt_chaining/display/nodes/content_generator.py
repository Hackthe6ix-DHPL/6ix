from uuid import UUID

from vellum_ee.workflows.display.editor import NodeDisplayData, NodeDisplayPosition
from vellum_ee.workflows.display.nodes import BaseInlinePromptNodeDisplay
from vellum_ee.workflows.display.nodes.types import NodeOutputDisplay, PortDisplayOverrides

from ...nodes.content_generator import ContentGenerator


class ContentGeneratorDisplay(BaseInlinePromptNodeDisplay[ContentGenerator]):
    label = "Content Generator"
    node_id = UUID("ea482f20-831e-478f-8c6d-9107c17fcca6")
    output_id = UUID("2adaa2e8-49d3-41be-b9c2-40b820267145")
    array_output_id = UUID("74846d85-fad0-4443-9f99-8f2cbc052ef0")
    target_handle_id = UUID("58838d6b-7b97-4914-8e7b-3837de70d7db")
    node_input_ids_by_name = {
        "prompt_inputs.outline": UUID("5fa4f798-4a47-4290-8347-1b38398bba6f"),
        "prompt_inputs.industry": UUID("080cb29a-a379-4636-9e49-8ed4ab7f67ba"),
        "prompt_inputs.audience": UUID("aaf3ac4d-a076-4978-b1ca-cad75115d202"),
    }
    attribute_ids_by_name = {"ml_model": UUID("3f7d516e-13f4-40c7-a42a-ce8da3cc06ff")}
    output_display = {
        ContentGenerator.Outputs.text: NodeOutputDisplay(id=UUID("2adaa2e8-49d3-41be-b9c2-40b820267145"), name="text"),
        ContentGenerator.Outputs.results: NodeOutputDisplay(
            id=UUID("74846d85-fad0-4443-9f99-8f2cbc052ef0"), name="results"
        ),
        ContentGenerator.Outputs.json: NodeOutputDisplay(id=UUID("3b3b0984-1a68-4969-9125-149657b293c1"), name="json"),
    }
    port_displays = {
        ContentGenerator.Ports.default: PortDisplayOverrides(id=UUID("23163100-e81c-41b2-b3c4-d8f2bd2eda18"))
    }
    display_data = NodeDisplayData(position=NodeDisplayPosition(x=1474, y=0), width=553, height=305)
