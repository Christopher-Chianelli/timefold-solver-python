import pathlib
import jpype
import jpype.imports
import importlib.metadata
from typing import List


def extract_python_translator_jars() -> list[str]:
    """Extracts and return a list of the Python Translator Java dependencies

    Invoking this function extracts Python Translator Dependencies from the javapython.jars module
    into a temporary directory and returns a list contains classpath entries for
    those dependencies. The temporary directory exists for the entire execution of the
    program.

    :return: None
    """
    return [str(p.locate()) for p in importlib.metadata.files('javapython') if p.name.endswith('.jar')]


def init(*args, path: List[str] = None, include_translator_jars: bool = True):
    """Start the JVM. Throws a RuntimeError if it is already started.

    :param args: JVM args.
    :param path: If not None, a list of dependencies to use as the classpath. Default to None.
    :param include_translator_jars: If True, add translators jars to path. Default to True.
    :return: None
    """
    if jpype.isJVMStarted():  # noqa
        raise RuntimeError('JVM already started.')
    if path is None:
        include_translator_jars = True
        path = []
    if include_translator_jars:
        path = path + extract_python_translator_jars()
    jpype.startJVM(*args, classpath=path, convertStrings=True)  # noqa

    from org.optaplanner.python.translator import CPythonBackedPythonInterpreter
    CPythonBackedPythonInterpreter.lookupAttributeOnPythonReferencePythonFunction = GetAttributeOnPythonObject()
    CPythonBackedPythonInterpreter.setAttributeOnPythonReferencePythonFunction = SetAttributeOnPythonObject()
    CPythonBackedPythonInterpreter.deleteAttributeOnPythonReferencePythonFunction = DeleteAttributeOnPythonObject()
    CPythonBackedPythonInterpreter.callPythonFunction = CallPythonFunction()


@jpype.JImplements('java.util.function.BiFunction', deferred=True)
class GetAttributeOnPythonObject:
    @jpype.JOverride()
    def apply(self, python_object, attribute_name):
        from .python_to_java_bytecode_translator import convert_to_java_python_like_object
        out = getattr(python_object, attribute_name)
        return convert_to_java_python_like_object(out)


@jpype.JImplements('org.optaplanner.python.translator.TriConsumer', deferred=True)
class SetAttributeOnPythonObject:
    @jpype.JOverride()
    def accept(self, python_object, attribute_name, value):
        setattr(python_object, attribute_name, value)


@jpype.JImplements('java.util.function.BiConsumer', deferred=True)
class DeleteAttributeOnPythonObject:
    @jpype.JOverride()
    def accept(python_object, attribute_name):
        delattr(python_object, attribute_name)


@jpype.JImplements('org.optaplanner.python.translator.TriFunction', deferred=True)
class CallPythonFunction:
    @jpype.JOverride()
    def apply(self, python_object, var_args_list, keyword_args_map):
        from .python_to_java_bytecode_translator import unwrap_python_like_object, convert_to_java_python_like_object
        actual_vargs = unwrap_python_like_object(var_args_list)
        actual_keyword_args = unwrap_python_like_object(keyword_args_map)
        out = python_object(*actual_vargs, **actual_keyword_args)
        return convert_to_java_python_like_object(out)


def ensure_init():
    """Start the JVM if it isn't started; does nothing otherwise

    Used by the translator to start the JVM when needed by a method, so
    users don't need to start the JVM themselves.

    :return: None
    """
    if jpype.isJVMStarted(): # noqa
        return
    else:
        init()


def set_class_output_directory(path: pathlib.Path):
    ensure_init()

    from org.optaplanner.python.translator import PythonBytecodeToJavaBytecodeTranslator # noqa
    PythonBytecodeToJavaBytecodeTranslator.classOutputRootPath = path
