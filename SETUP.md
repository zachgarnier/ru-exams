# Setup

**Quickest:** double-click `index.html` (Chrome/Edge recommended). Choose English or Français, then A1 or A2, then an exam.
**Or:** `python serve.py` (opens http://127.0.0.1:8000/index.html).

## Audio
1. Zero setup: the browser reads the Russian with its own voice (quality varies).
2. Better: `pip install edge-tts` then `python make_audio.py` (internet needed once). Creates `audio/<exam-id>/NN.mp3`
   for every exam. Reruns skip existing files and retry the flaky "NoAudioReceived" error automatically.
   If you used the previous version, your old `audio/L01.mp3` / `B01.mp3` files are moved to `audio/a1-1/` and `audio/a2-1/` automatically.

## Certificate
After at least one section: "Download certificate (PDF)", enter a name, choose "Save as PDF" in the print dialog (works offline, in EN or FR).

## Adding an exam to the bank
1. Copy `exams/_template.js` to `exams/a1-3.js` (or `a2-3.js`) and fill it in (first option of each `"o"` list = correct answer; `"english||français"` for bilingual strings).
2. Add the id to `exams/manifest.js`, e.g. `["a1-1","a1-2","a1-3","a2-1","a2-2"]`.
3. Run `python make_audio.py` for its audio. It then appears in the A1/A2 list automatically.
