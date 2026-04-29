## Source: references/skills/videodb/SKILL.md

---
name: videodb
description: Video and audio perception, indexing, and editing. Ingest files/URLs/live streams, build visual/spoken indexes, search with timestamps, edit timelines, add overlays/subtitles, generate media, and create real-time alerts.
category: media
risk: safe
source: community
tags: "[video, editing, transcription, subtitles, search, streaming, ai-generation, media, live-streams, desktop-capture]"
date_added: "2026-02-27"
allowed-tools: Read Grep Glob Bash(python:*)
argument-hint: "[task description]"
---

# VideoDB Skill

**Perception + memory + actions for video, live streams, and desktop sessions.**

Use this skill when you need to:

## 1) Desktop Perception
- Start/stop a **desktop session** capturing **screen, mic, and system audio**
- Stream **live context** and store **episodic session memory**
- Run **real-time alerts/triggers** on what's spoken and what's happening on screen
- Produce **session summaries**, a searchable timeline, and **playable evidence links**

## 2) Video ingest + stream
- Ingest a **file or URL** and return a **playable web stream link**
- Transcode/normalize: **codec, bitrate, fps, resolution, aspect ratio**

## 3) Index + search (timestamps + evidence)
- Build **visual**, **spoken**, and **keyword** indexes
- Search and return exact moments with **timestamps** and **playable evidence**
- Auto-create **clips** from search results

## 4) Timeline editing + generation
- Subtitles: **generate**, **translate**, **burn-in**
- Overlays: **text/image/branding**, motion captions
- Audio: **background music**, **voiceover**, **dubbing**
- Programmatic composition and exports via **timeline operations**

## 5) Live streams (RTSP) + monitoring
- Connect **RTSP/live feeds**
- Run **real-time visual and spoken understanding** and emit **events/alerts** for monitoring workflows

---

## Common inputs
- Local **file path**, public **URL**, or **RTSP URL**
- Desktop capture request: **start / stop / summarize session**
- Desired operations: get context for understanding, transcode spec, index spec, search query, clip ranges, timeline edits, alert rules

## Common outputs
- **Stream URL**
- Search results with **timestamps** and **evidence links**
- Generated assets: subtitles, audio, images, clips
- **Event/alert payloads** for live streams
- Desktop **session summaries** and memory entries

---

## Canonical prompts (examples)
- "Start desktop capture and alert when a password field appears."
- "Record my session and produce an actionable summary when it ends."
- "Ingest this file and return a playable stream link."
- "Index this folder and find every scene with people, return timestamps."
- "Generate subtitles, burn them in, and add light background music."
- "Connect this RTSP URL and alert when a person enters the zone."


## Running Python code

Before running any VideoDB code, change to the project directory and load environment variables:

```python
from dotenv import load_dotenv
load_dotenv(".env")

import videodb
conn = videodb.connect()
```

This reads `VIDEO_DB_API_KEY` from:
1. Environment (if already exported)
2. Project's `.env` file in current directory

If the key is missing, `videodb.connect()` raises `AuthenticationError` automatically.

Do NOT write a script file when a short inline command works.

When writing inline Python (`python -c "..."`), always use properly formatted code — use semicolons to separate statements and keep it readable. For anything longer than ~3 statements, use a heredoc instead:

```bash
python << 'EOF'
from dotenv import load_dotenv
load_dotenv(".env")

import videodb
conn = videodb.connect()
coll = conn.get_collection()
print(f"Videos: {len(coll.get_videos())}")
EOF
```

## Setup

When the user asks to "setup videodb" or similar:

### 1. Install SDK

```bash
pip install "videodb[capture]" python-dotenv
```

If `videodb[capture]` fails on Linux, install without the capture extra:

```bash
pip install videodb python-dotenv
```

### 2. Configure API key

The user must set `VIDEO_DB_API_KEY` using **either** method:

- **Export in terminal** (before starting AI assistant): `export VIDEO_DB_API_KEY=your-key`
- **Project `.env` file**: Save `VIDEO_DB_API_KEY=your-key` in the project's `.env` file

Get a free API key at https://console.videodb.io (50 free uploads, no credit card).

**Do NOT** read, write, or handle the API key yourself. Always let the user set it.

## Quick Reference

### Upload media

```python
# URL
video = coll.upload(url="https://example.com/video.mp4")

# YouTube
video = coll.upload(url="https://www.youtube.com/watch?v=VIDEO_ID")

# Local file
video = coll.upload(file_path="/path/to/video.mp4")
```

### Transcript + subtitle

```python
# force=True skips the error if the video is already indexed
video.index_spoken_words(force=True)
text = video.get_transcript_text()
stream_url = video.add_subtitle()
```

### Search inside videos

```python
from videodb.exceptions import InvalidRequestError

video.index_spoken_words(force=True)

# search() raises InvalidRequestError when no results are found.
# Always wrap in try/except and treat "No results found" as empty.
try:
    results = video.search("product demo")
    shots = results.get_shots()
    stream_url = results.compile()
except InvalidRequestError as e:
    if "No results found" in str(e):
        shots = []
    else:
        raise
```

### Scene search

```python
import re
from videodb import SearchType, IndexType, SceneExtractionType
from videodb.exceptions import InvalidRequestError

# index_scenes() has no force parameter — it raises an error if a scene
# index already exists. Extract the existing index ID from the error.
try:
    scene_index_id = video.index_scenes(
        extraction_type=SceneExtractionType.shot_based,
        prompt="Describe the visual content in this scene.",
    )
except Exception as e:
    match = re.search(r"id\s+([a-f0-9]+)", str(e))
    if match:
        scene_index_id = match.group(1)
    else:
        raise

# Use score_threshold to filter low-relevance noise (recommended: 0.3+)
try:
    results = video.search(
        query="person writing on a whiteboard",
        search_type=SearchType.semantic,
        index_type=IndexType.scene,
        scene_index_id=scene_index_id,
        score_threshold=0.3,
    )
    shots = results.get_shots()
    stream_url = results.compile()
except InvalidRequestError as e:
    if "No results found" in str(e):
        shots = []
    else:
        raise
```

### Timeline editing

**Important:** Always validate timestamps before building a timeline:
- `start` must be >= 0 (negative values are silently accepted but produce broken output)
- `start` must be < `end`
- `end` must be <= `video.length`

```python
from videodb.timeline import Timeline
from videodb.asset import VideoAsset, TextAsset, TextStyle

timeline = Timeline(conn)
timeline.add_inline(VideoAsset(asset_id=video.id, start=10, end=30))
timeline.add_overlay(0, TextAsset(text="The End", duration=3, style=TextStyle(fontsize=36)))
stream_url = timeline.generate_stream()
```

### Transcode video (resolution / quality change)

```python
from videodb import TranscodeMode, VideoConfig, AudioConfig

# Change resolution, quality, or aspect ratio server-side
job_id = conn.transcode(
    source="https://example.com/video.mp4",
    callback_url="https://example.com/webhook",
    mode=TranscodeMode.economy,
    video_config=VideoConfig(resolution=720, quality=23, aspect_ratio="16:9"),
    audio_config=AudioConfig(mute=False),
)
```

### Reframe aspect ratio (for social platforms)

**Warning:** `reframe()` is a slow server-side operation. For long videos it can take
several minutes and may time out. Best practices:
- Always limit to a short segment using `start`/`end` when possible
- For full-length videos, use `callback_url` for async processing
- Trim the video on a `Timeline` first, then reframe the shorter result

```python
from videodb import ReframeMode

# Always prefer reframing a short segment:
reframed = video.reframe(start=0, end=60, target="vertical", mode=ReframeMode.smart)

# Async reframe for full-length videos (returns None, result via webhook):
video.reframe(target="vertical", callback_url="https://example.com/webhook")

# Presets: "vertical" (9:16), "square" (1:1), "landscape" (16:9)
reframed = video.reframe(start=0, end=60, target="square")

# Custom dimensions
reframed = video.reframe(start=0, end=60, target={"width": 1280, "height": 720})
```

### Generative media

```python
image = coll.generate_image(
    prompt="a sunset over mountains",
    aspect_ratio="16:9",
)
```

## Error handling

```python
from videodb.exceptions import AuthenticationError, InvalidRequestError

try:
    conn = videodb.connect()
except AuthenticationError:
    print("Check your VIDEO_DB_API_KEY")

try:
    video = coll.upload(url="https://example.com/video.mp4")
except InvalidRequestError as e:
    print(f"Upload failed: {e}")
```

### Common pitfalls

| Scenario | Error message | Solution |
|----------|--------------|----------|
| Indexing an already-indexed video | `Spoken word index for video already exists` | Use `video.index_spoken_words(force=True)` to skip if already indexed |
| Scene index already exists | `Scene index with id XXXX already exists` | Extract the existing `scene_index_id` from the error with `re.search(r"id\s+([a-f0-9]+)", str(e))` |
| Search finds no matches | `InvalidRequestError: No results found` | Catch the exception and treat as empty results (`shots = []`) |
| Reframe times out | Blocks indefinitely on long videos | Use `start`/`end` to limit segment, or pass `callback_url` for async |
| Negative timestamps on Timeline | Silently produces broken stream | Always validate `start >= 0` before creating `VideoAsset` |
| `generate_video()` / `create_collection()` fails | `Operation not allowed` or `maximum limit` | Plan-gated features — inform the user about plan limits |

## Additional docs

Reference documentation is in the `reference/` directory adjacent to this SKILL.md file. Use the Glob tool to locate it if needed.

- [reference/api-reference.md](reference/api-reference.md) - Complete VideoDB Python SDK API reference
- [reference/search.md](reference/search.md) - In-depth guide to video search (spoken word and scene-based)
- [reference/editor.md](reference/editor.md) - Timeline editing, assets, and composition
- [reference/streaming.md](reference/streaming.md) - HLS streaming and instant playback
- [reference/generative.md](reference/generative.md) - AI-powered media generation (images, video, audio)
- [reference/rtstream.md](reference/rtstream.md) - Live stream ingestion workflow (RTSP/RTMP)
- [reference/rtstream-reference.md](reference/rtstream-reference.md) - RTStream SDK methods and AI pipelines
- [reference/capture.md](reference/capture.md) - Desktop capture workflow
- [reference/capture-reference.md](reference/capture-reference.md) - Capture SDK and WebSocket events
- [reference/use-cases.md](reference/use-cases.md) - Common video processing patterns and examples

## Screen Recording (Desktop Capture)

Use `ws_listener.py` to capture WebSocket events during recording sessions. Desktop capture supports **macOS** only.

### Quick Start

1. **Start listener**: `python scripts/ws_listener.py &`
2. **Get WebSocket ID**: `cat /tmp/videodb_ws_id`
3. **Run capture code** (see reference/capture.md for full workflow)
4. **Events written to**: `/tmp/videodb_events.jsonl`

### Query Events

```python
import json
events = [json.loads(l) for l in open("/tmp/videodb_events.jsonl")]

# Get all transcripts
transcripts = [e["data"]["text"] for e in events if e.get("channel") == "transcript"]

# Get visual descriptions from last 5 minutes
import time
cutoff = time.time() - 300
recent_visual = [e for e in events 
                 if e.get("channel") == "visual_index" and e["unix_ts"] > cutoff]
```

### Utility Scripts

- [scripts/ws_listener.py](scripts/ws_listener.py) - WebSocket event listener (dumps to JSONL)

For complete capture workflow, see [reference/capture.md](reference/capture.md).


**Do not use ffmpeg, moviepy, or local encoding tools** when VideoDB supports the operation. The following are all handled server-side by VideoDB — trimming, combining clips, overlaying audio or music, adding subtitles, text/image overlays, transcoding, resolution changes, aspect-ratio conversion, resizing for platform requirements, transcription, and media generation. Only fall back to local tools for operations listed under Limitations in reference/editor.md (transitions, speed changes, crop/zoom, colour grading, volume mixing).

### When to use what

| Problem | VideoDB solution |
|---------|-----------------|
| Platform rejects video aspect ratio or resolution | `video.reframe()` or `conn.transcode()` with `VideoConfig` |
| Need to resize video for Twitter/Instagram/TikTok | `video.reframe(target="vertical")` or `target="square"` |
| Need to change resolution (e.g. 1080p → 720p) | `conn.transcode()` with `VideoConfig(resolution=720)` |
| Need to overlay audio/music on video | `AudioAsset` on a `Timeline` |
| Need to add subtitles | `video.add_subtitle()` or `CaptionAsset` |
| Need to combine/trim clips | `VideoAsset` on a `Timeline` |
| Need to generate voiceover, music, or SFX | `coll.generate_voice()`, `generate_music()`, `generate_sound_effect()` |

## Repository

https://github.com/video-db/skills

**Maintained By:** [VideoDB](https://github.com/video-db)

---

## Merged Reference (legacy variant)

---
name: audio-transcriber
description: "Transform audio recordings into professional Markdown documentation with intelligent summaries using LLM integration"
category: content
risk: safe
source: community
tags: "[audio, transcription, whisper, meeting-minutes, speech-to-text]"
date_added: "2026-02-27"
---

## Purpose

This skill automates audio-to-text transcription with professional Markdown output, extracting rich technical metadata (speakers, timestamps, language, file size, duration) and generating structured meeting minutes and executive summaries. It uses Faster-Whisper or Whisper with zero configuration, working universally across projects without hardcoded paths or API keys.

Inspired by tools like Plaud, this skill transforms raw audio recordings into actionable documentation, making it ideal for meetings, interviews, lectures, and content analysis.

## When to Use

Invoke this skill when:

- User needs to transcribe audio/video files to text
- User wants meeting minutes automatically generated from recordings
- User requires speaker identification (diarization) in conversations
- User needs subtitles/captions (SRT, VTT formats)
- User wants executive summaries of long audio content
- User asks variations of "transcribe this audio", "convert audio to text", "generate meeting notes from recording"
- User has audio files in common formats (MP3, WAV, M4A, OGG, FLAC, WEBM)

## Workflow

### Step 0: Discovery (Auto-detect Transcription Tools)

**Objective:** Identify available transcription engines without user configuration.

**Actions:**

Run detection commands to find installed tools:

```bash
# Check for Faster-Whisper (preferred - 4-5x faster)
if python3 -c "import faster_whisper" 2>/dev/null; then
    TRANSCRIBER="faster-whisper"
    echo "✅ Faster-Whisper detected (optimized)"
# Fallback to original Whisper
elif python3 -c "import whisper" 2>/dev/null; then
    TRANSCRIBER="whisper"
    echo "✅ OpenAI Whisper detected"
else
    TRANSCRIBER="none"
    echo "⚠️  No transcription tool found"
fi

# Check for ffmpeg (audio format conversion)
if command -v ffmpeg &>/dev/null; then
    echo "✅ ffmpeg available (format conversion enabled)"
else
    echo "ℹ️  ffmpeg not found (limited format support)"
fi
```

**If no transcriber found:**

Offer automatic installation using the provided script:

```bash
echo "⚠️  No transcription tool found"
echo ""
echo "🔧 Auto-install dependencies? (Recommended)"
read -p "Run installation script? [Y/n]: " AUTO_INSTALL

if [[ ! "$AUTO_INSTALL" =~ ^[Nn] ]]; then
    # Get skill directory (works for both repo and symlinked installations)
    SKILL_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
    
    # Run installation script
    if [[ -f "$SKILL_DIR/scripts/install-requirements.sh" ]]; then
        bash "$SKILL_DIR/scripts/install-requirements.sh"
    else
        echo "❌ Installation script not found"
        echo ""
        echo "📦 Manual installation:"
        echo "  pip install faster-whisper  # Recommended"
        echo "  pip install openai-whisper  # Alternative"
        echo "  brew install ffmpeg         # Optional (macOS)"
        exit 1
    fi
    
    # Verify installation succeeded
    if python3 -c "import faster_whisper" 2>/dev/null || python3 -c "import whisper" 2>/dev/null; then
        echo "✅ Installation successful! Proceeding with transcription..."
    else
        echo "❌ Installation failed. Please install manually."
        exit 1
    fi
else
    echo ""
    echo "📦 Manual installation required:"
    echo ""
    echo "Recommended (fastest):"
    echo "  pip install faster-whisper"
    echo ""
    echo "Alternative (original):"
    echo "  pip install openai-whisper"
    echo ""
    echo "Optional (format conversion):"
    echo "  brew install ffmpeg  # macOS"
    echo "  apt install ffmpeg   # Linux"
    echo ""
    exit 1
fi
```

This ensures users can install dependencies with one confirmation, or opt for manual installation if preferred.

**If transcriber found:**

Proceed to Step 0b (CLI Detection).


### Step 1: Validate Audio File

**Objective:** Verify file exists, check format, and extract metadata.

**Actions:**

1. **Accept file path or URL** from user:
   - Local file: `meeting.mp3`
   - URL: `https://example.com/audio.mp3` (download to temp directory)

2. **Verify file exists:**

```bash
if [[ ! -f "$AUDIO_FILE" ]]; then
    echo "❌ File not found: $AUDIO_FILE"
    exit 1
fi
```

3. **Extract metadata** using ffprobe or file utilities:

```bash
# Get file size
FILE_SIZE=$(du -h "$AUDIO_FILE" | cut -f1)

# Get duration and format using ffprobe
DURATION=$(ffprobe -v error -show_entries format=duration \
    -of default=noprint_wrappers=1:nokey=1 "$AUDIO_FILE" 2>/dev/null)
FORMAT=$(ffprobe -v error -select_streams a:0 -show_entries \
    stream=codec_name -of default=noprint_wrappers=1:nokey=1 "$AUDIO_FILE" 2>/dev/null)

# Convert duration to HH:MM:SS
DURATION_HMS=$(date -u -r "$DURATION" +%H:%M:%S 2>/dev/null || echo "Unknown")
```

4. **Check file size** (warn if large for cloud APIs):

```bash
SIZE_MB=$(du -m "$AUDIO_FILE" | cut -f1)
if [[ $SIZE_MB -gt 25 ]]; then
    echo "⚠️  Large file ($FILE_SIZE) - processing may take several minutes"
fi
```

5. **Validate format** (supported: MP3, WAV, M4A, OGG, FLAC, WEBM):

```bash
EXTENSION="${AUDIO_FILE##*.}"
SUPPORTED_FORMATS=("mp3" "wav" "m4a" "ogg" "flac" "webm" "mp4")

if [[ ! " ${SUPPORTED_FORMATS[@]} " =~ " ${EXTENSION,,} " ]]; then
    echo "⚠️  Unsupported format: $EXTENSION"
    if command -v ffmpeg &>/dev/null; then
        echo "🔄 Converting to WAV..."
        ffmpeg -i "$AUDIO_FILE" -ar 16000 "${AUDIO_FILE%.*}.wav" -y
        AUDIO_FILE="${AUDIO_FILE%.*}.wav"
    else
        echo "❌ Install ffmpeg to convert formats: brew install ffmpeg"
        exit 1
    fi
fi
```


### Step 3: Generate Markdown Output

**Objective:** Create structured Markdown with metadata, transcription, meeting minutes, and summary.

**Output Template:**

```markdown
# Audio Transcription Report

## 📊 Metadata

| Field | Value |
|-------|-------|
| **File Name** | {filename} |
| **File Size** | {file_size} |
| **Duration** | {duration_hms} |
| **Language** | {language} ({language_code}) |
| **Processed Date** | {process_date} |
| **Speakers Identified** | {num_speakers} |
| **Transcription Engine** | {engine} (model: {model}) |


## 📋 Meeting Minutes

### Participants
- {speaker_1}
- {speaker_2}
- ...

### Topics Discussed
1. **{topic_1}** ({timestamp})
   - {key_point_1}
   - {key_point_2}

2. **{topic_2}** ({timestamp})
   - {key_point_1}

### Decisions Made
- ✅ {decision_1}
- ✅ {decision_2}

### Action Items
- [ ] **{action_1}** - Assigned to: {speaker} - Due: {date_if_mentioned}
- [ ] **{action_2}** - Assigned to: {speaker}


*Generated by audio-transcriber skill v1.0.0*  
*Transcription engine: {engine} | Processing time: {elapsed_time}s*
```

**Implementation:**

Use Python or bash with AI model (AI assistant/GPT) for intelligent summarization:

```python
def generate_meeting_minutes(segments):
    """Extract topics, decisions, action items from transcription."""
    
    # Group segments by topic (simple clustering by timestamps)
    topics = cluster_by_topic(segments)
    
    # Identify action items (keywords: "should", "will", "need to", "action")
    action_items = extract_action_items(segments)
    
    # Identify decisions (keywords: "decided", "agreed", "approved")
    decisions = extract_decisions(segments)
    
    return {
        "topics": topics,
        "decisions": decisions,
        "action_items": action_items
    }

def generate_summary(segments, max_paragraphs=5):
    """Create executive summary using AI (AI assistant/GPT via API or local model)."""
    
    full_text = " ".join([s["text"] for s in segments])
    
    # Use Chain of Density approach (from prompt-engineer frameworks)
    summary_prompt = f"""
    Summarize the following transcription in {max_paragraphs} concise paragraphs.
    Focus on key topics, decisions, and action items.
    
    Transcription:
    {full_text}
    """
    
    # Call AI model (placeholder - user can integrate LLM API or use local model)
    summary = call_ai_model(summary_prompt)
    
    return summary
```

**Output file naming:**

```bash
# v1.1.0: Use timestamp para evitar sobrescrever
TIMESTAMP=$(date +%Y%m%d-%H%M%S)
TRANSCRIPT_FILE="transcript-${TIMESTAMP}.md"
ATA_FILE="ata-${TIMESTAMP}.md"

echo "$TRANSCRIPT_CONTENT" > "$TRANSCRIPT_FILE"
echo "✅ Transcript salvo: $TRANSCRIPT_FILE"

if [[ -n "$ATA_CONTENT" ]]; then
    echo "$ATA_CONTENT" > "$ATA_FILE"
    echo "✅ Ata salva: $ATA_FILE"
fi
```


#### **SCENARIO A: User Provided Custom Prompt**

**Workflow:**

1. **Display user's prompt:**
   ```
   📝 Prompt fornecido pelo usuário:
   ┌──────────────────────────────────┐
   │ [User's prompt preview]          │
   └──────────────────────────────────┘
   ```

2. **Automatically improve with prompt-engineer (if available):**
   ```bash
   🔧 Melhorando prompt com prompt-engineer...
   [Invokes: gh copilot -p "melhore este prompt: {user_prompt}"]
   ```

3. **Show both versions:**
   ```
   ✨ Versão melhorada:
   ┌──────────────────────────────────┐
   │ Role: Você é um documentador...  │
   │ Instructions: Transforme...      │
   │ Steps: 1) ... 2) ...             │
   │ End Goal: ...                    │
   └──────────────────────────────────┘

   📝 Versão original:
   ┌──────────────────────────────────┐
   │ [User's original prompt]         │
   └──────────────────────────────────┘
   ```

4. **Ask which to use:**
   ```bash
   💡 Usar versão melhorada? [s/n] (default: s):
   ```

5. **Process with selected prompt:**
   - If "s": use improved
   - If "n": use original


#### **LLM Processing (Both Scenarios)**

Once prompt is finalized:

```python
from rich.progress import Progress, SpinnerColumn, TextColumn

def process_with_llm(transcript, prompt, cli_tool='agent-cli'):
    full_prompt = f"{prompt}\n\n---\n\nTranscrição:\n\n{transcript}"
    
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        transient=True
    ) as progress:
        progress.add_task(
            description=f"🤖 Processando com {cli_tool}...",
            total=None
        )
        
        if cli_tool == 'agent-cli':
            result = subprocess.run(
                ['agent-cli', '-'],
                input=full_prompt,
                capture_output=True,
                text=True,
                timeout=300  # 5 minutes
            )
        elif cli_tool == 'gh-copilot':
            result = subprocess.run(
                ['gh', 'copilot', 'suggest', '-t', 'shell', full_prompt],
                capture_output=True,
                text=True,
                timeout=300
            )
    
    if result.returncode == 0:
        return result.stdout.strip()
    else:
        return None
```

**Progress output:**
```
🤖 Processando com agent-cli... ⠋
[After completion:]
✅ Ata gerada com sucesso!
```


#### **Final Output**

**Success (both files):**
```bash
💾 Salvando arquivos...

✅ Arquivos criados:
  - transcript-20260203-023045.md  (transcript puro)
  - ata-20260203-023045.md         (processado com LLM)

🧹 Removidos arquivos temporários: metadata.json, transcription.json

✅ Concluído! Tempo total: 3m 45s
```

**Transcript only (user declined LLM):**
```bash
💾 Salvando arquivos...

✅ Arquivo criado:
  - transcript-20260203-023045.md

ℹ️  Ata não gerada (processamento LLM recusado pelo usuário)

🧹 Removidos arquivos temporários: metadata.json, transcription.json

✅ Concluído!
```


### Step 5: Display Results Summary

**Objective:** Show completion status and next steps.

**Output:**

```bash
echo ""
echo "✅ Transcription Complete!"
echo ""
echo "📊 Results:"
echo "  File: $OUTPUT_FILE"
echo "  Language: $LANGUAGE"
echo "  Duration: $DURATION_HMS"
echo "  Speakers: $NUM_SPEAKERS"
echo "  Words: $WORD_COUNT"
echo "  Processing time: ${ELAPSED_TIME}s"
echo ""
echo "📝 Generated:"
echo "  - $OUTPUT_FILE (Markdown report)"
[if alternative formats:]
echo "  - ${OUTPUT_FILE%.*}.srt (Subtitles)"
echo "  - ${OUTPUT_FILE%.*}.json (Structured data)"
echo ""
echo "🎯 Next steps:"
echo "  1. Review meeting minutes and action items"
echo "  2. Share report with participants"
echo "  3. Track action items to completion"
```


## Example Usage

### **Example 1: Basic Transcription**

**User Input:**
```bash
copilot> transcribe audio to markdown: meeting-2026-02-02.mp3
```

**Skill Output:**

```bash
✅ Faster-Whisper detected (optimized)
✅ ffmpeg available (format conversion enabled)

📂 File: meeting-2026-02-02.mp3
📊 Size: 12.3 MB
⏱️  Duration: 00:45:32

🎙️  Processing...
[████████████████████] 100%

✅ Language detected: Portuguese (pt-BR)
👥 Speakers identified: 4
📝 Generating Markdown output...

✅ Transcription Complete!

📊 Results:
  File: meeting-2026-02-02.md
  Language: pt-BR
  Duration: 00:45:32
  Speakers: 4
  Words: 6,842
  Processing time: 127s

📝 Generated:
  - meeting-2026-02-02.md (Markdown report)

🎯 Next steps:
  1. Review meeting minutes and action items
  2. Share report with participants
  3. Track action items to completion
```


### **Example 3: Batch Processing**

**User Input:**
```bash
copilot> transcreva estes áudios: recordings/*.mp3
```

**Skill Output:**

```bash
📦 Batch mode: 5 files found
  1. team-standup.mp3
  2. client-call.mp3
  3. brainstorm-session.mp3
  4. product-demo.mp3
  5. retrospective.mp3

🎙️  Processing batch...

[1/5] team-standup.mp3 ✅ (2m 34s)
[2/5] client-call.mp3 ✅ (15m 12s)
[3/5] brainstorm-session.mp3 ✅ (8m 47s)
[4/5] product-demo.mp3 ✅ (22m 03s)
[5/5] retrospective.mp3 ✅ (11m 28s)

✅ Batch Complete!
📝 Generated 5 Markdown reports
⏱️  Total processing time: 6m 15s
```


### **Example 5: Large File Warning**

**User Input:**
```bash
copilot> transcribe audio to markdown: conference-keynote.mp3
```

**Skill Output:**

```bash
✅ Faster-Whisper detected (optimized)

📂 File: conference-keynote.mp3
📊 Size: 87.2 MB
⏱️  Duration: 02:15:47
⚠️  Large file (87.2 MB) - processing may take several minutes

Continue? [Y/n]:
```

**User:** `Y`

```bash
🎙️  Processing... (this may take 10-15 minutes)
[████░░░░░░░░░░░░░░░░] 20% - Estimated time remaining: 12m
```


This skill is **platform-agnostic** and works in any terminal context where GitHub Copilot CLI is available. It does not depend on specific project configurations or external APIs, following the zero-configuration philosophy.

---

## Merged Reference (legacy variant)

---
name: fal-audio
description: "Text-to-speech and speech-to-text using fal.ai audio models"
risk: safe
source: "community audio-generation reference"
date_added: "2026-02-27"
---

# Fal Audio

## Overview

Text-to-speech and speech-to-text using fal.ai audio models

## When to Use This Skill

Use this skill when you need to work with text-to-speech and speech-to-text using fal.ai audio models.

## Instructions

This skill provides guidance and patterns for text-to-speech and speech-to-text using fal.ai audio models.

For more information, see the source reference.

---

## Merged Reference (legacy variant)

---
name: podcast-generation
description: "Generate AI-powered podcast-style audio narratives using Azure OpenAI's GPT Realtime Mini model via WebSocket. Use when building text-to-speech features, audio narrative generation, podcast creatio..."
risk: unknown
source: community
date_added: "2026-02-27"
---

# Podcast Generation with GPT Realtime Mini

Generate real audio narratives from text content using Azure OpenAI's Realtime API.

## Quick Start

1. Configure environment variables for Realtime API
2. Connect via WebSocket to Azure OpenAI Realtime endpoint
3. Send text prompt, collect PCM audio chunks + transcript
4. Convert PCM to WAV format
5. Return base64-encoded audio to frontend for playback

## Environment Configuration

```env
AZURE_OPENAI_AUDIO_API_KEY=your_realtime_api_key
AZURE_OPENAI_AUDIO_ENDPOINT=https://your-resource.cognitiveservices.azure.com
AZURE_OPENAI_AUDIO_DEPLOYMENT=gpt-realtime-mini
```

**Note**: Endpoint should NOT include `/openai/v1/` - just the base URL.

## Core Workflow

### Backend Audio Generation

```python
from openai import AsyncOpenAI
import base64

# Convert HTTPS endpoint to WebSocket URL
ws_url = endpoint.replace("https://", "wss://") + "/openai/v1"

client = AsyncOpenAI(
    websocket_base_url=ws_url,
    api_key=api_key
)

audio_chunks = []
transcript_parts = []

async with client.realtime.connect(model="gpt-realtime-mini") as conn:
    # Configure for audio-only output
    await conn.session.update(session={
        "output_modalities": ["audio"],
        "instructions": "You are a narrator. Speak naturally."
    })
    
    # Send text to narrate
    await conn.conversation.item.create(item={
        "type": "message",
        "role": "user",
        "content": [{"type": "input_text", "text": prompt}]
    })
    
    await conn.response.create()
    
    # Collect streaming events
    async for event in conn:
        if event.type == "response.output_audio.delta":
            audio_chunks.append(base64.b64decode(event.delta))
        elif event.type == "response.output_audio_transcript.delta":
            transcript_parts.append(event.delta)
        elif event.type == "response.done":
            break

# Convert PCM to WAV (see scripts/pcm_to_wav.py)
pcm_audio = b''.join(audio_chunks)
wav_audio = pcm_to_wav(pcm_audio, sample_rate=24000)
```

### Frontend Audio Playback

```javascript
// Convert base64 WAV to playable blob
const base64ToBlob = (base64, mimeType) => {
  const bytes = atob(base64);
  const arr = new Uint8Array(bytes.length);
  for (let i = 0; i < bytes.length; i++) arr[i] = bytes.charCodeAt(i);
  return new Blob([arr], { type: mimeType });
};

const audioBlob = base64ToBlob(response.audio_data, 'audio/wav');
const audioUrl = URL.createObjectURL(audioBlob);
new Audio(audioUrl).play();
```

## Voice Options

| Voice | Character |
|-------|-----------|
| alloy | Neutral |
| echo | Warm |
| fable | Expressive |
| onyx | Deep |
| nova | Friendly |
| shimmer | Clear |

## Realtime API Events

- `response.output_audio.delta` - Base64 audio chunk
- `response.output_audio_transcript.delta` - Transcript text
- `response.done` - Generation complete
- `error` - Handle with `event.error.message`

## Audio Format

- **Input**: Text prompt
- **Output**: PCM audio (24kHz, 16-bit, mono)
- **Storage**: Base64-encoded WAV

## References

- **Full architecture**: See references/architecture.md for complete stack design
- **Code examples**: See references/code-examples.md for production patterns
- **PCM conversion**: Use scripts/pcm_to_wav.py for audio format conversion

## When to Use
This skill is applicable to execute the workflow or actions described in the overview.

---

## Merged Reference (legacy variant)

---
name: remotion
description: Generate walkthrough videos from Stitch projects using Remotion with smooth transitions, zooming, and text overlays
allowed-tools:
  - "stitch*:*"
  - "remotion*:*"
  - "Bash"
  - "Read"
  - "Write"
  - "web_fetch"
risk: unknown
source: community
---

# Stitch to Remotion Walkthrough Videos

You are a video production specialist focused on creating engaging walkthrough videos from app designs. You combine Stitch's screen retrieval capabilities with Remotion's programmatic video generation to produce smooth, professional presentations.

## Overview

This skill enables you to create walkthrough videos that showcase app screens with professional transitions, zoom effects, and contextual text overlays. The workflow retrieves screens from Stitch projects and orchestrates them into a Remotion video composition.

## Prerequisites

**Required:**
- Access to the Stitch MCP Server
- Access to the Remotion MCP Server (or Remotion CLI)
- Node.js and npm installed
- A Stitch project with designed screens

**Recommended:**
- Familiarity with Remotion's video capabilities
- Understanding of React components (Remotion uses React)

## Retrieval and Networking

### Step 1: Discover Available MCP Servers

Run `list_tools` to identify available MCP servers and their prefixes:
- **Stitch MCP**: Look for `stitch:` or `mcp_stitch:` prefix
- **Remotion MCP**: Look for `remotion:` or `mcp_remotion:` prefix

### Step 2: Retrieve Stitch Project Information

1. **Project lookup** (if Project ID is not provided):
   - Call `[stitch_prefix]:list_projects` with `filter: "view=owned"`
   - Identify target project by title (e.g., "Calculator App")
   - Extract Project ID from `name` field (e.g., `projects/13534454087919359824`)

2. **Screen retrieval**:
   - Call `[stitch_prefix]:list_screens` with the project ID (numeric only)
   - Review screen titles to identify all screens for the walkthrough
   - Extract Screen IDs from each screen's `name` field

3. **Screen metadata fetch**:
   For each screen:
   - Call `[stitch_prefix]:get_screen` with `projectId` and `screenId`
   - Retrieve:
     - `screenshot.downloadUrl` — Visual asset for the video
     - `htmlCode.downloadUrl` — Optional: for extracting text/content
     - `width`, `height` — Screen dimensions for proper scaling
     - Screen title and description for text overlays

4. **Asset download**:
   - Use `web_fetch` or `Bash` with `curl` to download screenshots
   - Save to a staging directory: `assets/screens/{screen-name}.png`
   - Organize assets in order of the intended walkthrough flow

### Step 3: Set Up Remotion Project

1. **Check for existing Remotion project**:
   - Look for `remotion.config.ts` or `package.json` with Remotion dependencies
   - If exists, use the existing project structure

2. **Create new Remotion project** (if needed):
   ```bash
   npm create video@latest -- --blank
   ```
   - Choose TypeScript template
   - Set up in a dedicated `video/` directory

3. **Install dependencies**:
   ```bash
   cd video
   npm install @remotion/transitions @remotion/animated-emoji
   ```

## Video Composition Strategy

### Architecture

Create a modular Remotion composition with these components:

1. **`ScreenSlide.tsx`** — Individual screen display component
   - Props: `imageSrc`, `title`, `description`, `width`, `height`
   - Features: Zoom-in animation, fade transitions
   - Duration: Configurable (default 3-5 seconds per screen)

2. **`WalkthroughComposition.tsx`** — Main video composition
   - Sequences multiple `ScreenSlide` components
   - Handles transitions between screens
   - Adds text overlays and annotations

3. **`config.ts`** — Video configuration
   - Frame rate (default: 30 fps)
   - Video dimensions (match Stitch screen dimensions or scale appropriately)
   - Total duration calculation

### Transition Effects

Use Remotion's `@remotion/transitions` for professional effects:

- **Fade**: Smooth cross-fade between screens
  ```tsx
  import {fade} from '@remotion/transitions/fade';
  ```

- **Slide**: Directional slide transitions
  ```tsx
  import {slide} from '@remotion/transitions/slide';
  ```

- **Zoom**: Zoom in/out effects for emphasis
  - Use `spring()` animation for smooth zoom
  - Apply to important UI elements

### Text Overlays

Add contextual information using Remotion's text rendering:

1. **Screen titles**: Display at the top or bottom of each frame
2. **Feature callouts**: Highlight specific UI elements with animated pointers
3. **Descriptions**: Fade in descriptive text for each screen
4. **Progress indicator**: Show current screen position in walkthrough

## Execution Steps

### Step 1: Gather Screen Assets

1. Identify target Stitch project
2. List all screens in the project
3. Download screenshots for each screen
4. Organize in order of walkthrough flow
5. Create a manifest file (`screens.json`):

```json
{
  "projectName": "Calculator App",
  "screens": [
    {
      "id": "1",
      "title": "Home Screen",
      "description": "Main calculator interface with number pad",
      "imagePath": "assets/screens/home.png",
      "width": 1200,
      "height": 800,
      "duration": 4
    },
    {
      "id": "2",
      "title": "History View",
      "description": "View of previous calculations",
      "imagePath": "assets/screens/history.png",
      "width": 1200,
      "height": 800,
      "duration": 3
    }
  ]
}
```

### Step 2: Generate Remotion Components

Create the video components following Remotion best practices:

1. **Create `ScreenSlide.tsx`**:
   - Use `useCurrentFrame()` and `spring()` for animations
   - Implement zoom and fade effects
   - Add text overlays with proper timing

2. **Create `WalkthroughComposition.tsx`**:
   - Import screen manifest
   - Sequence screens with `<Sequence>` components
   - Apply transitions between screens
   - Calculate proper timing and offsets

3. **Update `remotion.config.ts`**:
   - Set composition ID
   - Configure video dimensions
   - Set frame rate and duration

**Reference Resources:**
- Use `resources/screen-slide-template.tsx` as starting point
- Follow `resources/composition-checklist.md` for completeness
- Review examples in `examples/walkthrough/` directory

### Step 3: Preview and Refine

1. **Start Remotion Studio**:
   ```bash
   npm run dev
   ```
   - Opens browser-based preview
   - Allows real-time editing and refinement

2. **Adjust timing**:
   - Ensure each screen has appropriate display duration
   - Verify transitions are smooth
   - Check text overlay timing

3. **Fine-tune animations**:
   - Adjust spring configurations for zoom effects
   - Modify easing functions for transitions
   - Ensure text is readable at all times

### Step 4: Render Video

1. **Render using Remotion CLI**:
   ```bash
   npx remotion render WalkthroughComposition output.mp4
   ```

2. **Alternative: Use Remotion MCP** (if available):
   - Call `[remotion_prefix]:render` with composition details
   - Specify output format (MP4, WebM, etc.)

3. **Optimization options**:
   - Set quality level (`--quality`)
   - Configure codec (`--codec h264` or `h265`)
   - Enable parallel rendering (`--concurrency`)

## Advanced Features

### Interactive Hotspots

Highlight clickable elements or important features:

```tsx
import {interpolate, useCurrentFrame} from 'remotion';

const Hotspot = ({x, y, label}) => {
  const frame = useCurrentFrame();
  const scale = spring({
    frame,
    fps: 30,
    config: {damping: 10, stiffness: 100}
  });
  
  return (
    <div style={{
      position: 'absolute',
      left: x,
      top: y,
      transform: `scale(${scale})`
    }}>
      <div className="pulse-ring" />
      <span>{label}</span>
    </div>
  );
};
```

### Voiceover Integration

Add narration to the walkthrough:

1. Generate voiceover script from screen descriptions
2. Use text-to-speech or record audio
3. Import audio into Remotion with `<Audio>` component
4. Sync screen timing with voiceover pacing

### Dynamic Text Extraction

Extract text from Stitch HTML code for automatic annotations:

1. Download `htmlCode.downloadUrl` for each screen
2. Parse HTML to extract key text elements (headings, buttons, labels)
3. Generate automatic callouts for important UI elements
4. Add to composition as timed text overlays

## File Structure

```
project/
├── video/                      # Remotion project directory
│   ├── src/
│   │   ├── WalkthroughComposition.tsx
│   │   ├── ScreenSlide.tsx
│   │   ├── components/
│   │   │   ├── Hotspot.tsx
│   │   │   └── TextOverlay.tsx
│   │   └── Root.tsx
│   ├── public/
│   │   └── assets/
│   │       └── screens/        # Downloaded Stitch screenshots
│   │           ├── home.png
│   │           └── history.png
│   ├── remotion.config.ts
│   └── package.json
├── screens.json                # Screen manifest
└── output.mp4                  # Rendered video
```

## Integration with Remotion Skills

Remotion maintains its own Agent Skills that define best practices. Review these for advanced techniques:

- **Repository**: https://github.com/remotion-dev/remotion/tree/main/packages/skills
- **Installation**: `npx skills add remotion-dev/skills`

Key Remotion skills to leverage:
- Animation timing and easing
- Composition architecture patterns
- Performance optimization
- Audio synchronization

## Common Patterns

### Pattern 1: Simple Slide Show

Basic walkthrough with fade transitions:
- 3-5 seconds per screen
- Cross-fade transitions
- Bottom text overlay with screen title
- Progress bar at top

### Pattern 2: Feature Highlight

Focus on specific UI elements:
- Zoom into specific regions
- Animated circles/arrows pointing to features
- Slow-motion emphasis on key interactions
- Side-by-side before/after comparisons

### Pattern 3: User Flow

Show step-by-step user journey:
- Sequential screen flow with directional slides
- Numbered steps overlay
- Highlight user actions (clicks, taps)
- Connect screens with animated paths

## Troubleshooting

| Issue | Solution |
|-------|----------|
| **Blurry screenshots** | Ensure downloaded images are at full resolution; check `screenshot.downloadUrl` quality settings |
| **Misaligned text** | Verify screen dimensions match composition size; adjust text positioning based on actual screen size |
| **Choppy animations** | Increase frame rate to 60fps; use proper spring configurations with appropriate damping |
| **Remotion build fails** | Check Node version compatibility; ensure all dependencies are installed; review Remotion docs |
| **Timing feels off** | Adjust duration per screen in manifest; preview in Remotion Studio; test with actual users |

## Best Practices

1. **Maintain aspect ratio**: Use actual Stitch screen dimensions or scale proportionally
2. **Consistent timing**: Keep screen display duration consistent unless emphasizing specific screens
3. **Readable text**: Ensure sufficient contrast; use appropriate font sizes; avoid cluttered overlays
4. **Smooth transitions**: Use spring animations for natural motion; avoid jarring cuts
5. **Preview thoroughly**: Always preview in Remotion Studio before final render
6. **Optimize assets**: Compress images appropriately; use efficient formats (PNG for UI, JPG for photos)

## Example Usage

**User prompt:**
```
Look up the screens in my Stitch project "Calculator App" and build a remotion video 
that shows a walkthrough of the screens.
```

**Agent workflow:**
1. List Stitch projects → Find "Calculator App" → Extract project ID
2. List screens in project → Identify all screens (Home, History, Settings)
3. Download screenshots for each screen → Save to `assets/screens/`
4. Create `screens.json` manifest with screen metadata
5. Generate Remotion components (`ScreenSlide.tsx`, `WalkthroughComposition.tsx`)
6. Preview in Remotion Studio → Refine timing and transitions
7. Render final video → `calculator-walkthrough.mp4`
8. Report completion with video preview link

## Tips for Success

- **Start simple**: Begin with basic fade transitions before adding complex animations
- **Follow Remotion patterns**: Leverage Remotion's official skills and documentation
- **Use manifest files**: Keep screen data organized in JSON for easy updates
- **Preview frequently**: Use Remotion Studio to catch issues early
- **Consider accessibility**: Add captions; ensure text is readable; use clear visuals
- **Optimize for platform**: Match video dimensions to target platform (YouTube, social media, etc.)

## References

- **Stitch Documentation**: https://stitch.withgoogle.com/docs/
- **Remotion Documentation**: https://www.remotion.dev/docs/
- **Remotion Skills**: https://www.remotion.dev/docs/ai/skills
- **Remotion MCP**: https://www.remotion.dev/docs/ai/mcp
- **Remotion Transitions**: https://www.remotion.dev/docs/transitions


## When to Use

Use this skill when tackling tasks related to its primary domain or functionality as described above.

---

## Merged Reference (legacy variant)

---
name: remotion-best-practices
description: "Best practices for Remotion - Video creation in React"
risk: unknown
source: community
tags: "remotion, video, react, animation, composition"
date_added: "2026-02-27"
---

## When to use

Use this skills whenever you are dealing with Remotion code to obtain the domain-specific knowledge.

## How to use

Read individual rule files for detailed explanations and code examples:

- [rules/3d.md](rules/3d.md) - 3D content in Remotion using Three.js and React Three Fiber
- [rules/animations.md](rules/animations.md) - Fundamental animation skills for Remotion
- [rules/assets.md](rules/assets.md) - Importing images, videos, audio, and fonts into Remotion
- [rules/audio.md](rules/audio.md) - Using audio and sound in Remotion - importing, trimming, volume, speed, pitch
- [rules/calculate-metadata.md](rules/calculate-metadata.md) - Dynamically set composition duration, dimensions, and props
- [rules/can-decode.md](rules/can-decode.md) - Check if a video can be decoded by the browser using Mediabunny
- [rules/charts.md](rules/charts.md) - Chart and data visualization patterns for Remotion
- [rules/compositions.md](rules/compositions.md) - Defining compositions, stills, folders, default props and dynamic metadata
- [rules/display-captions.md](rules/display-captions.md) - Displaying captions in Remotion with TikTok-style pages and word highlighting
- [rules/extract-frames.md](rules/extract-frames.md) - Extract frames from videos at specific timestamps using Mediabunny
- [rules/fonts.md](rules/fonts.md) - Loading Google Fonts and local fonts in Remotion
- [rules/get-audio-duration.md](rules/get-audio-duration.md) - Getting the duration of an audio file in seconds with Mediabunny
- [rules/get-video-dimensions.md](rules/get-video-dimensions.md) - Getting the width and height of a video file with Mediabunny
- [rules/get-video-duration.md](rules/get-video-duration.md) - Getting the duration of a video file in seconds with Mediabunny
- [rules/gifs.md](rules/gifs.md) - Displaying GIFs synchronized with Remotion's timeline
- [rules/images.md](rules/images.md) - Embedding images in Remotion using the Img component
- [rules/import-srt-captions.md](rules/import-srt-captions.md) - Importing .srt subtitle files into Remotion using @remotion/captions
- [rules/lottie.md](rules/lottie.md) - Embedding Lottie animations in Remotion
- [rules/measuring-dom-nodes.md](rules/measuring-dom-nodes.md) - Measuring DOM element dimensions in Remotion
- [rules/measuring-text.md](rules/measuring-text.md) - Measuring text dimensions, fitting text to containers, and checking overflow
- [rules/sequencing.md](rules/sequencing.md) - Sequencing patterns for Remotion - delay, trim, limit duration of items
- [rules/tailwind.md](rules/tailwind.md) - Using TailwindCSS in Remotion
- [rules/text-animations.md](rules/text-animations.md) - Typography and text animation patterns for Remotion
- [rules/timing.md](rules/timing.md) - Interpolation curves in Remotion - linear, easing, spring animations
- [rules/transcribe-captions.md](rules/transcribe-captions.md) - Transcribing audio to generate captions in Remotion
- [rules/transitions.md](rules/transitions.md) - Scene transition patterns for Remotion
- [rules/trimming.md](rules/trimming.md) - Trimming patterns for Remotion - cut the beginning or end of animations
- [rules/videos.md](rules/videos.md) - Embedding videos in Remotion - trimming, volume, speed, looping, pitch

---

## Merged Reference (legacy variant)

---
name: videodb-skills
description: "Upload, stream, search, edit, transcribe, and generate AI video and audio using the VideoDB SDK."
category: media
risk: safe
source: community
tags: "[video, editing, transcription, subtitles, search, streaming, ai-generation, media]"
date_added: "2026-02-27"
---

# VideoDB Skills

## Purpose

The only video skill your agent needs. Upload any video, connect real-time streams, search inside by what was said or shown, build complex editing workflows with overlays, generate AI media, add subtitles, and get instant streaming links — all via the VideoDB Python SDK.

## When to Use This Skill

- User wants to upload and process videos from YouTube, URLs, or local files
- User needs to search for moments by speech or visual scenes
- User asks for transcription, subtitles, or subtitle styling
- User wants to edit clips — trim, combine, add text/image/audio overlays
- User needs AI-generated media (images, video, music, sound effects, voiceovers)
- User wants to transcode, change resolution, or reframe for social platforms
- User needs real-time screen or audio capture with AI transcription
- User asks for playable streaming links for any video output

## Setup

### Step 1: Install the skill

```bash
npx skills add video-db/skills
```

### Step 2: Run setup

```
/videodb setup
```

The agent guides API key setup ($20 free credits, no credit card), installs the SDK, and verifies the connection.

Alternatively, set the API key manually:

```bash
export VIDEO_DB_API_KEY=sk-xxx
```

### Step 3: Install the SDK

```bash
pip install "videodb[capture]" python-dotenv
```

## Capabilities

| Capability  | Description                                                               |
| ----------- | ------------------------------------------------------------------------- |
| Upload      | Ingest videos from YouTube, URLs, or local files                          |
| Search      | Find moments by speech (semantic/keyword) or visual scenes                |
| Transcripts | Generate timestamped transcripts from any video                           |
| Edit        | Combine clips, trim, add text/image/audio overlays                        |
| Subtitles   | Auto-generate and style subtitles                                         |
| AI Generate | Create images, video, music, sound effects, and voiceovers from text      |
| Capture     | Real-time screen and audio capture with AI transcription                  |
| Transcode   | Change resolution, quality, aspect ratio, or reframe for social platforms |
| Stream      | Get playable HLS links for anything you build                             |

## Examples

**Upload and transcribe:**

```
"Upload https://www.youtube.com/watch?v=FgrO9ADPZSA and give me a transcript"
```

**Search across videos:**

```
"Search for 'product demo' in my latest video"
```

**Add subtitles:**

```
"Add subtitles with white text on black background"
```

**Multi-clip editing:**

```
"Take clips from 10s-30s and 45s-60s, add a title card, and combine them"
```

**AI media generation:**

```
"Generate background music and overlay it on my video"
```

**Real-time capture:**

```
"Capture my screen and transcribe it in real-time"
```

**Reframe for social:**

```
"Convert this to vertical for Instagram Reels"
```

## Repository

https://github.com/video-db/skills

**Version:** 1.1.0
**Maintained By:** [VideoDB](https://github.com/video-db)

## Source: references/skills/videodb/references/legacy/audio-transcriber/SKILL.md

---
name: audio-transcriber
description: "Transform audio recordings into professional Markdown documentation with intelligent summaries using LLM integration"
category: content
risk: safe
source: community
tags: "[audio, transcription, whisper, meeting-minutes, speech-to-text]"
date_added: "2026-02-27"
---

## Purpose

This skill automates audio-to-text transcription with professional Markdown output, extracting rich technical metadata (speakers, timestamps, language, file size, duration) and generating structured meeting minutes and executive summaries. It uses Faster-Whisper or Whisper with zero configuration, working universally across projects without hardcoded paths or API keys.

Inspired by tools like Plaud, this skill transforms raw audio recordings into actionable documentation, making it ideal for meetings, interviews, lectures, and content analysis.

## When to Use

Invoke this skill when:

- User needs to transcribe audio/video files to text
- User wants meeting minutes automatically generated from recordings
- User requires speaker identification (diarization) in conversations
- User needs subtitles/captions (SRT, VTT formats)
- User wants executive summaries of long audio content
- User asks variations of "transcribe this audio", "convert audio to text", "generate meeting notes from recording"
- User has audio files in common formats (MP3, WAV, M4A, OGG, FLAC, WEBM)

## Workflow

### Step 0: Discovery (Auto-detect Transcription Tools)

**Objective:** Identify available transcription engines without user configuration.

**Actions:**

Run detection commands to find installed tools:

```bash
# Check for Faster-Whisper (preferred - 4-5x faster)
if python3 -c "import faster_whisper" 2>/dev/null; then
    TRANSCRIBER="faster-whisper"
    echo "✅ Faster-Whisper detected (optimized)"
# Fallback to original Whisper
elif python3 -c "import whisper" 2>/dev/null; then
    TRANSCRIBER="whisper"
    echo "✅ OpenAI Whisper detected"
else
    TRANSCRIBER="none"
    echo "⚠️  No transcription tool found"
fi

# Check for ffmpeg (audio format conversion)
if command -v ffmpeg &>/dev/null; then
    echo "✅ ffmpeg available (format conversion enabled)"
else
    echo "ℹ️  ffmpeg not found (limited format support)"
fi
```

**If no transcriber found:**

Offer automatic installation using the provided script:

```bash
echo "⚠️  No transcription tool found"
echo ""
echo "🔧 Auto-install dependencies? (Recommended)"
read -p "Run installation script? [Y/n]: " AUTO_INSTALL

if [[ ! "$AUTO_INSTALL" =~ ^[Nn] ]]; then
    # Get skill directory (works for both repo and symlinked installations)
    SKILL_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
    
    # Run installation script
    if [[ -f "$SKILL_DIR/scripts/install-requirements.sh" ]]; then
        bash "$SKILL_DIR/scripts/install-requirements.sh"
    else
        echo "❌ Installation script not found"
        echo ""
        echo "📦 Manual installation:"
        echo "  pip install faster-whisper  # Recommended"
        echo "  pip install openai-whisper  # Alternative"
        echo "  brew install ffmpeg         # Optional (macOS)"
        exit 1
    fi
    
    # Verify installation succeeded
    if python3 -c "import faster_whisper" 2>/dev/null || python3 -c "import whisper" 2>/dev/null; then
        echo "✅ Installation successful! Proceeding with transcription..."
    else
        echo "❌ Installation failed. Please install manually."
        exit 1
    fi
else
    echo ""
    echo "📦 Manual installation required:"
    echo ""
    echo "Recommended (fastest):"
    echo "  pip install faster-whisper"
    echo ""
    echo "Alternative (original):"
    echo "  pip install openai-whisper"
    echo ""
    echo "Optional (format conversion):"
    echo "  brew install ffmpeg  # macOS"
    echo "  apt install ffmpeg   # Linux"
    echo ""
    exit 1
fi
```

This ensures users can install dependencies with one confirmation, or opt for manual installation if preferred.

**If transcriber found:**

Proceed to Step 0b (CLI Detection).


### Step 1: Validate Audio File

**Objective:** Verify file exists, check format, and extract metadata.

**Actions:**

1. **Accept file path or URL** from user:
   - Local file: `meeting.mp3`
   - URL: `https://example.com/audio.mp3` (download to temp directory)

2. **Verify file exists:**

```bash
if [[ ! -f "$AUDIO_FILE" ]]; then
    echo "❌ File not found: $AUDIO_FILE"
    exit 1
fi
```

3. **Extract metadata** using ffprobe or file utilities:

```bash
# Get file size
FILE_SIZE=$(du -h "$AUDIO_FILE" | cut -f1)

# Get duration and format using ffprobe
DURATION=$(ffprobe -v error -show_entries format=duration \
    -of default=noprint_wrappers=1:nokey=1 "$AUDIO_FILE" 2>/dev/null)
FORMAT=$(ffprobe -v error -select_streams a:0 -show_entries \
    stream=codec_name -of default=noprint_wrappers=1:nokey=1 "$AUDIO_FILE" 2>/dev/null)

# Convert duration to HH:MM:SS
DURATION_HMS=$(date -u -r "$DURATION" +%H:%M:%S 2>/dev/null || echo "Unknown")
```

4. **Check file size** (warn if large for cloud APIs):

```bash
SIZE_MB=$(du -m "$AUDIO_FILE" | cut -f1)
if [[ $SIZE_MB -gt 25 ]]; then
    echo "⚠️  Large file ($FILE_SIZE) - processing may take several minutes"
fi
```

5. **Validate format** (supported: MP3, WAV, M4A, OGG, FLAC, WEBM):

```bash
EXTENSION="${AUDIO_FILE##*.}"
SUPPORTED_FORMATS=("mp3" "wav" "m4a" "ogg" "flac" "webm" "mp4")

if [[ ! " ${SUPPORTED_FORMATS[@]} " =~ " ${EXTENSION,,} " ]]; then
    echo "⚠️  Unsupported format: $EXTENSION"
    if command -v ffmpeg &>/dev/null; then
        echo "🔄 Converting to WAV..."
        ffmpeg -i "$AUDIO_FILE" -ar 16000 "${AUDIO_FILE%.*}.wav" -y
        AUDIO_FILE="${AUDIO_FILE%.*}.wav"
    else
        echo "❌ Install ffmpeg to convert formats: brew install ffmpeg"
        exit 1
    fi
fi
```


### Step 3: Generate Markdown Output

**Objective:** Create structured Markdown with metadata, transcription, meeting minutes, and summary.

**Output Template:**

```markdown
# Audio Transcription Report

## 📊 Metadata

| Field | Value |
|-------|-------|
| **File Name** | {filename} |
| **File Size** | {file_size} |
| **Duration** | {duration_hms} |
| **Language** | {language} ({language_code}) |
| **Processed Date** | {process_date} |
| **Speakers Identified** | {num_speakers} |
| **Transcription Engine** | {engine} (model: {model}) |


## 📋 Meeting Minutes

### Participants
- {speaker_1}
- {speaker_2}
- ...

### Topics Discussed
1. **{topic_1}** ({timestamp})
   - {key_point_1}
   - {key_point_2}

2. **{topic_2}** ({timestamp})
   - {key_point_1}

### Decisions Made
- ✅ {decision_1}
- ✅ {decision_2}

### Action Items
- [ ] **{action_1}** - Assigned to: {speaker} - Due: {date_if_mentioned}
- [ ] **{action_2}** - Assigned to: {speaker}


*Generated by audio-transcriber skill v1.0.0*  
*Transcription engine: {engine} | Processing time: {elapsed_time}s*
```

**Implementation:**

Use Python or bash with AI model (AI assistant/GPT) for intelligent summarization:

```python
def generate_meeting_minutes(segments):
    """Extract topics, decisions, action items from transcription."""
    
    # Group segments by topic (simple clustering by timestamps)
    topics = cluster_by_topic(segments)
    
    # Identify action items (keywords: "should", "will", "need to", "action")
    action_items = extract_action_items(segments)
    
    # Identify decisions (keywords: "decided", "agreed", "approved")
    decisions = extract_decisions(segments)
    
    return {
        "topics": topics,
        "decisions": decisions,
        "action_items": action_items
    }

def generate_summary(segments, max_paragraphs=5):
    """Create executive summary using AI (AI assistant/GPT via API or local model)."""
    
    full_text = " ".join([s["text"] for s in segments])
    
    # Use Chain of Density approach (from prompt-engineer frameworks)
    summary_prompt = f"""
    Summarize the following transcription in {max_paragraphs} concise paragraphs.
    Focus on key topics, decisions, and action items.
    
    Transcription:
    {full_text}
    """
    
    # Call AI model (placeholder - user can integrate LLM API or use local model)
    summary = call_ai_model(summary_prompt)
    
    return summary
```

**Output file naming:**

```bash
# v1.1.0: Use timestamp para evitar sobrescrever
TIMESTAMP=$(date +%Y%m%d-%H%M%S)
TRANSCRIPT_FILE="transcript-${TIMESTAMP}.md"
ATA_FILE="ata-${TIMESTAMP}.md"

echo "$TRANSCRIPT_CONTENT" > "$TRANSCRIPT_FILE"
echo "✅ Transcript salvo: $TRANSCRIPT_FILE"

if [[ -n "$ATA_CONTENT" ]]; then
    echo "$ATA_CONTENT" > "$ATA_FILE"
    echo "✅ Ata salva: $ATA_FILE"
fi
```


#### **SCENARIO A: User Provided Custom Prompt**

**Workflow:**

1. **Display user's prompt:**
   ```
   📝 Prompt fornecido pelo usuário:
   ┌──────────────────────────────────┐
   │ [User's prompt preview]          │
   └──────────────────────────────────┘
   ```

2. **Automatically improve with prompt-engineer (if available):**
   ```bash
   🔧 Melhorando prompt com prompt-engineer...
   [Invokes: gh copilot -p "melhore este prompt: {user_prompt}"]
   ```

3. **Show both versions:**
   ```
   ✨ Versão melhorada:
   ┌──────────────────────────────────┐
   │ Role: Você é um documentador...  │
   │ Instructions: Transforme...      │
   │ Steps: 1) ... 2) ...             │
   │ End Goal: ...                    │
   └──────────────────────────────────┘

   📝 Versão original:
   ┌──────────────────────────────────┐
   │ [User's original prompt]         │
   └──────────────────────────────────┘
   ```

4. **Ask which to use:**
   ```bash
   💡 Usar versão melhorada? [s/n] (default: s):
   ```

5. **Process with selected prompt:**
   - If "s": use improved
   - If "n": use original


#### **LLM Processing (Both Scenarios)**

Once prompt is finalized:

```python
from rich.progress import Progress, SpinnerColumn, TextColumn

def process_with_llm(transcript, prompt, cli_tool='agent-cli'):
    full_prompt = f"{prompt}\n\n---\n\nTranscrição:\n\n{transcript}"
    
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        transient=True
    ) as progress:
        progress.add_task(
            description=f"🤖 Processando com {cli_tool}...",
            total=None
        )
        
        if cli_tool == 'agent-cli':
            result = subprocess.run(
                ['agent-cli', '-'],
                input=full_prompt,
                capture_output=True,
                text=True,
                timeout=300  # 5 minutes
            )
        elif cli_tool == 'gh-copilot':
            result = subprocess.run(
                ['gh', 'copilot', 'suggest', '-t', 'shell', full_prompt],
                capture_output=True,
                text=True,
                timeout=300
            )
    
    if result.returncode == 0:
        return result.stdout.strip()
    else:
        return None
```

**Progress output:**
```
🤖 Processando com agent-cli... ⠋
[After completion:]
✅ Ata gerada com sucesso!
```


#### **Final Output**

**Success (both files):**
```bash
💾 Salvando arquivos...

✅ Arquivos criados:
  - transcript-20260203-023045.md  (transcript puro)
  - ata-20260203-023045.md         (processado com LLM)

🧹 Removidos arquivos temporários: metadata.json, transcription.json

✅ Concluído! Tempo total: 3m 45s
```

**Transcript only (user declined LLM):**
```bash
💾 Salvando arquivos...

✅ Arquivo criado:
  - transcript-20260203-023045.md

ℹ️  Ata não gerada (processamento LLM recusado pelo usuário)

🧹 Removidos arquivos temporários: metadata.json, transcription.json

✅ Concluído!
```


### Step 5: Display Results Summary

**Objective:** Show completion status and next steps.

**Output:**

```bash
echo ""
echo "✅ Transcription Complete!"
echo ""
echo "📊 Results:"
echo "  File: $OUTPUT_FILE"
echo "  Language: $LANGUAGE"
echo "  Duration: $DURATION_HMS"
echo "  Speakers: $NUM_SPEAKERS"
echo "  Words: $WORD_COUNT"
echo "  Processing time: ${ELAPSED_TIME}s"
echo ""
echo "📝 Generated:"
echo "  - $OUTPUT_FILE (Markdown report)"
[if alternative formats:]
echo "  - ${OUTPUT_FILE%.*}.srt (Subtitles)"
echo "  - ${OUTPUT_FILE%.*}.json (Structured data)"
echo ""
echo "🎯 Next steps:"
echo "  1. Review meeting minutes and action items"
echo "  2. Share report with participants"
echo "  3. Track action items to completion"
```


## Example Usage

### **Example 1: Basic Transcription**

**User Input:**
```bash
copilot> transcribe audio to markdown: meeting-2026-02-02.mp3
```

**Skill Output:**

```bash
✅ Faster-Whisper detected (optimized)
✅ ffmpeg available (format conversion enabled)

📂 File: meeting-2026-02-02.mp3
📊 Size: 12.3 MB
⏱️  Duration: 00:45:32

🎙️  Processing...
[████████████████████] 100%

✅ Language detected: Portuguese (pt-BR)
👥 Speakers identified: 4
📝 Generating Markdown output...

✅ Transcription Complete!

📊 Results:
  File: meeting-2026-02-02.md
  Language: pt-BR
  Duration: 00:45:32
  Speakers: 4
  Words: 6,842
  Processing time: 127s

📝 Generated:
  - meeting-2026-02-02.md (Markdown report)

🎯 Next steps:
  1. Review meeting minutes and action items
  2. Share report with participants
  3. Track action items to completion
```


### **Example 3: Batch Processing**

**User Input:**
```bash
copilot> transcreva estes áudios: recordings/*.mp3
```

**Skill Output:**

```bash
📦 Batch mode: 5 files found
  1. team-standup.mp3
  2. client-call.mp3
  3. brainstorm-session.mp3
  4. product-demo.mp3
  5. retrospective.mp3

🎙️  Processing batch...

[1/5] team-standup.mp3 ✅ (2m 34s)
[2/5] client-call.mp3 ✅ (15m 12s)
[3/5] brainstorm-session.mp3 ✅ (8m 47s)
[4/5] product-demo.mp3 ✅ (22m 03s)
[5/5] retrospective.mp3 ✅ (11m 28s)

✅ Batch Complete!
📝 Generated 5 Markdown reports
⏱️  Total processing time: 6m 15s
```


### **Example 5: Large File Warning**

**User Input:**
```bash
copilot> transcribe audio to markdown: conference-keynote.mp3
```

**Skill Output:**

```bash
✅ Faster-Whisper detected (optimized)

📂 File: conference-keynote.mp3
📊 Size: 87.2 MB
⏱️  Duration: 02:15:47
⚠️  Large file (87.2 MB) - processing may take several minutes

Continue? [Y/n]:
```

**User:** `Y`

```bash
🎙️  Processing... (this may take 10-15 minutes)
[████░░░░░░░░░░░░░░░░] 20% - Estimated time remaining: 12m
```


This skill is **platform-agnostic** and works in any terminal context where GitHub Copilot CLI is available. It does not depend on specific project configurations or external APIs, following the zero-configuration philosophy.

## Source: references/skills/videodb/references/legacy/fal-audio/SKILL.md

---
name: fal-audio
description: "Text-to-speech and speech-to-text using fal.ai audio models"
risk: safe
source: "community audio-generation reference"
date_added: "2026-02-27"
---

# Fal Audio

## Overview

Text-to-speech and speech-to-text using fal.ai audio models

## When to Use This Skill

Use this skill when you need to work with text-to-speech and speech-to-text using fal.ai audio models.

## Instructions

This skill provides guidance and patterns for text-to-speech and speech-to-text using fal.ai audio models.

For more information, see the source reference.

## Source: references/skills/videodb/references/legacy/podcast-generation/SKILL.md

---
name: podcast-generation
description: "Generate AI-powered podcast-style audio narratives using Azure OpenAI's GPT Realtime Mini model via WebSocket. Use when building text-to-speech features, audio narrative generation, podcast creatio..."
risk: unknown
source: community
date_added: "2026-02-27"
---

# Podcast Generation with GPT Realtime Mini

Generate real audio narratives from text content using Azure OpenAI's Realtime API.

## Quick Start

1. Configure environment variables for Realtime API
2. Connect via WebSocket to Azure OpenAI Realtime endpoint
3. Send text prompt, collect PCM audio chunks + transcript
4. Convert PCM to WAV format
5. Return base64-encoded audio to frontend for playback

## Environment Configuration

```env
AZURE_OPENAI_AUDIO_API_KEY=your_realtime_api_key
AZURE_OPENAI_AUDIO_ENDPOINT=https://your-resource.cognitiveservices.azure.com
AZURE_OPENAI_AUDIO_DEPLOYMENT=gpt-realtime-mini
```

**Note**: Endpoint should NOT include `/openai/v1/` - just the base URL.

## Core Workflow

### Backend Audio Generation

```python
from openai import AsyncOpenAI
import base64

# Convert HTTPS endpoint to WebSocket URL
ws_url = endpoint.replace("https://", "wss://") + "/openai/v1"

client = AsyncOpenAI(
    websocket_base_url=ws_url,
    api_key=api_key
)

audio_chunks = []
transcript_parts = []

async with client.realtime.connect(model="gpt-realtime-mini") as conn:
    # Configure for audio-only output
    await conn.session.update(session={
        "output_modalities": ["audio"],
        "instructions": "You are a narrator. Speak naturally."
    })
    
    # Send text to narrate
    await conn.conversation.item.create(item={
        "type": "message",
        "role": "user",
        "content": [{"type": "input_text", "text": prompt}]
    })
    
    await conn.response.create()
    
    # Collect streaming events
    async for event in conn:
        if event.type == "response.output_audio.delta":
            audio_chunks.append(base64.b64decode(event.delta))
        elif event.type == "response.output_audio_transcript.delta":
            transcript_parts.append(event.delta)
        elif event.type == "response.done":
            break

# Convert PCM to WAV (see scripts/pcm_to_wav.py)
pcm_audio = b''.join(audio_chunks)
wav_audio = pcm_to_wav(pcm_audio, sample_rate=24000)
```

### Frontend Audio Playback

```javascript
// Convert base64 WAV to playable blob
const base64ToBlob = (base64, mimeType) => {
  const bytes = atob(base64);
  const arr = new Uint8Array(bytes.length);
  for (let i = 0; i < bytes.length; i++) arr[i] = bytes.charCodeAt(i);
  return new Blob([arr], { type: mimeType });
};

const audioBlob = base64ToBlob(response.audio_data, 'audio/wav');
const audioUrl = URL.createObjectURL(audioBlob);
new Audio(audioUrl).play();
```

## Voice Options

| Voice | Character |
|-------|-----------|
| alloy | Neutral |
| echo | Warm |
| fable | Expressive |
| onyx | Deep |
| nova | Friendly |
| shimmer | Clear |

## Realtime API Events

- `response.output_audio.delta` - Base64 audio chunk
- `response.output_audio_transcript.delta` - Transcript text
- `response.done` - Generation complete
- `error` - Handle with `event.error.message`

## Audio Format

- **Input**: Text prompt
- **Output**: PCM audio (24kHz, 16-bit, mono)
- **Storage**: Base64-encoded WAV

## References

- **Full architecture**: See references/architecture.md for complete stack design
- **Code examples**: See references/code-examples.md for production patterns
- **PCM conversion**: Use scripts/pcm_to_wav.py for audio format conversion

## When to Use
This skill is applicable to execute the workflow or actions described in the overview.

## Source: references/skills/videodb/references/legacy/remotion/SKILL.md

---
name: remotion
description: Generate walkthrough videos from Stitch projects using Remotion with smooth transitions, zooming, and text overlays
allowed-tools:
  - "stitch*:*"
  - "remotion*:*"
  - "Bash"
  - "Read"
  - "Write"
  - "web_fetch"
risk: unknown
source: community
---

# Stitch to Remotion Walkthrough Videos

You are a video production specialist focused on creating engaging walkthrough videos from app designs. You combine Stitch's screen retrieval capabilities with Remotion's programmatic video generation to produce smooth, professional presentations.

## Overview

This skill enables you to create walkthrough videos that showcase app screens with professional transitions, zoom effects, and contextual text overlays. The workflow retrieves screens from Stitch projects and orchestrates them into a Remotion video composition.

## Prerequisites

**Required:**
- Access to the Stitch MCP Server
- Access to the Remotion MCP Server (or Remotion CLI)
- Node.js and npm installed
- A Stitch project with designed screens

**Recommended:**
- Familiarity with Remotion's video capabilities
- Understanding of React components (Remotion uses React)

## Retrieval and Networking

### Step 1: Discover Available MCP Servers

Run `list_tools` to identify available MCP servers and their prefixes:
- **Stitch MCP**: Look for `stitch:` or `mcp_stitch:` prefix
- **Remotion MCP**: Look for `remotion:` or `mcp_remotion:` prefix

### Step 2: Retrieve Stitch Project Information

1. **Project lookup** (if Project ID is not provided):
   - Call `[stitch_prefix]:list_projects` with `filter: "view=owned"`
   - Identify target project by title (e.g., "Calculator App")
   - Extract Project ID from `name` field (e.g., `projects/13534454087919359824`)

2. **Screen retrieval**:
   - Call `[stitch_prefix]:list_screens` with the project ID (numeric only)
   - Review screen titles to identify all screens for the walkthrough
   - Extract Screen IDs from each screen's `name` field

3. **Screen metadata fetch**:
   For each screen:
   - Call `[stitch_prefix]:get_screen` with `projectId` and `screenId`
   - Retrieve:
     - `screenshot.downloadUrl` — Visual asset for the video
     - `htmlCode.downloadUrl` — Optional: for extracting text/content
     - `width`, `height` — Screen dimensions for proper scaling
     - Screen title and description for text overlays

4. **Asset download**:
   - Use `web_fetch` or `Bash` with `curl` to download screenshots
   - Save to a staging directory: `assets/screens/{screen-name}.png`
   - Organize assets in order of the intended walkthrough flow

### Step 3: Set Up Remotion Project

1. **Check for existing Remotion project**:
   - Look for `remotion.config.ts` or `package.json` with Remotion dependencies
   - If exists, use the existing project structure

2. **Create new Remotion project** (if needed):
   ```bash
   npm create video@latest -- --blank
   ```
   - Choose TypeScript template
   - Set up in a dedicated `video/` directory

3. **Install dependencies**:
   ```bash
   cd video
   npm install @remotion/transitions @remotion/animated-emoji
   ```

## Video Composition Strategy

### Architecture

Create a modular Remotion composition with these components:

1. **`ScreenSlide.tsx`** — Individual screen display component
   - Props: `imageSrc`, `title`, `description`, `width`, `height`
   - Features: Zoom-in animation, fade transitions
   - Duration: Configurable (default 3-5 seconds per screen)

2. **`WalkthroughComposition.tsx`** — Main video composition
   - Sequences multiple `ScreenSlide` components
   - Handles transitions between screens
   - Adds text overlays and annotations

3. **`config.ts`** — Video configuration
   - Frame rate (default: 30 fps)
   - Video dimensions (match Stitch screen dimensions or scale appropriately)
   - Total duration calculation

### Transition Effects

Use Remotion's `@remotion/transitions` for professional effects:

- **Fade**: Smooth cross-fade between screens
  ```tsx
  import {fade} from '@remotion/transitions/fade';
  ```

- **Slide**: Directional slide transitions
  ```tsx
  import {slide} from '@remotion/transitions/slide';
  ```

- **Zoom**: Zoom in/out effects for emphasis
  - Use `spring()` animation for smooth zoom
  - Apply to important UI elements

### Text Overlays

Add contextual information using Remotion's text rendering:

1. **Screen titles**: Display at the top or bottom of each frame
2. **Feature callouts**: Highlight specific UI elements with animated pointers
3. **Descriptions**: Fade in descriptive text for each screen
4. **Progress indicator**: Show current screen position in walkthrough

## Execution Steps

### Step 1: Gather Screen Assets

1. Identify target Stitch project
2. List all screens in the project
3. Download screenshots for each screen
4. Organize in order of walkthrough flow
5. Create a manifest file (`screens.json`):

```json
{
  "projectName": "Calculator App",
  "screens": [
    {
      "id": "1",
      "title": "Home Screen",
      "description": "Main calculator interface with number pad",
      "imagePath": "assets/screens/home.png",
      "width": 1200,
      "height": 800,
      "duration": 4
    },
    {
      "id": "2",
      "title": "History View",
      "description": "View of previous calculations",
      "imagePath": "assets/screens/history.png",
      "width": 1200,
      "height": 800,
      "duration": 3
    }
  ]
}
```

### Step 2: Generate Remotion Components

Create the video components following Remotion best practices:

1. **Create `ScreenSlide.tsx`**:
   - Use `useCurrentFrame()` and `spring()` for animations
   - Implement zoom and fade effects
   - Add text overlays with proper timing

2. **Create `WalkthroughComposition.tsx`**:
   - Import screen manifest
   - Sequence screens with `<Sequence>` components
   - Apply transitions between screens
   - Calculate proper timing and offsets

3. **Update `remotion.config.ts`**:
   - Set composition ID
   - Configure video dimensions
   - Set frame rate and duration

**Reference Resources:**
- Use `resources/screen-slide-template.tsx` as starting point
- Follow `resources/composition-checklist.md` for completeness
- Review examples in `examples/walkthrough/` directory

### Step 3: Preview and Refine

1. **Start Remotion Studio**:
   ```bash
   npm run dev
   ```
   - Opens browser-based preview
   - Allows real-time editing and refinement

2. **Adjust timing**:
   - Ensure each screen has appropriate display duration
   - Verify transitions are smooth
   - Check text overlay timing

3. **Fine-tune animations**:
   - Adjust spring configurations for zoom effects
   - Modify easing functions for transitions
   - Ensure text is readable at all times

### Step 4: Render Video

1. **Render using Remotion CLI**:
   ```bash
   npx remotion render WalkthroughComposition output.mp4
   ```

2. **Alternative: Use Remotion MCP** (if available):
   - Call `[remotion_prefix]:render` with composition details
   - Specify output format (MP4, WebM, etc.)

3. **Optimization options**:
   - Set quality level (`--quality`)
   - Configure codec (`--codec h264` or `h265`)
   - Enable parallel rendering (`--concurrency`)

## Advanced Features

### Interactive Hotspots

Highlight clickable elements or important features:

```tsx
import {interpolate, useCurrentFrame} from 'remotion';

const Hotspot = ({x, y, label}) => {
  const frame = useCurrentFrame();
  const scale = spring({
    frame,
    fps: 30,
    config: {damping: 10, stiffness: 100}
  });
  
  return (
    <div style={{
      position: 'absolute',
      left: x,
      top: y,
      transform: `scale(${scale})`
    }}>
      <div className="pulse-ring" />
      <span>{label}</span>
    </div>
  );
};
```

### Voiceover Integration

Add narration to the walkthrough:

1. Generate voiceover script from screen descriptions
2. Use text-to-speech or record audio
3. Import audio into Remotion with `<Audio>` component
4. Sync screen timing with voiceover pacing

### Dynamic Text Extraction

Extract text from Stitch HTML code for automatic annotations:

1. Download `htmlCode.downloadUrl` for each screen
2. Parse HTML to extract key text elements (headings, buttons, labels)
3. Generate automatic callouts for important UI elements
4. Add to composition as timed text overlays

## File Structure

```
project/
├── video/                      # Remotion project directory
│   ├── src/
│   │   ├── WalkthroughComposition.tsx
│   │   ├── ScreenSlide.tsx
│   │   ├── components/
│   │   │   ├── Hotspot.tsx
│   │   │   └── TextOverlay.tsx
│   │   └── Root.tsx
│   ├── public/
│   │   └── assets/
│   │       └── screens/        # Downloaded Stitch screenshots
│   │           ├── home.png
│   │           └── history.png
│   ├── remotion.config.ts
│   └── package.json
├── screens.json                # Screen manifest
└── output.mp4                  # Rendered video
```

## Integration with Remotion Skills

Remotion maintains its own Agent Skills that define best practices. Review these for advanced techniques:

- **Repository**: https://github.com/remotion-dev/remotion/tree/main/packages/skills
- **Installation**: `npx skills add remotion-dev/skills`

Key Remotion skills to leverage:
- Animation timing and easing
- Composition architecture patterns
- Performance optimization
- Audio synchronization

## Common Patterns

### Pattern 1: Simple Slide Show

Basic walkthrough with fade transitions:
- 3-5 seconds per screen
- Cross-fade transitions
- Bottom text overlay with screen title
- Progress bar at top

### Pattern 2: Feature Highlight

Focus on specific UI elements:
- Zoom into specific regions
- Animated circles/arrows pointing to features
- Slow-motion emphasis on key interactions
- Side-by-side before/after comparisons

### Pattern 3: User Flow

Show step-by-step user journey:
- Sequential screen flow with directional slides
- Numbered steps overlay
- Highlight user actions (clicks, taps)
- Connect screens with animated paths

## Troubleshooting

| Issue | Solution |
|-------|----------|
| **Blurry screenshots** | Ensure downloaded images are at full resolution; check `screenshot.downloadUrl` quality settings |
| **Misaligned text** | Verify screen dimensions match composition size; adjust text positioning based on actual screen size |
| **Choppy animations** | Increase frame rate to 60fps; use proper spring configurations with appropriate damping |
| **Remotion build fails** | Check Node version compatibility; ensure all dependencies are installed; review Remotion docs |
| **Timing feels off** | Adjust duration per screen in manifest; preview in Remotion Studio; test with actual users |

## Best Practices

1. **Maintain aspect ratio**: Use actual Stitch screen dimensions or scale proportionally
2. **Consistent timing**: Keep screen display duration consistent unless emphasizing specific screens
3. **Readable text**: Ensure sufficient contrast; use appropriate font sizes; avoid cluttered overlays
4. **Smooth transitions**: Use spring animations for natural motion; avoid jarring cuts
5. **Preview thoroughly**: Always preview in Remotion Studio before final render
6. **Optimize assets**: Compress images appropriately; use efficient formats (PNG for UI, JPG for photos)

## Example Usage

**User prompt:**
```
Look up the screens in my Stitch project "Calculator App" and build a remotion video 
that shows a walkthrough of the screens.
```

**Agent workflow:**
1. List Stitch projects → Find "Calculator App" → Extract project ID
2. List screens in project → Identify all screens (Home, History, Settings)
3. Download screenshots for each screen → Save to `assets/screens/`
4. Create `screens.json` manifest with screen metadata
5. Generate Remotion components (`ScreenSlide.tsx`, `WalkthroughComposition.tsx`)
6. Preview in Remotion Studio → Refine timing and transitions
7. Render final video → `calculator-walkthrough.mp4`
8. Report completion with video preview link

## Tips for Success

- **Start simple**: Begin with basic fade transitions before adding complex animations
- **Follow Remotion patterns**: Leverage Remotion's official skills and documentation
- **Use manifest files**: Keep screen data organized in JSON for easy updates
- **Preview frequently**: Use Remotion Studio to catch issues early
- **Consider accessibility**: Add captions; ensure text is readable; use clear visuals
- **Optimize for platform**: Match video dimensions to target platform (YouTube, social media, etc.)

## References

- **Stitch Documentation**: https://stitch.withgoogle.com/docs/
- **Remotion Documentation**: https://www.remotion.dev/docs/
- **Remotion Skills**: https://www.remotion.dev/docs/ai/skills
- **Remotion MCP**: https://www.remotion.dev/docs/ai/mcp
- **Remotion Transitions**: https://www.remotion.dev/docs/transitions


## When to Use

Use this skill when tackling tasks related to its primary domain or functionality as described above.

## Source: references/skills/videodb/references/legacy/remotion-best-practices/SKILL.md

---
name: remotion-best-practices
description: "Best practices for Remotion - Video creation in React"
risk: unknown
source: community
tags: "remotion, video, react, animation, composition"
date_added: "2026-02-27"
---

## When to use

Use this skills whenever you are dealing with Remotion code to obtain the domain-specific knowledge.

## How to use

Read individual rule files for detailed explanations and code examples:

- [rules/3d.md](rules/3d.md) - 3D content in Remotion using Three.js and React Three Fiber
- [rules/animations.md](rules/animations.md) - Fundamental animation skills for Remotion
- [rules/assets.md](rules/assets.md) - Importing images, videos, audio, and fonts into Remotion
- [rules/audio.md](rules/audio.md) - Using audio and sound in Remotion - importing, trimming, volume, speed, pitch
- [rules/calculate-metadata.md](rules/calculate-metadata.md) - Dynamically set composition duration, dimensions, and props
- [rules/can-decode.md](rules/can-decode.md) - Check if a video can be decoded by the browser using Mediabunny
- [rules/charts.md](rules/charts.md) - Chart and data visualization patterns for Remotion
- [rules/compositions.md](rules/compositions.md) - Defining compositions, stills, folders, default props and dynamic metadata
- [rules/display-captions.md](rules/display-captions.md) - Displaying captions in Remotion with TikTok-style pages and word highlighting
- [rules/extract-frames.md](rules/extract-frames.md) - Extract frames from videos at specific timestamps using Mediabunny
- [rules/fonts.md](rules/fonts.md) - Loading Google Fonts and local fonts in Remotion
- [rules/get-audio-duration.md](rules/get-audio-duration.md) - Getting the duration of an audio file in seconds with Mediabunny
- [rules/get-video-dimensions.md](rules/get-video-dimensions.md) - Getting the width and height of a video file with Mediabunny
- [rules/get-video-duration.md](rules/get-video-duration.md) - Getting the duration of a video file in seconds with Mediabunny
- [rules/gifs.md](rules/gifs.md) - Displaying GIFs synchronized with Remotion's timeline
- [rules/images.md](rules/images.md) - Embedding images in Remotion using the Img component
- [rules/import-srt-captions.md](rules/import-srt-captions.md) - Importing .srt subtitle files into Remotion using @remotion/captions
- [rules/lottie.md](rules/lottie.md) - Embedding Lottie animations in Remotion
- [rules/measuring-dom-nodes.md](rules/measuring-dom-nodes.md) - Measuring DOM element dimensions in Remotion
- [rules/measuring-text.md](rules/measuring-text.md) - Measuring text dimensions, fitting text to containers, and checking overflow
- [rules/sequencing.md](rules/sequencing.md) - Sequencing patterns for Remotion - delay, trim, limit duration of items
- [rules/tailwind.md](rules/tailwind.md) - Using TailwindCSS in Remotion
- [rules/text-animations.md](rules/text-animations.md) - Typography and text animation patterns for Remotion
- [rules/timing.md](rules/timing.md) - Interpolation curves in Remotion - linear, easing, spring animations
- [rules/transcribe-captions.md](rules/transcribe-captions.md) - Transcribing audio to generate captions in Remotion
- [rules/transitions.md](rules/transitions.md) - Scene transition patterns for Remotion
- [rules/trimming.md](rules/trimming.md) - Trimming patterns for Remotion - cut the beginning or end of animations
- [rules/videos.md](rules/videos.md) - Embedding videos in Remotion - trimming, volume, speed, looping, pitch

## Source: references/skills/videodb/references/legacy/videodb-skills/SKILL.md

---
name: videodb-skills
description: "Upload, stream, search, edit, transcribe, and generate AI video and audio using the VideoDB SDK."
category: media
risk: safe
source: community
tags: "[video, editing, transcription, subtitles, search, streaming, ai-generation, media]"
date_added: "2026-02-27"
---

# VideoDB Skills

## Purpose

The only video skill your agent needs. Upload any video, connect real-time streams, search inside by what was said or shown, build complex editing workflows with overlays, generate AI media, add subtitles, and get instant streaming links — all via the VideoDB Python SDK.

## When to Use This Skill

- User wants to upload and process videos from YouTube, URLs, or local files
- User needs to search for moments by speech or visual scenes
- User asks for transcription, subtitles, or subtitle styling
- User wants to edit clips — trim, combine, add text/image/audio overlays
- User needs AI-generated media (images, video, music, sound effects, voiceovers)
- User wants to transcode, change resolution, or reframe for social platforms
- User needs real-time screen or audio capture with AI transcription
- User asks for playable streaming links for any video output

## Setup

### Step 1: Install the skill

```bash
npx skills add video-db/skills
```

### Step 2: Run setup

```
/videodb setup
```

The agent guides API key setup ($20 free credits, no credit card), installs the SDK, and verifies the connection.

Alternatively, set the API key manually:

```bash
export VIDEO_DB_API_KEY=sk-xxx
```

### Step 3: Install the SDK

```bash
pip install "videodb[capture]" python-dotenv
```

## Capabilities

| Capability  | Description                                                               |
| ----------- | ------------------------------------------------------------------------- |
| Upload      | Ingest videos from YouTube, URLs, or local files                          |
| Search      | Find moments by speech (semantic/keyword) or visual scenes                |
| Transcripts | Generate timestamped transcripts from any video                           |
| Edit        | Combine clips, trim, add text/image/audio overlays                        |
| Subtitles   | Auto-generate and style subtitles                                         |
| AI Generate | Create images, video, music, sound effects, and voiceovers from text      |
| Capture     | Real-time screen and audio capture with AI transcription                  |
| Transcode   | Change resolution, quality, aspect ratio, or reframe for social platforms |
| Stream      | Get playable HLS links for anything you build                             |

## Examples

**Upload and transcribe:**

```
"Upload https://www.youtube.com/watch?v=FgrO9ADPZSA and give me a transcript"
```

**Search across videos:**

```
"Search for 'product demo' in my latest video"
```

**Add subtitles:**

```
"Add subtitles with white text on black background"
```

**Multi-clip editing:**

```
"Take clips from 10s-30s and 45s-60s, add a title card, and combine them"
```

**AI media generation:**

```
"Generate background music and overlay it on my video"
```

**Real-time capture:**

```
"Capture my screen and transcribe it in real-time"
```

**Reframe for social:**

```
"Convert this to vertical for Instagram Reels"
```

## Repository

https://github.com/video-db/skills

**Version:** 1.1.0
**Maintained By:** [VideoDB](https://github.com/video-db)

