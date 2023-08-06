import os
from typing import List

from dismod.dependency import DependencyContainer


DOT_TEMPLATE = """
digraph "%s" {
    %s
}
"""


def render_multiple_files(
    project_name: str,
    dependency_containers: List[DependencyContainer],
) -> None:
    if not os.path.exists("renders"):
        os.mkdir("renders")

    for dependency in dependency_containers:
        content = ""
        for _import in dependency.imports:
            if _import["from_statement"] is None:
                content += f"""
    "{dependency.basename}" -> "{_import["import_statements"][0]}" """

            if _import["from_statement"] is not None:
                content += f"""
    "{dependency.basename}" -> "{_import["from_statement"]}" """
                for statement in _import["import_statements"]:
                    content += f"""
    "{_import["from_statement"]}" -> "{statement}" """

        with open(f"renders/{dependency.basename}.dot", mode="w") as file:
            file.write(DOT_TEMPLATE % (project_name, content))
