using System;
using System.Threading;
using System.Diagnostics;
using System.IO;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class Consult : MonoBehaviour {

    public static string KEYPATHPYTHON = "KEYPATHPYTHON", KEYFILEXML = "KEYFILEXML";

    private Process process;

    private StreamWriter sortStreamWriter;

    private Thread thread;

    [SerializeField]
    private InputField inputPath,inputArgs;

    [SerializeField]
    private Text feedback;

    private string msg;

    private int count;

    public bool Run { get; set; }

    private bool startedThread;

    private void Start()
    {
        msg = "";
        inputPath.text = @"D:\Documentos\BinGTool\FactGenerator\Data.py";
    }

    private void Update()
    {
        feedback.text = msg;
    }

    private void OnApplicationQuit()
    {
        Stop();
    }

    public void StartThreadUI()
    {
        StartThread(inputPath.text, inputArgs.text);
    }

    public void StartThread(string fullFilename, string args)
    {
        if (!startedThread)
        {
            startedThread = true;
            Run = true;
            thread = new Thread(() => GetInstruction(fullFilename, args, PythonTools.GetPythonPath()));
            thread.Start();
        }
    }

    public void Stop()
    {
        Run = false;
        if (thread != null)
        {
            thread.Join();
        }
    }

    public void GetInstruction(string fullFilename, string args, string pathPythonEXE)
    {
        AddText("Start");
        try
        {
            if (!File.Exists(fullFilename))
            {
                AddText(".py dont exists: " + fullFilename);
                return;
            }

            fullFilename += " " + args;

            if (!File.Exists(pathPythonEXE))
            {
                AddText("Python.exe dont exists: " + pathPythonEXE);
                return;
            }

            //print("fullFilename: " + fullFilename);
            //print("pathPythonEXE: " + pathPythonEXE);

            process = new Process
            {
                StartInfo = new ProcessStartInfo(pathPythonEXE, fullFilename)
                {
                    RedirectStandardOutput = true,
                    RedirectStandardInput = true,
                    RedirectStandardError = true,
                    UseShellExecute = false,
                    CreateNoWindow = true,
                }
            };


            process.OutputDataReceived += P_OutputDataReceived;
            process.ErrorDataReceived += Process_ErrorDataReceived;
            //UnityEngine.Debug.Log("OutputDataReceived");

            process.Start();
            //UnityEngine.Debug.Log("Start()");

            try
            {
                sortStreamWriter = process.StandardInput;
            }
            catch (System.Exception e)
            {
                AddText("sortStreamWriter: " + e.Message);
            }


            //sortStreamWriter.WriteLine("C# make me do this");
            process.BeginOutputReadLine();
            //UnityEngine.Debug.Log("BeginOutputReadLine");
            //Console.WriteLine(process.StandardOutput.ReadToEnd());
        }
        catch (System.Exception e)
        {
            AddText(e.Message);
        }
        AddText("End");
    }

    private void Process_ErrorDataReceived(object sender, DataReceivedEventArgs e)
    {
        UnityEngine.Debug.Log(e.Data);
    }

    private void P_OutputDataReceived(object sender, DataReceivedEventArgs e)
    {
        AddText("Python: " + e.Data);

        if (e.Data.Contains("nome do arquivo xml: "))
        {
            UnityEngine.Debug.Log("add nome");
            sortStreamWriter.WriteLine("info.xml");
        }
        else if (e.Data.Contains("nome do caminho do arquivo xml: "))
        {
            UnityEngine.Debug.Log("add path");
            sortStreamWriter.WriteLine(@"D:\Documentos\BinGTool\FactGenerator");
        }
        else
        {
            //sortStreamWriter.WriteLine("oi");
        }
    }

    private void AddText(string s)
    {
        msg += s + "\n";
    }
}
