from flask import Flask, render_template, request
import tweepy

app = Flask(__name__)


def tweet(txt):
    CK = ""
    CS = ""
    AT = ""
    ATS = ""
    # ↑ここにKeyを入れてください。
    auth = tweepy.OAuthHandler(CK, CS)
    auth.set_access_token(AT, ATS)
    api = tweepy.API(auth)

    api.update_status(str(txt))


@app.route('/')
def hello_world():
    content = request.args.get("content")
    try:
        if content == None:
            return f"ざんねん！content内容がNoneなのでツイートされませんでした！/?content=hogeでアクセスしてください！"
        else:
            tweet(content)
            return f"Yeees! ツイートに成功しました: {content}"
    except:
        return f"Oh..... ツイートに失敗しました....: {content}"


if __name__ == '__main__':
    app.run()
