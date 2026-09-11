# distill

Turn the task you just completed into a skill.

You get a skill that performs the task for you when you invoke it.

[한국어](README.ko.md) · [Skill instructions](SKILL.md) · [MIT](LICENSE)

## Install

Paste this one line into your coding agent.

```text
Install https://github.com/boaz-hwang/distill in your skills directory using git clone.
```

## Use

When you're happy with the result, ask in the same session:

```text
I'm happy with this result. Use distill to turn this task into a reusable skill.
```

## How it works

1. Recommends one of three skill names and confirms a one-line description of the deliverable.
2. Proposes only the essential steps, one line each, and reconfirms any revisions.
3. Creates a concise skill from the confirmed process, with any needed templates and checks.

The agent chooses how to implement the task. Code checks objective criteria; short review questions cover the judgments left to you.
