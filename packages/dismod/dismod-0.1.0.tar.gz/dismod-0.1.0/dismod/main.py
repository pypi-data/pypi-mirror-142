import argparse
from typing import List

from dismod.dependency import DependencyContainer
from dismod.dot import render_multiple_files
from dismod.instruction import get_import_instructions
from dismod.instruction import get_instructions_from_file
from dismod.instruction import parse_instructions
from dismod.utils import collect_files_in_module


def create_argument_parser() -> argparse.ArgumentParser:
    """ """
    parser = argparse.ArgumentParser(
        prog="dismod",
        description="Generate dependency graphs for your codebase.",
    )

    parser.add_argument(
        "filepath",
        metavar="filepath",
        type=str,
        help="The path to the source code in your project.",
    )

    return parser


def get_import_dependency_list(files: List[str]) -> List[DependencyContainer]:
    """ """
    import_dependency_list = []

    for file in files:
        instructions = get_instructions_from_file(filepath=file)
        all_instructions = get_import_instructions(instructions=instructions)
        # Early exit, we don't care about files that don't have any import
        # statements, e.g; __init__.py or other simple file that has no import
        if not all_instructions:
            continue

        instructions_normalized = parse_instructions(
            instructions=all_instructions,
        )

        file_import_dependencies = DependencyContainer(filepath=file)
        file_import_dependencies.add_import(instructions_normalized)
        import_dependency_list.append(file_import_dependencies)
    return import_dependency_list


def main() -> int:
    """ """
    parser = create_argument_parser()
    args = parser.parse_args()

    # Collect all files that lives in the specified filepath
    files = collect_files_in_module(filepath=args.filepath)
    # Get a list of import dependencies for each file
    list_of_import_dependencies = get_import_dependency_list(files=files)

    # Render the results
    render_multiple_files(dependency_containers=list_of_import_dependencies)

    return 0
