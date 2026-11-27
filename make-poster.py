#!/usr/bin/env python3
"""Draw entry.png for news-image-20261127.

One-day world news poster for Friday 27 November 2026.
Stdlib + Pillow only, no network. Run: python3 make-poster.py
Writes entry.png next to this script (1024x1024, <= 1 MiB).
"""

import os

from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "entry.png")

W, H = 1024, 1024

# Palette: deep blue with orange accents, flat minimal style.
NAVY = (10, 30, 58)        # page background
NAVY2 = (16, 44, 82)       # panel background
NAVY3 = (22, 58, 104)      # lighter panel
INK = (255, 255, 255)
MUTED = (176, 200, 224)
CYAN = (64, 224, 226)
ORANGE = (255, 140, 40)
ORANGE_D = (214, 96, 16)
GOLD = (255, 196, 66)
RULE = (48, 96, 150)

BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_w):
    """Greedy word wrap using measured widths."""
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def text_block(draw, xy, lines, fnt, fill, leading):
    x, y = xy
    for ln in lines:
        draw.text((x, y), ln, font=fnt, fill=fill)
        y += leading
    return y


# ---------------------------------------------------------------- stories
# Lead story text is updated once the NZ Electoral Commission releases
# the official results at 14:00 NZT (01:00 UTC) on 27 November 2026.
LEAD = {
    "kicker": "LEAD  ·  NEW ZEALAND",
    "headline": "New Zealand decides: final count lands today",
    "body": (
        "Official results due at 2pm NZT: about 400,000 special votes "
        "decide whether PM Christopher Luxon's National-led coalition "
        "keeps its one-seat majority — or loses it, handing the balance "
        "to the Opportunity Party's seven MPs."
    ),
}

PANELS = [
    {
        "kicker": "ISLAMABAD",
        "title": "Three-way defence pact talks open",
        "body": (
            "Pakistan, Saudi Arabia and Turkey meet on a "
            "mutual defence deal."
        ),
        "icon": "flags",
    },
    {
        "kicker": "MARKETS",
        "title": "Stocks slide on tariff shock",
        "body": (
            "World shares fall on tariff and Gulf oil fears; "
            "Brent nears $96."
        ),
        "icon": "chart",
    },
    {
        "kicker": "UKRAINE",
        "title": "Kyiv strikes deep inside Russia",
        "body": (
            "Drones hit a fertiliser plant in Stavropol and "
            "a Su-34 air base."
        ),
        "icon": "drone",
    },
    {
        "kicker": "EUROPE",
        "title": "Estonia to shut rail link to Russia",
        "body": (
            "Tallinn moves to close its railway border, "
            "citing Russian sabotage."
        ),
        "icon": "rail",
    },
]

FOOTER = (
    "Houthis claim strikes on Saudi Jizan ports  ·  Thanksgiving storm: Macy's "
    "parade postponed, 500,000 lose power  ·  North Korea halts arms aid to "
    "Russia, Kyiv says  ·  Sinner out of Australian Open 2027 with knee injury"
)


# ---------------------------------------------------------------- icons
def draw_ballot(draw, cx, cy, s):
    """Flat ballot box with a ticked ballot paper."""
    # box
    draw.rounded_rectangle(
        [cx - s, cy - s * 0.55, cx + s, cy + s * 0.55],
        radius=int(s * 0.12), fill=NAVY3, outline=CYAN, width=3,
    )
    # slot
    draw.rectangle([cx - s * 0.55, cy - s * 0.55, cx + s * 0.55, cy - s * 0.38],
                   fill=NAVY)
    # ballot paper rising out of the slot
    draw.rectangle([cx - s * 0.42, cy - s * 1.25, cx + s * 0.42, cy - s * 0.45],
                   fill=INK)
    # tick on the paper
    draw.line([(cx - s * 0.28, cy - s * 0.82), (cx - s * 0.08, cy - s * 0.62),
               (cx + s * 0.30, cy - s * 1.05)],
              fill=ORANGE, width=6, joint="curve")
    # small tick boxes row on the box front
    for i, x in enumerate((cx - s * 0.55, cx - s * 0.05, cx + s * 0.45)):
        draw.rectangle([x, cy + s * 0.05, x + s * 0.28, cy + s * 0.33],
                       outline=MUTED, width=2)
        if i == 0:
            draw.line([(x + 2, cy + s * 0.19), (x + s * 0.10, cy + s * 0.28),
                       (x + s * 0.26, cy + s * 0.08)],
                      fill=ORANGE, width=3, joint="curve")


def draw_flags(draw, cx, cy, s):
    """Three small flags on poles: Pakistan, Saudi Arabia, Turkey."""
    # poles
    for dx in (-0.62, 0.0, 0.62):
        draw.line([(cx + dx * s, cy - s * 0.55), (cx + dx * s, cy + s * 0.75)],
                  fill=MUTED, width=3)
    # Pakistan: dark green flag with white stripe and crescent
    draw.rectangle([cx - s * 0.95, cy - s * 0.80, cx - s * 0.30, cy - s * 0.30],
                   fill=(20, 90, 50))
    draw.rectangle([cx - s * 0.95, cy - s * 0.80, cx - s * 0.80, cy - s * 0.30],
                   fill=INK)
    draw.ellipse([cx - s * 0.68, cy - s * 0.70, cx - s * 0.48, cy - s * 0.45],
                 fill=INK)
    # Saudi Arabia: green flag with white line (shahada, abstracted)
    draw.rectangle([cx - s * 0.33, cy - s * 0.80, cx + s * 0.33, cy - s * 0.30],
                   fill=(0, 110, 60))
    draw.line([(cx - s * 0.25, cy - s * 0.55), (cx + s * 0.25, cy - s * 0.55)],
              fill=INK, width=3)
    # Turkey: red flag with white crescent and star
    draw.rectangle([cx + s * 0.30, cy - s * 0.80, cx + s * 0.95, cy - s * 0.30],
                   fill=(227, 10, 23))
    draw.ellipse([cx + s * 0.48, cy - s * 0.70, cx + s * 0.68, cy - s * 0.45],
                 fill=INK)
    draw.ellipse([cx + s * 0.55, cy - s * 0.66, cx + s * 0.70, cy - s * 0.49],
                 fill=(227, 10, 23))


def draw_chart(draw, cx, cy, s):
    """Falling market chart: axes plus a descending line with dots."""
    # axes
    draw.line([(cx - s, cy + s * 0.7), (cx + s, cy + s * 0.7)], fill=MUTED, width=3)
    draw.line([(cx - s, cy - s * 0.8), (cx - s, cy + s * 0.7)], fill=MUTED, width=3)
    # descending line
    pts = [(cx - s * 0.85, cy - s * 0.55), (cx - s * 0.35, cy - s * 0.35),
           (cx + s * 0.10, cy + s * 0.05), (cx + s * 0.55, cy + s * 0.10),
           (cx + s * 0.90, cy + s * 0.55)]
    draw.line(pts, fill=ORANGE, width=5, joint="curve")
    for x, y in pts:
        draw.ellipse([x - 5, y - 5, x + 5, y + 5], fill=INK)
    # down arrow at the end
    draw.polygon([(cx + s * 0.90, cy + s * 0.55), (cx + s * 0.72, cy + s * 0.55),
                  (cx + s * 0.81, cy + s * 0.78)], fill=ORANGE)


def draw_drone(draw, cx, cy, s):
    """Small quadcopter drone, top view."""
    # arms
    draw.line([(cx - s, cy - s * 0.6), (cx + s, cy + s * 0.6)], fill=MUTED, width=5)
    draw.line([(cx - s, cy + s * 0.6), (cx + s, cy - s * 0.6)], fill=MUTED, width=5)
    # rotors
    for x, y in ((cx - s, cy - s * 0.6), (cx + s, cy - s * 0.6),
                 (cx - s, cy + s * 0.6), (cx + s, cy + s * 0.6)):
        draw.ellipse([x - s * 0.32, y - s * 0.32, x + s * 0.32, y + s * 0.32],
                     outline=CYAN, width=3)
    # body
    draw.rounded_rectangle([cx - s * 0.45, cy - s * 0.32, cx + s * 0.45, cy + s * 0.32],
                           radius=int(s * 0.12), fill=ORANGE)
    draw.ellipse([cx - s * 0.16, cy - s * 0.16, cx + s * 0.16, cy + s * 0.16],
                 fill=NAVY)


def draw_rail(draw, cx, cy, s):
    """Railway track receding, with a barrier."""
    # sleepers
    for i, yy in enumerate((cy - s * 0.55, cy - s * 0.15, cy + s * 0.25, cy + s * 0.60)):
        wdt = s * (0.35 + 0.22 * i)
        draw.rectangle([cx - wdt, yy, cx + wdt, yy + 6], fill=MUTED)
    # rails
    draw.line([(cx - s * 0.55, cy - s * 0.60), (cx - s * 0.95, cy + s * 0.75)],
              fill=INK, width=4)
    draw.line([(cx + s * 0.55, cy - s * 0.60), (cx + s * 0.95, cy + s * 0.75)],
              fill=INK, width=4)
    # barrier arm
    draw.line([(cx - s * 0.85, cy - s * 0.75), (cx + s * 0.85, cy - s * 0.95)],
              fill=ORANGE, width=7)
    draw.ellipse([cx - s * 0.95, cy - s * 0.85, cx - s * 0.65, cy - s * 0.55],
                 fill=GOLD)


ICONS = {
    "ballot": draw_ballot,
    "flags": draw_flags,
    "chart": draw_chart,
    "drone": draw_drone,
    "rail": draw_rail,
}


# ---------------------------------------------------------------- poster
def main():
    img = Image.new("RGB", (W, H), NAVY)
    d = ImageDraw.Draw(img)

    # --- masthead ---
    d.text((40, 26), "THE WORLD IN ONE PICTURE",
           font=font(BOLD, 46), fill=INK)
    d.text((40, 84), "2026.11.27  FRIDAY",
           font=font(BOLD, 26), fill=CYAN)
    d.text((560, 88), "Friday 27 November 2026",
           font=font(REG, 24), fill=MUTED)
    d.line([(40, 128), (984, 128)], fill=ORANGE, width=4)
    d.line([(40, 136), (984, 136)], fill=RULE, width=2)

    # --- lead panel ---
    d.rounded_rectangle([40, 156, 984, 512], radius=18, fill=NAVY2)
    d.rectangle([40, 156, 52, 512], fill=ORANGE)
    d.text((76, 176), LEAD["kicker"], font=font(BOLD, 24), fill=ORANGE)
    head_lines = wrap(d, LEAD["headline"], font(BOLD, 44), 620)
    y = text_block(d, (76, 212), head_lines, font(BOLD, 44), INK, 54)
    body_lines = wrap(d, LEAD["body"], font(REG, 25), 620)
    text_block(d, (76, y + 14), body_lines, font(REG, 25), MUTED, 34)
    # ballot illustration on the right
    draw_ballot(d, 830, 330, 105)

    # --- four small panels, 2 x 2 ---
    px, py = [40, 522], [532, 702]
    pw, ph, gap = 462, 150, 20
    for i, p in enumerate(PANELS):
        x0 = px[i % 2]
        y0 = py[i // 2]
        d.rounded_rectangle([x0, y0, x0 + pw, y0 + ph], radius=14, fill=NAVY2)
        d.rectangle([x0, y0, x0 + 8, y0 + ph], fill=CYAN)
        tx = x0 + 118
        d.text((tx, y0 + 12), p["kicker"], font=font(BOLD, 19), fill=ORANGE)
        title_lines = wrap(d, p["title"], font(BOLD, 25), pw - 140)
        yy = text_block(d, (tx, y0 + 38), title_lines, font(BOLD, 25), INK, 29)
        body_lines = wrap(d, p["body"], font(REG, 20), pw - 140)
        text_block(d, (tx, yy + 4), body_lines, font(REG, 20), MUTED, 24)
        ICONS[p["icon"]](d, x0 + 58, y0 + ph // 2 + 6, 34)

    # --- footer strip ---
    d.line([(40, 884), (984, 884)], fill=RULE, width=2)
    d.text((40, 900), "ALSO TODAY", font=font(BOLD, 19), fill=ORANGE)
    foot_lines = wrap(d, FOOTER, font(REG, 20), 944)
    text_block(d, (40, 928), foot_lines, font(REG, 20), MUTED, 26)

    img.save(OUT, "PNG", optimize=True)
    print("wrote", OUT, os.path.getsize(OUT), "bytes")


if __name__ == "__main__":
    main()
