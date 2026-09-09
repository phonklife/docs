> For Mintlify product knowledge (components, configuration, writing standards), install the Mintlify skill: `npx skills add https://mintlify.com/docs`

# Suno API documentation instructions

## About this project

- This repository contains the Mintlify documentation for Suno API
- Pages are MDX files with YAML frontmatter
- Site configuration lives in `docs.json`
- Run `mint dev` from the repository root to preview locally
- Run `mint broken-links` before finishing documentation changes

## Terminology

- Use **Suno API** for the product name
- Use **Suno** for the upstream music-generation service
- Use **clip** for an individual generated result returned by the API
- Use **song** only in user-facing explanations where the broader concept is clearer than **clip**
- Use **Cookie header** or `SUNO_COOKIE` when referring to authentication input
- Use **2Captcha** for the CAPTCHA-solving service name
- Use **persona** only for the Suno feature exposed by `GET /api/persona`
- Describe the project as **unofficial**, **open-source**, and **self-hostable** when explaining what it is

## Style preferences

- Use active voice and second person
- Keep sentences concise and concrete
- Use sentence case for headings
- Bold UI labels such as **Network** or **Headers**
- Use code formatting for commands, file names, paths, environment variables, headers, and endpoint paths
- Lead task-oriented pages with the user goal, then the required prerequisites
- Call out async behavior clearly when users must poll for completion
- Warn readers not to expose copied browser cookies or other credentials
- Avoid overstating guarantees about Suno internals, timing, quotas, or compatibility

## Content boundaries

- Do document the public behavior of the Suno API wrapper, including setup, authentication, deployment, polling, and endpoint usage
- Do document operational caveats that users must know, such as cookie expiry, CAPTCHA costs, and unofficial API limitations
- Do not describe the project as officially affiliated with or endorsed by Suno
- Do not keep generic Mintlify starter content that is unrelated to Suno API
- Do not invent unsupported endpoints, parameters, response fields, limits, or integrations
- Do not include real cookies, API keys, tokens, or copied user secrets in examples
