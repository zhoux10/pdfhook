
from src.extensions import db

from sqlalchemy.dialects.postgresql import JSON


class PDFForm(db.Model):
    __tablename__ = 'pdfform'
    id = db.Column(db.Integer, primary_key=True, index=True)
    added_on = db.Column(db.DateTime(), server_default=db.func.now())
    original_pdf = db.Column(db.LargeBinary)
    original_pdf_title = db.Column(db.String(128))
    fdf_mapping = db.Column(JSON)
    post_count = db.Column(db.Integer, default=0)
    latest_post = db.Column(db.DateTime())

    def __repr__(self):
        return '<PDFForm:"[{}] {}">'.format(self.id, self.original_pdf_title)
