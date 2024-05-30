import os
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from datetime import datetime


def save_report_as_pdf(company_name, report_content):
    # Create a directory for reports if it doesn't exist
    report_dir = 'reports'
    os.makedirs(report_dir, exist_ok=True)

    # Get the current date in the format DD.MM.YYYY
    current_date = datetime.now().strftime("%d.%m.%Y")

    # Initialize the count for the file naming
    count = 1

    # Generate the base filename
    base_filename = f"{company_name}-report-{current_date}"
    filename = f"{base_filename}-{count}.pdf"
    filepath = os.path.join(report_dir, filename)

    # Increment the count if the file already exists
    while os.path.exists(filepath):
        count += 1
        filename = f"{base_filename}-{count}.pdf"
        filepath = os.path.join(report_dir, filename)

    # Create the PDF
    c = canvas.Canvas(filepath, pagesize=letter)
    width, height = letter

    # Add content to the PDF
    c.setFont("Helvetica", 12)
    text_object = c.beginText(40, height - 40)
    for line in report_content.split('\n'):
        text_object.textLine(line)
    c.drawText(text_object)

    # Save the PDF
    c.save()
    print(f"Report saved as {filepath}")


# Example usage
'''
company_name = "IsBank"
report_content = """Here is the analysis report for IsBank.
- Financial Health: Excellent
- Market Trends: Positive
- Analyst Recommendations: Buy
"""
save_report_as_pdf(company_name, report_content)
'''
