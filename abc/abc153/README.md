# [ABC153](https://atcoder.jp/contests/abc153/tasks)

## 感想
a,b,c,d,eを自力で時間内で解けた

fも方針は立って愚直解は書けたが3ケースだけTLE．
計算量を減らす方法が思いつかず終了

## A~D問題
特に悩まず

等比数列の和の公式を若干忘れていたくらい

## E問題
DPで解けそうだなと思ってDPでやったら解けた

1次元のDPなのでそんなに難しくはない

## F問題
初めてF問題まで触った．

x座標でソートをして左から順番に爆弾を仕掛けていけばいけそうだと思ったらその通りだった．

しかし毎回爆弾の有効範囲を求めてその範囲内にいるモンスターの敵のHPを減らしていくやり方だと最悪N^2かかってし

セグメントツリーとかを使うのかな？と思った．（セグメントツリーでもいけるらしい）

今回は各爆弾の有効範囲とダメージをqueueでメモしておいて爆弾の合計ダメージを計算しておき，爆弾の有効範囲外になったら合計ダメージからその爆弾のダメージを減らすようにすればいける．

解説
https://www.youtube.com/watch?v=pKOPnK1JPLE&ab_channel=AtCoderLive
