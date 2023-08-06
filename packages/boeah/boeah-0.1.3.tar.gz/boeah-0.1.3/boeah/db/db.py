from abc import ABC, abstractmethod


class Grammar(ABC):

    @abstractmethod
    def compile(self):
        raise NotImplementedError


class SelectGrammar(Grammar):
    basic_clauses = []
    alias_clauses = []

    def __init__(self, basic_clauses=None):
        self.basic_clauses = basic_clauses

    def compile(self):
        compiled = ', '.join(self.basic_clauses)
        return f'SELECT {compiled}'


class FromGrammar(Grammar):
    table: str = None

    def __init__(self, table):
        self.table = table

    def compile(self):
        return f'FROM {self.table}'


class WhereGrammar(Grammar):
    """
    claouses = [{
        'column': '',
        'operator': '', # =, >, >=, <, <=,
        'values': ''
    }]
    """

    __allowed_operator = (
        '=',
        '!=',
        '<>',
        '>',
        '>=',
        '<',
        '<=',
        'IN',
        'LIKE'
    )

    clauses = []

    def __init__(self, and_clauses=None):
        self.and_clauses = and_clauses

    def compile(self):
        compiled = []
        for clause in self.and_clauses:
            column = clause['column']
            operator = clause['operator']
            if isinstance(clause['value'], str):
                value = "'" + clause['value'] + "'"
            else:
                value = clause['value']
            compiled.append(f'{column} {operator} {value}')

        return 'WHERE ' + ' AND '.join(compiled)


class Collection:
    def __init__(self, db):
        self.db = db

    def __call__(self, *args, **kwargs):
        return self.db

    def where(self, *args, **kwargs):
        self.db.where(**kwargs)
        return self

    def to_sql(self):
        select = (SelectGrammar(basic_clauses=self.db.__select__)).compile()
        table = (FromGrammar(table=self.db.__table__)).compile()
        where = (WhereGrammar(and_clauses=self.db.__where__)).compile()
        return f'{select} {table} {where}'

    @property
    def sql(self):
        return self.to_sql()


class DB:
    """
    DB.table('customers').select('a', 'b')
        .where()
        .group_by()
        .order_by()

    """

    __table__: str
    __select__ = ['*']

    # Store the where clause. It will contain dictionary {'column', 'operator', 'value'}
    __where__ = []

    def __init__(self):
        pass

    @staticmethod
    def table(table):
        db = DB()
        db.__table__ = table
        _select = db._compile_select()
        query = f'SELECT {_select} FROM {db.__table__}'
        return Collection(db)

    def select(self):
        """
        .select('a', 'b', 'c') -> SELECT a, b, c FROM ...
        .select('a, b, c') -> SELECT a, b, c FROM ...
        .select('a').select('b') -> SELECT a, b

        .select('a', as='abjad') -> SELECT a AS abjad
        .select({
            'a': 'abjad'
        }, 'b', 'c, d') -> SELECT a AS abjad, b, c, d


        .select(DB.raw('count(*)')) -> SELECT COUNT(*)
        .select(DB.count('*')) -> SELECT COUNT(*)
        .select('a', distinct=True) -> SELECT DISTINCT a
        :return:
        """
        return Collection

    def _compile_select(self):
        return ', '.join(self.__select__)

    def where(self, *args, **kwargs):
        """
        .where(a=1) -> WHERE a = 1
        .where(a=1, b=2) -> WHERE a = 1 AND b = 2
        .where(a=1).where(b=2) -> WHERE a = 1 AND b = 2
        .where(a=[1,2,3]) -> WHERE a IN (1,2,3)
        .where(a__gte=9) -> WHERE a >= 9
        .where('a', '>=', 9) -> WHERE a >= 9
        .where(DB.raw("email LIKE '%:val'", 'mamam'))
        .where(email__begins_with='x') -> WHERE email LIKE 'x%'
        .where(email__ends_with='y') -> WHERE email LIKE '%y'
        .where(email__contains='z') -> WHERE email LIKE '%z%'

        .where(a | b)

        .orWhere(c=2) -> OR c = 2
        .whereNone(d) -> WHERE d IS NULL
        .whereNotNone() -> WHERE d IS NOT NULL
        .whereBetween('price', [1, 9]) -> WHERE price BETWEEN 1 AND 9
        .whereExists(...)  # subquery
        :return:
        """
        for kwarg in kwargs:
            self.__where__.append({
                'column': kwarg,
                'operator': '=',
                'value': kwargs[kwarg]
            })
        return Collection(self)

    def group_by(self):
        """
        .group_by('id') -> GROUP BY id
        .group_by('id', 'name') -> GROUP BY id, name
        .group_by('id, name') -> GROUP BY id, name
        .group_by('id').group_by('name') -> GROUP BY id, name

        :return:
        """
        return Collection

    def order_by(self):
        """
        .order_by('name') -> ORDER BY name ASC
        .order_by('-name') -> ORDER BY name DESC
        .order_by('name', '-birth_at') -> ORDER BY name ASC, birth_at DESC
        .order_by('name, -birth_at') -> ORDER BY name ASC, birth_at DESC

        :return:
        """
        return Collection

    def having(self):
        """
        .having(DB.count('id'), '>=', 1) -> HAVING COUNT(*) >= 1
        :return:
        """
        return Collection

    def join(self):
        """
        .join('developers', on='developers.user_id = users.id', ) -> INNER JOIN developers ON developers.user_id = users.id
        :return:
        """
        return Collection

    def take(self):
        """
        .take(10) -> LIMIT 10
        :return:
        """
        pass

    def pluck(self):
        """
        .pluck('name') -> SELECT name FROM ...
        :return:
        """
        pass
