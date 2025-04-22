# Backend with Real Crawler

## 설치
```
pip install -r requirements.txt
playwright install
```

## 실행
```
gunicorn app:app --bind 0.0.0.0:8000
```