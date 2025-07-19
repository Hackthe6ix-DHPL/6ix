from uuid import UUID

from vellum_ee.workflows.display.editor import NodeDisplayData, NodeDisplayPosition
from vellum_ee.workflows.display.nodes import BaseNoteNodeDisplay

from ...nodes.note import Note


class NoteDisplay(BaseNoteNodeDisplay[Note]):
    label = "Note"
    node_id = UUID("8f1c249d-3146-49f3-a9f1-e6710093a5fa")
    text = "Guided Walkthrough\n\nhttps://www.loom.com/share/d032f3f6aeb44a8fbf8fe93c8bcf3775"
    style = None
    display_data = NodeDisplayData(
        position=NodeDisplayPosition(x=15.307375506359904, y=-765.4517976774526), width=731, height=670
    )
