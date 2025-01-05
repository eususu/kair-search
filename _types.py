from pydantic import BaseModel, Field, field_validator, validator

class ICNAirplane(BaseModel):
  strgFileNm:str
  typeOfFlight:str
  flightName:str = Field(alias='masterflight')
  airlineName:str = Field(alias='airlineNameKo')
  airportName1Ko:str
  arrivalOrDeparture:str
  estimatedTime:str = Field(alias='etime')
  terminalId:str
  terminal:str
  gatenumber:str
  exitnumber:str = Field(description='입국장 출구')
  carousel:str = Field(description="수하물 수취대")

  class Config():
    populate_by_name = True

  def to_str(self):
    values = []

    values.append(f'항공편={self.flightName}')

    is_arriaval = False
    if self.arrivalOrDeparture == "A":
      direction = "출국"
      values.append(f'- 출발지=인천국제공항')
    else:
      direction = "입국"
    #values.append(f'상태={self.arrivalOrDeparture}')
    values.append(f'- 터미널={self.terminal}')
    values.append(f'- 예상도착시간={self.estimatedTime}')
    values.append(f'- {direction}장 출구={self.exitnumber}')

    return "\n".join(values)
