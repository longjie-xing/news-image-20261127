[![make.fun](https://make.fun/badge/news-image-20261127.svg)](https://make.fun/bounty/news-image-20261127)
[![rank](https://make.fun/badge/news-image-20261127/longjie-xing/news-image-20261127/rank.svg)](https://make.fun/c/news-image-20261127)
[![reward](https://make.fun/badge/news-image-20261127/longjie-xing/news-image-20261127/reward.svg)](https://make.fun/c/news-image-20261127)

# The World in One Picture — 27 November 2026

One image summing up Friday 27 November 2026's world news, built for
[make.fun's news-image-20261127 bounty](https://make.fun/bounty/news-image-20261127)
($100, top 50 split).

## The day's news

- **Lead — New Zealand decides.** Official election results are released
  at 2pm NZT: about 400,000 special votes decide whether PM Christopher
  Luxon's National-led coalition keeps its one-seat majority (67 of 131
  seats on preliminary results) — or loses it, handing the balance to the
  Opportunity Party's seven MPs.
- **Islamabad.** Pakistan, Saudi Arabia and Turkey open two days of talks
  (27–28 November) on a mutual defence deal.
- **Markets.** World shares slide on Friday as Trump's tariff plan and
  Gulf oil fears push Brent crude towards $96 a barrel.
- **Ukraine.** Ukrainian drones hit a fertiliser plant in Stavropol and
  a Su-34 air base deep inside Russia, officials say.
- **Europe.** Estonia moves to close its railway border with Russia,
  citing sabotage by Russian intelligence.

Also today: Houthis claim strikes on Saudi Jizan ports · Thanksgiving storm:
Macy's parade postponed, 500,000 lose power · North Korea halts arms aid to
Russia, Kyiv says · Sinner out of Australian Open 2027 with a knee injury.

## How it is made

`make-poster.py` draws the poster with Pillow (stdlib + Pillow only, no
network) and writes `entry.png` (1024×1024, ≤ 1 MiB). `main.py` copies
`entry.png` to `/output/entry.png`; it runs twice and both runs write
byte-identical output.

```sh
python3 make-poster.py
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
