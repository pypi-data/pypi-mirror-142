import subprocess


def clone(url: str, target_directory: str) -> None:
    print(f'Cloning {url} into {target_directory} ...')
    subprocess.run(
        ['git', 'clone', url, target_directory], capture_output=True
    )
