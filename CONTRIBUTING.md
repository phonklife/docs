# Contribute to the documentation

Thank you for helping improve the Suno API documentation.

## How to contribute

### Option 1: Edit directly on GitHub

1. Open the page you want to change
2. Click the edit button on GitHub
3. Make your update and submit a pull request

### Option 2: Local development

1. Fork and clone this repository
2. Install the Mintlify CLI: `npm i -g mint`
3. Create a branch for your changes
4. Run `mint dev` from the repository root
5. Preview your changes at `http://localhost:3000`
6. Run `mint broken-links`
7. Commit your changes and submit a pull request

For more details on local development, see our [development guide](development.mdx).

## Writing guidelines

- **Use active voice**: Prefer direct instructions
- **Address the reader directly**: Use “you”
- **Keep terminology consistent**: Use `clip`, `Cookie header`, `SUNO_COOKIE`, and `2Captcha` consistently
- **Keep caveats explicit**: Call out unofficial behavior, polling requirements, and cookie expiry when relevant
- **Protect secrets**: Never paste real cookies, API keys, or tokens into examples
- **Validate links**: Run `mint broken-links` before you open or update a pull request
