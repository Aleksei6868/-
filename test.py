import main
def test_check_order():
    main.post_new_order()
    main.check_order().status_code
    assert main.check_order().status_code == 200
