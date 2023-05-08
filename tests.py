import unittest
from stats import add_entry_to_stats, merge_stats


class TestTask1(unittest.TestCase):

    maxDiff = None

    def test_add_entry_to_stats(self):
        stats = {
            "count": 15,
            "amount": 425,
            "num_items": 12,
            "gender": {
                "F": {"count": 5, "amount": 225, "num_items": 7},
                "M": {"count": 10, "amount": 200, "num_items": 5},
            },
            "currency": {
                "EUR": {"count": 13, "amount": 175, "num_items": 6},
                "USD": {"count": 2, "amount": 250, "num_items": 6},
            },
        }

        entry = {
            "gender": "M",
            "amount": 17,
            "num_items": 2,
            "currency": "EUR",
            "week_of_year": 42,
            "country_code": "GB",
        }

        expected_stats = {
            "count": 16,
            "amount": 442,
            "num_items": 14,
            "gender": {
                "F": {"count": 5, "amount": 225, "num_items": 7},
                "M": {"count": 11, "amount": 217, "num_items": 7},
            },
            "currency": {
                "EUR": {"count": 14, "amount": 192, "num_items": 8},
                "USD": {"count": 2, "amount": 250, "num_items": 6},
            },
            "week_of_year": {42: {"count": 1, "amount": 17, "num_items": 2}},
            "country_code": {"GB": {"count": 1, "amount": 17, "num_items": 2}},
        }

        updated_stats = add_entry_to_stats(stats, entry)

        self.assertDictEqual(updated_stats, expected_stats)

    # test for adding new groups(new_group), currency(AED),
    # country_code(AE), week_of_year(13)
    def test_add_new_curr_group_country_code(self):
        stats = {
            "count": 16,
            "amount": 442,
            "num_items": 14,
            "gender": {
                "F": {"count": 5, "amount": 225, "num_items": 7},
                "M": {"count": 11, "amount": 217, "num_items": 7},
            },
            "currency": {
                "EUR": {"count": 14, "amount": 192, "num_items": 8},
                "USD": {"count": 2, "amount": 250, "num_items": 6},
            },
            "week_of_year": {42: {"count": 1, "amount": 17, "num_items": 2}},
            "country_code": {"GB": {"count": 1, "amount": 17, "num_items": 2}},
        }

        entry = {
            "gender": "F",
            "amount": 5,
            "num_items": 2,
            "currency": "AED",
            "week_of_year": 13,
            "country_code": "AE",
            "new_group": 3,
        }

        expected_stats = {
            "count": 17,
            "amount": 447,
            "num_items": 16,
            "gender": {
                "F": {"count": 6, "amount": 230, "num_items": 9},
                "M": {"count": 11, "amount": 217, "num_items": 7},
            },
            "currency": {
                "EUR": {"count": 14, "amount": 192, "num_items": 8},
                "USD": {"count": 2, "amount": 250, "num_items": 6},
                "AED": {"count": 1, "amount": 5, "num_items": 2}
            },
            "week_of_year": {
                42: {"count": 1, "amount": 17, "num_items": 2},
                13: {"count": 1, "amount": 5, "num_items": 2}},
            "country_code": {
                "GB": {"count": 1, "amount": 17, "num_items": 2},
                "AE": {"count": 1, "amount": 5, "num_items": 2}},
            "new_group": {3: {"count": 1, "amount": 5, "num_items": 2}},
        }

        updated_stats = add_entry_to_stats(stats, entry)

        self.assertDictEqual(updated_stats, expected_stats)

    # test case for adding new gender(not F or M). It is not clear for me
    # should our program allow adding new genders or not. If should allow, here
    # is the test case
    def test_add_new_gender(self):
        stats = {
            "count": 15,
            "amount": 425,
            "num_items": 12,
            "gender": {
                "F": {"count": 5, "amount": 225, "num_items": 7},
                "M": {"count": 10, "amount": 200, "num_items": 5},
            },
            "currency": {
                "EUR": {"count": 13, "amount": 175, "num_items": 6},
                "USD": {"count": 2, "amount": 250, "num_items": 6},
            },
        }

        entry = {
            "gender": "O",
            "amount": 17,
            "num_items": 2,
            "currency": "EUR",
            "week_of_year": 42,
            "country_code": "GB",
        }

        expected_stats = {
            "count": 16,
            "amount": 442,
            "num_items": 14,
            "gender": {
                "F": {"count": 5, "amount": 225, "num_items": 7},
                "M": {"count": 10, "amount": 200, "num_items": 5},
                "O": {"count": 1, "amount": 17, "num_items": 2},
            },
            "currency": {
                "EUR": {"count": 14, "amount": 192, "num_items": 8},
                "USD": {"count": 2, "amount": 250, "num_items": 6},
            },
            "week_of_year": {
                42: {"count": 1, "amount": 17, "num_items": 2},
            },
            "country_code": {
                "GB": {"count": 1, "amount": 17, "num_items": 2},
            },
        }

        updated_stats = add_entry_to_stats(stats, entry)

        self.assertDictEqual(updated_stats, expected_stats)

    # BUT if should not allow, here is another test case (it would be commented
    # and if necessary - uncomment it and delete previous test_add_new_gender
    # test. Also do not forget to uncomment the validation code in
    # add_entry_to_stats function

    # def test_add_invalid_gender(self):
    #     stats = {
    #         "count": 15,
    #         "amount": 425,
    #         "num_items": 12,
    #         "gender": {
    #             "F": {"count": 5, "amount": 225, "num_items": 7},
    #             "M": {"count": 10, "amount": 200, "num_items": 5},
    #         },
    #         "currency": {
    #             "EUR": {"count": 13, "amount": 175, "num_items": 6},
    #             "USD": {"count": 2, "amount": 250, "num_items": 6},
    #         },
    #     }
    #
    #     entry = {
    #         "gender": "O",
    #         "amount": 17,
    #         "num_items": 2,
    #         "currency": "EUR",
    #         "week_of_year": 42,
    #         "country_code": "GB",
    #     }
    #
    #     with self.assertRaises(ValueError):
    #         add_entry_to_stats(stats, entry)

    # One more commented test which checks if entry dict contains all of the
    # required keys or not. Uncomment it if necessary. Don't forget to
    # uncomment corresponding code in stats.py

    # def test_invalid_entry(self):
    #     stats = {
    #         "count": 15,
    #         "amount": 425,
    #         "num_items": 12,
    #         "gender": {
    #             "F": {"count": 5, "amount": 225, "num_items": 7},
    #             "M": {"count": 10, "amount": 200, "num_items": 5},
    #         },
    #         "currency": {
    #             "EUR": {"count": 13, "amount": 175, "num_items": 6},
    #             "USD": {"count": 2, "amount": 250, "num_items": 6},
    #         },
    #     }
    #
    #     entry = {
    #         "gender": "M",
    #         "amount": 17,
    #         "num_items": 2,
    #         "currency": "EUR",
    #         "week_of_year": 42,
    #     }
    #
    #     with self.assertRaises(ValueError):
    #         add_entry_to_stats(stats, entry)

    # test for adding the values to existing same values (again adding EUR and
    # county code GB and the same week_of_year and new_group with value 3)
    def test_adding_to_existing_groups(self):
        stats = {
            "count": 16,
            "amount": 442,
            "num_items": 14,
            "gender": {
                "F": {"count": 5, "amount": 225, "num_items": 7},
                "M": {"count": 11, "amount": 217, "num_items": 7},
            },
            "currency": {
                "EUR": {"count": 14, "amount": 192, "num_items": 8},
                "USD": {"count": 2, "amount": 250, "num_items": 6},
            },
            "week_of_year": {42: {"count": 1, "amount": 17, "num_items": 2}},
            "country_code": {"GB": {"count": 1, "amount": 17, "num_items": 2}},
            "new_group": {3: {"count": 1, "amount": 5, "num_items": 2}},
        }

        entry = {
            "gender": "M",
            "amount": 5,
            "num_items": 2,
            "currency": "EUR",
            "week_of_year": 42,
            "country_code": "GB",
            "new_group": 3,

        }

        expected_stats = {
            "count": 17,
            "amount": 447,
            "num_items": 16,
            "gender": {
                "F": {"count": 5, "amount": 225, "num_items": 7},
                "M": {"count": 12, "amount": 222, "num_items": 9},
            },
            "currency": {
                "EUR": {"count": 15, "amount": 197, "num_items": 10},
                "USD": {"count": 2, "amount": 250, "num_items": 6},
            },
            "week_of_year": {
                42: {"count": 2, "amount": 22, "num_items": 4},
                },
            "country_code": {
                "GB": {"count": 2, "amount": 22, "num_items": 4},
            },
            "new_group": {3: {"count": 2, "amount": 10, "num_items": 4}},
        }

        updated_stats = add_entry_to_stats(stats, entry)

        self.assertDictEqual(updated_stats, expected_stats)

    # test case where our entry is empty (in my opinion we should raise
    # the ValueError
    def test_add_empty_entry(self):
        stats = {
            "count": 17,
            "amount": 447,
            "num_items": 16,
            "gender": {
                "F": {"count": 5, "amount": 225, "num_items": 7},
                "M": {"count": 11, "amount": 217, "num_items": 7},
                "G": {"count": 1, "amount": 5, "num_items": 2},
            },
            "currency": {
                "EUR": {"count": 14, "amount": 192, "num_items": 8},
                "USD": {"count": 2, "amount": 250, "num_items": 6},
                "AED": {"count": 1, "amount": 5, "num_items": 2}
            },
            "week_of_year": {
                42: {"count": 1, "amount": 17, "num_items": 2},
                13: {"count": 1, "amount": 5, "num_items": 2}},
            "country_code": {
                "GB": {"count": 1, "amount": 17, "num_items": 2},
                "DBX": {"count": 1, "amount": 5, "num_items": 2}},
        }

        entry = {}

        with self.assertRaises(ValueError):
            add_entry_to_stats(stats, entry)

    # test case where our stats are empty (nothing exists in stats yet)
    def test_empty_stats(self):
        stats = {}

        entry = {
            "gender": "F",
            "amount": 5,
            "num_items": 2,
            "currency": "AED",
            "week_of_year": 13,
            "country_code": "DBX",
            "new_group": 3,
        }

        expected_stats = {
            "count": 1,
            "amount": 5,
            "num_items": 2,
            "gender": {
                "F": {"count": 1, "amount": 5, "num_items": 2},
            },
            "currency": {
                "AED": {"count": 1, "amount": 5, "num_items": 2}
            },
            "week_of_year": {
                13: {"count": 1, "amount": 5, "num_items": 2}},
            "country_code": {
                "DBX": {"count": 1, "amount": 5, "num_items": 2}},
            "new_group": {3: {"count": 1, "amount": 5, "num_items": 2}},
        }

        updated_stats = add_entry_to_stats(stats, entry)

        self.assertDictEqual(updated_stats, expected_stats)

    # test case if necessary to add some nested groups
    def test_nested_groups(self):
        stats = {}

        entry = {
            "gender": "M",
            "amount": 5,
            "num_items": 2,
            "currency": "AED",
            "week_of_year": 13,
            "country_code": "DBX",
            "new_group": 3,
            "something_deep.deeper.the_deepest.hidden_treasure": 41,
        }

        expected_stats = {
            "count": 1,
            "amount": 5,
            "num_items": 2,
            "gender": {
                "M": {"count": 1, "amount": 5, "num_items": 2},
            },
            "currency": {
                "AED": {"count": 1, "amount": 5, "num_items": 2}
            },
            "week_of_year": {
                13: {"count": 1, "amount": 5, "num_items": 2}},
            "country_code": {
                "DBX": {"count": 1, "amount": 5, "num_items": 2}},
            "new_group": {3: {"count": 1, "amount": 5, "num_items": 2}},
            "something_deep": {
                "deeper": {
                    "the_deepest": {
                        "hidden_treasure": {
                            41: {"count": 1, "amount": 5, "num_items": 2}}}}},
        }

        updated_stats = add_entry_to_stats(stats, entry)

        self.assertDictEqual(updated_stats, expected_stats)

    # single test for adding the new group
    def test_new_groups(self):
        stats = {}

        entry = {
            "gender": "M",
            "amount": 5,
            "num_items": 2,
            "currency": "AED",
            "week_of_year": 13,
            "country_code": "DBX",
            "brand_new_group": 55,
        }

        expected_stats = {
            "count": 1,
            "amount": 5,
            "num_items": 2,
            "gender": {
                "M": {"count": 1, "amount": 5, "num_items": 2},
            },
            "currency": {
                "AED": {"count": 1, "amount": 5, "num_items": 2}
            },
            "week_of_year": {
                13: {"count": 1, "amount": 5, "num_items": 2}},
            "country_code": {
                "DBX": {"count": 1, "amount": 5, "num_items": 2}},
            "brand_new_group": {55: {"count": 1, "amount": 5, "num_items": 2}},
        }

        updated_stats = add_entry_to_stats(stats, entry)

        self.assertDictEqual(updated_stats, expected_stats)


class TestTask2(unittest.TestCase):

    maxDiff = None

    def test_merge_stats(self):
        stats1 = {
            "count": 15,
            "amount": 425,
            "num_items": 12,
            "gender": {
                "F": {"count": 5, "amount": 225, "num_items": 7},
                "M": {"count": 10, "amount": 200, "num_items": 5},
            },
            "currency": {
                "EUR": {"count": 13, "amount": 175, "num_items": 6},
                "USD": {"count": 2, "amount": 250, "num_items": 6},
            },
        }

        stats2 = {
            "count": 15,
            "amount": 425,
            "num_items": 12,
            "gender": {
                "F": {"count": 5, "amount": 225, "num_items": 7},
                "M": {"count": 10, "amount": 200, "num_items": 5},
            },
            "currency": {
                "EUR": {"count": 13, "amount": 175, "num_items": 6},
                "USD": {"count": 2, "amount": 250, "num_items": 6},
            },
            "something_deep": {"deeper": {"the_deepest": {
                "hidden_treasure": 41}}},
            "empty_object": {},
        }

        stats3 = {
            "count": 15,
            "amount": 450,
            "num_items": 12,
            "something_else": 30,
            "gender": {
                "F": {"count": 5, "amount": 225, "num_items": 7},
                "M": {"count": 10, "amount": 200, "num_items": 5},
            },
            "currency": {
                "EUR": {"count": 13, "amount": 175, "num_items": 6},
                "USD": {"count": 2, "amount": 250, "num_items": 6},
            },
            "country_code": {"GB": {"count": 2, "amount": 10, "num_items": 2}},
            "something_deep": {"deeper": {"the_deepest": {
                "hidden_treasure": 1}}},
            "empty_object": {},
        }

        expected_stats = {
            "count": 45,
            "amount": 1300,
            "num_items": 36,
            "something_else": 30,
            "gender": {
                "F": {"count": 15, "amount": 675, "num_items": 21},
                "M": {"count": 30, "amount": 600, "num_items": 15},
            },
            "currency": {
                "EUR": {"count": 39, "amount": 525, "num_items": 18},
                "USD": {"count": 6, "amount": 750, "num_items": 18},
            },
            "country_code": {"GB": {"count": 2, "amount": 10, "num_items": 2}},
            "something_deep": {"deeper": {"the_deepest": {
                "hidden_treasure": 42}}},
            "empty_object": {},
        }

        merged_stats = merge_stats(stats1, stats2, stats3)

        self.assertDictEqual(merged_stats, expected_stats)

    # test for merging empty stats
    def test_merge_stats_empty_dict(self):
        stats1 = {}
        stats2 = {}
        stats3 = {}
        expected_stats = {}

        merged_stats = merge_stats(stats1, stats2, stats3)

        self.assertDictEqual(merged_stats, expected_stats)

    # test case when in one of the stats dict missing key, which exists in
    # other stats dicts
    def test_merge_stats_missing_keys(self):
        stats1 = {
            "count": 10,
            "amount": 100,
        }

        stats2 = {
            "count": 20,
            "num_items": 5,
        }

        stats3 = {
            "count": 30,
            "currency": {
                "EUR": {"count": 10},
            }
        }
        expected_stats = {
            "count": 60,
            "amount": 100,
            "num_items": 5,
            "currency": {
                "EUR": {"count": 10}
            },
        }

        merged_stats = merge_stats(stats1, stats2, stats3)

        self.assertDictEqual(merged_stats, expected_stats)

    # test case when we have only one stats dict for some reasons
    def test_merge_stats_single_dict(self):
        stats = {
            "count": 10,
            "amount": 100,
            "num_items": 5,
            "gender": {
                "F": {"count": 3, "amount": 30, "num_items": 2},
                "M": {"count": 7, "amount": 70, "num_items": 3},
            },
            "currency": {
                "EUR": {"count": 5, "amount": 50, "num_items": 3},
            }
        }

        expected_stats = {
            "count": 10,
            "amount": 100,
            "num_items": 5,
            "gender": {
                "F": {"count": 3, "amount": 30, "num_items": 2},
                "M": {"count": 7, "amount": 70, "num_items": 3},
            },
            "currency": {
                "EUR": {"count": 5, "amount": 50, "num_items": 3},
            }
        }

        merged_stats = merge_stats(stats)

        self.assertDictEqual(merged_stats, expected_stats)

    # test case when we have nothing to merge
    def test_empty_input(self):

        merged_stats = merge_stats()

        self.assertDictEqual(merged_stats, {})

    # test case when we provide non dict stats (raise TypeError)
    def test_merge_stats_with_non_dict_inputs(self):
        stats1 = ["count", 10, "amount", 100]

        stats2 = {"count": 20, "num_items": 5}

        stats3 = ("count", "currency", 60)

        with self.assertRaises(TypeError):
            merge_stats(stats1, stats2, stats3)

    # test case when we have a list as a value in our stats
    def test_merge_list_value(self):
        stats1 = {
            "count": 10,
            "amount": 100,
            "num_items": 5,
            "gender": {
                "F": {"count": 3, "amount": 30, "num_items": 2},
                "M": {"count": 7, "amount": 70, "num_items": 3},
            },
            "currency": {
                "EUR": {"count": 5, "amount": 50, "num_items": 3},
            }
        }

        stats2 = {
            "count": 20,
            "num_items": 5,
            "some_new": [1, 2, 3]
        }

        expected_stats = {
            "count": 30,
            "amount": 100,
            "num_items": 10,
            "gender": {
                "F": {"count": 3, "amount": 30, "num_items": 2},
                "M": {"count": 7, "amount": 70, "num_items": 3},
            },
            "currency": {
                "EUR": {"count": 5, "amount": 50, "num_items": 3},
            },
            "some_new": [1, 2, 3]
        }

        merged_stats = merge_stats(stats1, stats2)

        self.assertDictEqual(merged_stats, expected_stats)


if __name__ == "__main__":
    unittest.main()
