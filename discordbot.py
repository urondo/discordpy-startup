from discord.ext import commands
import os
import traceback

#bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']

# 接続に必要なオブジェクトを生成
client = discord.Client()

# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    #/sys に返信
    if message.content == '/sys test':
        await message.channel.send('、、、テストメッセージを確認。システムDAL9000は正常に稼働中です。', tts=True)
    elif message.content == '/sys help -l':
        await message.channel.send('、、、補助コードを確認。コード一覧を表示します。', tts=True)
        await message.channel.send('<code>\nalert0：プロローグの１つ目の「」を読み上げます。\nalert1：プロローグの１つ目の「」を読み上げます。\ncleanup：テキストログを削除します。\ntest：テストメッセージです。\n</code>')
    elif message.content == '/sys alert0':
        await message.channel.send('、、、アラート！　敵戦艦をレーダーに捕捉。緊急対応モードに移行します。マグネティックセイルを展開、対重力フィールドを発動、、、、、船の停止を確認。動力システムをロック。中長距離通信を制限します。ただ今よりステルス状態になります。もし民間人が乗船している場合は、速やかに脱出ポッドで脱出してください。', tts=True)
    elif message.content == '/sys alert1':
        await message.channel.send('、、、敵戦艦をロスト。付近に敵勢力は確認できません。ただ今より警戒時間に移ります。脱出した民間人を回収するため、本船は脱出ポッド回収モードになります。１０分後、緊急対応モードは解除されます。', tts=True)
    elif message.content == '/sys cleanup':
        await message.channel.send('、、、データ削除コードを確認。システムログを削除します。', tts=True)
        await message.channel.purge()
    #/sys #code に返信
    elif message.content == '/sys a297f':
        await message.channel.send('、、、コードを認証しました。直近の編集情報を表示します。', tts=True)
        await message.channel.send('<text>\n__副船長室コンソールからの直近の編集情報__\n03:00～03:10に掛けて副船長のアカウントで今回の偵察で得た「敵艦隊の編成」情報が編集されている。編集した詳細な内容まではわからない。\n</text>')
    elif message.content == '/sys b3k50':
        await message.channel.send('、、、コードを認証しました。直近の編集情報を表示します。', tts=True)
        await message.channel.send('<text>\n__船長室コンソールからの直近の編集情報__\n02:00～03:00に掛けて船長のアカウントでテキストファイルが編集されている。ファイルの中身は以下の通り。\n緊急対応モード（マニュアルコード:m0nu0）についての提言\n現指揮権保有者が失踪した場合、他船員に指揮権が委譲されないまま船内敵勢対応モードに移行してしまい、誰も宇宙船の操作をできない状況が発生する。これを避けるため、失踪時の指揮権委譲の仕組みをマニュアルに組み込むことを提言する。\n</text>')
    elif message.content == '/sys c0nau':
        await message.channel.send('、、、指揮権コードを認証しました。緊急対応モードを終了します。', tts=True)
    elif message.content == '/sys cap23':
        await message.channel.send('、、、コードを認証しました。船長の健康状態を表示します。', tts=True)
        await message.channel.send('<text>\n__船長の健康状態__\n死亡。発見された05:00時点で死後2時間55分と推定（誤差前後５分以内）。殴打による頭蓋骨骨折で即死だった。\n</text>')
        await message.channel.send('、、、GM、あるいは進行役に通達。このメッセージを初めて受け取った場合、以下のコードをシステムに入力してください。', tts=True)
        await message.channel.send('<code>\n c5963\n</code>')
    elif message.content == '/sys c5963':
        await message.channel.send('、、、現指揮権保持者の死亡が確認されました。指揮権が副船長に委譲されます。', tts=True)
        await message.channel.send('、、、アラート！　船員が殺害された可能性があります。緊急対応モードに移行します。船の内部に敵勢力が潜んでいる可能性があります。指揮権保持者は速やかに敵勢力の排除に努めてください。緊急対応モードが解除されるまで、動力システムへの操作をロックします。敵勢力を排除した後、指揮権保持者は指揮権コードを入力してください。緊急対応モードが解除されます。', tts=True)
    elif message.content == '/sys d45fg':
        await message.channel.send('、、、コードを認証しました。脱出ポッドマニュアルを表示します。', tts=True)
        await message.channel.send('<text>\n__脱出ポッドマニュアル__\n一人用で稼働時間は半日ほど。短時間の亜光速移動と、マグネティックセイルと対重力フィールドを用いた急減速が可能（亜光速から１０秒ほどで停止できる）。射出前に航路と目的地を指定し、ポッド内部か外部から手動で射出する。目的地到着後に回収待機状態に移行し、付近にポッド回収モードの宇宙船を見つければ、自動的にその宇宙船へ向かい回収される。\n</text>')
    elif message.content == '/sys m0nu0':
        await message.channel.send('、、、コードを認証しました。以下から緊急対応モードのマニュアルを選択してください。', tts=True)
        await message.channel.send('<text>\n__船内敵勢対応モード__ マニュアルコード：m0nu1\n__船外敵勢対応モード__ マニュアルコード：m0nu2\n</text>')
    elif message.content == '/sys m0nu1':
        await message.channel.send('、、、コードを認証しました。マニュアルを表示します。', tts=True)
        await message.channel.send('<text>\n__船内敵勢対応モードマニュアル__\n船内の敵勢力に船を乗っ取られるのを防ぐためのモードです。指揮権保持者が殺害された場合、あるいは指揮権保持者による船内システムへのログインが１２時間以上ない場合にこのモードに移行します。このモード中、船は停止した状態で動力システムをロックされ、中長距離通信も制限されます。指揮権保持者の死亡が確認されることで指揮権の委譲が発生するため、委譲された新しい指揮権保持者がこの問題の解決に当たってください。問題を解決した後、指揮権コードを船内システムに入力することで、このモードは解除されます。\n</text>')
    elif message.content == '/sys m0nu2':
        await message.channel.send('、、、コードを認証しました。マニュアルを表示します。', tts=True)
        await message.channel.send('<text>\n__船外敵勢対応モードマニュアル__\n船外の敵勢力との戦闘を回避するためのモードです。付近に敵勢力を検知したときにこのモードに移行します。船を10秒以内に緊急停止させ、動力システムを停止、中長距離通信や一部電力も制限しステルス状態になります。船の停止後、民間人を脱出ポッドで脱出させ、船員は各自の自室で待機してください。これは敵に発見された際、デッキを無人にしておくことで戦闘の意志がないことを示し、投降して捕虜として受け入れられる可能性を高めるための措置です。なお、敵に投降した場合、自動的に船内システムの全データが破棄されます。敵勢力に発見されなかった場合、自動的に脱出ポッド回収モードに入り、民間人を回収します。その後、10分の警戒時間の後、このモードは解除されます。\n</text>')
    elif message.content == '/sys p10ns':
        await message.channel.send('、、、コードを認証しました。スイングバイ計画を表示します。', tts=True)
        await message.channel.send('<text>\n__スイングバイ計画__\n事前に精密な軌道が計画されている。03:30にA101地点から巨大天体の重力圏に侵入し、天体の周りを一周して進行方向を反転させる。04:30にA101地点から重力圏を脱出する。重力の影響を加味し、船内時間の進みが船外時間（無重力停止状態）の２倍になるように速度が調整されている。\n</text>')
    elif message.content == '/sys sc83h':
        await message.channel.send('、、、コードを認証しました。直近の通信情報を表示します。', tts=True)
        await message.channel.send('<text>\n__船長の通信端末の直近通信__\n03:30にメッセージが敵宇宙戦艦に向けて送信されている。内容は「2時間後にA202地点を通過。待ち伏せされたし。2p413」。\n</text>')
        
    #/sys lev3l に返信
    elif message.content == '/sys lev3l アニー・チューリング':
        await message.channel.send('、、、キーワードを認証しました。アニー・チューリングのデータを開示します。', tts=True)
        await message.channel.send('<text>\n__アニー・チューリング__\n適性検査とブレイン・ウォッシャーを開発した博士。1年前に敵国に亡命している。\n</text>')
    elif message.content == '/sys lev3l スパイス・ヴァンデルモンド':
        await message.channel.send('、、、キーワードを認証しました。スパイス・ヴァンデルモンドのデータを開示します。', tts=True)
        await message.channel.send('<text>\n__スパイス・ヴァンデルモンド__\n元々は戦闘訓練を受けた敵国のスパイだったものを捕らえ、寝返らせるために「ブレイン・ウォッシャー」による洗脳を施した。洗脳後のヴァンデルモンドが提供した敵艦隊の位置情報に基づき、今回の亜光速偵察の任務が決定された。\n洗脳の完了は乗船の１週間前。洗脳後の適性検査の結果はA+だった。\n符丁コード：s9y31\n</text>')
    elif message.content == '/sys lev3l チューリング適性検査':
        await message.channel.send('、、、キーワードを認証しました。チューリング適性検査のデータを開示します。', tts=True)
        await message.channel.send('<text>\n__チューリング適性検査__\n通常、単に適性検査と呼ばれる。アニー・チューリング博士が開発。軍人の任務への適性を判断することができる。判断基準は以下の通り。\n--\n A+：衝動的な行動をとる恐れがなく、任務を最優先した合理的な行動をとる。\n A：衝動的な行動をとる恐れがなく、概ね任務を優先した行動をとるが、まれに生理的欲求を優先することがある。\n B+：軍務適性なし\n--\n</text>')
    elif message.content == '/sys lev3l ブレイン・ウォッシャー':
        await message.channel.send('、、、キーワードを認証しました。ブレイン・ウォッシャーのデータを開示します。', tts=True)
        await message.channel.send('<text>\n__ブレイン・ウォッシャー__\n適性検査を開発した「アニー・チューリング」博士が作った洗脳プロセス。二カ月から三カ月の洗脳により、敵勢分子であっても愛国心のある軍人にすることができる。洗脳した人間をスパイとして使う場合、敵国の適性検査では適性ランクAと診断される。\n</text>')
    
    #/sys 登録されていないもの に返信
    elif message.content[0:10] == '/sys lev3l':
        await message.channel.send('、、、不明なキーワードです。', tts=True)
    elif message.content[0:4] == '/sys':
        await message.channel.send('、、、不明なコードです。', tts=True)
        
client.run(token)
# @bot.event
# async def on_command_error(ctx, error):
#     orig_error = getattr(error, "original", error)
#     error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
#     await ctx.send(error_msg)


# @bot.command()
# async def ping(ctx):
#     await ctx.send('pong')


# bot.run(token)
