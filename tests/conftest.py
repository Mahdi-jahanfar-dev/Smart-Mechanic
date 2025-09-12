from pytest import fixture
from fastapi.testclient import TestClient
from core.database_config import create_engine, SessionLocal, sessionmaker, Base, get_db
from core.config import settings
from sqlalchemy.pool import StaticPool
from core.main import app


# override memory db
@fixture(scope="module")
def overrided_memory_db():

    engine = create_engine(
        settings.TEST_DATABASE_URL,
        connect_args={"check_same_thread": False},
        # define memory db
        poolclass=StaticPool,
    )

    Base.metadata.create_all(engine)

    return engine


# test client instance
@fixture(scope="module")
def client_instance(overrided_memory_db):

    SessionLocal = sessionmaker(
        bind=overrided_memory_db, autoflush=False, autocommit=False
    )

    # db instance
    def override_db():

        db = SessionLocal()

        try:
            yield db
        finally:
            db.close()

    # overriding dependency
    app.dependency_overrides[get_db] = override_db

    # test client instance
    client = TestClient(app)

    return client
