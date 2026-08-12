#!/usr/bin/env bash
set -euo pipefail

usage() {
  printf 'Usage: %s [repository-path] [session-name]\n' "$(basename "$0")"
}

if ! command -v tmux >/dev/null 2>&1; then
  printf 'error: tmux is not installed or not on PATH\n' >&2
  exit 1
fi

repo="${1:-.}"
if [[ "$repo" == "-h" || "$repo" == "--help" ]]; then
  usage
  exit 0
fi
repo="$(cd "$repo" && pwd -P)"
base="$(basename "$repo")"
default_session="$(printf '%s' "$base" | tr '.:' '--' | tr -cd '[:alnum:]_-')"
session="${2:-$default_session}"

if [[ -z "$session" ]]; then
  printf 'error: session name resolved to an empty string\n' >&2
  exit 2
fi

if tmux has-session -t "$session" 2>/dev/null; then
  exec tmux attach-session -t "$session"
fi

tmux new-session -d -s "$session" -n agent -c "$repo"
tmux new-window -t "$session" -n test -c "$repo"
tmux new-window -t "$session" -n git -c "$repo"
tmux new-window -t "$session" -n logs -c "$repo"
tmux select-window -t "$session:agent"
exec tmux attach-session -t "$session"
