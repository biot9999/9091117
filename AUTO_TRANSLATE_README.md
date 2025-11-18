# 自动翻译功能 (Google Translate Integration)

## 功能说明

系统现在支持使用 Google Translate 自动翻译商品名称中的任意中文文本。

### 工作原理

1. **字典优先**: 首先使用内置字典翻译 150 个国家名和 12 个常用词组
2. **自动翻译**: 如果还有剩余中文字符，使用 Google Translate 自动翻译
3. **优雅降级**: 如果翻译失败，返回部分翻译的结果

### 安装依赖

```bash
pip install googletrans==4.0.0-rc1
```

### 环境变量配置

可选配置（默认启用）：

```bash
# 禁用自动翻译（仅使用字典）
DISABLE_AUTO_TRANSLATE=true

# 翻译超时时间（秒）
TRANSLATE_TIMEOUT=5
```

### 使用示例

**自动翻译前（仅字典）:**
```
【3-5年】优质老号 → 【3-5years】优质老号
```

**自动翻译后（字典 + Google Translate）:**
```
【3-5年】优质老号 → 【3-5years】Quality Old Account
墨西哥虚拟号码 → Mexico Virtual Number
限时优惠商品 → Limited Time Offer Products
```

### 翻译示例

| 中文 | 英文（字典） | 英文（字典 + 自动翻译） |
|------|------------|---------------------|
| 墨西哥🇲🇽+52 | Mexico🇲🇽+52 | Mexico🇲🇽+52 |
| 【3-8年】老号 | 【3-8years】Old Account | 【3-8years】Old Account |
| 【3-5年】优质老号 | 【3-5years】优质Old Account | 【3-5years】Quality Old Account |
| 高质量账号 | 高质量Account | High Quality Account |
| 限时优惠商品 | 限时优惠商品 | Limited Time Offer Products |

### 技术细节

**翻译流程:**
1. 用户切换到英文模式
2. 系统调用 `translate_product_name()` 方法
3. 使用字典替换 150 个国家名和 12 个常用词组
4. 检测是否还有中文字符
5. 如果有中文且 Google Translate 可用，调用 API 翻译
6. 返回最终翻译结果

**性能优化:**
- 字典翻译优先（速度快，无网络请求）
- Google Translate 仅在需要时调用
- 内置超时和错误处理
- 翻译失败时优雅降级

**免费额度:**
- Google Translate API 有免费额度限制
- `googletrans` 库使用非官方 API，无需付费
- 建议在生产环境监控使用量

### 注意事项

1. **网络依赖**: Google Translate 需要互联网连接
2. **速度**: 自动翻译会增加一点延迟（通常 < 1 秒）
3. **准确性**: 机器翻译可能不够精确，但足够理解
4. **可靠性**: 如果 Google 服务不可用，会回退到字典翻译

### 禁用自动翻译

如果不需要自动翻译功能，可以：

1. 设置环境变量：`DISABLE_AUTO_TRANSLATE=true`
2. 或者不安装 `googletrans` 库
3. 系统会自动回退到字典翻译模式

### 故障排查

**问题**: 翻译不工作
- 检查是否安装了 `googletrans` 库
- 检查网络连接
- 查看日志中的错误信息

**问题**: 翻译速度慢
- 这是正常的，Google Translate API 需要网络请求
- 考虑增加更多字典条目以减少 API 调用

**问题**: 翻译质量不佳
- 机器翻译有局限性
- 可以通过添加更多字典条目来改进常用词的翻译

### 维护建议

1. **定期更新字典**: 添加常用商品名词到翻译字典
2. **监控日志**: 关注翻译失败的情况
3. **用户反馈**: 收集用户对翻译质量的反馈
4. **备选方案**: 考虑使用其他翻译服务（如 DeepL）

