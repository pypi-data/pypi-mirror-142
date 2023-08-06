from datetime import datetime
from json import dumps
from typing import List, Optional

from pydantic import BaseModel, validator, NonNegativeFloat


def custom_dumps(args, *, default):
    for k, v in args.items():
        if isinstance(v, datetime):
            args[k] = v.strftime('%Y-%m-%d')
    return dumps(args, default=default)


class OperationItems(BaseModel):
    calculationDate: datetime
    isCalculationCommitted: bool
    contrAgentId: Optional[int]
    operationCategoryId: Optional[int]
    projectId: Optional[int]
    firstAdditionalOperationAttributeId: Optional[int]
    value: NonNegativeFloat

    class Config:
        json_dumps = custom_dumps

    @validator('projectId', 'operationCategoryId')
    def check_for_zero_ids(cls, v):
        if v == 0:
            return None
        else:
            return v


class IncomeOutcomeOperation(BaseModel):
    operationDate: datetime
    calculationDate: Optional[datetime]
    isCalculationCommitted: Optional[bool]
    contrAgentId: Optional[int]
    accountId: int
    operationCategoryId: Optional[int]
    comment: Optional[str]
    value: Optional[NonNegativeFloat]
    isCommitted: Optional[bool]
    items: Optional[List[OperationItems]]
    externalId: Optional[str]
    distributeCalculationDate: Optional[datetime]
    distributeCalculationType: Optional[str]

    class Config:
        json_dumps = custom_dumps


class MoveOperation(BaseModel):
    """
    valueByProjects: object     Сумма по проектам  not implemented!
    """
    debitingDate: datetime  # Дата списания
    admissionDate: datetime  # Дата зачисления
    debitingAccountId: int  # Счет списания
    admissionAccountId: int  # Счет зачисления
    debitingValue: Optional[NonNegativeFloat]  # Сумма списания
    admissionValue: Optional[NonNegativeFloat]  # Сумма зачисления
    comment: Optional[str]  # Комментарий
    isCommitted: Optional[bool]  # Признак того, что операция проведена
    importLogId: Optional[int]  # Идентификатор лога импорта
    debitingItems: Optional[List[OperationItems]]  # Части операции списания
    admissionItems: Optional[List[OperationItems]]  # Части операции зачисления
    debitingExternalId: Optional[str]  # Внешний идентификатор для списания
    admissionExternalId: Optional[str]  # Внешний идентификатор для зачисления

    class Config:
        json_dumps = custom_dumps

    def set_to_committed(self):
        self.isCommitted = True
        for item in self.debitingItems or []:
            item.isCalculationCommitted = True
            item.calculationDate = self.debitingDate
        for item in self.admissionItems or []:
            item.isCalculationCommitted = True
            item.calculationDate = self.admissionDate


class Account(BaseModel):
    title: str
    companyId: int
    accountType: str
    currencyCode: str
    longTitle: Optional[str]
    description: Optional[str]
    accountType: Optional[str]
    accountAcct: Optional[str]
    correspondentAcct: Optional[str]
    accountBik: Optional[str]
    accountBank: Optional[str]
    active: Optional[bool]
    remainder: Optional[float]
    remainderDate: datetime
    externalId: Optional[str]
    accountGroupId: Optional[int]


class AccountLink(BaseModel):
    accountId: int
    companyId: int
    externalId: Optional[str]
    title: Optional[str]


class CompanyLinkModel(BaseModel):
    companyId: int
    externalId: Optional[str]
    title: Optional[str]


class CurrencyLinkModel(BaseModel):
    currencyCode: str
    title: Optional[str]


class OperationCategoryLinkModel(BaseModel):
    operationCategoryId: int
    title: Optional[str]
    externalId: Optional[str]


class ProjectLinkModel(BaseModel):
    projectId: int
    title: Optional[str]
    externalId: Optional[str]


class ContrAgentLinkModel(BaseModel):
    contrAgentId: int
    title: Optional[str]
    externalId: Optional[str]


class OperationPartModel(BaseModel):
    isCalculationCommitted: bool
    project: Optional[ProjectLinkModel]
    contrAgent: Optional[ContrAgentLinkModel]
    operationCategory: Optional[OperationCategoryLinkModel]
    value: float
    valueInUserCurrency: float


class OperationModel(BaseModel):
    account: AccountLink
    accountCompany: CompanyLinkModel
    accountCurrency: CurrencyLinkModel
    boundMoveOperationId: Optional[int]
    comment: Optional[str]
    isCommitted: Optional[bool]
    operationCategory: OperationCategoryLinkModel
    operationId: int
    operationParts: List[OperationPartModel]
    operationType: str
    value: float
    valueInUserCurrency: float
