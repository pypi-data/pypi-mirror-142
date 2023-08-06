from datetime import datetime

import requests


class TelegramLogger:
    def __init__(self, token: str, chat_id: str) -> None:
        """TODO

        Args:
            token (str):
            chat_id (str):
        """
        self._url = f"https://api.telegram.org/bot{token}/sendMessage"
        self._chat_id: str = chat_id
        self._infos = []

    def add(self, msg: str) -> None:
        """TODO

        Args:
            msg (str):
        """
        self._infos.append(TelegramLogger.format_msg(msg))

    def flush(self) -> None:
        """TODO
        """
        if len(self._infos) == 0:
            return

        resp = requests.post(
            url=self._url,
            params={
                "chat_id": self._chat_id,
                "text": "\n".join(self._infos),
            },
        )
        resp.raise_for_status()
        self._infos = []

    def send(self, msg: str) -> None:
        """TODO

        Args:
            msg (str):
        """
        self.add(msg)
        self.flush()

    @staticmethod
    def format_msg(msg: str) -> str:
        """TODO

        Args:
            msg (str):

        Returns:
        """
        return f"{datetime.now().strftime('%b %d %H:%M:%S')}: {msg}"
