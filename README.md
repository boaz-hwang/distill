# distill

Turn the task you just completed into a skill.

You get a skill that performs the task for you when you invoke it.

[한국어](README.ko.md) · [Skill instructions](SKILL.md) · [MIT](LICENSE)

| Skill | Purpose |
| --- | --- |
| [distill](SKILL.md) | Create a skill from completed work. |
| [evolve](skills/evolve/README.md) | Improve one skill from actual execution records. |

## Background

Distill grew out of a problem: skills get longer as unnecessary instructions accumulate. It trusts capable models to exercise judgment and preserves only the conditions needed to reproduce a result the user is happy with. Its starting point is completed work: extract the successful process and quality criteria, then confirm them with the user. Leave implementation to the model, verify what can be checked with code, and use human judgment for the rest to improve the skill.

## Install

Paste this one line into your coding agent.

```text
Install https://github.com/boaz-hwang/distill in your skills directory using git clone.
```

## Use

When you're happy with the result, ask in the same session:

```text
Use distill to turn this task into a reusable skill.
```

Recommended models:

- Fable 5.1 high
- Astra 6 high

## How it works

1. Recommends one of three skill names and confirms a one-line description of the deliverable.
2. Proposes only the essential steps, one line each, and reconfirms any revisions.
3. Creates a concise skill from the confirmed process, with any needed templates and checks.

The agent chooses how to implement the task. Code checks objective criteria; short review questions cover the judgments left to you.
