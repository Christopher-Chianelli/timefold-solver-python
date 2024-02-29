package ai.timefold.jpyinterpreter;

import java.util.List;
import java.util.Map;

import ai.timefold.jpyinterpreter.types.PythonModule;
import ai.timefold.jpyinterpreter.types.PythonString;
import ai.timefold.jpyinterpreter.types.errors.PythonTraceback;
import ai.timefold.jpyinterpreter.types.numeric.PythonInteger;

public interface PythonInterpreter {
    PythonInterpreter DEFAULT = new CPythonBackedPythonInterpreter();

    PythonLikeObject getGlobal(Map<String, PythonLikeObject> globalsMap, String name);

    void setGlobal(Map<String, PythonLikeObject> globalsMap, String name, PythonLikeObject value);

    void deleteGlobal(Map<String, PythonLikeObject> globalsMap, String name);

    PythonModule importModule(PythonInteger level, List<PythonString> fromList, Map<String, PythonLikeObject> globalsMap,
            Map<String, PythonLikeObject> localsMap, String moduleName);

    /**
     * Writes output without a trailing newline to standard output
     *
     * @param output the text to write
     */
    void write(String output);

    /**
     * Reads a line from standard input
     *
     * @return A line read from standard input
     */
    String readLine();

    PythonTraceback getTraceback();
}
