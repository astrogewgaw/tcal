import sys
import pandas as pd
import sqlalchemy as db

from pathlib import Path
from tabulate import tabulate

from tcal.consts import *


class TCAL(object):
    def __init__(self):

        """"""

        self.dbname = ".".join([PKGNAME, "db"])
        self.dbpath = "/".join([SQLPREFIX, str(DBMPATH), self.dbname])
        self.engine = db.create_engine(self.dbpath)
        self.metadata = db.MetaData()

        self.table = db.Table(
            PKGNAME, self.metadata, autoload=True, autoload_with=self.engine
        )

    def load(self):

        """"""

        with self.engine.connect() as connect:

            query = db.select([self.table])
            proxy = connect.execute(query)
            result = proxy.fetchall()

            df = pd.DataFrame(result)
            df.columns = DFHEADER

        return df

    def update(self):

        """"""

        with self.engine.connect() as connect:

            data = pd.read_csv(UPLINK, header=SKIPLINES)
            data.columns = DBHEADER

            data.to_sql(PKGNAME, connect, if_exists="replace", index=False)

    def save(self, filename, fmt="csv"):

        """"""

        df = self.load()

        if fmt == ".csv":

            df.to_csv(filename, index=False)

        elif fmt == ".xlsx":

            df.to_excel(filename)

        elif fmt == ".md":

            mddf = df.copy(deep=True)

            rows = []
            for index, row in mddf.iterrows():
                rows.append(row["Twitter Handle"])

            mdrows = []
            for row in rows:
                if row:
                    rmrow = row.replace("@", "")
                    link = "".join([TWITTERLINK, rmrow])
                    template = "[{}]({})"
                    mdlink = template.format(row, link)
                    row = mdlink
                mdrows.append(row)

            mddf["Twitter Handle"] = mdrows

            mark = tabulate(
                mddf, headers=df.columns, showindex=False, tablefmt="github"
            )

            with open(filename, "w+") as outfile:
                outfile.write(mark)

    def search(self, name, position, institute):

        """"""

        with self.engine.connect() as connect:

            conds = []

            if not any([name, position, institute]):

                query = db.select([self.table])
                proxy = connect.execute(query)
                results = proxy.fetchall()

            else:

                if name:

                    namesearch = "%{}%".format(name)
                    conds.append(self.table.columns.name.like(namesearch))

                if position:

                    if position == "None":

                        pass

                    elif position == "Other":

                        conditionals = [
                            (self.table.columns.position.like("%Undergrad%")),
                            (self.table.columns.position.like("%Grad%")),
                            (self.table.columns.position.like("%Postdoc%")),
                            (self.table.columns.position.like("%Professor%")),
                        ]

                        cond = db.not_(db.or_(*conditionals))

                        conds.append(cond)

                    else:

                        posisearch = "%{}%".format(position)

                        conds.append(self.table.columns.position.like(posisearch))

                if institute:

                    instisearch = "%{}%".format(institute)
                    conds.append(self.table.columns.institute.like(instisearch))

                conditional = db.and_(*conds)

                query = db.select([self.table]).where(conditional)
                proxy = connect.execute(query)
                results = proxy.fetchall()

            header = DFHEADER

        return [results, header]
