#!/usr/bin/env python3
"""One-shot migration of docx notes -> Hugo content bundles. Not meant to be re-run idempotently on hand-edited output."""
import re
import shutil
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCX_DIR = Path.home() / "Desktop/pcubed-solutions/docx/184_notes"
CONTENT_DIR = ROOT / "content" / "notes"

WEEKS = [
    ("week-01-charges-field-potential", "Week 1: Charges, Electric Field & Electric Potential", 1),
    ("week-02-charges-superposition", "Week 2: Charges & Superposition", 2),
    ("week-03-electric-force-energy", "Week 3: Electric Force & Energy", 3),
    ("week-04-modeling-distributions-of-charge", "Week 4: Modeling Distributions of Charge", 4),
    ("week-05-moving-charges-batteries", "Week 5: Modeling Moving Charges & Batteries", 5),
    ("week-06-resistors-combinations", "Week 6: Resistors & Combinations of Resistors", 6),
    ("week-07-combinations-part-2", "Week 7: Combinations of Resistors (Part 2)", 7),
    ("week-08-capacitors-combinations", "Week 8: Capacitors & Combinations of Capacitors", 8),
    ("week-09-magnetic-field-moving-point-charge", "Week 9: Magnetic Field from a Moving Point Charge", 9),
    ("week-10-magnetic-field-of-a-wire", "Week 10: Magnetic Field of a Wire", 10),
    ("week-11-sources-of-magnetic-fields", "Week 11: Sources of Magnetic Fields", 11),
    ("week-12-magnetic-force", "Week 12: Magnetic Force", 12),
    ("week-13-em-so-far-flux-shortcuts", "Week 13: E&M so far, Flux, & Short Cuts", 13),
    ("week-14-induction", "Week 14: Induction", 14),
]

# slug -> (week_dir, weight within week)
PAGES = {
    "math_review": ("week-01-charges-field-potential", 1),
    "charge": ("week-01-charges-field-potential", 2),
    "pc_efield": ("week-01-charges-field-potential", 3),
    "pc_potential": ("week-01-charges-field-potential", 4),
    "relating_ev": ("week-01-charges-field-potential", 5),

    "charge_and_matter": ("week-02-charges-superposition", 1),
    "charging_discharging": ("week-02-charges-superposition", 2),
    "superposition": ("week-02-charges-superposition", 3),
    "dipole_sup": ("week-02-charges-superposition", 4),
    "using_python": ("week-02-charges-superposition", 5),
    "python_syntax": ("week-02-charges-superposition", 6),
    "comp_super": ("week-02-charges-superposition", 7),

    "force_review": ("week-03-electric-force-energy", 1),
    "pc_force": ("week-03-electric-force-energy", 2),
    "energy_review": ("week-03-electric-force-energy", 3),
    "pc_energy": ("week-03-electric-force-energy", 4),
    "pc_vefu": ("week-03-electric-force-energy", 5),

    "line_fields": ("week-04-modeling-distributions-of-charge", 1),
    "dq": ("week-04-modeling-distributions-of-charge", 2),
    "linecharge": ("week-04-modeling-distributions-of-charge", 3),
    "dist_charges": ("week-04-modeling-distributions-of-charge", 4),
    "patterns_fields": ("week-04-modeling-distributions-of-charge", 5),

    "motiv_movingq": ("week-05-moving-charges-batteries", 1),
    "batteries": ("week-05-moving-charges-batteries", 2),
    "q_in_wires": ("week-05-moving-charges-batteries", 3),
    "gradient": ("week-05-moving-charges-batteries", 4),

    "defining_current": ("week-06-resistors-combinations", 1),
    "current": ("week-06-resistors-combinations", 2),
    "resistors": ("week-06-resistors-combinations", 3),
    "r_energy": ("week-06-resistors-combinations", 4),
    "resistivity": ("week-06-resistors-combinations", 5),
    "r_series": ("week-06-resistors-combinations", 6),
    "r_parallel": ("week-06-resistors-combinations", 7),

    "kirchoffs_rules": ("week-07-combinations-part-2", 1),
    "combinations": ("week-07-combinations-part-2", 2),

    "cap_charging": ("week-08-capacitors-combinations", 1),
    "cap_in_cir": ("week-08-capacitors-combinations", 2),
    "c_series": ("week-08-capacitors-combinations", 3),
    "c_parallel": ("week-08-capacitors-combinations", 4),

    "mag_interaction": ("week-09-magnetic-field-moving-point-charge", 1),
    "moving_q": ("week-09-magnetic-field-moving-point-charge", 2),
    "rhr": ("week-09-magnetic-field-moving-point-charge", 3),

    "superposition_b": ("week-10-magnetic-field-of-a-wire", 1),
    "b_current": ("week-10-magnetic-field-of-a-wire", 2),

    "b_sup_comp": ("week-11-sources-of-magnetic-fields", 1),
    "b_shapes": ("week-11-sources-of-magnetic-fields", 2),
    "perm_mag": ("week-11-sources-of-magnetic-fields", 3),
    "motiv_b_force": ("week-11-sources-of-magnetic-fields", 4),
    "q_b_force": ("week-11-sources-of-magnetic-fields", 5),
    "q_path": ("week-11-sources-of-magnetic-fields", 6),

    "i_b_force": ("week-12-magnetic-force", 1),
    "b_summary": ("week-12-magnetic-force", 2),

    "what_happens": ("week-13-em-so-far-flux-shortcuts", 1),
    "b_flux": ("week-13-em-so-far-flux-shortcuts", 2),
    "ind_i": ("week-13-em-so-far-flux-shortcuts", 3),
    "induced_current": ("week-13-em-so-far-flux-shortcuts", 4),
    "relating_e": ("week-13-em-so-far-flux-shortcuts", 5),

    "ind_graphs": ("week-14-induction", 1),
    "b_flux_t": ("week-14-induction", 2),
    "ac": ("week-14-induction", 3),
    "electric_field": ("week-14-induction", 4),
}

assert len(PAGES) == 61

LINK_MAP = {slug: f"/notes/{week_dir}/{slug}/" for slug, (week_dir, _) in PAGES.items()}

# Cross-course links back into the already-migrated 183_notes (mechanics) site,
# which lives at dannycaballero.info/pcubed/ on the same domain.
PCUBED_LINK_MAP = {
    "scalars_and_vectors": "/pcubed/notes/week-01-modeling-motion-no-net-force/scalars_and_vectors/",
    "displacement_and_velocity": "/pcubed/notes/week-01-modeling-motion-no-net-force/displacement_and_velocity/",
    "modeling_with_vpython": "/pcubed/notes/week-01-modeling-motion-no-net-force/modeling_with_vpython/",
    "relative_motion": "/pcubed/notes/week-01-modeling-motion-no-net-force/relative_motion/",
    "graphing_motion": "/pcubed/notes/week-01-modeling-motion-no-net-force/graphing_motion/",
    "momentum": "/pcubed/notes/week-02-modeling-motion-net-force/momentum/",
    "momentum_principle": "/pcubed/notes/week-02-modeling-motion-net-force/momentum_principle/",
    "acceleration": "/pcubed/notes/week-02-modeling-motion-net-force/acceleration/",
    "motionpredict": "/pcubed/notes/week-02-modeling-motion-net-force/motionpredict/",
    "constantf": "/pcubed/notes/week-02-modeling-motion-net-force/constantf/",
    "localg": "/pcubed/notes/week-02-modeling-motion-net-force/localg/",
    "iterativepredict": "/pcubed/notes/week-02-modeling-motion-net-force/iterativepredict/",
    "drag": "/pcubed/notes/week-02-modeling-motion-net-force/drag/",
    "gravitation": "/pcubed/notes/week-03-newtonian-gravitation/gravitation/",
    "grav_accel": "/pcubed/notes/week-03-newtonian-gravitation/grav_accel/",
    "ucm": "/pcubed/notes/week-03-newtonian-gravitation/ucm/",
    "impulsegraphs": "/pcubed/notes/week-04-05-springs-contact-interactions/impulsegraphs/",
    "springmotion": "/pcubed/notes/week-04-05-springs-contact-interactions/springmotion/",
    "freebodydiagrams": "/pcubed/notes/week-04-05-springs-contact-interactions/freebodydiagrams/",
    "friction": "/pcubed/notes/week-04-05-springs-contact-interactions/friction/",
    "mp_multi": "/pcubed/notes/week-04-05-springs-contact-interactions/mp_multi/",
    "collisions": "/pcubed/notes/week-04-05-springs-contact-interactions/collisions/",
    "model_of_solids": "/pcubed/notes/week-06-solids-curved-motion/model_of_solids/",
    "model_of_a_wire": "/pcubed/notes/week-06-solids-curved-motion/model_of_a_wire/",
    "youngs_modulus": "/pcubed/notes/week-06-solids-curved-motion/youngs_modulus/",
    "curving_motion": "/pcubed/notes/week-06-solids-curved-motion/curving_motion/",
    "center_of_mass": "/pcubed/notes/week-06-solids-curved-motion/center_of_mass/",
    "define_energy": "/pcubed/notes/week-07-energy-transfer/define_energy/",
    "point_particle": "/pcubed/notes/week-07-energy-transfer/point_particle/",
    "work": "/pcubed/notes/week-07-energy-transfer/work/",
    "work_by_nc_forces": "/pcubed/notes/week-07-energy-transfer/work_by_nc_forces/",
    "potential_energy": "/pcubed/notes/week-07-energy-transfer/potential_energy/",
    "grav_and_spring_pe": "/pcubed/notes/week-07-energy-transfer/grav_and_spring_pe/",
    "rest_mass": "/pcubed/notes/week-07-energy-transfer/rest_mass/",
    "spring_pe": "/pcubed/notes/week-08-potential-energy-applications/spring_pe/",
    "force_and_pe": "/pcubed/notes/week-08-potential-energy-applications/force_and_pe/",
    "newton_grav_pe": "/pcubed/notes/week-08-potential-energy-applications/newton_grav_pe/",
    "grav_pe_graphs": "/pcubed/notes/week-08-potential-energy-applications/grav_pe_graphs/",
    "escape_speed": "/pcubed/notes/week-08-potential-energy-applications/escape_speed/",
    "colliding_systems": "/pcubed/notes/week-08-potential-energy-applications/colliding_systems/",
    "internal_energy": "/pcubed/notes/week-10-internal-energy-heat/internal_energy/",
    "heat": "/pcubed/notes/week-10-internal-energy-heat/heat/",
    "power": "/pcubed/notes/week-10-internal-energy-heat/power/",
    "system_choice": "/pcubed/notes/week-10-internal-energy-heat/system_choice/",
    "energy_dissipation": "/pcubed/notes/week-10-internal-energy-heat/energy_dissipation/",
    "energy_sep": "/pcubed/notes/week-11-multi-particle-energy/energy_sep/",
    "rot_ke": "/pcubed/notes/week-11-multi-particle-energy/rot_ke/",
    "pp_vs_real": "/pcubed/notes/week-11-multi-particle-energy/pp_vs_real/",
    "proof_of_pp": "/pcubed/notes/week-11-multi-particle-energy/proof_of_pp/",
    "discovery_of_the_nucleus": "/pcubed/notes/week-12-14-collisions-rotational-motion/discovery_of_the_nucleus/",
    "angular_motivation": "/pcubed/notes/week-12-14-collisions-rotational-motion/angular_motivation/",
    "torque": "/pcubed/notes/week-12-14-collisions-rotational-motion/torque/",
    "static_eq": "/pcubed/notes/week-12-14-collisions-rotational-motion/static_eq/",
    "torquediagram": "/pcubed/notes/week-12-14-collisions-rotational-motion/torquediagram/",
    "ang_momentum": "/pcubed/notes/week-12-14-collisions-rotational-motion/ang_momentum/",
    "l_principle": "/pcubed/notes/week-12-14-collisions-rotational-motion/l_principle/",
    "l_conservation": "/pcubed/notes/week-12-14-collisions-rotational-motion/l_conservation/",
    "fundamental_principles": "/pcubed/notes/week-15-core-principles/fundamental_principles/",
}

HEADING_RE = re.compile(r"^(#{1,2})\s+(.*)$")
WIKI_LINK_RE = re.compile(
    r"https?://(?:www\.)?msuperl\.org/wikis/pcubed/doku\.php\?id=184_notes:([a-zA-Z0-9_]+)(#[a-zA-Z0-9_]*)?"
)
CROSS_WIKI_LINK_RE = re.compile(
    r"https?://(?:www\.)?msuperl\.org/wikis/pcubed/doku\.php\?id=183_notes:([a-zA-Z0-9_]+)(#[a-zA-Z0-9_]*)?"
)
OTHER_WIKI_LINK_RE = re.compile(
    r"https?://(?:www\.)?msuperl\.org/wikis/pcubed/doku\.php\?id=([a-zA-Z0-9_:]+)"
)
YOUTUBE_BLOCK_RE = re.compile(
    r"\[<img[^\n]*?/>\]\(https://www\.youtube\.com/watch\?v=([A-Za-z0-9_-]+)\)\n\n"
    r"Video:[^\n]*\[watch on YouTube\]\(https://www\.youtube\.com/watch\?v=\1\)\n?"
)
MATH_BLOCK_RE = re.compile(r"^``` math\n(.*?)\n```$", re.DOTALL | re.MULTILINE)
INLINE_MATH_RE = re.compile(r"\$`(.+?)`\$")
SIMULATION_LINE_RE = re.compile(r"^Interactive simulation: (.+?) — <(\S+)>$", re.MULTILINE)


def convert_docx(slug: str, bundle_dir: Path):
    docx_path = DOCX_DIR / f"184_notes_{slug}.docx"
    bundle_dir.mkdir(parents=True, exist_ok=True)
    subprocess.run(
        ["pandoc", str(docx_path), "-t", "gfm", "--wrap=none",
         "-o", "index.md", "--extract-media=."],
        cwd=bundle_dir, check=True,
    )
    media_dir = bundle_dir / "media"
    if media_dir.exists() and not any(media_dir.iterdir()):
        media_dir.rmdir()


def split_title(text: str):
    lines = text.lstrip("\n").split("\n")
    idx = next((i for i, l in enumerate(lines) if HEADING_RE.match(l)), None)
    if idx is None:
        raise ValueError("no heading found")
    textbook_ref = " ".join(l.strip() for l in lines[:idx] if l.strip()) or None
    title = HEADING_RE.match(lines[idx]).group(2).strip()
    body = "\n".join(lines[idx + 1:]).lstrip("\n")
    return title, textbook_ref, body


def demote_headings(body: str) -> str:
    in_fence = False
    levels = []
    out_lines = []
    for line in body.split("\n"):
        if line.startswith("```"):
            in_fence = not in_fence
        elif not in_fence:
            m = re.match(r"^(#{1,6})\s", line)
            if m:
                levels.append(len(m.group(1)))
    if not levels:
        return body
    shift = min(levels) - 2
    if shift <= 0:
        return body
    in_fence = False
    for line in body.split("\n"):
        if line.startswith("```"):
            in_fence = not in_fence
            out_lines.append(line)
            continue
        if not in_fence:
            m = re.match(r"^(#{1,6})(\s.*)$", line)
            if m:
                new_level = max(2, len(m.group(1)) - shift)
                line = ("#" * new_level) + m.group(2)
        out_lines.append(line)
    return "\n".join(out_lines)


def convert_math(body: str) -> str:
    def block_sub(m):
        return f"$$\n{m.group(1)}\n$$"

    body = MATH_BLOCK_RE.sub(block_sub, body)

    out_lines = []
    for line in body.split("\n"):
        in_table_row = line.lstrip().startswith("|")

        def inline_sub(m, in_table_row=in_table_row):
            inner = m.group(1)
            if in_table_row:
                inner = inner.replace("|", "&#124;")
            return f"${inner}$"

        out_lines.append(INLINE_MATH_RE.sub(inline_sub, line))
    return "\n".join(out_lines)


def convert_youtube(body: str) -> str:
    return YOUTUBE_BLOCK_RE.sub(lambda m: f"{{{{< youtube {m.group(1)} >}}}}\n", body)


def convert_simulations(body: str) -> str:
    def sub(m):
        title = m.group(1).replace('"', '\\"')
        url = m.group(2)
        return f'{{{{< simulation src="{url}" title="{title}" >}}}}'

    return SIMULATION_LINE_RE.sub(sub, body)


def rewrite_links(body: str) -> str:
    def wiki_sub(m):
        slug = m.group(1)
        anchor = m.group(2) or ""
        if slug in LINK_MAP:
            return LINK_MAP[slug] + anchor
        return m.group(0)

    body = WIKI_LINK_RE.sub(wiki_sub, body)

    def cross_sub(m):
        slug = m.group(1)
        anchor = m.group(2) or ""
        if slug in PCUBED_LINK_MAP:
            return PCUBED_LINK_MAP[slug] + anchor
        return m.group(0)

    body = CROSS_WIKI_LINK_RE.sub(cross_sub, body)

    def other_sub(m):
        full_id = m.group(1)
        if ":" in full_id:
            namespace, leaf = full_id.split(":", 1)
            leaf = leaf.split(":")[-1]
            if namespace == "184_notes" and leaf in LINK_MAP:
                return LINK_MAP[leaf]
            if namespace == "183_notes" and leaf in PCUBED_LINK_MAP:
                return PCUBED_LINK_MAP[leaf]
        return "https://www.msuperl.org/wikis/pcubed/doku.php?id=" + full_id

    body = OTHER_WIKI_LINK_RE.sub(other_sub, body)
    return body


def yaml_single_quote(value: str) -> str:
    return "'" + value.replace("'", "''") + "'"


def process_page(slug: str, week_dir: str, weight: int):
    bundle_dir = CONTENT_DIR / week_dir / slug
    convert_docx(slug, bundle_dir)
    raw = (bundle_dir / "index.md").read_text()
    title, textbook_ref, body = split_title(raw)
    title = convert_math(title)
    body = demote_headings(body)
    body = convert_math(body)
    body = convert_youtube(body)
    body = convert_simulations(body)
    body = rewrite_links(body)

    fm_lines = ["---", f"title: {yaml_single_quote(title)}", f"weight: {weight}"]
    if textbook_ref:
        fm_lines.append(f"textbook_ref: {yaml_single_quote(textbook_ref)}")
    fm_lines.append("---\n")
    (bundle_dir / "index.md").write_text("\n".join(fm_lines) + "\n" + body)


def write_week_index(week_dir: str, title: str, weight: int):
    d = CONTENT_DIR / week_dir
    d.mkdir(parents=True, exist_ok=True)
    (d / "_index.md").write_text(
        "\n".join(["---", f'title: "{title}"', f"weight: {weight}", "---", ""])
    )


def write_notes_index():
    CONTENT_DIR.mkdir(parents=True, exist_ok=True)
    (CONTENT_DIR / "_index.md").write_text(
        "\n".join(["---", 'title: "Notes"', "---", ""])
    )


def main():
    if CONTENT_DIR.exists():
        shutil.rmtree(CONTENT_DIR)
    write_notes_index()
    for week_dir, title, weight in WEEKS:
        write_week_index(week_dir, title, weight)
    todo = []
    for slug, (week_dir, weight) in PAGES.items():
        process_page(slug, week_dir, weight)
        text = (CONTENT_DIR / week_dir / slug / "index.md").read_text()
        notes = []
        if "ALT TEXT NEEDED" in text:
            notes.append(f"{text.count('ALT TEXT NEEDED')} image(s) missing alt text")
        if "MANUAL REVIEW" in text:
            notes.append("embed/link flagged for manual review")
        if notes:
            todo.append(f"{week_dir}/{slug}: " + "; ".join(notes))
        print(f"ok: {week_dir}/{slug}")
    (ROOT / "scripts" / "content-todo.txt").write_text("\n".join(todo) + "\n")
    print(f"\n{len(todo)} pages have pending content todos; see scripts/content-todo.txt")


if __name__ == "__main__":
    main()
