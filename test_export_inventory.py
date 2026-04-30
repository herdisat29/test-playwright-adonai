def test_export_inventory_excel(page):
    # 1. Login
    page.goto("https://pj.maggio.seru.app/web#action=login")
    page.fill("#login", "admin")
    page.fill("#password", "admin")
    page.click("button[type='submit']")
    page.wait_for_load_state("load")

    page.goto("https://pj.maggio.seru.app/web#action=114&active_id=mail.box_inbox&cids=1&menu_id=91")
    page.get_by_role("link").click()
    page.wait_for_load_state("load")

    # 2. Klik menu Inventory
    page.get_by_role("menuitem", name="Stok Persediaan").click()
    page.wait_for_load_state("load")

    # 3. Klik menu Reporting
    page.get_by_role("button", name="Laporan").click()
    page.get_by_role("menuitem", name="Specific Inventory Report").click()
    page.get_by_role("textbox", name="Date To").click()
    page.get_by_role("textbox", name="Date To").press("ArrowRight")
    page.get_by_role("textbox", name="Date To").fill("31/12/2025")
    page.get_by_role("textbox", name="Date To").press("Enter")
    page.get_by_text("Specific Inventory Report ×").click()
    page.get_by_role("textbox", name="Location").click()
    page.get_by_role("textbox", name="Location").fill("pkyn")
    page.get_by_role("textbox", name="Location").press("Enter")
    
    # 6. Download Excel
    with page.expect_download() as download_info:
        page.get_by_role("button", name="Print Excel").click()

    download = download_info.value
    download.save_as(f"inventory_PKYN_{download.suggested_filename}")
    print("File downloaded:", download.suggested_filename)
    assert download.suggested_filename.endswith(".xls")