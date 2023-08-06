from unittest import TestCase
from unittest.mock import patch

from airflow import AirflowException
from airflow.models import Connection
from pycarlo.core import Session

from airflow_mcd.hooks import SessionHook

SAMPLE_ID = 'foo'
SAMPLE_TOKEN = 'bar'
SAMPLE_CONN_ID = 'mcd_default_session'
SAMPLE_EXTRA = {'mcd_id': SAMPLE_ID, 'mcd_token': SAMPLE_TOKEN}
SAMPLE_CONNECTION = Connection(extra=SAMPLE_EXTRA)


class SessionHookTest(TestCase):
    def setUp(self) -> None:
        self._session = SessionHook(mcd_session_conn_id=SAMPLE_CONN_ID)

    def test_session_id_is_set(self):
        self.assertEqual(self._session.mcd_session_conn_id, SAMPLE_CONN_ID)

    @patch('airflow_mcd.hooks.session_hook.Session')
    @patch.object(SessionHook, 'get_connection')
    def test_get_conn(self, get_connection_mock, session_mock):
        expected_session = Session(mcd_id=SAMPLE_ID, mcd_token=SAMPLE_TOKEN)
        get_connection_mock.return_value = SAMPLE_CONNECTION
        session_mock.return_value = expected_session

        self.assertEqual(self._session.get_conn(), expected_session)
        get_connection_mock.assert_called_once_with(SAMPLE_CONN_ID)
        session_mock.assert_called_once_with(mcd_id=SAMPLE_ID, mcd_token=SAMPLE_TOKEN)

    @patch('airflow_mcd.hooks.session_hook.Session')
    @patch.object(SessionHook, 'get_connection')
    def test_get_conn_with_login_and_password(self, get_connection_mock, session_mock):
        login = 'foo'
        password = 'qux'
        connection = Connection(login=login, password=password)
        expected_session = Session(mcd_id=login, mcd_token=password)

        get_connection_mock.return_value = connection
        session_mock.return_value = expected_session

        self.assertEqual(self._session.get_conn(), expected_session)
        get_connection_mock.assert_called_once_with(SAMPLE_CONN_ID)
        session_mock.assert_called_once_with(mcd_id=login, mcd_token=password)

    @patch.object(SessionHook, 'get_connection')
    def test_get_conn_with_missing_extra(self, get_connection_mock):
        get_connection_mock.return_value = Connection()

        with self.assertRaises(AirflowException) as context:
            self._session.get_conn()
        self.assertEqual(str(context.exception), 'Missing expected key \'mcd_id\' from connection extra.')
