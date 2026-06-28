# ds-init Roadmap

## Vision

Make `ds-init` the go-to CLI for starting new data science workflows — eliminating
15 minutes of copy-pasting boilerplate before a single line of real work begins.

---

## Versions

### 0.3.0 (shipped)
- Pre-commit hooks (black/isort/ruff + sanity checks)
- Read the Docs build config
- Project roadmap

### 1.0.0 (next milestone)
- `ds-init` ships stable API and the four templates (basic, cv, nlp, time-series)
  behave consistently; README accurately reflects 1-command install and usage.
- No breaking CLI changes after 1.0.0 without a new major version.

### 2.0.0 (longer term)
- Plugin system for community-contributed templates (e.g., healthcare, finance)
- GPU-aware dependency selection (pytorch-cuda vs. pytorch-cpu)
- Built-in GitHub/GitLab repo bootstrap (`ds-init my-project --with-repo`)

---

## Non-Goals

- Hosted project management; `ds-init` is scaffolding only
- IDE-specific wizardry; output should work in VS Code, PyCharm, or a terminal
