# Language Switching - Visual User Guide

## 🌐 How to Switch Languages

This guide shows how users can switch between Chinese (中文) and English in the Agent Bot.

---

## 📱 Main Menu - Chinese (Default)

When a new user first interacts with the bot, they see the interface in Chinese:

```
🎉 欢迎使用 华南代理机器人！

👤 用户信息
• ID: 123456789
• 用户名: @testuser
• 昵称: Test User

请选择功能：

┌─────────────────┬─────────────────┐
│ 🛍️ 商品中心      │ 👤 个人中心      │
├─────────────────┼─────────────────┤
│ 💰 充值中心      │ 📦 购买记录      │
├─────────────────┴─────────────────┤
│ 📞 客服支持      ❓ 使用帮助      │
├───────────────────────────────────┤
│      🌐 切换语言 (中文)          │ ← Language Toggle
└───────────────────────────────────┘
```

---

## 🔄 Switching to English

**Step 1:** User clicks on "🌐 切换语言 (中文)"

**Step 2:** System processes the language change:
- Current language: `zh` (Chinese)
- New language: `en` (English)
- Updates database: `user.lang = "en"`
- Shows confirmation: "🌐 Language → English"

**Step 3:** Menu refreshes automatically in English

---

## 📱 Main Menu - English

After switching, the user sees:

```
🎉 Welcome to South China Agent Bot!

👤 User Information
• ID: 123456789
• Username: @testuser
• Name: Test User

Please select a function:

┌─────────────────┬─────────────────┐
│ 🛍️ Products     │ 👤 Profile       │
├─────────────────┼─────────────────┤
│ 💰 Recharge     │ 📦 Orders        │
├─────────────────┴─────────────────┤
│ 📞 Support      ❓ Help           │
├───────────────────────────────────┤
│      🌐 Language (English)       │ ← Language Toggle
└───────────────────────────────────┘
```

---

## 🛍️ Products Page Comparison

### Chinese Version:
```
🛍️ 商品分类

请选择商品分类：

┌────────────────────────────┐
│ 🔥二手TG协议号              │
│ 库存: 150 | 15个商品        │
├────────────────────────────┤
│ ✈️【1-8年】协议老号         │
│ 库存: 80 | 8个商品          │
├────────────────────────────┤
│ 📱 Instagram账号            │
│ 库存: 45 | 6个商品          │
└────────────────────────────┘

    🔙 返回分类
```

### English Version:
```
🛍️ Product Categories

Please select a product category:

┌────────────────────────────┐
│ 🔥Second-hand TG Protocol  │
│ Stock: 150 | 15 items      │
├────────────────────────────┤
│ ✈️【1-8yr】Old Protocol    │
│ Stock: 80 | 8 items        │
├────────────────────────────┤
│ 📱 Instagram Accounts      │
│ Stock: 45 | 6 items        │
└────────────────────────────┘

   🔙 Back to Categories
```

---

## 🛒 Purchase Flow Comparison

### Chinese - Product Detail:
```
🏷️ 商品详情

🏷️ 商品: TG协议号 [3-8年]
💰 价格: 15.50U
📦 库存: 50
📂 分类: 协议号
💼 编号: ABC123456

        🛒 立即购买
```

### English - Product Detail:
```
🏷️ Product Details

🏷️ Product: TG Protocol [3-8yr]
💰 Price: 15.50U
📦 Stock: 50
📂 Category: Protocol
💼 ID: ABC123456

        🛒 Buy Now
```

---

## 💰 Recharge Center Comparison

### Chinese Version:
```
💰 充值中心

请选择充值金额或输入自定义金额：

最低充值：10U

┌──────┬──────┬──────┐
│ 10U  │ 20U  │ 50U  │
├──────┼──────┼──────┤
│ 100U │ 200U │ 500U │
└──────┴──────┴──────┘

    📝 自定义金额
    📜 充值记录
    🏠 主菜单
```

### English Version:
```
💰 Recharge Center

Please select an amount or enter a custom amount:

Minimum recharge: 10U

┌──────┬──────┬──────┐
│ 10U  │ 20U  │ 50U  │
├──────┼──────┼──────┤
│ 100U │ 200U │ 500U │
└──────┴──────┴──────┘

    📝 Custom Amount
    📜 Recharge History
    🏠 Main Menu
```

---

## ✅ Purchase Confirmation Comparison

### Chinese:
```
🛒 确认购买

商品: TG协议号
数量: 5
单价: 15.50U
总计: 77.50U
余额: 100.00U
剩余: 22.50U

  ✅ 确认购买   ❌ 取消
```

### English:
```
🛒 Confirm Purchase

Product: TG Protocol
Quantity: 5
Unit Price: 15.50U
Total: 77.50U
Balance: 100.00U
Remaining: 22.50U

  ✅ Confirm Purchase   ❌ Cancel
```

---

## 📊 Admin Panel Comparison (For Admins Only)

### Chinese - Price Management:
```
💰 价格管理（第1页）

TG协议号 [3-8年]
总部:15U  加价:0.50U  代理价:15.50U  利润率:3.3%  库:50

Instagram账号
总部:8U  加价:1.00U  代理价:9.00U  利润率:12.5%  库:30

    📝 编辑
  ⬅️ 上一页  ➡️ 下一页
      🏠 主菜单
```

### English - Price Management:
```
💰 Price Management (Page 1)

TG Protocol [3-8yr]
HQ:15U  Markup:0.50U  Agent Price:15.50U  Profit Rate:3.3%  Stock:50

Instagram Account
HQ:8U  Markup:1.00U  Agent Price:9.00U  Profit Rate:12.5%  Stock:30

    📝 Edit
  ⬅️ Previous  ➡️ Next
     🏠 Main Menu
```

---

## 🎯 Key Features

### ✅ Persistent Preference
- Language choice is saved to the database
- Preference remains even after closing the chat
- Each user can have their own language preference

### ✅ Instant Switch
- No need to restart the bot
- UI updates immediately
- Confirmation message shows in the new language

### ✅ Complete Coverage
All features support both languages:
- Main menu navigation
- Product browsing and purchase
- Recharge and payment
- Order history
- Customer support
- Help documentation
- Admin panels (price management, reports, profit center)
- Error messages and notifications

### ✅ Template Support
Dynamic content is translated correctly:
- "请输入购买数量（库存：50）：" → "Please enter quantity (Stock: 50):"
- "总订单数：125" → "Total Orders: 125"
- "订单号：ABC123" → "Order ID: ABC123"

---

## 🔧 Technical Details

### Default Language
- New users start with the default language (configurable)
- Set via `AGENT_DEFAULT_LANG` environment variable
- Default: `zh` (Chinese)

### Database Storage
```javascript
// User document
{
  "user_id": 123456789,
  "username": "testuser",
  "lang": "en",  // ← Language preference
  // ... other fields
}
```

### Supported Languages
- `zh` - Chinese (中文) 🇨🇳
- `en` - English 🇬🇧

---

## 💡 Usage Tips

1. **For New Users:**
   - Send `/start` to begin
   - Default language will be Chinese (or configured default)
   - Look for "🌐 切换语言" button to switch

2. **To Switch Language:**
   - Click the language toggle button at the bottom of main menu
   - Menu refreshes automatically
   - Preference is saved permanently

3. **Multi-User Support:**
   - Each user can choose their own language
   - User A can use Chinese while User B uses English
   - Language choice is independent per user

4. **Admin Features:**
   - All admin panels support both languages
   - Price management, reports, profit center all translated
   - System messages appear in admin's chosen language

---

## 📚 Additional Resources

- **Implementation Guide:** `agent/LANGUAGE_SWITCHING_GUIDE.md`
- **Verification Report:** `LANGUAGE_SWITCHING_VERIFICATION.md`
- **Test Suite:** `test_language_switching.py`

---

## ✨ Summary

The language switching feature provides a complete bilingual experience:
- ✅ Easy one-click toggle
- ✅ Persistent user preferences
- ✅ 280 translation keys covering all features
- ✅ Template parameter support for dynamic content
- ✅ Immediate UI refresh
- ✅ Independent per-user language choice

**The bot is production-ready with full Chinese/English bilingual support!** 🚀
