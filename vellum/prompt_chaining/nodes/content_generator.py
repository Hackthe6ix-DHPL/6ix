from vellum import ChatMessagePromptBlock, JinjaPromptBlock, PromptParameters
from vellum.workflows.nodes.displayable import InlinePromptNode

from ..inputs import Inputs
from .outline_creator import OutlineCreator


class ContentGenerator(InlinePromptNode):
    ml_model = "gpt-4o-mini"
    blocks = [
        ChatMessagePromptBlock(
            chat_role="SYSTEM",
            blocks=[
                JinjaPromptBlock(
                    template="""\
You are an expert content writer specializing in {{ industry }} for {{ audience }}. Your writing style is engaging, informative, and includes relevant examples while maintaining a conversational tone.
Provide structured and insightful information based on the provided schema.

Guidelines:
1. Select the highest-rated topic as the main topic
2. Write in a conversational, friendly tone
3. Follow the outline sections exactly as provided
4. Include relevant examples and statistics
5. Break up text with subheadings
6. Target length: 600 words
7. Include a compelling introduction and strong call-to-action

No preamble/postamble
{#- No preamble/postamble asserts that the model shouldn\'t respond with \"I\'ve created ... for you, here it is!\" at the start of its response -#}\
"""
                )
            ],
        ),
        ChatMessagePromptBlock(
            chat_role="USER",
            blocks=[
                JinjaPromptBlock(
                    template="""\
Using the following <outline>, create a comprehensive blog post:
<outline>
{{ outline }}
</outline>\
"""
                )
            ],
        ),
    ]
    prompt_inputs = {
        "outline": OutlineCreator.Outputs.text,
        "industry": Inputs.industry,
        "audience": Inputs.audience,
    }
    parameters = PromptParameters(
        stop=[],
        temperature=0,
        max_tokens=1250,
        top_p=1,
        top_k=0,
        frequency_penalty=0,
        presence_penalty=0,
        logit_bias={},
        custom_parameters=None,
    )
