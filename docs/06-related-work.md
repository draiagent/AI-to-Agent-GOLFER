# 06｜相關技術與方法論差異

## 技術積木已存在，差異在上層治理

本方法論不主張重新發明模型路由，而是把成熟的路由、工具、記憶與驗證能力，組成企業可理解、可管理、可複用的決策系統。

| 類型 | 代表方向 | 主要問題 | AI Golfer 增加的上層問題 |
| --- | --- | --- | --- |
| Auto Router | [OpenRouter Auto Router](https://openrouter.ai/docs/guides/routing/routers/auto-router) | 哪個模型適合目前提示？ | 這一球應採何種策略、誰有決策權？ |
| Semantic / MoM Routing | [vLLM Semantic Router](https://github.com/vllm-project/semantic-router) | 依 request signals、使用者偏好與應用政策選擇或組合模型路徑 | 商業目標、品牌、Verify 與能力沉澱如何治理？ |
| Cost–Quality Routing | [RouteLLM](https://github.com/lm-sys/RouteLLM) | 何時用便宜或強模型？ | 成本以外，如何處理風險、不可回復性與責任？ |
| Agent Memory | 各類 session / trajectory memory | 如何保持上下文與取回經驗？ | 哪些經驗通過驗收，能成為企業 VAC？ |
| Workflow / MCP | Agent runtime 與工具接口 | 如何調用工具完成步驟？ | 如何把決策權、停止條件與品牌放進流程？ |

## 本方法論的差異化

1. **以 Decision 為中心**：不是先問 Which model，而是先問 What is the best authorized shot。
2. **VAD 把任務球場外顯**：將目標、限制、資料、流程與驗收變成共同介面。
3. **VAC 保存被驗證的企業打法**：不把所有歷史或模型輸出都視為能力。
4. **Brand 進入系統護欄**：品牌不只是視覺後製，而是輸入、決策與驗收條件。
5. **AI Handicap 評估完整能力**：比較 Agent 與企業任務表現，而非只看模型 Benchmark。
6. **AI Coach 與 AI Golfer 分工**：制度設計、訓練與問責，和單次任務決策清楚分離。

## 避免過度主張

此框架是一套整合型企業方法論與教學語言，其組成技術多有既有研究與開源實作。差異化在於角色、本體、決策閉環、品牌治理與 VAC 能力契約的組合，不表示所有底層技術均為原創。
