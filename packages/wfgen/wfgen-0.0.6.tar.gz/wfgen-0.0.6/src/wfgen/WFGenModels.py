from datetime import date, datetime
from typing import Optional

from sqlmodel import Field, SQLModel


class Request(SQLModel, table=True):
    id: str = Field(default=None, primary_key=True)
    number: int
    description: Optional[str]
    status: Optional[str]
    openedAtUTC: Optional[datetime]
    closedAtUTC: Optional[datetime]
    requesterId: Optional[str] = Field(default=None, foreign_key="user.id")
    typeOpportunite: Optional[str]
    gravite: Optional[str]
    numeroCommande: Optional[str]
    dateEvenement: Optional[date]
    nomClient: Optional[str]
    noArticle: Optional[str]
    designationArticle: Optional[str]
    pointExpedition: Optional[str]
    chauffeur: Optional[str]
    representant: Optional[str]
    conseiller: Optional[str]
    espece: Optional[str]
    detailsDemande: Optional[str]
    catSousCat: Optional[str]
    catSousCatReel: Optional[str]
    catSousCat2: Optional[str]
    doumentCreerPar: Optional[str]
    montant: Optional[str]


class User(SQLModel, table=True):
    id: str = Field(default=None, primary_key=True)
    firstName: Optional[str]
    lastName: Optional[str]
    userName: str
    email: Optional[str]
    isActive: bool
    department: Optional[str]


class Action(SQLModel, table=True):
    id: str = Field(default=None, primary_key=True)
    name: str
    description: str
    openedAtUTC: Optional[datetime]
    closedAtUTC: Optional[datetime]
    limit: Optional[str]
    requestId: str = Field(default=None, foreign_key="request.id")
    assigneeId: Optional[str] = Field(default=None, foreign_key="user.id")
    comments: Optional[str]


class MetaSynchro(SQLModel, table=True):
    id: str = Field(default=None, primary_key=True)
    lastPageNumber: Optional[int]
    lastPageSize: Optional[int]
    lastRunUTC: Optional[datetime]
    lastId: Optional[str]
