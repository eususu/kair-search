from typing import Optional
from pydantic import BaseModel, Field, field_validator

class ICNAirplane(BaseModel):
  strgFileNm:str
  typeOfFlight:str
  flightName:str = Field(alias='masterflight')
  airlineName:str = Field(alias='airlineNameKo')
  airportName1Ko:str
  arrivalOrDeparture:str
  estimatedTime:str = Field(alias='etime')
  stattxt:str
  terminalId:str
  terminal:str
  gatenumber:str
  exitnumber:Optional[str]= Field(default=None, description='입국장 출구')
  carousel:Optional[str]= Field(default=None, description="수하물 수취대")

  class Config():
    populate_by_name = True

  def to_str(self):
    values = []

    values.append(f'항공편={self.flightName}')

    is_arriaval = False
    if self.arrivalOrDeparture == "A":
      direction = "출국"
      inout = "입구"
      values.append(f'- 출발지=인천국제공항')
    else:
      direction = "입국"
      inout = "출구"
    #values.append(f'상태={self.arrivalOrDeparture}')
    values.append(f'- {direction} 터미널={self.terminal}')
    values.append(f'- {direction}장 {inout}={self.exitnumber if self.exitnumber else "미정"}')
    values.append(f'- {direction} 게이트={self.gatenumber}')

    values.append(f'- 예상도착시간={self.estimatedTime}')
    values.append(f'- 항공기 상태={self.stattxt if self.stattxt else "알수없음"}')

    return "\n".join(values)
