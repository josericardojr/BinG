using System;
using System.Collections;
using System.IO;

public class PythonTools
{

    public static string GetPythonPath()
    {
        string pathPython = "did not find";
        IDictionary environmentVariables = Environment.GetEnvironmentVariables();
        string pathVariable = environmentVariables["Path"] as string;
        if (pathVariable != null)
        {
            string[] allPaths = pathVariable.Split(';');
            foreach (var path in allPaths)
            {
                string pythonPathFromEnv = path + @"python.exe";
                //& !pythonPathFromEnv.Contains("Python2")
                if (File.Exists(pythonPathFromEnv))
                {
                    //print("Change: ");
                    pathPython = pythonPathFromEnv;
                    //print("Path: " + pathPython);
                }
            }
        }
        // 
        //print("___________________");
        //print("Final: " + pathPython);
        return pathPython;
    }
}
