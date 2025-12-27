pip install -r requirements.txt
cd pdf_to_docx
python manage.py collectstatic --noinput
python manage.py migrate
