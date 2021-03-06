from fixture import DataTestCase, SQLAlchemyFixture
from sqlalchemy import create_engine

from models import metadata, UserTable, RegionTable
from fixtures import RegionData, UserData

# import logging
# logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)

engine = create_engine('postgresql://postgres:@localhost/sqlagg_test')
metadata.bind = engine
metadata.create_all()


class BaseTest(DataTestCase):
    datasets = [UserData, RegionData]
    fixture = SQLAlchemyFixture(
        engine=metadata.bind,
        env={"UserData": UserTable, "RegionData": RegionTable})

    @classmethod
    def metadata(cls):
        return metadata
