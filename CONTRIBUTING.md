# Contributing

Thank you for improving this learning resource. Contributions can be corrections, clearer
explanations, new exercises, additional notebooks, or documentation fixes.

## Before you start

- Search existing issues and pull requests to avoid duplicate work.
- For a large change or a new module, open an issue first and describe the scope.
- Keep changes focused. Small, reviewable pull requests are easier to evaluate.

## Ground rules

- Do not commit secrets, API keys, tokens, passwords, or private credentials.
- Do not commit personal data or machine-specific absolute paths.
- Do not add large datasets or generated artifacts when a built-in or synthetic example will do.
- Do not remove existing notes or code unless the change is clearly justified.
- Be respectful and constructive in reviews and discussions.

## Notebook standards

A new or substantially changed notebook should:

1. Have a clear title and a short introduction.
2. List learning objectives.
3. Explain the key concepts before the code that uses them.
4. Use a fixed random seed (`RANDOM_STATE = 42` or a seeded generator).
5. Run from top to bottom without errors.
6. Use relative paths or built-in datasets.
7. Include a summary and exercises.
8. Keep outputs small enough to review comfortably.

Keep executed outputs in committed notebooks so learners can read them on GitHub. Clear outputs only
if the output is misleading, excessively large, or contains machine-specific information.

## Code style

- Prefer readable names over abbreviations.
- Keep cells focused; one idea per cell.
- Use `Pipeline` and `ColumnTransformer` for preprocessing when appropriate.
- Avoid deprecated scikit-learn APIs.
- Use `random_state` consistently.
- Do not hard-code absolute paths.
- Do not print huge arrays or dataframes; use `.head()` or summaries.
- Suppress warnings only when they are known and harmless, and explain why.

## Documentation style

- Use plain language and short paragraphs.
- Define abbreviations on first use.
- Link to related modules with relative paths.
- Keep tables aligned and avoid overly wide columns.
- Do not use emojis in committed documentation unless the file already uses them.

## Commit messages

Use short, descriptive messages. Examples:

```text
fix: correct ROC curve label in evaluation notebook
docs: clarify target encoding leakage
feat: add calibration section to pipelines module
```

## Pull request checklist

- [ ] The change is focused and described clearly.
- [ ] Notebooks run without errors from a clean kernel.
- [ ] Outputs are committed and reviewed.
- [ ] No secrets, personal paths, or private data are included.
- [ ] Documentation links still resolve.
- [ ] New dependencies are added to `requirements.txt`.
- [ ] The contribution follows the existing style.

## Reporting a problem

When reporting a bug, include:

- the notebook and cell name or number;
- the Python and package versions;
- the full error message;
- what you expected and what happened;
- a minimal reproduction if possible.

## Adding a module

New modules should fill a genuine gap in the curriculum. Before building one, check the module index
in [`Advanced_ML/README.md`](Advanced_ML/README.md). A proposal should state:

- the topic and why it belongs in the course;
- prerequisites;
- the dataset and its license;
- the key concepts and exercises;
- the estimated runtime.

## License

By contributing, you agree that your contribution is released under the repository's
[MIT License](LICENSE).
