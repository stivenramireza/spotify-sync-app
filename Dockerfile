FROM python:3.8

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

ENV PYTHON_ENV production

EXPOSE 8000

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]