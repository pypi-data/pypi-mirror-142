__all__ = ['DeleteTableResponse', 'DeleteTableError']

from ayradb.rest.http.response import Response
import re
from dataclasses import dataclass


class DeleteTableError:
    # Request errors (local)
    INVALID_FIELD_NAME = -1
    # AyraDB errors
    TABLE_NOT_FOUND = 1
    INTERNAL_ERROR = 100


ERROR_DICT = {
    "ERROR: [00005]:(00002): TFA_QDADRTBL_0002: the table does not exist":DeleteTableError.TABLE_NOT_FOUND,
    # Errors that shouldn't happen since they are internally managed
    "ERROR: [00016]:(00002): TFA_EEPA_018: endpoint action can't be done with this request method": DeleteTableError.INTERNAL_ERROR,
}


@dataclass
class DeleteTableResponse:

    _SEPARATOR = b'\x3b'
    success: bool
    error_code: int
    _error_msg: str

    def __init__(self, success, error_code, _error_msg=""):
        self.success = success
        self.error_code = error_code
        self._error_msg = _error_msg

    @staticmethod
    def from_http_response(res: Response):
        if res.status_code == 200:
            return DeleteTableResponse(True, 0)
        else:
            # Case error returned by ayra
            _error_msg = ""
            success = False
            error = res.body.decode('ascii')
            # Search for server name inside error message
            match = re.search(r'^(([\s\S])+(?=(ERROR)))', error)
            if match is not None:
                # Case server name present in error
                error = error[match.end():]  # Remove server name from error
            internal_error = DeleteTableError.INTERNAL_ERROR
            try:
                error_code = ERROR_DICT[error]
            except KeyError:
                error_code = internal_error
            if error_code == internal_error:
                _error_msg = error
                # TODO: save in a log file

            return DeleteTableResponse(success, error_code, _error_msg=_error_msg)
