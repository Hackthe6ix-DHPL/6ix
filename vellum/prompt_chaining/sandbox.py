from vellum.workflows.sandbox import WorkflowSandboxRunner

from .inputs import Inputs
from .workflow import Workflow

if __name__ != "__main__":
    raise Exception("This file is not meant to be imported")


runner = WorkflowSandboxRunner(
    workflow=Workflow(),
    inputs=[
        Inputs(audience="Working professionals targeting midsize businesses", industry="Marketing Technology"),
        Inputs(
            audience="C Suite Executives wanting to increase their pace of AI product development without compromising quality. ",
            industry="Artificial Intelligence + B2B SaaS",
        ),
    ],
)

runner.run()
