import os
from typing import List

from dismod.dependency import DependencyContainer

_CLUSTER_DOT_SUBGRAPH_TEMPLATE = """
    subgraph "%s" {
        %s
        label = "%s";
    }
"""

CLUSTER_DOT_TEMPLATE = """
digraph "%s" {
    graph [compound=true engine=sfdp];

    %s
}
"""

DOT_TEMPLATE = """
digraph "%s" {
    graph [compound=true engine=sfdp];
    %s
}
"""


def render_cluster_files(
    project_name: str,
    dependency_containers: List[DependencyContainer],
) -> None:
    """ """
    if not os.path.exists("renders"):
        os.mkdir("renders")

    subgraphs = ""

    for dependency in dependency_containers:
        content = ""
        for _import in dependency.imports:
            basename = dependency.basename.rsplit(".", 1)[0]
            if _import["from_statement"] is None:
                content += f"""
\t"{basename}" -> "{_import["import_statements"][0]}";
"""

            if _import["from_statement"] is not None:
                content += f"""
\t"{basename}" -> "{_import["from_statement"]}";
"""
                for statement in _import["import_statements"]:
                    content += f"""
\t"{_import["from_statement"]}" -> "{statement}";
"""
        subgraph = _CLUSTER_DOT_SUBGRAPH_TEMPLATE % (
            basename,
            content,
            dependency.basename,
        )

        subgraphs += subgraph

    with open(f"renders/{project_name}.dot", mode="w") as file:
        file.write(CLUSTER_DOT_TEMPLATE % (project_name, subgraphs))


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
\t"{dependency.basename}" -> "{_import["import_statements"][0]}"
"""

            if _import["from_statement"] is not None:
                content += f"""
\t"{dependency.basename}" -> "{_import["from_statement"]}"
"""
                for statement in _import["import_statements"]:
                    content += f"""
\t"{_import["from_statement"]}" -> "{statement}"
"""

        with open(f"renders/{dependency.basename}.dot", mode="w") as file:
            file.write(DOT_TEMPLATE % (project_name, content))
