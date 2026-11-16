# Publishing this repository

Target GitHub account: `CongjianL`.
Suggested repository: `biology-research-superpowers`.

The connected GitHub integration can write repository files/branches but **cannot create new repositories**. The target repository must exist before an automatic upload can happen.

## Create a new empty repository

Open https://github.com/new?name=biology-research-superpowers under the `CongjianL` account. Choose public/private deliberately. Do not pre-populate it with a README, license or gitignore, because these files are already present here.

## Publish from a downloaded source archive

In a shell inside the source folder:

```bash
git init -b main
git add .
git commit -m "Initial biology research superpowers Codex plugin"
git remote add origin https://github.com/CongjianL/biology-research-superpowers.git
git push -u origin main
```

Alternatively, after creation, provide the repository URL in the ChatGPT conversation with the connected GitHub integration and ask it to upload the reviewed source tree. It should create an isolated branch or initial commit, check the tree and then report the commit SHA.

## Review before making public

- Review the original MIT license and upstream credit.
- Do not commit private study data, raw reads, credentials, patient information or unpublished confidential manuscripts.
- Run the offline tests shown in `TEST_REPORT.md`.
- Verify Codex marketplace installation on a supported local Codex release.
