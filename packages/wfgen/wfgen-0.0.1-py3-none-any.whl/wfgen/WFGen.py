import json
import logging
import os
import time
from argparse import Action
from datetime import datetime

import requests
from sqlalchemy import exc
from sqlmodel import Session, SQLModel, create_engine, null, select

from src.wfgen.WFGenModels import Action, MetaSynchro, Request, User


class WFGen:
    LOGLEVEL = os.environ.get("LOGLEVEL", "WARNING").upper()
    logging.basicConfig(
        encoding="utf-8",
        level=LOGLEVEL,
        format="%(asctime)s\t%(levelname)s\t%(message)s",
    )

    def __init__(self):
        engine = create_engine(
            f"postgresql://{os.environ['DATABASE_USER']}:{os.environ['DATABASE_PASSWORD']}@{os.environ['DATABASE_SERVER']}:5432/{os.environ['DATABASE_NAME']}"
        )
        SQLModel.metadata.create_all(engine)
        self.session = Session(engine)

    def make_graph_request(self, query: str = "", variables: dict = {}):
        """Function to standardize requests made to the GraphQL API.

        Args:
            query (str): The query to send to the API.
            variables (dict): Variables to pass to the query.
        """
        base_url = "https://vm-wfgen-prod-0/wfgen/graphql"

        headers = {
            "Authorization": f"Basic {os.environ['WFGEN_AUTH']}",
            "Content-Type": "application/json",
        }

        response = requests.request(
            "GET",
            base_url,
            headers=headers,
            json={"query": query, "variables": variables},
            verify=False,
        )
        return json.loads(response.text)

    def import_requests(
        self, page_number: int = 1, page_size: int = 3000, incremental: bool = True
    ):
        """Import all requests from WFGen.

        Args:
            page_number (int, optional): The number of the page to start from.
            page_size (int, optional): How much requests to return per page.
            incremental (bool, optional): Run in incremental mode or not.
        """
        query = """
        query($pageNumber: Int, $pageSize: Int){
            requests(page: {number: $pageNumber, size: $pageSize}) {
                totalCount
                hasNextPage
                items {
                id
                number
                description
                openedAt
                status
                closedAt
                requester {
                    id
                }
                actions {
                    items {
                    id
                    status
                    description
                    closedAt
                    openedAt
                    updatedAt
                    limit
                    assignee {
                        userName
                    }          
                    }
                }
                dataset(filter: {names: ["INITIATEUR_TYPE_OPPORTUNITE", "INITIATEUR_GRAVITE", "DEMANDE_NUMERO_COMMANDE", "DEMANDE_DATE_COMMANDE", "DEMANDE_NOM_CLIENT", "DEMANDE_ARTICLE", "DEMANDE_DESIGNATION", "DEMANDE_POINT_EXPEDITION1", "DEMANDE_CHAUFFEUR", "DEMANDE_REPRESENTANT", "DEMANDE_CONSEILLER", "DEMANDE_ESPECE_ARTICLE", "DEMANDE_COMMENTAIRES", "MISE_A_JOUR_CAT_SOUS_CATEGORIE", "TRAITEMENT_FINAL_CATEGORIE_SOUS_CAT111", "DEMANDE_CATEGORIE_SOUS_CAT11", "DEMANDE_DOCUMENT_CREER_PAR", "TRAITEMENT_FINAL_MONTANT"]}) {
                    items {
                    description
                    name
                    textValue
                    id
                    }
                }
                }
            }
            }        
        """
        next_page = True

        # If incremental is enabled, check the database for the last page requested and start from there
        if incremental:
            statement = select(MetaSynchro).where(MetaSynchro.id == "Requests")
            results = self.session.exec(statement)
            last_request = results.first()
            if last_request is not None:
                page_number = last_request.lastPageNumber
                page_size = last_request.lastPageSize

        while next_page:
            query_variables = {"pageNumber": page_number, "pageSize": page_size}
            requests = self.make_graph_request(query, query_variables)
            total_count = requests["data"]["requests"]["totalCount"]
            logging.info(
                f"Getting Requests page {page_number} of {round(total_count/page_size)} with {page_size} values"
            )

            for request in requests["data"]["requests"]["items"]:
                dataset = request["dataset"]["items"]
                typeOpportunite = null
                gravite = null
                numeroCommande = null
                dateEvenement = null
                nomClient = null
                noArticle = null
                designationArticle = null
                pointExpedition = null
                chauffeur = null
                representant = null
                conseiller = null
                espece = null
                detailsDemande = null
                catSousCat = null
                catSousCatReel = null
                catSousCat2 = null
                doumentCreerPar = null
                montant = null

                # In WFGen, custom data are stored in a dataset for each request.
                for data in dataset:
                    if data["name"] == "INITIATEUR_TYPE_OPPORTUNITE":
                        typeOpportunite = data["textValue"]
                    if data["name"] == "INITIATEUR_GRAVITE":
                        gravite = data["textValue"]
                    if data["name"] == "DEMANDE_NUMERO_COMMANDE":
                        numeroCommande = data["textValue"]
                    if data["name"] == "DEMANDE_DATE_COMMANDE":
                        dateEvenement = data["textValue"]
                    if data["name"] == "DEMANDE_NOM_CLIENT":
                        nomClient = data["textValue"]
                    if data["name"] == "DEMANDE_ARTICLE":
                        noArticle = data["textValue"]
                    if data["name"] == "DEMANDE_DESIGNATION":
                        designationArticle = data["textValue"]
                    if data["name"] == "DEMANDE_POINT_EXPEDITION1":
                        pointExpedition = data["textValue"]
                    if data["name"] == "DEMANDE_CHAUFFEUR":
                        chauffeur = data["textValue"]
                    if data["name"] == "DEMANDE_REPRESENTANT":
                        representant = data["textValue"]
                    if data["name"] == "DEMANDE_CONSEILLER":
                        conseiller = data["textValue"]
                    if data["name"] == "DEMANDE_ESPECE_ARTICLE":
                        espece = data["textValue"]
                    if data["name"] == "DEMANDE_COMMENTAIRES":
                        detailsDemande = data["textValue"]
                    if data["name"] == "MISE_A_JOUR_CAT_SOUS_CATEGORIE":
                        catSousCat = data["textValue"]
                    if data["name"] == "TRAITEMENT_FINAL_CATEGORIE_SOUS_CAT111":
                        catSousCatReel = data["textValue"]
                    if data["name"] == "DEMANDE_CATEGORIE_SOUS_CAT11":
                        catSousCat2 = data["textValue"]
                    if data["name"] == "DEMANDE_DOCUMENT_CREER_PAR":
                        doumentCreerPar = data["textValue"]
                    if data["name"] == "TRAITEMENT_FINAL_MONTANT":
                        montant = data["textValue"]

                request_obj = Request(
                    id=request["id"],
                    number=request["number"],
                    description=request["description"],
                    status=request["status"],
                    openedAt=request["openedAt"],
                    closedAt=request["closedAt"],
                    requesterId=request["requester"]["id"],
                    typeOpportunite=typeOpportunite,
                    gravite=gravite,
                    numeroCommande=numeroCommande,
                    dateEvenement=dateEvenement,
                    nomClient=nomClient,
                    noArticle=noArticle,
                    designationArticle=designationArticle,
                    pointExpedition=pointExpedition,
                    chauffeur=chauffeur,
                    representant=representant,
                    conseiller=conseiller,
                    espece=espece,
                    detailsDemande=detailsDemande,
                    catSousCat=catSousCat,
                    catSousCatReel=catSousCatReel,
                    catSousCat2=catSousCat2,
                    doumentCreerPar=doumentCreerPar,
                    montant=montant,
                )
                self.session.add(request_obj)
                try:
                    logging.info(f"Saved Request id {request['id']} to database")
                    self.session.commit()
                except exc.IntegrityError as e:
                    logging.debug(f"Request {request['id']}\t{e.orig.pgerror}")
                    self.session.rollback()
                    continue

            meta = MetaSynchro(
                id="Requests",
                lastPageNumber=page_number,
                lastPageSize=page_size,
                lastRun=datetime.now(),
                lastId=request["id"],
            )
            self.session.merge(meta)
            self.session.commit()

            next_page = requests["data"]["requests"]["hasNextPage"]
            if next_page:
                page_number += 1

    def import_actions(
        self, page_number: int = 1, page_size: int = 3000, incremental: bool = True
    ):
        """Import all actions from WFGen.

        Args:
            page_number (int, optional): The number of the page to start from.
            page_size (int, optional): How much actions to return per page.
            incremental (bool, optional): Run in incremental mode or not.
        """
        query = """
            query ($pageNumber: Int, $pageSize: Int) {
                actions(page: {number: $pageNumber, size: $pageSize}) {
                    totalCount
                    hasNextPage
                    items {
                        id
                        name
                        description
                        status
                        openedAt
                        closedAt
                        limit
                        request {
                            id
                            number
                        }
                        dataset(filter: {names: ["DEMANDE_COMMENTAIRES", "ENQUETE_COMMENTAIRES", "RE_ENQUETE_COMMENTAIRES", "LABORATOIRE_COMMENTAIRES", "NUTRITION_COMMENTAIRES", "MISE_A_JOUR_COMMENTAIRES", "TRAITEMENT_FINAL_COMMENTAIRES", "APPROB_DIR_RECLAMATION_COMMENTAIRES", "APPROB_DIR_RETOUR_COMMENTAIRES"]}) {
                            items {
                                name
                                description
                                textValue
                            }
                        }
                    }
                }
            }
        """
        next_page = True

        # If incremental is enabled, check the database for the last page requested and start from there
        if incremental:
            statement = select(MetaSynchro).where(MetaSynchro.id == "Actions")
            results = self.session.exec(statement)
            last_action = results.first()
            if last_action is not None:
                page_number = last_action.lastPageNumber
                page_size = last_action.lastPageSize

        while next_page:
            query_variables = {"pageNumber": page_number, "pageSize": page_size}
            actions = self.make_graph_request(query, query_variables)
            total_count = actions["data"]["actions"]["totalCount"]
            logging.info(
                f"Getting Actions page {page_number} of {round(total_count/page_size)} with {page_size} values"
            )

            for action in actions["data"]["actions"]["items"]:
                try:
                    comments = action["dataset"]["items"][0]["textValue"]
                except IndexError as e:
                    comments = null

                action_obj = Action(
                    id=action["id"],
                    name=action["name"],
                    description=action["description"],
                    openedAt=action["openedAt"],
                    closedAt=action["closedAt"],
                    limit=action["limit"],
                    requestId=action["request"]["id"],
                    comments=comments,
                )
                self.session.add(action_obj)
                try:
                    self.session.commit()
                    logging.info(f"Saved Action id {action['id']} to database")
                except exc.IntegrityError as e:
                    logging.debug(f"Action {action['id']}\t{e.orig.pgerror}")
                    self.session.rollback()
                    continue

            meta = MetaSynchro(
                id="Actions",
                lastPageNumber=page_number,
                lastPageSize=page_size,
                lastRun=datetime.now(),
                lastId=action["id"],
            )
            self.session.merge(meta)
            self.session.commit()

            next_page = actions["data"]["actions"]["hasNextPage"]
            if next_page:
                page_number += 1

    def import_users(self, page_number: int = 1, page_size: int = 3000):
        """Import all users from WFGen.

        Args:
            page_number (int, optional): The number of the page to start from.
            page_size (int, optional): How much users to return per page.
        """

        query = """
        query($pageNumber: Int, $pageSize: Int){
            users(page: {number: $pageNumber, size: $pageSize}){
                totalCount
                hasNextPage
                    items{
                        id
                        firstName
                        lastName
                        userName
                        email
                        isActive
                        department                   
                }
            }
        }
        """
        query_variables = {"pageNumber": page_number, "pageSize": page_size}
        users = self.make_graph_request(query, query_variables)
        total_count = users["data"]["users"]["totalCount"]

        logging.info(
            f"Getting Users page {page_number} of {round(total_count/page_size)} with {page_size} values"
        )

        for user in users["data"]["users"]["items"]:
            user_obj = User(
                id=user["id"],
                firstName=user["firstName"],
                lastName=user["lastName"],
                userName=user["userName"],
                email=user["email"],
                isActive=user["isActive"],
                department=user["department"],
            )
            self.session.merge(user_obj)
            logging.info(f"User with id {user['id']} saved to the database")
        try:
            self.session.commit()
            logging.info(f"Saved {total_count} Users to database")
        except Exception as e:
            logging.debug(f"Some error occured while downloading users")
            self.session.rollback()
            pass

    def close_session(self):
        """Close SQLAlchemy session."""
        self.session.close()

    def import_all(self, incremental: bool = True):
        """Import users, requests and actions from WFGen.

        Args:
            incremental (bool, optional): Run in incremental mode or not.
        """
        self.import_users()
        self.import_requests()
        self.import_actions()
        self.close_session()


if __name__ == "__main__":
    wfgen = WFGen()
    wfgen.import_all()
