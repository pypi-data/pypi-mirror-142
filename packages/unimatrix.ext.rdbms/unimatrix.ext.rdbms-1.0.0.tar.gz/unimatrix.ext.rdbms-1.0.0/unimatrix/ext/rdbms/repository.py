"""Declares :class:`Repository`."""
import typing

import sqlalchemy
from sqlalchemy.engine import Result
from sqlalchemy.exc import NoResultFound
from sqlalchemy.sql.dml import Delete
from sqlalchemy.sql.dml import Update
from sqlalchemy.sql.selectable import Select
from unimatrix.ext import rdbms


EXECUTABLE = typing.Union[Delete, Update, Select]
RESULT = typing.Union[Result]


class Repository:
    """Integrates the :term:`Repository Layer` with relational database systems
    using the :mod:`sqlalchemy` package. Implements :class:`ddd.Repository`.
    """
    #: Specifies the connection that is used by the repository implementation,
    #: as specified using the :mod:`unimatrix.ext.rdbms` framework.
    alias: str = 'self'

    async def commit(self) -> None:
        """Commit the current database transaction."""
        await self.__session.commit()

    async def get_tuple(self, query: EXECUTABLE):
        """Return a single tuple from the given query. The query is expected
        to yield exactly one tuple. Raises :class:`ddd.DoesNotExist` if there
        is no tuple matched by the predicate.
        """
        result = await self.execute(query)
        try:
            return result.one()
        except NoResultFound:
            raise self.DoesNotExist

    async def execute(self, query: EXECUTABLE) -> Result:
        """Execute the given `query` and return the result. Does not evaluate
        the result.
        """
        return await self.__session.execute(query)

    async def nextval(self, name: str) -> int:
        """Return the next value of sequence `name`."""
        result = await self.execute(sqlalchemy.func.nextval(name))
        return result.scalars().one()

    async def persist_declarative(self,
        dao,
        merge: bool = False,
        flush: bool = False
    ) -> 'dao':
        """Persist a declarative SQLAlchemy object."""
        if not merge:
            self.__session.add(dao)
        else:
            await self.__session.merge(dao)
        if flush:
            await self.__session.flush()
        return dao

    async def setup_context(self) -> 'self':
        self.__session = rdbms.session(self.alias)
        await self.__session.__aenter__()
        return self

    async def teardown_context(self, cls, exception, traceback) -> bool:
        await self.__session.__aexit__(cls, exception, traceback)
        self.__session = None
        return False

    def atomic(self):
        """Return a context manager wrapping the code in a database
        transaction.
        """
        return self.__session.begin()
