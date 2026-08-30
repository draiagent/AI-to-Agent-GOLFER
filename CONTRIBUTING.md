# Contributing

歡迎提交錯誤修正、產業案例、教學回饋、規格改進與翻譯。

## 貢獻原則

1. 案例需去識別化，不提交客戶秘密、個資或未授權內容。
2. 新增打法前，必須說明適用情境、風險、驗收與失效條件。
3. 不把單次成功描述為普遍有效；區分觀察、推論與已驗證結果。
4. 不綁定單一模型或工具；若有依賴，請明確標示。
5. 品牌內容需符合 [`templates/brand-guardrail.md`](templates/brand-guardrail.md)。

## Pull Request 檢查

```bash
python -m pip install -r requirements-dev.txt
python scripts/validate_examples.py
python -m unittest discover -s tests
```

請在 PR 說明：問題、改動、驗證方式、風險、相容性與素材授權。
