# Security Policy

## Supported versions

The `main` branch is the supported version of this educational repository.

## Scope

This repository contains notebooks, notes, and small educational datasets. It does not operate a
production service. Security reports are still welcome for:

- accidentally committed credentials or tokens;
- personal or sensitive data in a dataset or notebook output;
- unsafe code that could harm a learner who runs it;
- dependency confusion or malicious package suggestions;
- links that redirect to unexpected or unsafe content.

## Reporting a vulnerability

Please report security concerns privately through GitHub's security advisory feature:

1. Open the repository's **Security** tab.
2. Choose **Report a vulnerability**.
3. Describe the issue, affected files, and steps to reproduce.

Do not open a public issue for a secret leak or a privacy problem until it has been addressed.

## What to include

- the affected file or notebook;
- the commit or branch;
- the potential impact;
- reproduction steps or a minimal example;
- any suggested fix.

## Response

Reports will be reviewed as time permits. If a secret or personal datum is confirmed, the maintainer
will remove it from the current branch and may rewrite history or rotate the affected credential.
Because this is an educational project, no response-time guarantee is provided.

## For learners

- Never commit your own API keys, passwords, or private datasets.
- Review notebook outputs before sharing them; outputs can contain local paths or data.
- Run notebooks in a virtual environment.
- Treat downloaded notebooks and datasets as untrusted code and data.
- Report suspicious changes rather than running them.
