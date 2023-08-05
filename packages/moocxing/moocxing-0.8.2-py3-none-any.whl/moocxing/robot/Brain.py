from moocxing.robot import LoadPlugin
import logging

log = logging.getLogger(__name__)


class Brain:
    def __init__(self, MODULE):
        self.plugins = LoadPlugin.loadPlugin(MODULE)

    def query(self, text, chat=False):
        if text:
            for plugin in self.plugins.values():
                if not plugin.isValid(text):
                    continue
                log.info("匹配到" + plugin.SLUG + "技能")
                plugin.handle(text)
                return True
            else:
                if chat:
                    log.info("已匹配到闲聊功能")
                    self.plugins["chat"].handle("chat" + text)
                    return True
                log.info("未匹配到技能")
                return False
        else:
            log.info("---识别内容为空---")
        return False
