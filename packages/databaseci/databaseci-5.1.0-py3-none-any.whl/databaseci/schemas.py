from schemainspect import get_inspector


class Schemas:
    def inspect(self):
        with self._t_namedtuple() as t:

            t.q("create table t(id int);")
            i = get_inspector(t)

        return i
