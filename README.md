# Coding_Agent

A self-hosted AI coding agent that works entirely through GitHub — no laptop or terminal needed. It behaves like an autonomous coding assistant: you describe what you want in an Issue, and it writes the code, runs the tests, and opens a Pull Request for you to review.

Runs on GitHub Actions using [Aider](https://aider.chat) with Google's **Gemini API (free tier)** as the model.

## Setup (one-time)

1. Go to **Settings → Secrets and variables → Actions** on this repo.
2. Add a repository secret named `GEMINI_API_KEY` with a free Gemini API key from [Google AI Studio](https://aistudio.google.com/apikey).
3. That's it — `GITHUB_TOKEN` is provided automatically by GitHub Actions.

## How to use it (from your phone)

1. Open the **Issues** tab → **New Issue**. You can use the "Ask the Coding Agent" template, or just type your own issue.
2. In the issue body, start with `aider:` followed by what you want, e.g.:
   ```
   aider: create a Python function that fetches NSE stock prices and add a test for it
   ```
3. The agent will:
   - Create a new branch
   - Write the code
   - Run `pytest`
   - Commit and push the changes
   - Open a Pull Request
   - Comment back on your issue when it's done (success, error, or no changes made)
4. To keep refining the same piece of work, comment on the **Pull Request** itself starting with `aider: ...`. The agent will push more commits to that same branch instead of starting over.
5. Review the PR diff on GitHub and merge it whenever you're happy with the result.

## Notes

- Only comments/issues from the repo owner trigger the agent (see the `if:` condition in the workflow) — safe to leave the repo private or public.
- `tests/test_smoke.py` is a placeholder so `pytest` always has something to run; the agent will add real tests as it builds features.
- Put any dependencies your generated code needs into `requirements.txt` — the agent will keep it updated.
