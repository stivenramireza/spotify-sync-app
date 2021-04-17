from pydantic import BaseModel
from fastapi import Form


class Account(BaseModel):
    oauth_token_1: str = Form(...)
    oauth_token_2: str = Form(...)

    @classmethod
    def as_form(cls, oauth_token_1: str = Form(...), oauth_token_2: str = Form(...)):
        return cls(oauth_token_1=oauth_token_1, oauth_token_2=oauth_token_2)
