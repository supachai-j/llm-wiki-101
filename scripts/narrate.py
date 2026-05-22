"""Repo-local narration generator for LLM Wiki 101.

Wraps the global narrating-course-slides Gemini generator but overrides the
voice map and delivery style for THIS deck's shape (22 slides, 2 tracks) so
re-runs are reproducible and the global skill stays untouched.

Usage:
    export GEMINI_API_KEY="$(cat ~/.config/gemini-key)"
    python3 scripts/narrate.py slides/training-en.html
    TTS_SLIDES="1,9" python3 scripts/narrate.py slides/training-th.html   # sample subset
"""
import asyncio, importlib.util, os, sys
from pathlib import Path

SKILL = Path.home() / ".claude/skills/narrating-course-slides/scripts/generate-gemini-tts.py"
spec = importlib.util.spec_from_file_location("gen_gemini_tts", SKILL)
gen = importlib.util.module_from_spec(spec)
spec.loader.exec_module(gen)

# Voice rotation for this deck (F/M alternation by block).
# Track A foundations 1-7 (F) · 8-14 conviction (M) · 15-17 how-it-works (F)
# · 18-20 engineering checklist (M) · 21-22 wrap (F)
gen.VOICE_MAP = {}
gen.assign(1, 3, "Aoede")    # title + agenda + central claim — warm F
gen.assign(4, 7, "Kore")     # layers/RAG/Zettelkasten/genealogy — clear F
gen.assign(8, 14, "Charon")  # template/citation/ingest/lint/TrackB/schema/tooling — conviction M
gen.assign(15, 17, "Aoede")  # failure modes/provenance/integration — F
gen.assign(18, 20, "Puck")   # metrics/anti-patterns/checklist — M
gen.assign(21, 22, "Kore")   # sources + Q&A — warm F

_PACE = "Keep a brisk, natural pace like a real person talking, not reading aloud. Stress the key terms and numbers."

def style_for(idx):
    if idx <= 2:   return "Speak warmly and conversationally, like welcoming a class — friendly, with a smile in your voice. " + _PACE
    if idx <= 7:   return "Speak with curiosity, building understanding step by step, like a teacher excited about the topic. " + _PACE
    if idx <= 14:  return "Speak with conviction, like a confident instructor. Slow down a touch on the key rule or principle name for weight, then return to pace. " + _PACE
    if idx <= 17:  return "Speak clearly and practically, walking through how the system works and how it breaks. " + _PACE
    if idx <= 20:  return "Speak like a senior engineer running a checklist — practical and measured. " + _PACE
    return "Speak warmly, wrapping up and inviting questions — friendly and reflective. " + _PACE

gen.style_for = style_for

if __name__ == "__main__":
    asyncio.run(gen.main())
