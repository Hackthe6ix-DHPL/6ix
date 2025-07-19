from uuid import UUID

from vellum_ee.workflows.display.editor import NodeDisplayData, NodeDisplayPosition
from vellum_ee.workflows.display.nodes import BaseFinalOutputNodeDisplay
from vellum_ee.workflows.display.nodes.types import NodeOutputDisplay

from ...nodes.final_output import FinalOutput


class FinalOutputDisplay(BaseFinalOutputNodeDisplay[FinalOutput]):
    label = "Final Output"
    node_id = UUID("9ad957f3-24ca-41e6-8c9a-3b1f3b7665f9")
    target_handle_id = UUID("76f4e297-b12c-4bf2-87b6-4ea93b3c0bcd")
    output_name = "final-output"
    node_input_ids_by_name = {"node_input": UUID("e03c0945-da25-4402-b880-6c0bacd4b755")}
    output_display = {
        FinalOutput.Outputs.value: NodeOutputDisplay(id=UUID("a9351c63-fc50-4657-a5d4-c87cf7fb4387"), name="value")
    }
    display_data = NodeDisplayData(position=NodeDisplayPosition(x=2084, y=34), width=521, height=257)
