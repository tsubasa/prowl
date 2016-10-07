Prowl-lite
==========

Prowlの通知機能をサポート

主な機能
--------

- テキストやURLをiOSへプッシュ通知
- 通知にプライオリティを指定

サンプルコード
--------------

    prowl = Prowl(APIKEY)

    # テキストを通知
    prowl.add('application', 'event', 'description')

    # URLを通知
    prowl.add('application', 'event', 'description', url='https://example.com')

    # 優先順位を高で通知
    prowl.add('application', 'event', 'description', priority=3)
