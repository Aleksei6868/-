import main
# Горшков Алексей, 9-я когорта — Финальный проект. Инженер по тестированию плюс
def test_check_order():
    main.post_new_order()
    main.check_order().status_code
    assert main.check_order().status_code == 200
