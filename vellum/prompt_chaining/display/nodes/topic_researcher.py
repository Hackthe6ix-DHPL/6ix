from uuid import UUID

from vellum_ee.workflows.display.editor import NodeDisplayData, NodeDisplayPosition
from vellum_ee.workflows.display.nodes import BaseInlinePromptNodeDisplay
from vellum_ee.workflows.display.nodes.types import NodeOutputDisplay, PortDisplayOverrides

from ...nodes.topic_researcher import TopicResearcher


class TopicResearcherDisplay(BaseInlinePromptNodeDisplay[TopicResearcher]):
    label = "Topic Researcher"
    node_id = UUID("ae010bf8-2f22-4ff1-85c0-3ae4dbf7a8d5")
    output_id = UUID("5f105895-50a2-44eb-aaee-2dd8ab21930b")
    array_output_id = UUID("6b2d5ed1-b292-45a6-a6f5-2cfe42e7e210")
    target_handle_id = UUID("f968efa0-bcb6-432e-a821-bc589ed17d8b")
    node_input_ids_by_name = {
        "prompt_inputs.audience": UUID("a55d235f-484f-4836-a422-3a7cf95fbaf6"),
        "prompt_inputs.industry": UUID("a6cc0f8a-3788-471f-8d93-5db7d0eac674"),
    }
    attribute_ids_by_name = {"ml_model": UUID("854dc284-5d6b-422b-a28a-aa6cbd4d6075")}
    output_display = {
        TopicResearcher.Outputs.text: NodeOutputDisplay(id=UUID("5f105895-50a2-44eb-aaee-2dd8ab21930b"), name="text"),
        TopicResearcher.Outputs.results: NodeOutputDisplay(
            id=UUID("6b2d5ed1-b292-45a6-a6f5-2cfe42e7e210"), name="results"
        ),
        TopicResearcher.Outputs.json: NodeOutputDisplay(id=UUID("b5b3d211-4d69-4868-b4b9-23dcdc3ceae5"), name="json"),
    }
    port_displays = {
        TopicResearcher.Ports.default: PortDisplayOverrides(id=UUID("4df00227-56c3-4b73-a585-09f1e78e19db"))
    }
    display_data = NodeDisplayData(position=NodeDisplayPosition(x=254, y=27), width=553, height=252)
