import pandas as pd
import os
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
    Image
)
from reportlab.lib.styles import getSampleStyleSheet


def generate_pdf_report():
    print("Starting PDF report generation...")

    kpi_path = "reports/kpi_summary.csv"
    output_path = "reports/Sales_Report.pdf"

    if not os.path.exists(kpi_path):
        print("Error: kpi_summary.csv not found")
        return

    kpi_df = pd.read_csv(kpi_path)

    doc = SimpleDocTemplate(output_path, pagesize=A4)
    styles = getSampleStyleSheet()
    story = []

    title = Paragraph("Python Sales Analytics Automation Report", styles["Title"])
    story.append(title)
    story.append(Spacer(1, 20))

    intro = Paragraph(
        "This report presents automated sales analysis, KPI summary, "
        "business performance charts, and key insights generated using Python.",
        styles["BodyText"]
    )
    story.append(intro)
    story.append(Spacer(1, 20))

    heading = Paragraph("KPI Summary", styles["Heading2"])
    story.append(heading)

    table_data = [["Metric", "Value"]] + kpi_df.values.tolist()

    table = Table(table_data)
    table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.darkblue),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("GRID", (0, 0), (-1, -1), 1, colors.black),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
        ("BACKGROUND", (0, 1), (-1, -1), colors.lightgrey),
    ]))

    story.append(table)
    story.append(Spacer(1, 25))

    chart_heading = Paragraph("Business Charts", styles["Heading2"])
    story.append(chart_heading)
    story.append(Spacer(1, 10))

    charts = [
        "charts/monthly_sales_trend.png",
        "charts/category_sales.png",
        "charts/region_profit.png",
        "charts/payment_mode.png",
        "charts/delivery_status.png"
    ]

    for chart in charts:
        if os.path.exists(chart):
            story.append(Image(chart, width=450, height=250))
            story.append(Spacer(1, 20))

    conclusion = Paragraph(
        "Conclusion: This project successfully automates data cleaning, "
        "sales KPI calculation, chart generation, Excel reporting, PDF reporting, "
        "and interactive dashboard creation using Python.",
        styles["BodyText"]
    )

    story.append(conclusion)

    doc.build(story)

    print("PDF report generated successfully")
    print("Report saved at:", output_path)