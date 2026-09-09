# Suno API documentation

This repository contains the Mintlify documentation site for Suno API.

## Repository structure

- `docs.json` defines site configuration and navigation
- `index.mdx`, `introduction.mdx`, `quickstart.mdx`, and `deployment.mdx` cover the main user journey
- `configuration/` documents authentication and runtime configuration
- `guides/` contains task-based walkthroughs
- `api-reference/` documents the HTTP endpoints

## Local development

Install the Mintlify CLI:

```bash
npm i -g mint
```

Start a local preview from the repository root:

```bash
mint dev
```

Validate internal links before you finish:

```bash
mint broken-links
```

## Writing priorities

- Keep the project positioned as an unofficial Suno API wrapper
- Explain cookie-based authentication and 2Captcha requirements clearly
- Distinguish between synchronous waits and async polling flows
- Never include real cookies, API keys, or other secrets in examples

## AI-assisted writing

Install the Mintlify documentation skill if you use an AI editor:

```bash
npx skills add https://mintlify.com/docs
```

Then customize `AGENTS.md` and follow its terminology, style, and content-boundary rules.
