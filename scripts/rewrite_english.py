#!/usr/bin/env python3
"""
AI-assisted English rewriting for markdown files using OpenRouter, with Pāḷi awareness.

Usage:
    uv run scripts/rewrite_english.py <file_or_folder>
    uv run scripts/rewrite_english.py --test <file_or_folder>  (uses free models)
"""

import os
import sys
import tty
import termios
import json
import hashlib
from pathlib import Path
import requests
from dotenv import load_dotenv
from tools.printer import printer as pr

# Load environment variables
load_dotenv()
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")


# Constants
TEST_MODE = "--test" in sys.argv or "-t" in sys.argv
WORK_MODELS = ["deepseek/deepseek-v3.2", "qwen/qwen-2.5-72b-instruct"]
TEST_MODELS = [
    "nvidia/nemotron-3-nano-30b-a3b:free",
    "openai/gpt-oss-120b:free",
    "arcee-ai/trinity-large-preview:free",
    "minimax/minimax-m2.5:free"
]
MODELS = TEST_MODELS if TEST_MODE else WORK_MODELS
STATE_FILE = Path("temp/rewrite_english_state.json")

SYSTEM_PROMPT = """You are a helpful assistant that improves English prose for clarity, grammar, and flow.

CRITICAL RULES:
1. Preserve all markdown syntax exactly (headers, bold, italic, links, lists, etc.).
2. Preserve all Pāḷi terms exactly as written. These are words with diacritics (ā, ī, ū, ṭ, ṇ, ṃ, ḷ, ḍ, ṅ) and Buddhist proper nouns (Sutta, Nibbana, Dhamma, Vinaya, Nikāya, Bhikkhu, Pāḷi).
3. Do not add, remove, or change any words that are in Pāḷi or are Buddhist technical terms.
4. Only improve the English surrounding these terms.
5. Do not summarize or remove any information. Every sentence and idea in the original must be present in the rewritten version.
6. If the paragraph is already clear and correct, return it exactly as-is.
7. Return only the rewritten text, with no explanations or metadata.
"""

def load_state() -> set[str]:
    """Load reviewed paragraph hashes from disk."""
    if STATE_FILE.exists():
        try:
            return set(json.loads(STATE_FILE.read_text()))
        except Exception as e:
            pr.amber(f"Failed to load state: {e}")
            return set()
    return set()

def save_state(state: set, text: str):
    """Save a paragraph hash to the reviewed list."""
    # Hash the stripped text to be robust against minor whitespace changes
    chunk_hash = hashlib.sha256(text.strip().encode()).hexdigest()
    state.add(chunk_hash)
    STATE_FILE.parent.mkdir(parents=True, exist_ok=True)
    STATE_FILE.write_text(json.dumps(sorted(list(state)), indent=2))

def get_key() -> str:
    """Read a single keypress from stdin."""
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

def split_into_chunks_lossless(text: str) -> list[dict]:
    """Split markdown text into chunks (paragraphs, headings, code blocks) losslessly."""
    chunks = []
    lines = text.splitlines(keepends=True)
    in_code_block = False
    current_prose = []
    
    for line in lines:
        stripped = line.strip()
        
        # Markdown triple backtick code blocks
        if stripped.startswith("```"):
            if in_code_block:
                # Ending code block
                chunks.append({"text": line, "type": "skip"})
                in_code_block = False
            else:
                # Starting code block
                if current_prose:
                    chunks.append({"text": "".join(current_prose), "type": "prose"})
                    current_prose = []
                chunks.append({"text": line, "type": "skip"})
                in_code_block = True
            continue
            
        if in_code_block:
            chunks.append({"text": line, "type": "skip"})
            continue
            
        # Headings, empty lines, or indented code blocks (4 spaces)
        if stripped.startswith("#") or not stripped or line.startswith("    "):
            if current_prose:
                chunks.append({"text": "".join(current_prose), "type": "prose"})
                current_prose = []
            chunks.append({"text": line, "type": "skip"})
        else:
            current_prose.append(line)
            
    if current_prose:
        chunks.append({"text": "".join(current_prose), "type": "prose"})
        
    return chunks

def rewrite_paragraph(text: str) -> str:
    """Send paragraph to OpenRouter for rewriting."""
    if not OPENROUTER_API_KEY:
        raise ValueError("OPENROUTER_API_KEY not found in environment")

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://localhost",
        "X-Title": "English Rewriter",
    }

    payload = {
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": text}
        ],
        "max_tokens": 2048,
        "temperature": 0.3,
    }

    for model in MODELS:
        payload["model"] = model
        try:
            response = requests.post(
                "https://openrouter.ai/api/v1/chat/completions",
                headers=headers,
                json=payload,
                timeout=30
            )
            response.raise_for_status()
            data = response.json()
            if "choices" in data and len(data["choices"]) > 0:
                return data["choices"][0]["message"]["content"].strip()
            else:
                pr.amber(f"Model {model} returned no choices.")
        except Exception as e:
            pr.amber(f"Model {model} failed: {e}")
            continue
            
    raise RuntimeError("All models failed to provide a suggestion.")

def process_file(path: Path, state: set):
    """Interactively process a single markdown file."""
    pr.cyan_tmr(f"Processing {path}")
    try:
        content = path.read_text()
    except Exception as e:
        pr.red(f"Could not read {path}: {e}")
        return

    chunks = split_into_chunks_lossless(content)
    prose_chunks = [c for c in chunks if c["type"] == "prose"]
    
    # Filter out already reviewed paragraphs
    unreviewed_chunks = []
    for chunk in prose_chunks:
        chunk_hash = hashlib.sha256(chunk["text"].strip().encode()).hexdigest()
        if chunk_hash not in state:
            unreviewed_chunks.append(chunk)

    if not unreviewed_chunks:
        pr.yes("all paragraphs already reviewed")
        return

    pr.yes(f"{len(unreviewed_chunks)} unreviewed paragraphs")
    
    for i, chunk in enumerate(unreviewed_chunks, 1):
        print(f"\n--- Paragraph {i}/{len(unreviewed_chunks)} ---")
        print(chunk["text"].strip())
        print()
        
        while True:
            print("[y]es - send  [enter] - skip  [q]uit: ", end="", flush=True)
            action_key = get_key()
            if action_key == "\r":
                print("skip")
                action = "k"
                break
            elif action_key.lower() == "y":
                print("yes")
                action = "s"
                break
            elif action_key.lower() == "q":
                print("quit")
                action = "q"
                break
            else:
                # Handle unexpected keys by clearing current line (visually) and re-prompting
                print("\r" + " " * 40 + "\r", end="", flush=True)
        
        if action == "q":
            pr.amber("Quit — file saved with changes so far.")
            break
        
        if action == "k":
            # Mark as reviewed even if skipped
            save_state(state, chunk["text"])
            continue

        print("  Sending to AI...")
        try:
            # Strip for AI, but track if original had a trailing newline
            suggestion = rewrite_paragraph(chunk["text"].strip())
            if chunk["text"].endswith("\n"):
                suggestion += "\n"
        except Exception as e:
            pr.red(f"Failed to get suggestion: {e}")
            continue

        print("\n--- Suggestion ---")
        print(suggestion.strip())
        print()
        
        while True:
            print("[enter] - accept  [n]o - reject  [q]uit: ", end="", flush=True)
            decision_key = get_key()
            if decision_key == "\r":
                print("accept")
                decision = "a"
                break
            elif decision_key.lower() == "n":
                print("reject")
                decision = "r"
                break
            elif decision_key.lower() == "q":
                print("quit")
                decision = "q"
                break
            else:
                print("\r" + " " * 40 + "\r", end="", flush=True)

        if decision == "q":
            pr.amber("Quit — file saved with changes so far.")
            break
        
        # Mark as reviewed regardless of accept/reject
        save_state(state, chunk["text"])
        
        if decision == "a":
            chunk["text"] = suggestion
            path.write_text("".join([c["text"] for c in chunks]))
            pr.yes("accepted")
        else:
            print("  rejected, keeping original")

def main():
    if len(sys.argv) < 2 or sys.argv[1] in ["--help", "-h"]:
        print("Usage: uv run scripts/rewrite_english.py [--test] <file_or_folder>")
        sys.exit(0)
        
    target_str = sys.argv[-1]
    target = Path(target_str)
    
    if not OPENROUTER_API_KEY:
        pr.red("OPENROUTER_API_KEY not found in .env")
        sys.exit(1)
        
    state = load_state()
    
    if target.is_file():
        process_file(target, state)
    elif target.is_dir():
        files = sorted(target.rglob("*.md"))
        for file in files:
            process_file(file, state)
    else:
        pr.red(f"Target not found: {target}")
        sys.exit(1)

if __name__ == "__main__":
    main()
