from pydantic import BaseModel
from llm import inference, inference_json

class Schedule(BaseModel):
    depart_airport: str
    depart_datetime: str
    arrive_airport: str
    arrive_datetime: str

def extract_schedule(query:str):

    system_prompt = """
you are helpful assistant.

follow below instructions:
- 질문하는 사람은 한국의 공항을 이용하는 사람이라고 가정합니다.
- 공항이름은 코드로 입력합니다.

"""
    json_schema = {
        "name": "extract_flight_schedule",
        "schema": {
            "type": "object",
            "properties": {
                "depart_airport": {"type": "string"},
                "depart_datetime": {"type": "string"},
                "arrive_airport": {"type": "string"},
                "arrive_datetime": {"type": "string"},
            },
            "required": ['depart_airport', 'arrive_airport', 'depart_datetime', 'arrive_datetime'],
            "additionalProperties": False,
        },
        "strict": True,
    }


    #answer = inference_json(prompt=system_prompt, content="", query=query, json_schema=json_schema)
    answer = '{"depart_airport":"ICN","depart_datetime":"2024-01-13T10:00:00","arrive_airport":"PVG","arrive_datetime":"2024-01-13T11:30:00"}'
    answer = Schedule.model_validate_json(answer)
    print(answer)

    return answer
