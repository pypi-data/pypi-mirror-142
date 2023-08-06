from typing import List

import graphviz

from dismod.dependency import DependencyContainer


def render_multiple_files(
    dependency_containers: List[DependencyContainer],
) -> None:
    """ """
    for tree in dependency_containers:
        dot = graphviz.Digraph(f"Dependency graph for {tree.basename}.")
        dot.node(tree.basename)
        for _import in tree.imports:
            if _import["from_statement"] is None:
                dot.edge(tree.basename, _import["import_statements"][0])

            if _import["from_statement"] is not None:
                dot.edge(tree.basename, _import["from_statement"])

                for statement in _import["import_statements"]:
                    dot.edge(_import["from_statement"], statement)
        dot.render(f"renders/{tree.basename}.gv", view=False)
