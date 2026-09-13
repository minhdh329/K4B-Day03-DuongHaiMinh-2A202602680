# 📊 BÁO CÁO THU HOẠCH NGHIỆM THU BÀI LAB 3 (BƯỚC 3 — SUBMISSION ARTIFACT)

> **Họ và Tên Học viên:** Dương Hải Minh  
> **Mã Sinh Viên / Mã Học viên:** 2A2026202680  
> **Chủ đề Lựa chọn:** Trợ lý Tuyển dụng & Sàng lọc CV

---

## 1. BẢNG CHẤM ĐIỂM AGENTIC FIT SCORING MATRIX (ĐÁNH GIÁ CHỦ ĐỀ)

| Tiêu chí Đánh giá | Mức độ (1 - 5) | Giải trình chi tiết lý do chọn điểm |
| :--- | :---: | :--- |
| **1. Multi-step Reasoning** | 5 / 5 | Agent phải thực hiện suy luận chuỗi: đầu tiên tra cứu tiêu chí JD, đối chiếu điều kiện, sau đó mới quyết định gọi công cụ lên lịch.|
| **2. Tool Interaction** | 5 / 5 | Yêu cầu tương tác độc lập với ít nhất hai hệ thống: CSDL tuyển dụng để lấy tiêu chí)= và hệ thống lịch/email để gửi thông báo. |
| **3. Dynamic Decision** | 4 / 5 | Hành động tiếp theo thay đổi linh hoạt phụ thuộc vào kết quả của tool trước đó |
| **4. Long Horizon Goal** | 4 / 5 | Quản lý trạng thái xuyên suốt từ lúc nhận lệnh của HR đến khi xác nhận chốt lịch hẹn thành công. |
| **TỔNG ĐIỂM AGENTIC FIT** | 18**/ 20** | *Nếu tổng điểm > 12/20: Bài toán rất phù hợp triển khai Agentic System.* |

---

## 2. TRÍCH XUẤT KẾT QUẢ WATERFALL TRACE LOG (SAU KHI CHẠY TEST SUITE TRÊN API THẬT)

> ⚠️ **YÊU CẦU NGHIỆM THU:** Mở tệp `.env` điền `GEMINI_API_KEY` (hoặc `OPENAI_API_KEY`) để kết nối LLM thật trước khi thực thi `python src/app.py --all`. Bài nộp chỉ dùng Mock Offline Provider sẽ không đạt điểm nghiệm thực tế.

Dán 1 đoạn trích xuất log tiêu biểu từ file `docs/trace_waterfall.json` sinh ra từ phản hồi LLM API thật:

```json
[
  {
    "step": 1,
    "query": "Tôi muốn đặt lịch phỏng vấn cho ứng viên Nguyễn Văn A vào 10:00 sáng mai với anh Hoàng.",
    "action_type": "TOOL_EXECUTION",
    "thought": "Gemini quyết định gọi công cụ 'schedule_interview' với tham số: {\"interviewer\": \"anh Hoàng\", \"datetime_str\": \"10:00 sáng mai\", \"candidate_name\": \"Nguyễn Văn A\"}",
    "tool_name": "schedule_interview",
    "arguments": {
      "interviewer": "anh Hoàng",
      "datetime_str": "10:00 sáng mai",
      "candidate_name": "Nguyễn Văn A"
    },
    "observation": {
      "status": "SUCCESS",
      "booking_id": "INT-NguyễnVănA-01",
      "candidate": "Nguyễn Văn A",
      "datetime": "10:00 sáng mai",
      "interviewer": "anh Hoàng",
      "message": "Đã chốt lịch phỏng vấn cho Nguyễn Văn A với anh Hoàng vào 10:00 sáng mai."
    },
    "latency_ms": 1921.89
  },
  {
    "step": 2,
    "query": "Tôi muốn đặt lịch phỏng vấn cho ứng viên Nguyễn Văn A vào 10:00 sáng mai với anh Hoàng.",
    "action_type": "FINAL_ANSWER",
    "thought": "Tổng hợp kết quả từ MCP Server thành công.",
    "output": "Đã chốt lịch phỏng vấn cho Nguyễn Văn A với anh Hoàng vào 10:00 sáng mai.",
    "latency_ms": 10.0
  }
]
```

---

## 3. TỔNG KẾT KẾT QUẢ NGHIỆM THU & NỘP BÀI

- [x] Đã điền API Key thật trong `.env` và xác nhận Agent chạy mượt mà trên LLM API thật (Gemini/OpenAI).
- **Tổng số Test Cases đã chạy thành công:** 5 / 5 test cases.
- **Số lượt gọi Tool qua MCP Server chính xác:** 4 lượt.
- **Kết quả đẩy Repo nộp bài:** [x] Đã Commit và Push mã nguồn thành công lên GitHub cá nhân.

---

> ✅ **HOÀN TẤT NỘP BÀI:** Sao chép đường link GitHub Repository cá nhân của bạn và dán vào ô nộp bài trên hệ thống LMS VLearn để hoàn tất Bài Lab 3!
