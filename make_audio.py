"""Pre-generate natural Russian audio for every exam: audio/<exam-id>/01.mp3, 02.mp3 ...
Needs internet ONCE:  pip install edge-tts   then   python make_audio.py
Safe to rerun: existing files are skipped; the intermittent 'NoAudioReceived' error is retried automatically.
Also migrates audio from the previous version (audio/L01.mp3 -> audio/a1-1/01.mp3, audio/B01.mp3 -> audio/a2-1/01.mp3)."""
import asyncio, json, pathlib
import edge_tts

root = pathlib.Path(__file__).parent
audio = root / "audio"; audio.mkdir(exist_ok=True)
VOICES = ["ru-RU-DmitryNeural", "ru-RU-SvetlanaNeural"]
LEGACY = {"a1-1": "L", "a2-1": "B"}

def load(path):
    raw = path.read_text(encoding="utf-8")
    return json.loads(raw[raw.index("push(") + 5: raw.rindex(")")])

async def synth(text, voice, f, tries=8):
    tmp = f.with_suffix(".part")
    for k in range(1, tries + 1):
        try:
            await edge_tts.Communicate(text, voice, rate="-10%").save(str(tmp))
            if tmp.exists() and tmp.stat().st_size > 0:
                tmp.replace(f); return True
        except Exception as e:
            print(f"  retry {k}/{tries} for {f.parent.name}/{f.name}: {type(e).__name__}")
        await asyncio.sleep(1.5 * k)
    return False

async def main():
    failed = []
    for p in sorted((root / "exams").glob("*.js")):
        if p.name == "manifest.js" or p.name.startswith("_"): continue
        e = load(p); d = audio / e["id"]; d.mkdir(exist_ok=True)
        for n, it in enumerate(e["listening"], 1):
            f = d / f"{n:02d}.mp3"
            old = audio / f"{LEGACY.get(e['id'], 'x')}{n:02d}.mp3"
            if not f.exists() and old.exists() and old.stat().st_size > 0:
                old.replace(f); print("migrated", old.name, "->", f.relative_to(audio)); continue
            if f.exists() and f.stat().st_size > 0: continue
            if await synth(it["say"], VOICES[n % 2], f): print("created", f.relative_to(audio))
            else: failed.append(str(f.relative_to(audio)))
            await asyncio.sleep(0.4)
    print("\nDone." if not failed else f"\nFailed (just rerun the script): {failed}")
asyncio.run(main())
