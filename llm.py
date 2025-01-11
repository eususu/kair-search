def inference(prompt:str, content:str, query:str):
  import lite_llm_client as lmc
  client = lmc.LiteLLMClient(lmc.OpenAIConfig())
  messages = [
     lmc.LLMMessage(role=lmc.LLMMessageRole.SYSTEM, content=prompt),
     lmc.LLMMessage(role=lmc.LLMMessageRole.USER, content=f'{content}\n{query}'),
  ]
  answer = client.chat_completions(messages)
  return answer

def inference_json(prompt:str, content:str, query:str, json_schema:dict):
  import lite_llm_client as lmc
  client = lmc.LiteLLMClient(lmc.OpenAIConfig())
  messages = [
     lmc.LLMMessage(role=lmc.LLMMessageRole.SYSTEM, content=prompt),
     lmc.LLMMessage(role=lmc.LLMMessageRole.USER, content=f'{content}\n{query}'),
  ]
  answer = client.chat_completions(messages, json_schema=json_schema)
  return answer