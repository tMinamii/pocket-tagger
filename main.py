import requests

import json


class Pocket:
    """Pocketの認証トークン."""

    def __init__(self):
        """初期化."""
        with open("key.json", "r") as f:
            key = json.load(f)
            self.consumer_key: str = key["pocket"]["consumer_key"]
            self.access_token: str = key["pocket"]["access_token"]

    def fetch_items(self, count: int, offset: int):
        """Pocketから記事を取得する."""
        url = "https://getpocket.com/v3/get"
        headers = {"Content-Type": "application/json"}
        data = json.dumps(
            {
                "consumer_key": self.consumer_key,
                "access_token": self.access_token,
                "count": count,
                "offset": offset,
            }
        )
        resp = requests.get(url=url, headers=headers, data=data)
        return resp.json()


if __name__ == "__main__":
    """Main."""
    p = Pocket()

    count = 50
    i = 0
    resp = p.fetch_items(count, i)
    for k, v in resp["list"].items():
        title = v["resolved_title"]
        url = v["resolved_url"]
        print(title, url)

    while len(resp["list"]):
        i += 1
        resp = p.fetch_items(count, i * count)

        for k, v in resp["list"].items():
            title = v["resolved_title"]
            url = v["resolved_url"]
            print(title, url)


tags = {
    "wsl": ["wsl", "doc"],
    "react": ["react", "frontend"],
    "markdown": ["markdown", "doc"],
    "vue": ["vue", "frontend"],
    "nuxt": ["nuxt", "vue", "frontend"],
    "コード": ["programming", "architecture"],
    "architecture": ["programming", "architecture"],
    "go": ["go", "programming"],
    "golang": ["go", "programming"],
    "aws": ["aws"],
    "lambda": ["aws", "serverless"],
    "serverless": ["aws", "serverless"],
    "twitter": ["twitter"],
    "vscode": ["vscode", "editor"],
    "vim": ["vim", "editor"],
    "neovim": ["vim", "editor"],
}
