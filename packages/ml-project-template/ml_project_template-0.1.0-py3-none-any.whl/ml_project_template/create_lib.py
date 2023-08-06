from pathlib import Path
import ml_project_template
import argparse
from string import Template


def create_project(root_path, output_path_root):
    root_path = root_path / 'project'
    packages_path = output_path_root / 'packages'
    if not packages_path.is_dir():
        packages_path.mkdir()
    for path in sorted(root_path.rglob('*')):
        first_dir = path.relative_to(root_path).parts [0]
        if first_dir == '.git' or first_dir == '.ipynb_checkpoints' or path.suffix == '.sh' or "__pycache__" in path.relative_to(root_path).parts:
            continue
        if path.is_dir():
            output_path_dir = output_path_root/ path.relative_to(root_path)
            if not output_path_dir.is_dir():
                output_path_dir.mkdir()
            continue
        text = path.read_text()
        
        output_path = output_path_root / Path(*[p if p!='recoform' else package_name for p in path.relative_to(root_path).parts])
        output_path.write_text(text)


def create_package(root_path, output_path_root, package_name, package_type):
    root_path = root_path / f'{package_type}_package'
    for path in sorted(root_path.rglob('*')):
        first_dir = path.relative_to(root_path).parts [0]
        if first_dir == '.git' or first_dir == '.ipynb_checkpoints' or path.suffix == '.sh' or "__pycache__" in path.relative_to(root_path).parts:
            continue
        if path.is_dir():
            path_parts = [Template(p).substitute(package_name=package_name) for p in path.relative_to(root_path).parts]
            output_path_dir = output_path_root/ Path(*path_parts)
            if not output_path_dir.is_dir():
                output_path_dir.mkdir()
            continue
        text = path.read_text()
        t = Template(text)
        text = t.substitute(package_name=package_name)
        
        output_path = output_path_root / Path(*[Template(p).substitute(package_name=package_name) for p in path.relative_to(root_path).parts])
        output_path.write_text(text)


def main():
    parser = argparse.ArgumentParser(prog ='mlproject',
                                     description ='Create ML Project Template')
    parser.add_argument('project_or_app', metavar='project_or_app', action ='store', choices=['startproject', 'startml', 'startapi'],
                        default = False, help ="startproject or startapp")
    parser.add_argument('project_path', metavar='project_path', action ='store',
                        default = False, help ="Root path for the project.")
  
    args = parser.parse_args()

    root_path = Path(ml_project_template.__file__).resolve().parent / 'files'

    output_path_root = Path(args.project_path).resolve()
    package_name = args.project_path

    if not output_path_root.is_dir():
        output_path_root.mkdir()

    if args.project_or_app == "startproject":
        create_project(root_path, output_path_root)
    elif args.project_or_app == "startml":
        create_package(root_path, output_path_root, package_name, 'ml')
    elif args.project_or_app == "startapi":
        create_package(root_path, output_path_root, package_name, 'api')

    print(f"Created the template in {output_path_root}")

    

    