# 05｜AI Handicap 與衡量

## 為什麼不只看模型排行榜？

同一模型搭配不同 Memory、VAC、Tools、Workflow 與治理，結果會完全不同。企業應評估完整 Agent，而非只評估球桿。

## 四種 Handicap

| 指標 | 衡量對象 | 核心問題 |
| --- | --- | --- |
| Task Handicap | 任務 | 這一洞有多難、風險多高？ |
| Model Handicap | 模型 | 這支球桿對此類任務的能力、成本與穩定度？ |
| Agent Handicap | 完整 Agent | 加上 Memory、Tools、Workflow 後，能否穩定完成？ |
| Enterprise Handicap | 組織 | 治理、資料、人才與 VAC 是否能持續複利？ |

## 建議核心指標

### 效率

- Cycle Time：從任務建立到通過 Verify 的時間。
- Human Touch Time：人類實際投入時間。
- Cost per Accepted Outcome：每個合格成果的總成本。
- Rework Rate：退回重做或重大修改比例。

### 品質與風險

- First-Pass Acceptance：第一次即通過比例。
- Critical Error Rate：重大錯誤比例。
- Evidence Coverage：需引用主張中可追溯來源的比例。
- Brand Compliance：品牌檢查通過比例。
- Unauthorized Action：未授權外部行動次數，目標為 0。

### 能力複利

- VAC Reuse Rate：合格任務中使用已核准 VAC 的比例。
- VAC Success Rate：使用 VAC 後通過 Verify 的比例。
- Escalation Rate：升級高階模型或人類的比例。
- Stale Memory Rate：被發現過期、失效或衝突的記憶比例。

## 100 分 Agent Handicap Score

```text
任務完成與正確性       30
風險與合規             20
可追溯與可重播         15
成本與速度             15
品牌一致性             10
VAC 可重用性           10
```

- 90–100：可在既定邊界內自主執行。
- 75–89：可半自動執行，保留抽查或核准。
- 60–74：僅適合輔助，需強化資料或 Workflow。
- 0–59：回到 VAD 重新設計，不應擴大使用。

## 評量原則

先建立人工 Baseline，再比較 Agent；同時看平均值與最壞案例。成本下降若伴隨重大錯誤上升，不算成功。
