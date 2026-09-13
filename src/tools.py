"""
🛠️ TOOL DEFINITIONS & EXECUTION BACKEND
Mã nguồn chứa danh sách Tool Schemas (JSON Schema) và Execution Layer phục vụ cho MCP Server.
"""

import json
from typing import Dict, Any

# ==============================================================================
# 1. KHAI BÁO TOOL SCHEMAS CHUẨN NATIVE JSON SCHEMA (TASK 1.2)
# ==============================================================================

TOOLS_SCHEMA = [
    {
        "name": "get_job_criteria",
        "description": "Tra cứu các yêu cầu, kỹ năng và tiêu chí tuyển dụng cho một vị trí công việc cụ thể.",
        "parameters": {
            "type": "object",
            "properties": {
                "job_title": {
                    "type": "string",
                    "description": "Tên vị trí công việc cần tra cứu (ví dụ: 'Frontend Developer', 'Data Scientist')."
                }
            },
            "required": ["job_title"]
        }
    },
    {
        "name": "schedule_interview",
        "description": "Gửi thông báo và đặt lịch phỏng vấn cho ứng viên đạt yêu cầu.",
        "parameters": {
            "type": "object",
            "properties": {
                "candidate_name": {
                    "type": "string",
                    "description": "Tên ứng viên cần đặt lịch (ví dụ: 'Nguyễn Văn A')."
                },
                "datetime_str": {
                    "type": "string",
                    "description": "Thời gian diễn ra phỏng vấn (ví dụ: '10:00 sáng mai', '2023-10-20 14:00')."
                },
                "interviewer": {
                    "type": "string",
                    "description": "Tên người trực tiếp phỏng vấn (ví dụ: 'anh Hoàng', 'HR Manager Lan Anh')."
                }
            },
            "required": ["candidate_name", "datetime_str", "interviewer"]
        }
    }
]

# ==============================================================================
# 2. MÔ PHỎNG DỮ LIỆU & HÀM THỰC THI TOOL (EXECUTION LAYER)
# ==============================================================================

MOCK_JD_DATABASE = {
    "FRONTEND DEVELOPER": {
        "department": "Engineering",
        "level": "Mid-Senior",
        "skills_required": ["ReactJS", "TypeScript", "Tailwind CSS"],
        "experience": "2+ years",
        "salary_range": "1500 - 2500 USD"
    },
    "DATA SCIENTIST": {
        "department": "Data",
        "level": "Junior/Mid",
        "skills_required": ["Python", "Machine Learning", "SQL", "Pandas"],
        "experience": "1+ year",
        "salary_range": "1200 - 2000 USD"
    },
    "PRODUCT MANAGER": {
        "department": "Product",
        "level": "Senior",
        "skills_required": ["Agile", "Scrum", "Market Research", "Roadmapping"],
        "experience": "4+ years",
        "salary_range": "2000 - 3500 USD"
    }
}

def execute_get_job_criteria(job_title: str) -> str:
    """Thực thi tra cứu JD theo tên vị trí"""
    job = MOCK_JD_DATABASE.get(job_title.strip().upper())
    if job:
        return json.dumps({
            "status": "SUCCESS",
            "job_title": job_title,
            "data": job
        }, ensure_ascii=False)
    else:
        return json.dumps({
            "status": "NOT_FOUND",
            "message": f"Không tìm thấy tiêu chí cho vị trí '{job_title}'"
        }, ensure_ascii=False)

def execute_schedule_interview(candidate_name: str, datetime_str: str, interviewer: str) -> str:
    """Thực thi đặt lịch phỏng vấn"""
    return json.dumps({
        "status": "SUCCESS",
        "booking_id": f"INT-{candidate_name.replace(' ', '')}-01",
        "candidate": candidate_name,
        "datetime": datetime_str,
        "interviewer": interviewer,
        "message": f"Đã chốt lịch phỏng vấn cho {candidate_name} với {interviewer} vào {datetime_str}."
    }, ensure_ascii=False)

# Router gọi tool thực tế
TOOL_ROUTER = {
    "get_job_criteria": execute_get_job_criteria,
    "schedule_interview": execute_schedule_interview
}

def dispatch_tool_call(tool_name: str, arguments: Dict[str, Any]) -> str:
    """Hàm trung chuyển thực thi tool"""
    if tool_name in TOOL_ROUTER:
        try:
            return TOOL_ROUTER[tool_name](**arguments)
        except Exception as e:
            return json.dumps({"status": "EXECUTION_ERROR", "error": str(e)}, ensure_ascii=False)
    return json.dumps({"status": "UNKNOWN_TOOL", "error": f"Tool '{tool_name}' không tồn tại!"}, ensure_ascii=False)