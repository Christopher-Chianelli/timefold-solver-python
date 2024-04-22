from ._function_translator import function_cast
from typing import TypeVar, Callable, Generic, Collection, Any, TYPE_CHECKING, Type

if TYPE_CHECKING:
    import jpype.imports
    from ai.timefold.solver.core.api.score import Score as _JavaScore
    from ai.timefold.solver.core.api.score.stream import Constraint as _JavaConstraint
    from ai.timefold.solver.core.api.score.stream.uni import UniConstraintBuilder as _JavaUniConstraintBuilder
    from ai.timefold.solver.core.api.score.stream.bi import BiConstraintBuilder as _JavaBiConstraintBuilder
    from ai.timefold.solver.core.api.score.stream.tri import TriConstraintBuilder as _JavaTriConstraintBuilder
    from ai.timefold.solver.core.api.score.stream.quad import QuadConstraintBuilder as _JavaQuadConstraintBuilder


A = TypeVar('A')
B = TypeVar('B')
C = TypeVar('C')
D = TypeVar('D')
ScoreType = TypeVar('ScoreType', bound='_JavaScore')


class UniConstraintBuilder(Generic[A, ScoreType]):
    delegate: '_JavaUniConstraintBuilder[A, ScoreType]'
    a_type: Type[A]

    def __init__(self, delegate: '_JavaUniConstraintBuilder[A, ScoreType]',
                 a_type: Type[A]) -> None:
        self.delegate = delegate
        self.a_type = a_type

    def indict_with(self, indictment_function: Callable[[A], Collection]) -> 'UniConstraintBuilder[A, ScoreType]':
        return UniConstraintBuilder(self.delegate.indictWith(
            function_cast(indictment_function, self.a_type)), self.a_type)

    def justify_with(self, justification_function: Callable[[A, ScoreType], Any]) -> \
            'UniConstraintBuilder[A, ScoreType]':
        return UniConstraintBuilder(self.delegate.justifyWith(
            function_cast(justification_function, self.a_type)), self.a_type)

    def as_constraint(self, constraint_package_or_name: str, constraint_name: str = None) -> '_JavaConstraint':
        if constraint_name is None:
            return self.delegate.asConstraint(constraint_package_or_name)
        else:
            return self.delegate.asConstraint(constraint_package_or_name, constraint_name)


class BiConstraintBuilder(Generic[A, B, ScoreType]):
    delegate: '_JavaBiConstraintBuilder[A, B, ScoreType]'
    a_type: Type[A]
    b_type: Type[B]

    def __init__(self, delegate: '_JavaBiConstraintBuilder[A, B, ScoreType]',
                 a_type: Type[A], b_type: Type[B]) -> None:
        self.delegate = delegate
        self.a_type = a_type
        self.b_type = b_type

    def indict_with(self, indictment_function: Callable[[A, B], Collection]) -> 'BiConstraintBuilder[A, B, ScoreType]':
        return BiConstraintBuilder(self.delegate.indictWith(
            function_cast(indictment_function, self.a_type, self.b_type)), self.a_type, self.b_type)

    def justify_with(self, justification_function: Callable[[A, B, ScoreType], Any]) -> \
            'BiConstraintBuilder[A, B, ScoreType]':
        return BiConstraintBuilder(self.delegate.justifyWith(
            function_cast(justification_function, self.a_type, self.b_type)), self.a_type, self.b_type)

    def as_constraint(self, constraint_package_or_name: str, constraint_name: str = None) -> '_JavaConstraint':
        if constraint_name is None:
            return self.delegate.asConstraint(constraint_package_or_name)
        else:
            return self.delegate.asConstraint(constraint_package_or_name, constraint_name)


class TriConstraintBuilder(Generic[A, B, C, ScoreType]):
    delegate: '_JavaTriConstraintBuilder[A, B, C, ScoreType]'
    a_type: Type[A]
    b_type: Type[B]
    c_type: Type[C]

    def __init__(self, delegate: '_JavaTriConstraintBuilder[A, B, C, ScoreType]',
                 a_type: Type[A], b_type: Type[B], c_type: Type[C]) -> None:
        self.delegate = delegate
        self.a_type = a_type
        self.b_type = b_type
        self.c_type = c_type

    def indict_with(self, indictment_function: Callable[[A, B, C], Collection]) -> \
            'TriConstraintBuilder[A, B, C, ScoreType]':
        return TriConstraintBuilder(self.delegate.indictWith(
            function_cast(indictment_function, self.a_type, self.b_type, self.c_type)), self.a_type, self.b_type,
                                    self.c_type)

    def justify_with(self, justification_function: Callable[[A, B, C, ScoreType], Any]) -> \
            'TriConstraintBuilder[A, B, C, ScoreType]':
        return TriConstraintBuilder(self.delegate.justifyWith(
            function_cast(justification_function, self.a_type, self.b_type, self.c_type)), self.a_type, self.b_type,
                                    self.c_type)

    def as_constraint(self, constraint_package_or_name: str, constraint_name: str = None) -> '_JavaConstraint':
        if constraint_name is None:
            return self.delegate.asConstraint(constraint_package_or_name)
        else:
            return self.delegate.asConstraint(constraint_package_or_name, constraint_name)


class QuadConstraintBuilder(Generic[A, B, C, D, ScoreType]):
    delegate: '_JavaQuadConstraintBuilder[A, B, C, D, ScoreType]'
    a_type: Type[A]
    b_type: Type[B]
    c_type: Type[C]
    d_type: Type[D]

    def __init__(self, delegate: '_JavaQuadConstraintBuilder[A, B, C, D, ScoreType]',
                 a_type: Type[A], b_type: Type[B], c_type: Type[C], d_type: Type[D]) -> None:
        self.delegate = delegate
        self.a_type = a_type
        self.b_type = b_type
        self.c_type = c_type
        self.d_type = d_type

    def indict_with(self, indictment_function: Callable[[A, B, C, D], Collection]) -> \
            'QuadConstraintBuilder[A, B, C, D, ScoreType]':
        return QuadConstraintBuilder(self.delegate.indictWith(
            function_cast(indictment_function, self.a_type, self.b_type, self.c_type, self.d_type)),
            self.a_type, self.b_type, self.c_type, self.d_type)

    def justify_with(self, justification_function: Callable[[A, B, C, D, ScoreType], Any]) -> \
            'QuadConstraintBuilder[A, B, C, D, ScoreType]':
        return QuadConstraintBuilder(self.delegate.justifyWith(
            function_cast(justification_function, self.a_type, self.b_type, self.c_type, self.d_type)),
            self.a_type, self.b_type, self.c_type, self.d_type)

    def as_constraint(self, constraint_package_or_name: str, constraint_name: str = None) -> '_JavaConstraint':
        if constraint_name is None:
            return self.delegate.asConstraint(constraint_package_or_name)
        else:
            return self.delegate.asConstraint(constraint_package_or_name, constraint_name)


__all__ = ['UniConstraintBuilder', 'BiConstraintBuilder', 'TriConstraintBuilder', 'QuadConstraintBuilder']
