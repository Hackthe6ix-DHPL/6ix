from vellum import (
    ChatMessagePromptBlock,
    PlainTextPromptBlock,
    PromptParameters,
    PromptSettings,
    RichTextPromptBlock,
    VariablePromptBlock,
)
from vellum.workflows.nodes.displayable import InlinePromptNode

from ..inputs import Inputs
from .topic_researcher import TopicResearcher


class OutlineCreator(InlinePromptNode):
    ml_model = "gpt-4o-mini"
    blocks = [
        ChatMessagePromptBlock(
            chat_role="SYSTEM",
            blocks=[
                RichTextPromptBlock(
                    blocks=[
                        PlainTextPromptBlock(
                            text="""\
You are a content outline specialist. 
You will receive a list of <topics> with ratings to help you create a detailed, engaging outline targeted at \
"""
                        ),
                        VariablePromptBlock(input_variable="audience"),
                        PlainTextPromptBlock(
                            text="""\
.

You will:
1. Select the highest-rated topic(s)
2. Create a detailed outline for a 1000-word blog post (to be written later)
3. Include specific sections for real-world examples and actionable tips
4. Add placeholders for relevant statistics or case studies

No preamble/postamble\
"""
                        ),
                    ]
                )
            ],
        ),
        ChatMessagePromptBlock(
            chat_role="USER",
            blocks=[
                RichTextPromptBlock(
                    blocks=[
                        PlainTextPromptBlock(
                            text="""\
Here are the rated topics:
<topics>
\
"""
                        ),
                        VariablePromptBlock(input_variable="topics"),
                        PlainTextPromptBlock(
                            text="""\

</topics>\
"""
                        ),
                    ]
                ),
                RichTextPromptBlock(
                    state="DISABLED",
                    blocks=[
                        PlainTextPromptBlock(
                            text="""\
This Prompt Block is disabled and will not impact the prompt.

It\'s research that suggests using XML tags like <topics> above can improve model performance. Intuitively, it helps models better understand the beginning and end of long pieces of context. It\'s also helpful for team collaboration while prompt engineering.\
"""
                        )
                    ],
                ),
            ],
        ),
    ]
    prompt_inputs = {
        "audience": Inputs.audience,
        "topics": TopicResearcher.Outputs.text,
    }
    parameters = PromptParameters(
        stop=[],
        temperature=0,
        max_tokens=500,
        top_p=1,
        top_k=0,
        frequency_penalty=0,
        presence_penalty=0,
        logit_bias={},
        custom_parameters=None,
    )
    settings = PromptSettings(stream_enabled=True)
