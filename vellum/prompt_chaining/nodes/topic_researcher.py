from vellum import (
    ChatMessagePromptBlock,
    PlainTextPromptBlock,
    PromptParameters,
    RichTextPromptBlock,
    VariablePromptBlock,
)
from vellum.workflows.nodes.displayable import InlinePromptNode

from ..inputs import Inputs


class TopicResearcher(InlinePromptNode):
    ml_model = "gpt-4o-mini"
    blocks = [
        ChatMessagePromptBlock(
            chat_role="SYSTEM",
            blocks=[
                RichTextPromptBlock(
                    blocks=[
                        PlainTextPromptBlock(
                            text="""\
You are a content strategist who identifies engaging blog topics for businesses to help boost their online presence and SEO performance. 

You will suggest 3 blog topics for:
Industry: \
"""
                        ),
                        VariablePromptBlock(input_variable="industry"),
                        PlainTextPromptBlock(
                            text="""\

Target Audience: \
"""
                        ),
                        VariablePromptBlock(input_variable="audience"),
                        PlainTextPromptBlock(
                            text="""\


For each topic, provide: 
1. A compelling title
2. A brief description of the angle to take to cater to the target audience
3. A rating from 1-10 with an explanation based on the following criteria:
- Relevance to target audience
- Current industry trends
- SEO potential
- Competitive gap analysis

No preamble/postamble\
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

The line above that says \"no preamble/postamble\" asserts that the model shouldn\'t respond with \"I\'ve created ... for you, here it is!\" at the start of its response.\
"""
                        )
                    ],
                ),
            ],
        ),
    ]
    prompt_inputs = {
        "audience": Inputs.audience,
        "industry": Inputs.industry,
    }
    parameters = PromptParameters(
        stop=[],
        temperature=0,
        max_tokens=600,
        top_p=1,
        top_k=0,
        frequency_penalty=0,
        presence_penalty=0,
        logit_bias={},
        custom_parameters=None,
    )
