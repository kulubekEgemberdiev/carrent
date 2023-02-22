# from django.test import TestCase
#
# from agreement.models import Agreement, Service
#
#
# class AgreementsTest(TestCase):
#     @classmethod
#     def setUpTestData(cls):
#         super().setUpTestData()
#         cls.agr = Agreement.objects.create(
#             registration_date='2023-02-16',
#             reserve_id=2,
#             total=25000,
#             total_summ=26000,
#             territory_of_use='Бишкек'
#         )
#
#     # def test_verbose_name(self):
#     #     agr = AgreementsTest.agr
#     #     field_verboses = {'territory_of_use': 'Территория использования ТС'}
#     #     for field, expected_value in field_verboses.items():
#     #         with self.subTest(field=field):
#     #             self.assertEqual(
#     #                 agr._meta.get_field(field).verbose_name, expected_value)
