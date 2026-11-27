#!/usr/bin/env python3
"""Keep marketplace.json pinned to released plugin versions.

--check  fail if the marketplace, plugin manifests and release config disagree
--write  point every marketplace entry at the tag of its current release
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REPO_URL = "https://github.com/GetLendWell/lendwellai.git"
MARKETPLACE = ROOT / ".claude-plugin" / "marketplace.json"
CONFIG = ROOT / "release-please-config.json"
MANIFEST = ROOT / ".release-please-manifest.json"
TAG = re.compile(r"^(?P<component>[a-z0-9-]+)-v(?P<version>\d+\.\d+\.\d+)$")


def load(path):
    return json.loads(path.read_text())


def semver(version):
    return tuple(int(part) for part in version.split("."))


def main(mode):
    marketplace = load(MARKETPLACE)
    packages = load(CONFIG)["packages"]
    versions = load(MANIFEST)
    entries = {entry["name"]: entry for entry in marketplace["plugins"]}
    errors = []

    plugin_dirs = {f"plugins/{d.name}" for d in (ROOT / "plugins").iterdir() if d.is_dir()}
    for missing in sorted(plugin_dirs - packages.keys()):
        errors.append(f"{missing} is not in release-please-config.json")

    for path, package in packages.items():
        name = package["component"]
        version = versions.get(path)
        if version is None:
            errors.append(f"{path} is not in .release-please-manifest.json")
            continue

        plugin = load(ROOT / path / ".claude-plugin" / "plugin.json")
        if plugin["name"] != name:
            errors.append(f"{path}: plugin.json name is {plugin['name']}, expected {name}")
        if plugin["version"] != version:
            errors.append(f"{path}: plugin.json version is {plugin['version']}, manifest says {version}")

        entry = entries.get(name)
        if entry is None:
            errors.append(f"{name} is not in marketplace.json")
            continue

        expected = {"source": "git-subdir", "url": REPO_URL, "path": path}
        source = entry.get("source", {})
        if mode == "write":
            entry["source"] = {**expected, "ref": f"{name}-v{version}"}
            continue

        for key, value in expected.items():
            if source.get(key) != value:
                errors.append(f"{name}: marketplace source.{key} is {source.get(key)}, expected {value}")
        match = TAG.match(source.get("ref", ""))
        if not match or match["component"] != name:
            errors.append(f"{name}: marketplace ref {source.get('ref')} is not a {name}-vX.Y.Z tag")
        elif semver(match["version"]) > semver(version):
            errors.append(f"{name}: marketplace ref {source['ref']} is ahead of version {version}")

    if mode == "write":
        MARKETPLACE.write_text(json.dumps(marketplace, indent=2) + "\n")

    for error in errors:
        print(f"error: {error}", file=sys.stderr)
    return 1 if errors else 0


if __name__ == "__main__":
    if len(sys.argv) != 2 or sys.argv[1] not in ("--check", "--write"):
        sys.exit(__doc__)
    sys.exit(main(sys.argv[1].lstrip("-")))
