import time

def test_export_stock_onhand(page):
    # 1. Login
    page.goto("https://pj.maggio.seru.app/web/login")
    page.get_by_role("textbox", name="Email").fill("admin")
    page.get_by_role("textbox", name="Email").press("Tab")
    page.get_by_role("textbox", name="Password").fill("admin")
    page.get_by_role("button", name="Log in").click()
    page.wait_for_load_state("load")

    page.goto("https://pj.maggio.seru.app/web#action=114&active_id=mail.box_inbox&cids=1&menu_id=91")
    page.get_by_role("link").click()
    page.wait_for_load_state("load")

    # 2. Navigasi ke Laporan Stok Persediaan
    page.get_by_role("menuitem", name="Stok Persediaan").click()
    page.get_by_role("button", name="Laporan").click()
    page.get_by_role("menuitem", name="Laporan Stok Persediaan").click()
    page.wait_for_load_state("load")

    # 3. Set tanggal inventory
    page.get_by_role("button", name="Stok Persediaan pada Tanggal").click()
    date_field = page.get_by_role("textbox", name="Stok Persediaan pada Tanggal")
    date_field.click(click_count=3)
    date_field.fill("01/01/2026 00:00:05")
    page.get_by_role("button", name="Konfirmasi").click()
    page.wait_for_load_state("load")

    # 4. Group By: Created by
    page.get_by_role("button", name=" Dikelompokkan berdasarkan").click()
    page.get_by_role("button", name="Tambahkan Grup Kustom").click()
    page.get_by_role("combobox").select_option("create_uid")
    page.get_by_role("button", name="Terapkan").click()

    # 5. Filter: Cost > 0
    page.get_by_role("button", name=" Penyaring").click()
    page.get_by_role("button", name="Tambahkan Penyaring Sendiri").click()
    page.get_by_role("combobox").first.select_option("harga_jual")
    page.get_by_role("combobox").nth(1).select_option(">")
    page.get_by_role("button", name="Terapkan").click()

    # 6. Filter: Perkiraan Stok > 0
    page.get_by_role("button", name="Tambahkan Penyaring Sendiri").click()
    page.get_by_role("combobox").first.select_option("virtual_available")
    page.get_by_role("combobox").nth(1).select_option(">")
    page.get_by_role("button", name="Terapkan").click()
    page.wait_for_load_state("load")

    # 7. Filter: Created by = septa
    page.get_by_role("button", name="Tambahkan Penyaring Sendiri").click()
    page.get_by_role("combobox").first.select_option("create_uid")
    page.get_by_role("textbox").fill("septa")
    page.get_by_role("button", name="Terapkan").click()
    page.wait_for_load_state("load")

    # 8. Tunggu loading beres
    time.sleep(10)
    page.wait_for_selector(".blockUI.blockOverlay", state="hidden", timeout=60000)

    # Expand grup Septa
    page.locator(".o_group_name", has_text="Septa").click()
    time.sleep(5)
    page.wait_for_selector(".blockUI.blockOverlay", state="hidden", timeout=30000)
    page.evaluate("document.querySelector('th.o_list_record_selector input[type=checkbox]').click()")
    time.sleep(3)
    page.wait_for_selector(".o_list_selection_box", state="visible", timeout=30000)
    page.locator(".o_list_selection_box a").click()
    
    # 9. Export
    with page.expect_download() as download_info:
        page.get_by_role("button", name=" Tindakan").click()
        page.get_by_role("menuitemcheckbox", name="Ekspor").click()
        page.get_by_role("button", name="Ekspor").click()

    download = download_info.value
    download.save_as(f"stock_onhand_septa_{download.suggested_filename}")
    print("Downloaded:", download.suggested_filename)
    assert download.suggested_filename.endswith(".xlsx")