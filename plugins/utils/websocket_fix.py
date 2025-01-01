#实现黑白名单判断，后续aiReplyCore的阻断也将在这里实现
import asyncio
import json

import websockets

from developTools.adapters.websocket_adapter import WebSocketBot
from developTools.event.eventFactory import EventFactory
from developTools.event.events import GroupMessageEvent, PrivateMessageEvent


class ExtendBot(WebSocketBot):
    def __init__(self, uri: str,config):
        super().__init__(uri)
        self.config = config
    async def _receive(self):
        """
        接收服务端消息并分发处理。
        """
        try:
            async for response in self.websocket:
                data = json.loads(response)
                self.logger.info(f"收到服务端响应: {data}")

                # 如果是响应消息
                if "status" in data and "echo" in data:
                    echo = data["echo"]
                    future = self.response_callbacks.pop(echo, None)
                    if future and not future.done():
                        future.set_result(data)
                elif "post_type" in data:
                    event_obj = EventFactory.create_event(data)
                    try:
                        if event_obj.post_type=="meta_event":

                            if event_obj.meta_event_type=="lifecycle":
                                self.id = int(event_obj.self_id)
                                self.logger.info(f"Bot ID: {self.id}")
                    except:
                        pass
                    if isinstance(event_obj, GroupMessageEvent):
                        if self.config.settings["bot_config"]["group_handle_logic"]=="blacklist":
                            if event_obj.group_id not in self.config.censor_group["blacklist"]:
                                if self.config.settings["bot_config"]["user_handle_logic"] == "blacklist":
                                    if event_obj.user_id not in self.config.censor_user["blacklist"]:
                                        asyncio.create_task(self.event_bus.emit(event_obj))
                                    else:
                                        self.logger.info(f"用户{event_obj.user_id}在黑名单中，跳过处理。")
                                elif self.config.settings["bot_config"]["user_handle_logic"] == "whitelist":
                                    if event_obj.user_id in self.config.censor_user["whitelist"]:
                                        asyncio.create_task(self.event_bus.emit(event_obj))
                                    else:
                                        self.logger.info(f"用户{event_obj.user_id}不在白名单中，跳过处理。")
                            else:
                                self.logger.info(f"群{event_obj.group_id}在黑名单中，跳过处理。")
                        elif self.config.settings["bot_config"]["group_handle_logic"]=="whitelist":
                            if event_obj.group_id in self.config.censor_group["whitelist"]:
                                if self.config.settings["bot_config"]["user_handle_logic"] == "blacklist":
                                    if event_obj.user_id not in self.config.censor_user["blacklist"]:
                                        asyncio.create_task(self.event_bus.emit(event_obj))
                                    else:
                                        self.logger.info(f"用户{event_obj.user_id}在黑名单中，跳过处理。")
                                elif self.config.settings["bot_config"]["user_handle_logic"] == "whitelist":
                                    if event_obj.user_id in self.config.censor_user["whitelist"]:
                                        asyncio.create_task(self.event_bus.emit(event_obj))
                                    else:
                                        self.logger.info(f"用户{event_obj.user_id}不在白名单中，跳过处理。")
                            else:
                                self.logger.info(f"群{event_obj.group_id}不在白名单中，跳过处理。")
                    elif isinstance(event_obj,PrivateMessageEvent):
                        if self.config.settings["bot_config"]["user_handle_logic"]=="blacklist":
                            if event_obj.user_id not in self.config.censor_user["blacklist"]:
                                asyncio.create_task(self.event_bus.emit(event_obj))
                            else:
                                self.logger.info(f"用户{event_obj.user_id}在黑名单中，跳过处理。")
                        elif self.config.settings["bot_config"]["user_handle_logic"]=="whitelist":
                            if event_obj.user_id in self.config.censor_user["whitelist"]:
                                asyncio.create_task(self.event_bus.emit(event_obj))
                            else:
                                self.logger.info(f"用户{event_obj.user_id}不在白名单中，跳过处理。")
                    elif event_obj:
                        asyncio.create_task(self.event_bus.emit(event_obj))  #不能await，否则会阻塞
                    else:
                        self.logger.warning("无法匹配事件类型，跳过处理。")
                else:
                    self.logger.warning("收到未知消息格式，已忽略。")
        except websockets.exceptions.ConnectionClosedError as e:
            self.logger.warning(f"WebSocket 连接关闭: {e}")
            self.logger.warning("5秒后尝试重连")
            await asyncio.sleep(5)
            await self._connect_and_run()
        except Exception as e:
            self.logger.error(f"接收消息时发生错误: {e}", exc_info=True)
        finally:
            # 取消所有未完成的 Future
            for future in self.response_callbacks.values():
                if not future.done():
                    future.cancel()
            self.response_callbacks.clear()
            self.receive_task = None