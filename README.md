# Food Classification API

## Giới thiệu
Đây là API phân loại món ăn sử dụng mô hình **Zero-shot classification** từ HuggingFace.

---

## Công nghệ sử dụng
- FastAPI
- Transformers (HuggingFace)
- Model: typeform/distilbert-base-uncased-mnli

---

## Cách chạy
python3 -m uvicorn main:app --reload

API Endpoints
- GET /
→ Kiểm tra API hoạt động
- GET /health
→ Kiểm tra trạng thái server
- POST /predict
→ Phân loại món ăn

Ví dụ Input

{
"text": "I love pho"
}

Output

{
  "input": "I love pho",
  "predicted_label": "Vietnamese food",
  "confidence": 0.82
}