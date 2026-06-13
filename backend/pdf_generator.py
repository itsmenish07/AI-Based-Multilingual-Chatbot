from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import getSampleStyleSheet


def generate_pdf(
    scheme_name,
    documents
):

    filename = f"{scheme_name}.pdf"

    pdf = SimpleDocTemplate(
        filename
    )

    styles = getSampleStyleSheet()

    content = []

    content.append(
        Paragraph(
            f"{scheme_name} Checklist",
            styles["Title"]
        )
    )

    content.append(
        Spacer(1, 12)
    )

    for doc in documents:

        content.append(
            Paragraph(
                f"✓ {doc}",
                styles["Normal"]
            )
        )

    pdf.build(content)

    return filename