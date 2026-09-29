# generate-diagrams.py
"""
Generate 3 architecture diagrams for GIG 1 project using matplotlib.
Output: screenshots/architecture-diagram.png
        screenshots/data-flow-diagram.png
        screenshots/erd-diagram.png
"""
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

OUTPUT_DIR = "screenshots"
os.makedirs(OUTPUT_DIR, exist_ok=True)


def draw_box(ax, x, y, w, h, text, color="#4A90E2", text_color="white", fontsize=10):
    box = FancyBboxPatch(
        (x, y), w, h,
        boxstyle="round,pad=0.05",
        facecolor=color, edgecolor="black", linewidth=1.5
    )
    ax.add_patch(box)
    ax.text(x + w / 2, y + h / 2, text, ha="center", va="center",
            color=text_color, fontsize=fontsize, fontweight="bold")


def draw_arrow(ax, x1, y1, x2, y2, color="black"):
    arrow = FancyArrowPatch(
        (x1, y1), (x2, y2),
        arrowstyle="->", mutation_scale=20, color=color, linewidth=1.5
    )
    ax.add_patch(arrow)


def draw_architecture_diagram():
    fig, ax = plt.subplots(figsize=(14, 8))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 8)
    ax.axis("off")
    ax.set_title("GIG 1 - System Architecture", fontsize=16, fontweight="bold", pad=20)

    # Data Sources
    draw_box(ax, 0.5, 5.5, 2.5, 1.2, "Data Sources\n(API, CSV, DB)", "#E67E22")
    # Airflow
    draw_box(ax, 0.5, 3.5, 2.5, 1.2, "Apache Airflow\n(Orchestration)", "#3498DB")
    # Extract
    draw_box(ax, 3.5, 5.5, 2.5, 1.2, "Extract\n(Pandas)", "#27AE60")
    # Transform
    draw_box(ax, 3.5, 3.5, 2.5, 1.2, "Transform\n(Pandas)", "#27AE60")
    # Load
    draw_box(ax, 3.5, 1.5, 2.5, 1.2, "Load\n(SQLAlchemy)", "#27AE60")
    # PostgreSQL
    draw_box(ax, 7, 3.5, 2.5, 1.2, "PostgreSQL 15\n(Data Warehouse)", "#2980B9")
    # Streamlit
    draw_box(ax, 10.5, 3.5, 2.5, 1.2, "Streamlit\n(Dashboard)", "#E74C3C")
    # Docker
    draw_box(ax, 7, 1.5, 6, 1.0, "Docker Container Environment", "#7F8C8D")

    # Arrows
    draw_arrow(ax, 3.0, 6.1, 3.5, 6.1)
    draw_arrow(ax, 3.0, 4.1, 3.5, 4.1)
    draw_arrow(ax, 6.0, 5.5, 6.0, 4.7)
    draw_arrow(ax, 6.0, 3.5, 6.0, 2.7)
    draw_arrow(ax, 6.0, 2.1, 7.0, 4.1)
    draw_arrow(ax, 9.5, 4.1, 10.5, 4.1)
    draw_arrow(ax, 1.75, 4.7, 1.75, 5.5)

    plt.tight_layout()
    plt.savefig(f"{OUTPUT_DIR}/architecture-diagram.png", dpi=150, bbox_inches="tight")
    plt.close()
    print("Created: architecture-diagram.png")


def draw_data_flow_diagram():
    fig, ax = plt.subplots(figsize=(14, 6))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 6)
    ax.axis("off")
    ax.set_title("GIG 1 - Data Flow Pipeline", fontsize=16, fontweight="bold", pad=20)

    draw_box(ax, 0.5, 3, 2.5, 1.5, "Step 1\nEXTRACT\n\nXLSX to CSV", "#E67E22")
    draw_box(ax, 3.8, 3, 2.5, 1.5, "Step 2\nTRANSFORM\n\nClean, Dedup", "#27AE60")
    draw_box(ax, 7.1, 3, 2.5, 1.5, "Step 3\nLOAD\n\nTo PostgreSQL", "#2980B9")
    draw_box(ax, 10.4, 3, 2.5, 1.5, "Step 4\nVISUALIZE\n\nStreamlit", "#E74C3C")

    draw_arrow(ax, 3.0, 3.75, 3.8, 3.75)
    draw_arrow(ax, 6.3, 3.75, 7.1, 3.75)
    draw_arrow(ax, 9.6, 3.75, 10.4, 3.75)

    ax.text(1.75, 2, "1,067,371 rows\n43.5 MB", ha="center", fontsize=9, color="#555")
    ax.text(5.05, 2, "Clean data\n768,845 rows", ha="center", fontsize=9, color="#555")
    ax.text(8.35, 2, "fact_trips\n768,845 rows", ha="center", fontsize=9, color="#555")
    ax.text(11.65, 2, "4 KPIs\n3 charts", ha="center", fontsize=9, color="#555")

    ax.text(7, 0.7, "Total Execution Time: ~4 minutes", ha="center",
            fontsize=11, fontweight="bold", color="#333",
            bbox=dict(boxstyle="round", facecolor="#F0F0F0", edgecolor="gray"))

    plt.tight_layout()
    plt.savefig(f"{OUTPUT_DIR}/data-flow-diagram.png", dpi=150, bbox_inches="tight")
    plt.close()
    print("Created: data-flow-diagram.png")


def draw_erd_diagram():
    fig, ax = plt.subplots(figsize=(10, 8))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis("off")
    ax.set_title("GIG 1 - ERD: fact_trips Table", fontsize=16, fontweight="bold", pad=20)

    draw_box(ax, 1, 8.5, 8, 0.8, "fact_trips", "#2980B9", fontsize=13)

    columns = [
        ("trip_id", "SERIAL", "PK"),
        ("invoice_no", "VARCHAR(20)", ""),
        ("stock_code", "VARCHAR(20)", ""),
        ("description", "VARCHAR(255)", ""),
        ("quantity", "INTEGER", ""),
        ("invoice_date", "TIMESTAMP", ""),
        ("unit_price", "NUMERIC(10,2)", ""),
        ("customer_id", "VARCHAR(20)", ""),
        ("country", "VARCHAR(50)", ""),
        ("created_at", "TIMESTAMP", ""),
    ]

    y = 8.2
    for col_name, col_type, marker in columns:
        h = 0.6
        y -= h
        bg_color = "#ECF0F1" if marker != "PK" else "#F39C12"
        box = FancyBboxPatch(
            (1, y), 8, h,
            boxstyle="square,pad=0",
            facecolor=bg_color, edgecolor="#333", linewidth=1
        )
        ax.add_patch(box)
        ax.text(1.2, y + h / 2, col_name, ha="left", va="center",
                fontsize=10, fontweight="bold" if marker == "PK" else "normal")
        ax.text(4.5, y + h / 2, col_type, ha="left", va="center",
                fontsize=9, color="#555", style="italic")
        if marker:
            ax.text(8.5, y + h / 2, marker, ha="center", va="center",
                    fontsize=9, fontweight="bold", color="white",
                    bbox=dict(boxstyle="round,pad=0.2", facecolor="#E74C3C"))

    ax.text(5, 1.2, "Indexes: idx_invoice_date, idx_customer_id, idx_country, idx_stock_code",
            ha="center", fontsize=9, color="#555",
            bbox=dict(boxstyle="round", facecolor="#F0F0F0", edgecolor="gray"))

    plt.tight_layout()
    plt.savefig(f"{OUTPUT_DIR}/erd-diagram.png", dpi=150, bbox_inches="tight")
    plt.close()
    print("Created: erd-diagram.png")


if __name__ == "__main__":
    print("Generating 3 diagrams...")
    draw_architecture_diagram()
    draw_data_flow_diagram()
    draw_erd_diagram()
    print(f"\nAll diagrams saved to: {OUTPUT_DIR}/")