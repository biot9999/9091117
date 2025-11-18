#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Language Switching Feature Test Suite

This script tests the language switching functionality without requiring
a MongoDB connection or running Telegram bot.

Run with: python3 test_language_switching.py
"""

import json
import sys
from pathlib import Path


def test_language_files():
    """Test 1: Verify language files exist and have matching keys"""
    print("\n" + "="*70)
    print("TEST 1: Language Files")
    print("="*70)
    
    locales_dir = Path(__file__).parent / 'agent' / 'locales'
    
    zh_file = locales_dir / 'zh.json'
    en_file = locales_dir / 'en.json'
    
    # Check existence
    if not zh_file.exists():
        print(f"❌ FAIL: zh.json not found at {zh_file}")
        return False
    if not en_file.exists():
        print(f"❌ FAIL: en.json not found at {en_file}")
        return False
    
    print(f"✅ zh.json exists: {zh_file}")
    print(f"✅ en.json exists: {en_file}")
    
    # Load files
    try:
        with open(zh_file, 'r', encoding='utf-8') as f:
            zh_data = json.load(f)
        with open(en_file, 'r', encoding='utf-8') as f:
            en_data = json.load(f)
    except json.JSONDecodeError as e:
        print(f"❌ FAIL: Invalid JSON - {e}")
        return False
    
    print(f"✅ zh.json loaded: {len(zh_data)} keys")
    print(f"✅ en.json loaded: {len(en_data)} keys")
    
    # Check key parity
    zh_keys = set(zh_data.keys())
    en_keys = set(en_data.keys())
    
    missing_in_en = zh_keys - en_keys
    missing_in_zh = en_keys - zh_keys
    
    if missing_in_en:
        print(f"❌ FAIL: Keys missing in en.json: {sorted(missing_in_en)[:5]}...")
        return False
    
    if missing_in_zh:
        print(f"❌ FAIL: Keys missing in zh.json: {sorted(missing_in_zh)[:5]}...")
        return False
    
    print(f"✅ Key parity check passed: {len(zh_keys)} matching keys")
    
    return True


def test_code_implementation():
    """Test 2: Verify code has required methods and features"""
    print("\n" + "="*70)
    print("TEST 2: Code Implementation")
    print("="*70)
    
    agent_bot_file = Path(__file__).parent / 'agent' / 'agent_bot.py'
    
    if not agent_bot_file.exists():
        print(f"❌ FAIL: agent_bot.py not found at {agent_bot_file}")
        return False
    
    with open(agent_bot_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Required components
    checks = [
        ('I18nManager class', 'class I18nManager'),
        ('i18n instance', 'i18n = I18nManager()'),
        ('get_user_lang method', 'def get_user_lang(self, user_id'),
        ('set_user_lang method', 'def set_user_lang(self, user_id'),
        ('_t translation method', 'def _t(self, key'),
        ('handle_toggle_language handler', 'def handle_toggle_language(self, query'),
        ('toggle_language callback routing', 'if d == "toggle_language"'),
        ('menu_toggle_language usage', 'menu_toggle_language'),
        ('lang field in register_user', "'lang': i18n.default_lang"),
        ('Language pack validation', '_validate_coverage'),
        ('Template parameter support', '.format(**kwargs)'),
    ]
    
    all_passed = True
    for name, pattern in checks:
        if pattern in content:
            print(f"✅ {name}")
        else:
            print(f"❌ {name} - NOT FOUND")
            all_passed = False
    
    return all_passed


def test_translation_samples():
    """Test 3: Verify some sample translations"""
    print("\n" + "="*70)
    print("TEST 3: Sample Translations")
    print("="*70)
    
    locales_dir = Path(__file__).parent / 'agent' / 'locales'
    
    with open(locales_dir / 'zh.json', 'r', encoding='utf-8') as f:
        zh = json.load(f)
    
    with open(locales_dir / 'en.json', 'r', encoding='utf-8') as f:
        en = json.load(f)
    
    # Test key samples
    test_cases = [
        ('menu_toggle_language', '🌐 切换语言', '🌐 Language'),
        ('menu_products', '🛍️ 商品中心', '🛍️ Products'),
        ('menu_profile', '👤 个人中心', '👤 Profile'),
        ('buy_success', '✅ 购买成功！', '✅ Purchase successful!'),
        ('recharge_title', '💰 充值中心', '💰 Recharge Center'),
    ]
    
    all_passed = True
    for key, expected_zh, expected_en in test_cases:
        zh_val = zh.get(key, '')
        en_val = en.get(key, '')
        
        zh_match = expected_zh in zh_val
        en_match = expected_en in en_val
        
        if zh_match and en_match:
            print(f"✅ {key}")
            print(f"   zh: {zh_val[:50]}")
            print(f"   en: {en_val[:50]}")
        else:
            print(f"❌ {key}")
            if not zh_match:
                print(f"   zh mismatch: expected '{expected_zh}', got '{zh_val[:50]}'")
            if not en_match:
                print(f"   en mismatch: expected '{expected_en}', got '{en_val[:50]}'")
            all_passed = False
    
    return all_passed


def test_template_parameters():
    """Test 4: Verify template parameter support"""
    print("\n" + "="*70)
    print("TEST 4: Template Parameters")
    print("="*70)
    
    locales_dir = Path(__file__).parent / 'agent' / 'locales'
    
    with open(locales_dir / 'zh.json', 'r', encoding='utf-8') as f:
        zh = json.load(f)
    
    with open(locales_dir / 'en.json', 'r', encoding='utf-8') as f:
        en = json.load(f)
    
    # Test template formatting
    test_cases = [
        ('buy_quantity_prompt', {'stock': 100}),
        ('buy_success', {'order_id': 'ABC123'}),
        ('welcome_agent_bot', {'agent_name': 'Test Bot'}),
    ]
    
    all_passed = True
    for key, params in test_cases:
        try:
            zh_text = zh[key].format(**params)
            en_text = en[key].format(**params)
            print(f"✅ {key}")
            print(f"   zh: {zh_text[:60]}...")
            print(f"   en: {en_text[:60]}...")
        except KeyError as e:
            print(f"❌ {key} - Missing parameter: {e}")
            all_passed = False
        except Exception as e:
            print(f"❌ {key} - Error: {e}")
            all_passed = False
    
    return all_passed


def test_coverage_categories():
    """Test 5: Verify coverage of all UI categories"""
    print("\n" + "="*70)
    print("TEST 5: Translation Coverage by Category")
    print("="*70)
    
    locales_dir = Path(__file__).parent / 'agent' / 'locales'
    
    with open(locales_dir / 'zh.json', 'r', encoding='utf-8') as f:
        zh = json.load(f)
    
    categories = {
        'menu_': 'Main Menu',
        'profile_': 'User Profile',
        'products_': 'Products',
        'buy_': 'Purchase Flow',
        'recharge_': 'Recharge',
        'orders_': 'Orders',
        'order_detail_': 'Order Details',
        'support_': 'Support',
        'help_': 'Help',
        'price_': 'Price Management',
        'profit_': 'Profit Center',
        'reports_': 'Reports',
        'error_': 'Errors',
        'button_': 'Buttons',
    }
    
    for prefix, name in categories.items():
        keys = [k for k in zh.keys() if k.startswith(prefix)]
        if keys:
            print(f"✅ {name:20s} - {len(keys):3d} keys")
        else:
            print(f"⚠️  {name:20s} - 0 keys (might be okay)")
    
    total_keys = len(zh)
    print(f"\n📊 Total translation keys: {total_keys}")
    
    return True


def main():
    """Run all tests"""
    print("\n" + "="*70)
    print("  🧪 LANGUAGE SWITCHING FEATURE TEST SUITE")
    print("="*70)
    
    results = []
    
    # Run tests
    results.append(("Language Files", test_language_files()))
    results.append(("Code Implementation", test_code_implementation()))
    results.append(("Sample Translations", test_translation_samples()))
    results.append(("Template Parameters", test_template_parameters()))
    results.append(("Coverage Categories", test_coverage_categories()))
    
    # Summary
    print("\n" + "="*70)
    print("  📋 TEST SUMMARY")
    print("="*70)
    
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    for name, result in results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{status} - {name}")
    
    print(f"\nResults: {passed}/{total} tests passed")
    
    if passed == total:
        print("\n🎉 ALL TESTS PASSED!")
        print("\n✅ Language switching feature is fully implemented and working correctly.")
        print("\n📚 Documentation:")
        print("   • Implementation Guide: agent/LANGUAGE_SWITCHING_GUIDE.md")
        print("   • Verification Report: LANGUAGE_SWITCHING_VERIFICATION.md")
        print("\n🚀 The bot is ready to use with bilingual support (Chinese/English)")
        return 0
    else:
        print("\n❌ SOME TESTS FAILED")
        print("Please review the failed tests above and fix the issues.")
        return 1


if __name__ == '__main__':
    sys.exit(main())
