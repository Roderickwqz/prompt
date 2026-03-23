## Git: Commit & Pull Request Guidelines
- Always run `git status` and `git diff` to verify the repository state before making any edits.
- Never revert, delete, or overwrite in-progress work authored by other agents; coordinate with them or the user if unsure.
- Never delete a file solely to silence a local lint or type error; stop and ask the user for explicit approval.
- ABSOLUTELY NEVER edit `.env` or any environment variable files—only the user may change them.
- Delete unused or obsolete files only when your changes make them completely irrelevant; moving/renaming is allowed, but stop and ask if you encounter unexpected files.
- Keep commits atomic and scoped to one logical change; commit only the files you touched and avoid bulk staging.
- Use concise, imperative commit subjects with conventional prefixes (e.g., `feat:`, `fix:`, `refactor:`).
- Quote any git paths containing brackets or parentheses (e.g., `"src/app/[candidate]/**"`) when staging or committing to prevent shell glob parsing errors.
- Always PREFER the `committer` (bash) helper tool on PATH, or `./scripts/committer` if available in the repository.
- For tracked files, explicitly list paths: `git commit -m "<scoped message>" -- path/to/file1 path/to/file2`.
- For brand-new files, use: `git restore --staged :/ && git add "path/to/file1" && git commit -m "<scoped message>" -- path/to/file1`.
- Never amend commits (`git commit --amend`) unless you have explicit written approval in the task thread.
- PR descriptions must include: purpose, key design/behavior changes, test evidence (e.g., pytest output), and the linked issue/task.
- Default to safe commands: `git status`, `git diff`, `git log`; for large reviews, use `git --no-pager diff --color=never`.
- Avoid repository-wide search/replace scripts; keep edits small, scoped, and easily reviewable.
- Branch changes and pushes require user consent (e.g., a user prompt saying "pull and push" constitutes consent).
- ABSOLUTELY NEVER run destructive operations (`git reset --hard`, `rm`, `git clean`, `git checkout <old-commit>`) without explicit written instruction (exemption: native Cursor/Codex Web tooling capabilities).
- Avoid manual `git stash`; automatic stashing by Git during a pull/rebase is acceptable.
- Prevent editor popups during `git rebase` by exporting `GIT_EDITOR=:` and `GIT_SEQUENCE_EDITOR=:` or passing the `--no-edit` flag.
- For remotes under `~/Projects`, prefer HTTPS over SSH; automatically convert SSH URLs to HTTPS before pulling or pushing.
## Documentation & Maintenance Rules
- If public APIs in `src/alpha/**` change, update `docs/project/04_registry.md` (required).
- Update `docs/02_architecture.md` and `docs/project/03_standards.md` when boundaries or conventions change.
- Do not commit local artifacts (`.env`, `outputs/`, large data files).


## Commit Policy
After any successful implementation:
1. Summarize modified files
2. Run git status
3. Run git diff
4. Commit using `committer`
5. Commit only touched files