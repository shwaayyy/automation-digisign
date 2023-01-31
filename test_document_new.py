import time

from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.support.select import Select

from object import *

doc = doc_object
form = form_object
mail = mail_object


def delay(sec):
    time.sleep(sec)


def test_web1_1(driver, **kwargs):
    """Unggah Dokumen PDF"""
    is_pdf = kwargs.get('exe', 'pdf')
    seal = kwargs.get('seal', False)

    if seal is False:
        form.username(driver).send_keys("ditest6@tandatanganku.com" + Keys.ENTER)
        delay(2)
        form.password(driver).send_keys("Coba1234" + Keys.ENTER)
        delay(4)
    else:
        form.username(driver).send_keys("wahyuhi" + Keys.ENTER)
        delay(2)
        form.password(driver).send_keys("Kijang321!" + Keys.ENTER)
        delay(4)
        doc.choose_account(driver).click()

    delay(3)
    if is_pdf == "pdf":
        form.doc_file(driver).send_keys("D:\\repository\\try\\PyTest-dev\\src\\file\\report.pdf")
    else:
        form.doc_file(driver).send_keys("D:\\repository\\try\\PyTest-dev\\src\\file\\image.jpeg")
    delay(4)
    form.doc_submit(driver).click()
    delay(2)


def test_web1_2(driver):
    """Unggah Dokumen selain PDF"""
    test_web1_1(driver, exe="img")


def test_web2_1_1(driver, **kwargs):
    """Pengaturan dokumen yang ingin dikirim sesuai"""
    is_next = kwargs.get('is_next', False)
    is_not_locked = kwargs.get('is_not_locked', False)
    test_web1_1(driver)

    doc.button_add_me(driver).click()
    doc.btn_detail_doc(driver).click()

    if is_next is True:
        if is_not_locked is True:
            doc.btn_add_sign(driver).click()

        doc.btn_send_doc(driver).click()
        delay(1)
        doc.btn_process_send_doc(driver).click()

        try:
            assert doc.icon_x_swal(driver) is not None
        except Exception as error:
            print(error)

        delay(1)
        doc.button_swal_confirm_ok(driver).click()
    else:
        try:
            assert doc.canvas(driver) is not None
        except Exception as error:
            print(error)
        delay(2)


def test_web2_1_2(driver):
    """Pengaturan dokumen yang ingin dikirim tidak sesuai ( sudah lewat dari tanggal sekarang )"""
    test_web1_1(driver)

    doc.btn_choose_expired_date(driver).click()

    for i in range(6):
        doc.btn_previous_month_date(driver).click()
        delay(1)

    doc.date(driver).click()
    doc.button_ok_date(driver).click()

    try:
        assert doc.icon_x_swal(driver) is not None
        delay(3)
    except Exception as error:
        print(error)

    delay(1)


def test_web2_2_1(driver, **kwargs):
    """Tidak isi form penerima dokumen"""
    is_filled = kwargs.get('is_filled', False)
    test_web1_1(driver)

    if is_filled is True:
        doc.name_first_receiver(driver).send_keys("wahyu")
        doc.email_first_receiver(driver).send_keys("ditest6@tandatanganku.com")

    doc.btn_detail_doc(driver).click()
    delay(2)

    if is_filled is False:
        try:
            assert doc.err_name_receiver(driver) is not None
            assert doc.err_email_receiver(driver) is not None
            delay(3)
        except Exception as err:
            print(err)
    else:
        try:
            assert doc.canvas(driver) is not None
            delay(3)
        except Exception as err:
            print(err)


def test_web2_2_2(driver):
    """Isi form penerima dokumen"""
    test_web2_2_1(driver, is_filled=True)


def test_web_2_2_3(driver):
    """isi form penerima dokumen dengan nama kosong"""
    test_web1_1(driver)

    doc.email_first_receiver(driver).send_keys("ditest6@tandatanganku.com")
    doc.btn_detail_doc(driver).click()

    try:
        assert doc.err_name_receiver(driver) is not None
        delay(3)
    except Exception as err:
        print(err)

    delay(2)


def test_web_2_2_4(driver):
    """isi form penerima dokumen dengan spasi saja"""
    test_web1_1(driver)

    doc.name_first_receiver(driver).send_keys(" ")
    doc.email_first_receiver(driver).send_keys("ditest6@tandatanganku.com")
    doc.btn_detail_doc(driver).click()

    try:
        assert doc.err_name_receiver(driver) is not None
        delay(3)
    except Exception as err:
        print(err)

    delay(2)


def test_web2_2_5(driver):
    """isi form email penerima kosong"""
    test_web1_1(driver)

    doc.name_first_receiver(driver).send_keys("wahyu")

    doc.btn_detail_doc(driver).click()
    delay(2)

    try:
        assert doc.err_email_receiver(driver) is not None
        delay(3)
    except Exception as err:
        print(err)


def test_web2_2_6(driver):
    """isi form email penerima dengan format email salah"""
    test_web1_1(driver)

    doc.name_first_receiver(driver).send_keys("wayy")
    doc.email_first_receiver(driver).send_keys("ditest28")

    doc.btn_detail_doc(driver).click()
    delay(2)

    try:
        assert doc.err_email_receiver(driver) is not None
        delay(3)
    except Exception as error:
        print(error)


def test_web2_3_1(driver):
    """Mengatur tanda tangan Sesuai urutan dengan urutan dibutuhkan tandatangan di awal"""
    test_web1_1(driver)

    doc.label_sort_sign(driver).click()
    doc.button_add_me(driver).click()

    doc.btn_detail_doc(driver).click()
    delay(2)

    try:
        assert doc.canvas(driver) is not None
        delay(3)
    except Exception as err:
        print(err)


def test_web2_3_2(driver, **kwargs):
    """Mengatur tanda tangan Sesuai urutan dengan urutan dibutuhkan pengecekan di akhir"""
    select = kwargs.get('select', "Dibutuhkan Pengecekan")
    seal = kwargs.get('seal', False)
    test_web1_1(driver, seal=seal)

    doc.button_add_me(driver).click()
    doc.label_sort_sign(driver).click()

    if select is "Dibutuhkan Tandatangan":
        Select(doc.select_action_need(driver)).select_by_visible_text("Dibutuhkan Pengecekan")
    else:
        pass

    doc.button_add_receiver(driver).click()
    doc.input_name_receiver_2(driver).send_keys("Aziz")
    doc.input_email_receiver_2(driver).send_keys("aziz@digi-id.id")

    if select is "Dibutuhkan Tandatangan":
        doc.btn_detail_doc(driver).click()
        delay(2)
        try:
            assert doc.canvas(driver) is not None
            delay(3)
        except Exception as err:
            raise err
    elif select is "Dibutuhkan Pengecekan":
        Select(doc.select_action_need_2(driver)).select_by_visible_text(select)
        doc.btn_detail_doc(driver).click()
        delay(2)
        try:
            assert doc.icon_x_swal(driver) is not None
            delay(3)
        except Exception as e:
            raise e


def test_web2_3_3(driver, **kwargs):
    """Mengatur tanda tangan Sesuai urutan dengan urutan dibutuhkan pengecekan di awal"""
    seal = kwargs.get('seal', False)
    test_web2_3_2(driver, select="Dibutuhkan Tandatangan", seal=seal)


def test_web2_3_4(driver, **kwargs):
    """Memilih tindakan dibutuhkan paraf"""
    is_full = kwargs.get('full', False)
    is_corp = kwargs.get('corp', False)
    test_web1_1(driver, seal=is_corp)

    doc.email_first_receiver(driver).send_keys("ditest6@tandatanganku.com")
    doc.name_first_receiver(driver).send_keys("digi")
    Select(doc.select_action_need(driver)).select_by_visible_text("Dibutuhkan Paraf")

    doc.btn_detail_doc(driver).click()

    if is_full is True:
        doc.button_paraf(driver).click()
        delay(2)
        ActionChains(driver).drag_and_drop_by_offset(doc.paraf_box(driver), 10, 100).perform()

        doc.lock_paraf_1(driver).click()
        doc.btn_set_email(driver).click()
        doc.btn_send_doc(driver).click()
        doc.btn_process_send_doc(driver).click()

        doc.confirm_after_send_doc(driver).click()

        delay(5)
    else:
        try:
            assert doc.canvas(driver) is not None
            delay(2)
        except Exception as err:
            print(err)

        delay(2)


def test_web2_4_1(driver):
    """Tidak menentukan lokasi Paraf pada dokumen"""
    test_web2_3_4(driver)

    doc.btn_send_doc(driver).click()
    doc.btn_process_send_doc(driver).click()

    try:
        assert doc.sign_null(driver) is not None
    except Exception as err:
        print(err)

    delay(5)


def test_web2_4_2(driver):
    """penentuan lokasi paraf"""
    test_web2_3_4(driver, corp=True)


def test_web2_5_1(driver):
    """Memilih tindakan untuk seal Dokumen"""
    test_web1_1(driver, seal=True)

    Select(doc.select_email_seal(driver)).select_by_visible_text("wahyu@digi-id.id")
    delay(2)

    doc.button_add_me(driver).click()
    doc.btn_detail_doc(driver).click()

    try:
        assert doc.canvas(driver) is not None
    except Exception as err:
        print(err)

    delay(2)


def test_web2_5_2(driver):
    """Tidak menentukan lokasi segel pada dokumen"""
    test_web2_5_1(driver)

    doc.btn_send_doc(driver).click()
    doc.btn_process_send_doc(driver).click()

    try:
        assert doc.sign_null(driver) is not None
        delay(3)
    except Exception as err:
        print(err)

    delay(5)


def test_web2_5_3(driver):
    """Penentuan lokasi segel pada dokumen"""
    test_web2_5_1(driver)

    ActionChains(driver).drag_and_drop_by_offset(doc.imgsealer(driver), 100, 100).perform()
    delay(3)

    doc.button_lockseal(driver).click()
    doc.btn_send_doc(driver).click()
    doc.btn_process_send_doc(driver).click()

    doc.confirm_after_send_doc(driver).click()

    delay(5)


