# じゃんけんゲームをREST API化してください
# Path: api.py
# モジュールをインポート
from flask import Flask, request, jsonify
import random

# Flaskクラスのインスタンスを生成
app = Flask(__name__)

# じゃんけんの手をリストで定義
janken_list = ['gu', 'cyoki', 'pa']

# ルーティングの設定
@app.route('/janken', methods=['POST'])
def janken():
    # リクエストボディを取得
    req = request.json
    # プレイヤーの手を取得
    p = req['player']
    # コンピュータの手をランダムに選択
    c = random.choice(janken_list)
    # 勝敗を判定
    if p == c:
        result = 'あいこです。'
    elif (p == 'gu' and c == 'cyoki') or (p == 'cyoki' and c == 'pa') or (p == 'pa' and c == 'gu'):
        result = 'あなたの勝ちです。'
    else:
        result = 'あなたの負けです。'
    # レスポンスボディを生成
    res = {
        'player': p,
        'computer': c,
        'result': result
    }
    # レスポンスボディをJSON形式に変換して返却
    return jsonify(res)

# 実行する
if __name__ == '__main__':
    app.run(debug=True)