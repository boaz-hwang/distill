# distill

Turn work you're happy with into a skill that can do it again.

[한국어](README.ko.md) · [Skill instructions](SKILL.md) · [MIT license](LICENSE)

Work with your agent normally. Finish in one pass or iterate until the result
meets your standards. When **you** consider it done, invoke `distill` in that
session. It extracts the minimum guidance needed to reproduce that quality.

## How it works

1. **Confirm the destination.** Get three name candidates, one recommendation,
   and a one-line description of the deliverable. Correct the proposal if needed.
2. **Confirm the process.** Review the fewest sufficient steps, one line each,
   including necessary inputs, templates, and the proposed evaluation split.
   Requested changes come back for confirmation.
3. **Receive the skill.** The agent writes the confirmed process with only the
   guidance that affects quality, plus any resources it actually needs.
4. **Evaluate and improve.** Reusable code checks handle what can be objectively
   verified. A short human review covers the remaining judgments. Specific
   feedback improves the skill without accumulating a rule for every incident.

The two confirmations are real pauses. Distill does not write the target skill
before the process is approved or add a third approval gate at delivery.

## Why this stays small

The source of truth is the accepted result and the feedback that made it good.
The session's entire sequence of tool calls is not a reusable procedure.
Failed approaches disappear; essential constraints learned through corrections
remain. Values specific to one run become inputs.

Every instruction has to justify its presence: would removing it make a capable
agent miss an accepted requirement? If not, it goes. Necessary detail stays.
There is no arbitrary word limit and no overflow manual hiding the same excess.

Distill assumes a capable model that can choose its implementation. It does not
pin a model, claim a benchmark advantage, or need a provider-specific API.

## Install and use

This repository is one skill directory following the
[Agent Skills specification](https://agentskills.io/specification).
Clone it into a skill location supported by your agent, keeping the folder name
`distill`:

```sh
# Run from your agent's skills directory.
git clone https://github.com/boaz-hwang/distill.git distill
```

Reload skill discovery if your client requires it. At the end of a successful
session, explicitly invoke `distill` using your client's skill invocation UI or
syntax, with a request such as:

> I'm happy with this result. Use distill to make a reusable skill from this session.

The agent needs the relevant conversation and accepted artifact. If that context
is missing or was compacted away, distill asks for the specific missing evidence.
It does not automatically collect other conversations. Discussion follows the
user's language; the skill instructions are in English.

## What code can and cannot check

Checks in a **generated skill** must target that task's accepted requirements.
For a report, code might reconcile totals against source records; a person might
judge whether its recommendation is useful to the intended reader. Counting words
cannot settle that judgment. Distill asks the agent to test a checker against both
an accepted example and an example that violates a requirement.

Distill itself includes a small **package validator**:

```sh
uv run /path/to/distill/scripts/validate_skill.py /path/to/generated-skill
```

Requires Python 3.10+ and [uv](https://docs.astral.sh/uv/). The first run downloads
the pinned [Agent Skills reference validator](https://github.com/agentskills/agentskills/tree/main/skills-ref)
and its dependencies; Git is needed to fetch it. Later runs can reuse the cache.
The script returns JSON and exits `0` when its checks pass, `1` when they fail.
It checks skill metadata and bundled Python syntax without executing target code.
It explicitly reports outcome quality as `not_evaluated`. Non-Python scripts,
runtime dependencies, and actual output quality need their own checks.

Skill-format validation is not evidence that a skill reproduces your result.
Fresh-input trials and the human review questions provide that evidence.

## Development

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements-dev.txt
.venv/bin/python scripts/validate_skill.py .
.venv/bin/python -m unittest discover -s tests -v
```

CI runs the package validator and its tests. These do not test a model's
conversation behavior. [Behavioral scenarios](evals/scenarios.md) provide
fictional sessions for testing the two confirmation gates, minimality, and
evaluation quality in an agent client. Record the model, actual responses,
generated artifacts, and human judgments when running them.

Contributions should show a concrete result or decision that improves. Prefer
a small change supported by an observed failure over a new universal rule.
Do not include private conversations or client artifacts in issues or fixtures.
