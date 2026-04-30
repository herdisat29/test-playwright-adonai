# Playwright Automation Test - Odoo Adonai

Automation test suite untuk sistem Odoo menggunakan Playwright Python + pytest.

## Tech Stack
- Python 3.11
- Playwright
- pytest

## Struktur Project
pages/          → Page Object Model classes
tests/          → Test files
conftest.py     → pytest configuration

## Test Cases
| No | Test | Status |
|----|------|--------|
| TC01 | Login sukses | ✅ |
| TC02 | Login gagal (kredensial salah) | ✅ |
| TC03 | Verifikasi halaman dashboard setelah login | ✅ |
| TC04 | Logout | ✅ |

## Cara Jalanin
```bash
pip install pytest-playwright
playwright install chromium
pytest tests/ -v --headed
```