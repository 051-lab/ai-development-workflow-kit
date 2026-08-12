# Project

## Project Name
Sample Project

## Purpose
Demonstrate how concise V1.1 project state can look after initialization.

## Current Scope
A small command-line utility with one supported command.

## Architecture
Single executable entry point plus focused tests. No network services or persistent database.

## Tech Stack
Python 3 standard library and `unittest`.

## Supported Environments
Windows 11 and WSL Ubuntu with Python 3.12 or newer.

## Repository Conventions
Source under `src/`; tests under `tests/`; generated files are not committed.

## Non-Negotiable Constraints
No third-party runtime dependencies.

## Verification Commands
`python -m unittest -v`

## Definition of Healthy
Clean Git working tree and all unit tests passing.
