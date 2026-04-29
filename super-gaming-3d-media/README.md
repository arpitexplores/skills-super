# Super Gaming 3D Media

Build and improve games, 3D web experiences, animation, audio/video workflows, and media tooling.

## Install

Copy this folder into your agent's skills directory, then restart or reload the agent.

```bash
cp -R super-gaming-3d-media ~/.your-agent/skills/
```

Use it by name:

```text
Use $super-gaming-3d-media to help with this request.
```

## Best For

- game development
- Unity/Unreal/Godot workflows
- Three.js and 3D web
- animation systems
- audio/video tooling

## Outputs

- game or 3D implementation plan
- engine-specific guidance
- animation/media workflow
- performance notes
- asset pipeline checklist

## Modules

| Module | Purpose |
| --- | --- |
| `animation-motion.md` | Animation, motion design, timelines, interaction motion, and media movement systems |
| `game-dev.md` | Game engine workflows, gameplay systems, mechanics, scenes, performance, and build considerations |
| `media-audio-video.md` | Audio, video, media processing, editing workflows, and asset pipeline guidance |

## Example Prompts

- `Use $super-gaming-3d-media to plan this Three.js scene.`
- `Use $super-gaming-3d-media to improve this Unity gameplay system.`
- `Use $super-gaming-3d-media to design an animation pipeline.`

## Package Contents

- `SKILL.md` is the installable skill entry point.
- `references/modules/` contains detailed workflows loaded only when needed.
- `agents/` contains optional agent metadata where supported.
- `scripts/` and `assets/` are optional helpers when bundled.

## Compatibility

This skill is plain Markdown and is intended to be agent-agnostic. If a bundled helper mentions a specific tool path, translate that instruction to the equivalent path for your environment.

## Version

See `VERSION` and `CHANGELOG.md`.

## Licence

MIT. See the root repository `LICENSE`.
