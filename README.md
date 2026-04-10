# Food Classification API

## Giới thiệu
Đây là API phân loại món ăn sử dụng mô hình Zero-shot classification.

## Công nghệ sử dụng
- FastAPI
- Transformers (HuggingFace)
- Model: typeform/distilbert-base-uncased-mnli

## Cách chạy
python3 -m uvicorn main:app --reload

API endpoints
GET / → kiểm tra API
GET /health → kiểm tra trạng thái
POST /predict → phân loại món ăn
Ví dụ input

{
"text": "I love pho"
}

Output

{
"predicted_label": "Vietnamese food",
"confidence": 0.8
}