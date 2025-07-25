from run.ai_llm.service.aiReplyHandler.default_freeModels import free_model_result


async def defaultModelRequest(ask_prompt,proxy=None,model_name="gpt-4o-mini"):
    if proxy is not None and proxy !="":
        proxies={"http://": proxy, "https://": proxy}
    else:
        proxies=None
    return await free_model_result(ask_prompt,proxies,model_name)