"""Generate README charts from labour_force_data.csv."""
import csv, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

BLUE, ORANGE = "#2a78d6", "#eb6834"
INK, MUTED, GRID, SURF = "#0b0b0b", "#52514e", "#e6e5e1", "#fcfcfb"

rows = list(csv.DictReader(open("labour_force_data.csv")))
labels = ["Sep '25", "Oct", "Nov", "Dec", "Jan '26"]
lf = [float(r["labour_force_k"]) for r in rows]
emp = [float(r["employment_k"]) for r in rows]
unemp = [float(r["unemployment_k"]) for r in rows]
part = [float(r["participation_rate_pct"]) for r in rows]
ur = [u / l * 100 for u, l in zip(unemp, lf)]
d_lf = [b - a for a, b in zip(lf, lf[1:])]
d_emp = [b - a for a, b in zip(emp, emp[1:])]

def style(ax, title, sub, ylabel):
    ax.set_facecolor(SURF); ax.figure.set_facecolor(SURF)
    for s in ("top", "right", "left"): ax.spines[s].set_visible(False)
    ax.spines["bottom"].set_color(GRID)
    ax.grid(axis="y", color=GRID, lw=0.8); ax.set_axisbelow(True)
    ax.tick_params(colors=MUTED, length=0, labelsize=10)
    ax.set_ylabel(ylabel, color=MUTED, fontsize=10)
    ax.figure.text(0.06, 0.95, title, fontsize=14, fontweight="bold", color=INK, ha="left", va="top")
    ax.figure.text(0.06, 0.885, sub, fontsize=10, color=MUTED, ha="left", va="top")

def save(fig, name):
    fig.savefig(f"{name}.png", dpi=200, facecolor=SURF); plt.close(fig)

x = range(5)

# 2. Monthly changes
fig, ax = plt.subplots(figsize=(8, 4.6)); fig.subplots_adjust(top=0.78, bottom=0.12, left=0.12, right=0.95)
w = 0.36; xs = list(range(4))
b1 = ax.bar([i - w/2 for i in xs], d_lf, w * 0.94, color=BLUE, label="Change in labour force")
b2 = ax.bar([i + w/2 for i in xs], d_emp, w * 0.94, color=ORANGE, label="Change in employment")
for bars in (b1, b2):
    for r in bars:
        v = r.get_height()
        ax.text(r.get_x() + r.get_width()/2, v + (6 if v >= 0 else -6), f"{v:+.1f}", ha="center",
                va="bottom" if v >= 0 else "top", fontsize=9, color=MUTED)
ax.axhline(0, color=MUTED, lw=1)
ax.set_xticks(xs, labels[1:]); ax.set_ylim(-150, 110)
ax.legend(frameon=False, loc="lower left", labelcolor=MUTED, fontsize=10)
style(ax, "Month-over-month change", "Thousands of persons. January: employment −24.8k, labour force −119.0k.", "Thousands")
save(fig, "02_monthly_changes")

# 3. Participation
fig, ax = plt.subplots(figsize=(8, 4.6)); fig.subplots_adjust(top=0.78, bottom=0.12, left=0.12, right=0.95)
ax.plot(x, part, color=BLUE, lw=2, marker="o", ms=7, mec=SURF, mew=2)
for i, v in enumerate(part):
    ax.text(i, v + 0.04, f"{v:.1f}%", ha="center", fontsize=9, color=MUTED)
ax.set_xticks(list(x), labels); ax.set_ylim(64.8, 65.6)
style(ax, "Labour force participation rate", "Percent. Held at 65.2% for three months, rose to 65.4% in December, then dropped to 65.0%.", "Percent")
save(fig, "03_participation_rate")

# 4. Unemployment rate
fig, ax = plt.subplots(figsize=(8, 4.6)); fig.subplots_adjust(top=0.78, bottom=0.12, left=0.12, right=0.95)
ax.plot(x, ur, color=BLUE, lw=2, marker="o", ms=7, mec=SURF, mew=2)
for i, v in enumerate(ur):
    ax.text(i, v + 0.05, f"{v:.2f}%", ha="center", fontsize=9, color=MUTED)
ax.set_xticks(list(x), labels); ax.set_ylim(6.2, 7.3)
style(ax, "Unemployment rate", "Percent = unemployment ÷ labour force. The headline drop to 6.5% in January.", "Percent")
save(fig, "04_unemployment_rate")

print([round(v, 3) for v in ur], [round(v, 1) for v in d_lf], [round(v, 1) for v in d_emp])
print("unemp change", round(unemp[4]-unemp[3], 1), "check", round(d_lf[-1]-d_emp[-1], 1))
