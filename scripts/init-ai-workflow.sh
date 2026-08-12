#!/usr/bin/env bash
set -euo pipefail

usage() {
  printf 'Usage: %s [repository-path] [--force]\n' "$(basename "$0")"
}

repo="."
force=0
for arg in "$@"; do
  case "$arg" in
    --force) force=1 ;;
    -h|--help) usage; exit 0 ;;
    *)
      if [[ "$repo" != "." ]]; then
        printf 'error: only one repository path may be supplied\n' >&2
        usage >&2
        exit 2
      fi
      repo="$arg"
      ;;
  esac
done

repo="$(cd "$repo" && pwd -P)"
script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd -P)"
kit_root="$(cd "$script_dir/.." && pwd -P)"
source_dir="$kit_root/templates/docs/ai"
target_dir="$repo/docs/ai"

if [[ ! -d "$source_dir" ]]; then
  printf 'error: template directory not found: %s\n' "$source_dir" >&2
  exit 1
fi

mkdir -p "$target_dir"
files=(PROJECT.md STATE.md DECISIONS.md REFERENCES.md INBOX.md)

for name in "${files[@]}"; do
  src="$source_dir/$name"
  dst="$target_dir/$name"
  if [[ -e "$dst" && "$force" -ne 1 ]]; then
    printf 'preserve  %s\n' "$dst"
    continue
  fi
  cp "$src" "$dst"
  printf 'write     %s\n' "$dst"
done

printf 'ready     %s\n' "$target_dir"
