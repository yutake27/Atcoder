# abc180 メモ
## [e問題](https://atcoder.jp/contests/abc180/tasks/abc180_e)

巡回セールスマン問題

nが大きいと解けないNP完全問題

nが小さい時はbitDPで解ける

詳しい資料が https://www.slideshare.net/chokudai/wap-atcoder4 にある．

既に通った都市の集合と最後に通った都市の情報があれば，DPで解ける．

既に通った都市はbitで保存し，最後に通った都市は番号をそのまま保存

二次元配列　dp[1 <<n][n] を作成し,DPで値を更新していけばコストが求まる．

最後に開始地点に戻ってくる必要があるのを忘れずに．