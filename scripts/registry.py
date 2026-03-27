#!/usr/bin/env python3
import os
import ast
import argparse
from dataclasses import dataclass
from typing import List, Dict, Tuple, Any

@dataclass
class Symbol:
    name: str
    file_path: str
    line_number: int
    description: str
    signature: str
    type: str  # 'function' or 'class'

def clean_docstring(docstring: str) -> str:
    """Extract the first meaningful paragraph/line from a docstring."""
    if not docstring:
        return "No docstring provided."
    lines = [line.strip() for line in docstring.split('\n') if line.strip()]
    return lines[0] if lines else "No docstring provided."

def _format_ast_node(node: ast.AST | None) -> str:
    if node is None:
        return ""
    try:
        return ast.unparse(node)
    except Exception:
        return ""


def _format_arg(arg: ast.arg, default: ast.expr | None = None) -> str:
    rendered = arg.arg
    annotation = _format_ast_node(arg.annotation)
    if annotation:
        rendered += f": {annotation}"
    if default is not None:
        default_text = _format_ast_node(default)
        rendered += f" = {default_text}" if default_text else " = ..."
    return rendered


def get_signature(node: Any, lines: List[str] | None = None) -> str:
    """Extract and format the signature of a function node."""
    _ = lines
    try:
        args = node.args
        rendered_params: list[str] = []

        positional = list(args.posonlyargs) + list(args.args)
        positional_defaults = [None] * (len(positional) - len(args.defaults)) + list(args.defaults)

        for idx, arg in enumerate(args.posonlyargs):
            rendered_params.append(_format_arg(arg, positional_defaults[idx]))
        if args.posonlyargs:
            rendered_params.append("/")

        for offset, arg in enumerate(args.args, start=len(args.posonlyargs)):
            rendered_params.append(_format_arg(arg, positional_defaults[offset]))

        if args.vararg is not None:
            rendered_params.append(_format_arg(args.vararg).join(["*", ""]))
        elif args.kwonlyargs:
            rendered_params.append("*")

        for arg, default in zip(args.kwonlyargs, args.kw_defaults):
            rendered_params.append(_format_arg(arg, default))

        if args.kwarg is not None:
            rendered_params.append(f"**{_format_arg(args.kwarg)}")

        signature = f"({', '.join(rendered_params)})"
        ret = _format_ast_node(getattr(node, "returns", None))
        if ret:
            signature += f" -> {ret}"
        return signature
    except Exception:
        pass
    return "Signature unavailable"

def get_symbols(file_path: str) -> List[Symbol]:
    """Parse a python file and extract public classes and functions."""
    symbols = []
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        tree = ast.parse(content)
    except (SyntaxError, FileNotFoundError, UnicodeDecodeError):
        return []

    lines = content.splitlines()

    for node in tree.body:
        # Handle Top-Level Functions and Classes
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            # Skip private members
            if node.name.startswith('_'):
                continue
            
            is_class = isinstance(node, ast.ClassDef)
            symbol_type = 'class' if is_class else 'function'
            
            symbols.append(Symbol(
                name=node.name,
                file_path=file_path,
                line_number=node.lineno,
                description=clean_docstring(ast.get_docstring(node)),
                signature="Class Definition" if is_class else get_signature(node, lines),
                type=symbol_type
            ))
            
            # Handle Public Class Methods
            if is_class:
                for sub_node in node.body:
                    if isinstance(sub_node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                        if sub_node.name.startswith('_'):
                            continue
                        
                        symbols.append(Symbol(
                            name=f"{node.name}.{sub_node.name}",
                            file_path=file_path,
                            line_number=sub_node.lineno,
                            description=clean_docstring(ast.get_docstring(sub_node)),
                            signature=get_signature(sub_node, lines),
                            type='function'
                        ))
    return symbols

def generate_markdown(sections: Dict[str, List[Tuple[str, List[Symbol]]]], total_count: int):
    """Print the formatted registry in Markdown to stdout."""
    print("# Project Registry\n")
    print("Public callable registry for the current codebase.\n")
    print("**Criteria:** Public top-level functions + public class methods (private helpers starting with `_` are excluded).\n")
    
    print("## Summary\n")
    print(f"- Total indexed callables: **{total_count}**")
    for sec_name, items in sorted(sections.items()):
        count = sum(len([s for s in syms if s.type == 'function' or '.' in s.name]) for _, syms in items)
        print(f"- `{sec_name.lower()}`: {count}")
    print()

    for section_name in sorted(sections.keys()):
        print(f"## {section_name}\n")
        sections[section_name].sort(key=lambda x: x[0])
        for path, symbols in sections[section_name]:
            print(f"### `{path}`\n")
            print("| Symbol Name | Location | Description | Signature |")
            print("|---|---|---|---|")
            for sym in symbols:
                # Escape pipe characters in signatures for markdown table safety
                safe_sig = sym.signature.replace('|', '\\|')
                print(f"| `{sym.name}` | `{sym.file_path}:{sym.line_number}` | {sym.description} | `{safe_sig}` |")
            print()

def main():
    parser = argparse.ArgumentParser(description="Automated Python Project Registry Generator")
    parser.add_argument("--path", default="./src", help="Directory to scan (default: ./src)")
    parser.add_argument("--exclude", nargs='+', default=['tests', '__pycache__', 'venv'], help="Directories to exclude")
    args = parser.parse_args()

    if not os.path.exists(args.path):
        print(f"Error: Path '{args.path}' does not exist.")
        return

    sections: Dict[str, List[Tuple[str, List[Symbol]]]] = {}
    all_callables_count = 0

    for root, dirs, files in os.walk(args.path):
        # Filter excluded directories in-place
        dirs[:] = [d for d in dirs if d not in args.exclude]
        
        for file in files:
            if file.endswith('.py') and not file.startswith('__'):
                path = os.path.join(root, file)
                syms = get_symbols(path)
                if not syms:
                    continue
                
                # Determine Section based on the first sub-directory after args.path
                rel_path = os.path.relpath(path, args.path)
                parts = rel_path.split(os.sep)
                section_key = parts[0].capitalize() if len(parts) > 1 else "Root"
                
                if section_key not in sections:
                    sections[section_key] = []
                
                sections[section_key].append((path, syms))
                all_callables_count += len([s for s in syms if s.type == 'function' or '.' in s.name])

    generate_markdown(sections, all_callables_count)

if __name__ == "__main__":
    main()
