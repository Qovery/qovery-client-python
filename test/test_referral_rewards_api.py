"""
    Qovery API

    - Qovery is the fastest way to deploy your full-stack apps on any Cloud provider. - ℹ️ The API is stable and still in development.   # noqa: E501

    The version of the OpenAPI document: 1.0.3
    Contact: support+api+documentation@qovery.com
    Generated by: https://openapi-generator.tech
"""


import unittest

import qovery
from qovery.api.referral_rewards_api import ReferralRewardsApi  # noqa: E501


class TestReferralRewardsApi(unittest.TestCase):
    """ReferralRewardsApi unit test stubs"""

    def setUp(self):
        self.api = ReferralRewardsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_account_referral(self):
        """Test case for get_account_referral

        Get your referral information  # noqa: E501
        """
        pass

    def test_post_account_reward_claim(self):
        """Test case for post_account_reward_claim

        Claim a reward  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
