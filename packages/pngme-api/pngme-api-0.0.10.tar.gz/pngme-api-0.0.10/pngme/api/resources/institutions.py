from typing import List

from pydantic import BaseModel

from ..core import BaseClient
from ..types import AccountType, Currency

PATH = "/users/{user_uuid}/institutions"


class InstitutionNames(BaseModel):
    name: str
    display_name: str


class Institution(BaseModel):
    institution_id: str
    institution: InstitutionNames
    currency: Currency
    account_types: List[AccountType]


class InstitutionsMeta(BaseModel):
    user_uuid: str
    client_uuid: str


class InstitutionsResponse(BaseModel):
    meta: InstitutionsMeta
    institutions: List[Institution]

    class Config:
        fields = {"meta": "_meta"}


class BaseInstitutionsResource:
    def __init__(self, client: BaseClient):
        self._client = client

    async def _get(self, user_uuid: str) -> List[Institution]:
        async with self._client.session() as session:
            response = await session.get(PATH.format(user_uuid=user_uuid))

        assert response.status_code == 200, response.text
        return InstitutionsResponse(**response.json()).institutions


class AsyncInstitutionsResource(BaseInstitutionsResource):
    async def get(self, user_uuid: str) -> List[Institution]:
        return await self._get(user_uuid)


class SyncInstitutionsResource(BaseInstitutionsResource):
    def get(self, user_uuid: str) -> List[Institution]:
        return self._client.run(self._get(user_uuid))
