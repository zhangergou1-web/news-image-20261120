# The World in One Day — 20 November 2026

A program that writes one image summing up Friday 20 November 2026's world
news, for make.fun's bounty "Sum up 20 November's world news in one image".

Run it:

```sh
python3 main.py
```

It writes the 1024×1024 front-page image to `/output/entry.png`.

## The six stories

1. **World Court** — the ICJ rules Myanmar committed genocide against the
   Rohingya, the first genocide finding against a state in the court's
   80-year history.
2. **Summit** — Trump, Xi and Putin sign a nuclear declaration in Shenzhen;
   nuclear war "must never be fought".
3. **Markets** — sell-off sweeps Asia and Wall Street: Nikkei -5.1%,
   Nasdaq -5.2%, S&P -3.7%; Anthropic -8.5% after its +17% debut.
4. **Ukraine** — third strike on the Crimea Bridge in four days; rail halted.
5. **Gulf** — Houthi missiles hit Riyadh's finance district, damaging the
   PIF tower.
6. **America** — the Senate rejects limits on Iran war powers, 51–48.

## Layout

- `main.py` — the entrypoint. Decodes the image and writes `/output/entry.png`.
- `entry.png.b64` — the image itself, base64-encoded, so the whole entry is
  plain text.
- `build.py` — the generator that drew the image (Pillow). Run it to rebuild
  `entry.png` from the story list, then re-encode it.
- `LICENSE` — MIT.

## License

MIT. See `LICENSE`.
