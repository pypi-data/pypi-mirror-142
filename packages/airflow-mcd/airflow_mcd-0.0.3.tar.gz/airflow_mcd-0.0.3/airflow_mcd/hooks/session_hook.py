from airflow import AirflowException

try:
    from airflow.hooks.base import BaseHook

    HOOK_SOURCE = None
except ImportError:
    # For Airflow 1.10.*
    from airflow.hooks.base_hook import BaseHook

    HOOK_SOURCE = 'mcd_session'
from pycarlo.core import Session


class SessionHook(BaseHook):
    def __init__(self, mcd_session_conn_id: str):
        """
        MCD Session Hook. Retrieves connection details from the Airflow `Connection` object.

        The `mcd_id` can be configured via the connection "login", and the `mcd_token` via the connection "password".

        Alternatively, either `mcd_id` or `mcd_token` can be configured in the connection "extra", with values passed
        via "login" or "password" taking precedence.
        {
            "mcd_id": "foo",
            "mcd_token": "bar"
        }

        :param mcd_session_conn_id: Connection ID for the MCD session.
        """
        self.mcd_session_conn_id = mcd_session_conn_id

        super().__init__(**(dict(source=HOOK_SOURCE) if HOOK_SOURCE is not None else {}))

    def get_conn(self) -> Session:
        """
        Gets a connection for the hook.

        :return: MCD access session.
        """
        connection = self.get_connection(self.mcd_session_conn_id)
        connection_extra = connection.extra_dejson
        try:
            return Session(
                mcd_id=connection.login or connection_extra['mcd_id'],
                mcd_token=connection.password or connection_extra['mcd_token'],
                **(dict(endpoint=connection.host) if connection.host else {})
            )
        except KeyError as err:
            raise AirflowException(f'Missing expected key {err} from connection extra.')
