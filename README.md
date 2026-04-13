# Food Classification API

## Thông tin sinh viên

* Họ tên: Nguyễn Thành Nam
* MSSV: 24120386

---

## Mô hình sử dụng

* Tên mô hình: typeform/distilbert-base-uncased-mnli
* Link: https://huggingface.co/typeform/distilbert-base-uncased-mnli

---

## Mô tả hệ thống

API dùng FastAPI để phân loại món ăn từ văn bản.
Sử dụng mô hình zero-shot classification từ HuggingFace.

---

## Hướng dẫn cài đặt

Cài thư viện:

pip install fastapi uvicorn transformers torch requests

---

## Hướng dẫn chạy

Chạy server:

python3 -m uvicorn main:app --reload

Mở trình duyệt:

http://127.0.0.1:8000/docs

---

## Gọi API

### Endpoint:

POST /predict

### Request:

{
"text": "I love Vietnamese food like pho"
}

### Response:

{
  "input": "I love Vietnamese food like pho",
  "result": {
    "label": "Vietnamese food",
    "confidence": 0.9975
    }
}

## Demo video 
https://drive.google.com/drive/folders/1PkybiiyTZVgiBcSqHxtTMLxS0A3JIeh8?usp=sharing
