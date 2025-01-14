package ai.timefold.jpyinterpreter.types.collections;

import java.util.Iterator;

import ai.timefold.jpyinterpreter.PythonLikeObject;
import ai.timefold.jpyinterpreter.PythonOverloadImplementor;
import ai.timefold.jpyinterpreter.PythonUnaryOperator;
import ai.timefold.jpyinterpreter.types.AbstractPythonLikeObject;
import ai.timefold.jpyinterpreter.types.BuiltinTypes;
import ai.timefold.jpyinterpreter.types.PythonLikeType;
import ai.timefold.jpyinterpreter.types.errors.StopIteration;

public class PythonIterator<T> extends AbstractPythonLikeObject implements Iterator<T> {
    private final Iterator<T> delegate;

    static {
        PythonOverloadImplementor.deferDispatchesFor(PythonIterator::registerMethods);
    }

    private static PythonLikeType registerMethods() throws NoSuchMethodException {
        BuiltinTypes.ITERATOR_TYPE.addUnaryMethod(PythonUnaryOperator.NEXT, PythonIterator.class.getMethod("nextPythonItem"));
        BuiltinTypes.ITERATOR_TYPE.addUnaryMethod(PythonUnaryOperator.ITERATOR, PythonIterator.class.getMethod("getIterator"));
        return BuiltinTypes.ITERATOR_TYPE;
    }

    public PythonIterator(PythonLikeType type) {
        super(type);
        this.delegate = this;
    }

    public PythonIterator(Iterator<T> delegate) {
        super(BuiltinTypes.ITERATOR_TYPE);
        this.delegate = delegate;
    }

    @Override
    public boolean hasNext() {
        return delegate.hasNext();
    }

    @Override
    public T next() {
        if (!delegate.hasNext()) {
            throw new StopIteration();
        }
        return delegate.next();
    }

    public PythonLikeObject nextPythonItem() {
        if (!delegate.hasNext()) {
            throw new StopIteration();
        }
        return (PythonLikeObject) delegate.next();
    }

    public PythonIterator<T> getIterator() {
        return this;
    }
}
