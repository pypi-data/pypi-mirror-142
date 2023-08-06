import sqlite3
from datetime import date, datetime, timedelta

from PyPtt import PTT


class PTTCrawler:
    def __init__(self, id: str, passwd: str):
        self.bot: PTT.API = PTT.API()
        self.bot.login(id, passwd, kick_other_login=True)

    def __call__(self, *boards):
        for board in boards:
            end_index = self.bot.get_newest_index(
                index_type=PTT.data_type.index_type.BBS,
                board=board,
                search_type=PTT.data_type.post_search_type.PUSH,
                search_condition="30",
            )
            start_index = end_index - 750 + 1

            self.bot.crawl_board(
                crawl_type=PTT.data_type.crawl_type.BBS,
                post_handler=PTTCrawler.post_handler,
                board=board,
                start_index=start_index,
                end_index=end_index,
                # start_aid=start_aid,
                # end_aid=end_aid,
                search_type=PTT.data_type.post_search_type.PUSH,
                search_condition="30"
                # search_list: list
                # query_bool: bool
                # start_page: int
                # end_page: int
            )

    def logout(self):
        self.bot.logout()

    @staticmethod
    def post_handler(post_info: PTT.data_type.PostInfo):
        if post_info.date is None:
            return

        if datetime.strptime(
            post_info.date, "%a %b %d %H:%M:%S %Y"
        ).date() < date.today() - timedelta(days=2):
            print(f"{post_info.aid} {post_info.index} {post_info.date} SKIPPED")
            return

        parsed_post_info = PTTCrawler.parse_post_info(post_info)

    @staticmethod
    def parse_post_info(post_info):
        board = post_info.board
        aid = post_info.aid
        index = post_info.index
        author = post_info.author.split(" ")[0]
        datetime_ = datetime.strptime(post_info.date, "%a %b %d %H:%M:%S %Y").date()
        title = post_info.title
        content = post_info.content
        ip = post_info.ip
        push_list = post_info.push_list  # need processing?

        return {
            "board": board,
            "aid": aid,
            "index": index,
            "author": author,
            "date": date,
            "datetime": datetime_,
            "title": title,
            "content": content,
            "push_list": push_list,
        }


if __name__ == "__main__":
    con = sqlite3.connect("ptt.db")

    crawler = PTTCrawler("inch446", "41yx9yuu")
    crawler("Gossiping", "Stock")
    crawler.logout()
