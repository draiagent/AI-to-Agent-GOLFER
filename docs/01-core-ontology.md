# 01｜核心角色與名詞

## 角色責任

| 角色 | 責任 | 不應混淆 |
| --- | --- | --- |
| Human Sponsor | 設定商業目標、資源與風險容忍度 | 不把責任外包給模型 |
| AI Coach | 設計方法、訓練、評量與持續改善 | 不一定親自執行每個任務 |
| AI Golfer | 在授權範圍內做出一次完整決策並執行 | 不是單純 Router 或聊天助理 |
| AI Caddie | 蒐集資訊、提示風險、提出建議 | 無最終決策權，除非另有授權 |
| Human Approver | 核准高風險、不可回復或受規範決策 | 核准必須留下證據 |
| Auditor / Reviewer | 檢查輸入、執行紀錄、輸出與規範 | 不應只看最終文案 |

## 核心物件

### VAD — Course Map

把任務目標、利害關係人、素材、資料、限制、風險、流程與驗收畫成所有角色都能理解的任務圖。VAD 是「這一球面對什麼」，不是最終打法。

### Memory — Yardage Book

保存已知事實、歷史結果、組織偏好、政策與情境。Memory 必須標示來源、更新時間、可信度、存取權與失效日期。

### Decision — Commit to the Shot

AI Golfer 依目標、風險、可回復性、期限、成本與經驗，選擇進攻、保守、升級、詢問、停止或轉交人類。

### Golf Bag — Model & Tool Registry

列出可用模型、工具與接口的能力、成本、延遲、隱私、可靠性與限制。它提供選項，不取代決策。

### Workflow — Pre-shot Routine

明確列出輸入、步驟、工具、角色、例外、重試、停止條件與輸出。Workflow 應可追蹤、可重播、可回復。

### Verify — Scorecard

以正確性、完整性、風險、品牌、成本、速度與商業 KPI 驗收。Verify 應與 Goal 同時定義，不是在最後臨時挑毛病。

### VAC — Shot Playbook

將已通過 Verify 的成功打法，連同適用條件、版本、失效條件與責任人，保存為可重用能力。VAC 不是提示詞收藏，而是完整能力契約。

### Brand — Team Identity

規範受眾、定位、語氣、視覺、事實聲明、敏感內容、禁語與署名。品牌護欄要能進入 Workflow 與 Verify。

## VAD、Memory、VAC 的邊界

| 問題 | VAD | Memory | VAC |
| --- | --- | --- | --- |
| 現在面對什麼？ | 主要負責 | 提供歷史 | 提供相似打法 |
| 已知哪些事實？ | 引用 | 主要負責 | 引用必要知識 |
| 上次怎麼成功？ | 可顯示 | 保存結果 | 主要負責 |
| 下次能否重複？ | 不直接決定 | 不直接決定 | 以適用與失效條件決定 |

## VAC 最低能力契約

一個可用的 VAC 至少需要：

```text
Trigger + Inputs + Context + Decision Rule + Model/Tool Policy
+ Workflow + Permissions + Verification + Failure Path
+ Brand Guardrail + Owner + Version + Expiry
```

少了其中任何關鍵項目，VAC 就可能只是漂亮範本，而非企業能力。
