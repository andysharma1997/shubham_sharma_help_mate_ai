from contextvars import ContextVar,Token

REQUEST_ID_CTX_KEY = "request_id"
ORG_ID_CTX_KEY = 'org_id'
MEETING_ID_CTX_KEY = 'meeting_id'



class ContextMiddelware:
    
    _request_id_ctx_var: ContextVar[str] = ContextVar(REQUEST_ID_CTX_KEY, default=None)
    
    @staticmethod
    def get_request_id() -> str:
        return ContextMiddelware._request_id_ctx_var.get()
    
    @staticmethod
    def set_request_id(value: str) -> Token:
        return ContextMiddelware._request_id_ctx_var.set(value)
    
    @staticmethod
    def reset_request_id(token: Token) -> None:
        ContextMiddelware._request_id_ctx_var.reset(token)
    
