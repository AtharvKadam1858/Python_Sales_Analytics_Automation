from src.data_cleaning import clean_data
from src.data_analysis import analyze_data
from src.visualization import create_charts
from src.report_generator import generate_excel_report
from src.pdf_report import generate_pdf_report
from src.business_insights import generate_business_insights


def main():
    print("=" * 50)
    print("Python Sales Analytics Automation Project")
    print("=" * 50)

    clean_data()
    analyze_data()
    create_charts()
    generate_excel_report()
    generate_pdf_report()
    generate_business_insights()

    print("=" * 50)
    print("Project executed successfully")
    print("=" * 50)


if __name__ == "__main__":
    main()