# TOFIX

Findings from a code scan on 2026-10-04.

## Medium

- `rsconstruct.toml:41` - the ruff and mypy processors (`rsconstruct.toml:45` too) cover `scripts`, `config` and `exercises`, but 21 tracked Python files live in `compose/`, `examples/` and `python_samples/` and are never linted or type-checked, while `config/` holds no Python at all (only `.lua`). Set `src_dirs` to the folders that actually hold `.py` files: `scripts`, `exercises`, `compose`, `examples`, `python_samples` (`ruff check` on the three missing folders already passes).
- `compose/examples/envrionment_variables_interpolation/README.md:12` - states that a `.env` file has no effect unless an `env_file` section is added; Compose reads `.env` from the project directory automatically for variable interpolation, which is exactly what this example is about (`env_file` only injects variables into the container). Correct the conclusion.

## Low

- `scripts/dockerhub_set_description.py:15` - Docker Hub username/password and repo name are hardcoded placeholders in the source, so the script cannot be used without editing in a real password; take the username and repo as arguments and the password from pass(1) as `scripts/login.sh:10` does. Also `api_endpoint.format(...)` at line 48 is a no-op on an already-interpolated f-string - drop it.
- `rsconstruct.toml:36` - zspell checks only `exercises` and `notes`, while 37 markdown files under `compose/` and `examples/` (linted by rumdl at `rsconstruct.toml:32`) are never spell-checked; add those dirs.
- `compose/examples/envrionment_variables_interpolation` - directory name is misspelled ("envrionment"), as is `compose/exercises/cpu_affinty` ("affinty"); rename both.
