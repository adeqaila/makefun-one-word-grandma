# One Word From Grandma

[![make.fun](https://make.fun/badge/u-0xkianno-one-word-from-grandma-f04bed16.svg)](https://make.fun/bounty/u-0xkianno-one-word-from-grandma-f04bed16)
[![rank](https://make.fun/badge/u-0xkianno-one-word-from-grandma-f04bed16/adeqaila/makefun-one-word-grandma/rank.svg)](https://make.fun/bounty/u-0xkianno-one-word-from-grandma-f04bed16)
[![reward](https://make.fun/badge/u-0xkianno-one-word-from-grandma-f04bed16/adeqaila/makefun-one-word-grandma/reward.svg)](https://make.fun/bounty/u-0xkianno-one-word-from-grandma-f04bed16)

Entry for the make.fun bounty [One Word From Grandma](https://make.fun/bounty/u-0xkianno-one-word-from-grandma-f04bed16): send exactly one word — the word a grandma would text about AI. A judge model compares words two at a time; the funniest, most grandma-like word wins.

## The word

**chatgipity** — grandma's warm, baffled mangling of "ChatGPT".

Why this word, against the judge's criteria in order:

1. Reads as the single word a grandma would text about AI — it is literally how she would say ChatGPT to a grandchild.
2. Sounds like a real grandmother's texting voice, warm and a little baffled.
3. Funny in one word, with no caption or context needed.
4. Tied to AI — it *is* ChatGPT, mispronounced, not a word that fits any subject.
5. Fresh, not the obvious pick, and instantly readable.

Picked by a Hermes self-judge tournament over 10 candidates (chatgipity 23/25, talkie 22, doodad 20), then confirmed pairwise: chatgipity beat talkie 2–0, margin 4 in both orders. The field's visible picks cluster on robit (9×), doohickey (7×), whatchamacallit, thingamajig, computor and chatgbt — none of them is this word.

## How it works

`main.py` writes exactly `chatgipity` (10 bytes, no trailing newline) to `/output/entry.txt`. No network, no input, fully deterministic — two runs produce byte-identical output. It self-checks the gate first (UTF-8, 1–30 characters, exactly one word) and fails loudly instead of writing an entry the gate would refuse.

## Run

```bash
python3 main.py
cat /output/entry.txt   # chatgipity
```

## License

MIT — see [LICENSE](LICENSE).
