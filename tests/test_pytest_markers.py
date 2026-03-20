import pytest
#
# # @pytest.mark.smoke
# # def test_smoke_case():
# #     assert True
# #
# # @pytest.mark.regression
# # def test_regression_case():
# #     assert True
# #
# #
# # @pytest.mark.fast
# # def test_fast():
# #     pass
# #
# # @pytest.mark.slow
# # def test_slow():
# #     pass
# #
# # @pytest.mark.smoke
# # class TestSuite:
# #     def test_case1(self):
# #         pass
# #
# #     def test_case2(self):
# #         pass
# #
#
# @pytest.mark.regression
# class TestUserAuthentication:
#
#     @pytest.mark.smoke
#     def test_login(self):
#         pass
#
#     @pytest.mark.slow
#     def test_password_reset(self):
#         pass
#
#     def test_logout(self):
#         pass
#
# @pytest.mark.smoke
# @pytest.mark.regression
# @pytest.mark.critical
# def test_critical_login():
#     pass
#
# @pytest.mark.api
# class TestUserInterface:
#     @pytest.mark.smoke
#     @pytest.mark.critical
#     def test_login(self):
#         pass
#
#     @pytest.mark.regression
#     def test_forgot_password(self):
#         pass
#
#     @pytest.mark.smoke
#     def test_signup(self):
#         pass
#
# @pytest.mark.smoke
# class TestLogin:
#     @pytest.mark.smoke
#     def test_valid_login(self):
#         pass
#
#     @pytest.mark.regression
#     def test_invalid_login(self):
#         pass
#
# @pytest.mark.regression
# class TestRegistration:
#     @pytest.mark.regression
#     def test_valid_registration(self):
#         pass
#
#     @pytest.mark.smoke
#     def test_invalid_registration(self):
#         pass
#
# @pytest.mark.smoke
# @pytest.mark.regression
# class TestCheckout:
#     @pytest.mark.smoke
#     @pytest.mark.regression
#     def test_valid_checkout(self):
#         pass
#
#     def test_invalid_checkout(self):
#         pass
#
# def test_search():
#     pass