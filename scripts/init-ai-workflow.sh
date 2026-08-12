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
written=0
preserved=0

if [[ "$force" -eq 1 ]]; then
  printf 'force     replacing canonical workflow state in %s\n' "$target_dir"
elif [[ -e "$target_dir/PROJECT.md" || -e "$target_dir/STATE.md" || -e "$target_dir/DECISIONS.md" || -e "$target_dir/REFERENCES.md" || -e "$target_dir/INBOX.md" ]]; then
  printf 'existing  workflow state detected; preserving existing files\n'
fi

for name in "${files[@]}"; do
  src="$source_dir/$name"
  dst="$target_dir/$name"
  if [[ -e "$dst" && "$force" -ne 1 ]]; then
    printf 'preserve  %s\n' "$dst"
    preserved=$((preserved + 1))
    continue
  fi
  cp "$src" "$dst"
  printf 'write     %s\n' "$dst"
  written=$((written + 1))
done

printf 'summary   written: %d\n' "$written"
printf 'summary   preserved: %d\n' "$preserved"
if [[ "$force" -ne 1 && "$preserved" -gt 0 ]]; then
  printf 'guidance  use --force only to intentionally replace existing workflow state\n'
fi
printf 'ready     %s\n' "$target_dir"
