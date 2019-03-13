import os

from iconsdk.builder.call_builder import CallBuilder
from iconsdk.builder.transaction_builder import DeployTransactionBuilder, CallTransactionBuilder
from iconsdk.libs.in_memory_zip import gen_deploy_data_content
from iconsdk.signed_transaction import SignedTransaction
from tbears.libs.icon_integrate_test import IconIntegrateTestBase, SCORE_INSTALL_ADDRESS

DIR_PATH = os.path.abspath(os.path.dirname(__file__))


class TestInterfaceExercise(IconIntegrateTestBase):
    TEST_HTTP_ENDPOINT_URI_V3 = "http://127.0.0.1:9000/api/v3"
    SCORE_PROJECT = os.path.abspath(os.path.join(DIR_PATH, '..'))
    WORKSHOP_PROJECT = os.path.abspath(os.path.join(DIR_PATH, '../../workshop_exercise'))

    def setUp(self):
        super().setUp()

        self.icon_service = None
        # if you want to send request to network, uncomment next line and set self.TEST_HTTP_ENDPOINT_URI_V3
        # self.icon_service = IconService(HTTPProvider(self.TEST_HTTP_ENDPOINT_URI_V3))

        # install SCORE

        self._workshop_score = self._deploy_score(self.WORKSHOP_PROJECT)['scoreAddress']
        params = {"_scoreAddress": self._workshop_score}
        self._score_address = self._deploy_score(project=self.SCORE_PROJECT, params=params)['scoreAddress']

    def tearDown(self):
        print("-"*180)

    def _deploy_score(self, project, params: dict = None, to: str = SCORE_INSTALL_ADDRESS) -> dict:
        # Generates an instance of transaction for deploying SCORE.
        transaction = DeployTransactionBuilder() \
            .from_(self._test1.get_address()) \
            .to(to) \
            .step_limit(100_000_000_000) \
            .nid(3) \
            .nonce(100) \
            .content_type("application/zip") \
            .content(gen_deploy_data_content(project)) \
            .params(params) \
            .build()

        # Returns the signed transaction object having a signature
        signed_transaction = SignedTransaction(transaction, self._test1)

        # process the transaction in local
        tx_result = self.process_transaction(signed_transaction, self.icon_service)

        self.assertTrue('status' in tx_result)
        self.assertEqual(1, tx_result['status'])
        self.assertTrue('scoreAddress' in tx_result)

        return tx_result

    def test_score_update(self):
        # update SCORE
        tx_result = self._deploy_score(project=self.SCORE_PROJECT, to=self._score_address)
        print("Update")

        self.assertEqual(self._score_address, tx_result['scoreAddress'])

    def test_call_hello(self):
        # Generates a call instance using the CallBuilder
        call = CallBuilder().from_(self._test1.get_address()) \
            .to(self._score_address) \
            .method("interfaceScoreExercise") \
            .build()

        # Sends the call request
        response = self.process_call(call, self.icon_service)
        print(response)

        self.assertEqual("Hello", response)

    def test_get_status(self):
        call = CallBuilder().from_(self._test1.get_address()) \
            .to(self._score_address) \
            .method("getScoreStatus") \
            .build()

        # Sends the call request
        response = self.process_call(call, self.icon_service)
        print(response)

    def test_time_recording(self):
        call = CallBuilder().from_(self._test1.get_address()) \
            .to(self._score_address) \
            .method("getTimeRecording") \
            .build()

        # Sends the call request
        response = self.process_call(call, self.icon_service)
        print(response)

    def test_modify_status(self):
        params = {"_scoreName": "Modified SCORE Name",
                  "_introduction": "Modified Introduction"}
        transaction = CallTransactionBuilder() \
            .method("modifyScoreStatus") \
            .params(params) \
            .step_limit(10000000000) \
            .to(self._score_address) \
            .build()

        signed_transaction = SignedTransaction(transaction, self._test1)
        self.process_transaction(signed_transaction)

        self.test_get_status()
        self.test_time_recording()
