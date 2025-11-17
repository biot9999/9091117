# Bilingual Language Switching Implementation Guide

## Overview

This document describes the bilingual (Chinese/English) language switching capability implemented for the Agent Bot (`agent/agent_bot.py`).

## Features

### 1. i18n Infrastructure

**Language Packs:**
- Located in `agent/locales/`
- `zh.json` - Chinese translations (280 keys)
- `en.json` - English translations (280 keys)
- 100% coverage verified at startup

**Strict Coverage Validation:**
- The bot performs strict validation at startup
- All language packs must have exactly the same keys
- If coverage mismatch detected, the bot exits with a detailed error message listing missing/extra keys
- This ensures 100% UI coverage when English is selected

**Default Language Configuration:**
- Set via `AGENT_DEFAULT_LANG` environment variable
- Default value: `zh` (Chinese)
- Supported values: `zh`, `en`

### 2. Translation System

**I18nManager Class:**
```python
from agent_bot import i18n

# Get translation
text = i18n.get("menu_products", "en")  # Returns "🛍️ Products"

# With template parameters
text = i18n.get("buy_quantity_prompt", "en", stock=100)
# Returns "Please enter quantity (Stock: 100):"
```

**Translation Helper Method:**
```python
# In AgentBotCore
self._t(key, user_id, **kwargs)

# Examples:
self.core._t("menu_products", uid)  # Auto-detects user's language
self.core._t("buy_quantity_prompt", uid, stock=100)  # With parameters
```

### 3. Per-User Language Preference

**Storage:**
- Stored in `lang` field in user documents
- Collection: `agent_users_{agent_bot_id}`
- Defaults to `AGENT_DEFAULT_LANG` for new users

**API Methods:**
```python
# Get user's language preference
lang = self.core.get_user_lang(user_id)  # Returns "zh" or "en"

# Set user's language preference
success = self.core.set_user_lang(user_id, "en")  # Returns True/False
```

### 4. Language Toggle Button

**Location:**
- Added to the bottom of the main menu
- Shows current language: "🌐 切换语言 (中文)" or "🌐 Language (English)"

**Behavior:**
- One-click toggle between Chinese and English
- Immediately refreshes the UI in the new language
- Persists preference to MongoDB
- Shows confirmation message in the newly selected language

**Implementation:**
```python
def handle_toggle_language(self, query):
    """Handle language toggle"""
    uid = query.from_user.id
    current_lang = self.core.get_user_lang(uid)
    new_lang = "en" if current_lang == "zh" else "zh"
    
    if self.core.set_user_lang(uid, new_lang):
        lang_name = "English" if new_lang == "en" else "中文"
        query.answer(f"Language switched to {lang_name}")
        self.show_main_menu(query)
```

## Translated UI Pages

### Fully Translated (100% Coverage):
- ✅ Main Menu
- ✅ User Profile
- ✅ Product Categories List
- ✅ Support Page
- ✅ Help Page
- ✅ UI Helper Messages

### Partially Translated (Core Functionality):
- 🟡 Product Detail Pages
- 🟡 Purchase Flows
- 🟡 Recharge Flows
- 🟡 Order History
- 🟡 Admin Panels (Price Management, Reports, Profit Center)

## Translation Keys Structure

### Key Naming Convention:
```
{section}_{element}_{detail}

Examples:
menu_products          - Main menu product button
profile_title          - Profile page title
buy_quantity_prompt    - Purchase quantity prompt
error_generic          - Generic error message
```

### Key Categories:
- `menu_*` - Main menu and navigation
- `profile_*` - User profile page
- `products_*` - Product listing and categories
- `category_products_*` - Product category details
- `product_detail_*` - Individual product details
- `buy_*` - Purchase flows
- `recharge_*` - Recharge/top-up flows
- `orders_*` - Order history
- `order_detail_*` - Order details
- `support_*` - Customer support
- `help_*` - Help and usage instructions
- `price_*` - Price management (admin)
- `profit_*` - Profit center (admin)
- `reports_*` - System reports (admin)
- `error_*` - Error messages
- `button_*` - Generic button labels

## Usage Examples

### Example 1: Simple Translation
```python
def show_main_menu(self, query):
    uid = query.from_user.id
    
    kb = [
        [InlineKeyboardButton(
            self.core._t("menu_products", uid), 
            callback_data="products"
        )],
        [InlineKeyboardButton(
            self.core._t("menu_back_main", uid), 
            callback_data="back_main"
        )]
    ]
    
    text = self.core._t("menu_back_main", uid)
    self.safe_edit_message(query, text, kb)
```

### Example 2: Translation with Parameters
```python
def show_buy_confirmation(self, query, product_name, quantity, price):
    uid = query.from_user.id
    
    text = f"{self.core._t('buy_confirm_title', uid)}\n\n"
    text += f"{self.core._t('buy_confirm_product', uid)}: {product_name}\n"
    text += f"{self.core._t('buy_confirm_quantity', uid)}: {quantity}\n"
    text += f"{self.core._t('buy_confirm_total', uid)}: {price}U\n"
    
    kb = [[
        InlineKeyboardButton(
            self.core._t('buy_confirm_button', uid),
            callback_data=f"confirm_buy_{product_id}"
        ),
        InlineKeyboardButton(
            self.core._t('buy_confirm_cancel', uid),
            callback_data="cancel"
        )
    ]]
    
    self.safe_edit_message(query, text, kb)
```

### Example 3: Dynamic Template
```python
def show_stock_message(self, query, stock_count):
    uid = query.from_user.id
    
    # Using template parameter
    message = self.core._t(
        "buy_quantity_prompt", 
        uid, 
        stock=stock_count
    )
    # Chinese: "请输入购买数量（库存：100）："
    # English: "Please enter quantity (Stock: 100):"
    
    query.message.reply_text(message)
```

## Adding New Translations

### Step 1: Add keys to both language files

**agent/locales/zh.json:**
```json
{
  "my_new_feature_title": "新功能标题",
  "my_new_feature_description": "这是一个新功能的描述"
}
```

**agent/locales/en.json:**
```json
{
  "my_new_feature_title": "New Feature Title",
  "my_new_feature_description": "This is a description of the new feature"
}
```

### Step 2: Use in code
```python
def show_new_feature(self, query):
    uid = query.from_user.id
    
    text = f"{self.core._t('my_new_feature_title', uid)}\n\n"
    text += self.core._t('my_new_feature_description', uid)
    
    self.safe_edit_message(query, text, kb)
```

### Step 3: Test startup validation
```bash
# The bot will validate on startup
# If keys don't match, it will exit with an error:
❌ Language pack coverage validation FAILED:
  Reference language: zh (280 keys)
  ❌ Language 'en' is missing 1 key(s):
     - my_new_feature_description
```

## Environment Variables

### Required:
- `BOT_TOKEN` - Telegram bot token
- `MONGODB_URI` - MongoDB connection string
- `AGENT_USDT_ADDRESS` - Agent's USDT receiving address

### Optional (i18n-related):
- `AGENT_DEFAULT_LANG` - Default language for new users (default: `zh`)
  - Supported values: `zh`, `en`

## Startup Validation

When the bot starts, it performs strict validation:

```
✅ Loaded language pack: zh (280 keys)
✅ Loaded language pack: en (280 keys)
✅ Language pack coverage validation PASSED: All 2 languages have 280 matching keys
```

If validation fails:
```
❌ Language pack coverage validation FAILED:
  Reference language: zh (280 keys)
  ❌ Language 'en' is missing 2 key(s):
     - menu_new_feature
     - menu_another_feature
  ❌ Language 'en' has 1 extra key(s):
     - menu_old_feature

💡 All language packs must have exactly the same keys!
   Please update the language files to match and try again.
```

The bot will exit with code 1 if validation fails.

## Database Schema

### User Document (agent_users_{id}):
```javascript
{
  "user_id": 123456789,
  "count_id": 1,
  "username": "user123",
  "first_name": "John",
  "fullname": "John",
  "USDT": 0.0,
  "zgje": 0.0,
  "zgsl": 0,
  "creation_time": "2024-01-01 12:00:00",
  "register_time": "2024-01-01 12:00:00",
  "last_active": "2024-01-01 12:00:00",
  "last_contact_time": "2024-01-01 12:00:00",
  "status": "active",
  "lang": "en"  // ← Language preference field
}
```

## Testing

### Manual Testing Checklist:

1. **Startup Validation:**
   - [ ] Bot starts successfully with matching language packs
   - [ ] Bot refuses to start if keys don't match
   - [ ] Error message clearly shows missing/extra keys

2. **Language Toggle:**
   - [ ] Toggle button appears in main menu
   - [ ] Shows current language correctly
   - [ ] Clicking toggle switches language
   - [ ] UI refreshes immediately in new language
   - [ ] Preference persists after bot restart
   - [ ] Confirmation message shows in new language

3. **UI Coverage:**
   - [ ] Main menu fully translated
   - [ ] Profile page fully translated
   - [ ] Product categories fully translated
   - [ ] Support page fully translated
   - [ ] Help page fully translated
   - [ ] Error messages translated

4. **User Flow:**
   - [ ] New user gets default language
   - [ ] User can toggle language at any time
   - [ ] Language preference remembered across sessions
   - [ ] Multiple users can have different languages

## Troubleshooting

### Problem: Bot won't start
**Check:**
1. Language files exist in `agent/locales/`
2. Both files are valid JSON
3. Both files have exactly the same keys
4. AGENT_DEFAULT_LANG is set to a supported language

### Problem: Translation not working
**Check:**
1. Key exists in both language files
2. Using correct method: `self.core._t(key, uid)`
3. User ID is being passed correctly
4. User has language preference set (check database)

### Problem: Wrong language displayed
**Check:**
1. User's language preference in database
2. AGENT_DEFAULT_LANG environment variable
3. Language toggle was clicked (check user.lang field)

## Future Enhancements

Potential improvements for future updates:

1. **Additional Languages:**
   - Add more language files (e.g., `es.json`, `fr.json`)
   - Update I18nManager to support more than 2 languages
   - Add language selector UI (dropdown/list instead of toggle)

2. **Admin Tools:**
   - Translation management panel
   - Missing translation detector
   - Translation export/import tools

3. **User Preferences:**
   - Remember last selected menu
   - Currency display preferences
   - Time zone preferences

4. **Coverage Improvements:**
   - Complete translation of all admin panels
   - Complete translation of all notification messages
   - Translation of dynamic content from database

## License and Credits

This language switching implementation was added to the Agent Bot system.
- Implementation Date: 2024
- Language Pairs: Chinese (zh) ↔ English (en)
- Total Translation Keys: 280
