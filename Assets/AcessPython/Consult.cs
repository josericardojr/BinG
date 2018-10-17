using System;
using System.Threading;
using System.Diagnostics;
using System.IO;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class Consult : MonoBehaviour {

    public static string KEYPATHPYTHON = "KEYPATHPYTHON", KEYFILEXML = "KEYFILEXML", COMMAND_ASK_PATH = "COMMAND_ASK_PATH", COMMAND_REPEAT = "COMMAND_REPEAT", COMMAND_QUIT = "COMMAND_QUIT";

    private static string KEY_NO_MSG = "KEY_NO_MSG";

    private static string DATA_STANDARD_PATH = "DATA_STANDARD_PATH";

    private Process process;

    private StreamWriter sortStreamWriter;

    private Thread thread, threadAnwser;

    [SerializeField]
    private InputField inputMsg;

    [SerializeField]
    private Text feedback;

    [SerializeField]
    private string msg, lastPythonMsg, awnserMsg;

    private string standardPath;

    private int count;

    public bool Run { get; set; }

    private bool startedThread;

    private void Start()
    {
        msg = "";

        standardPath = PlayerPrefs.GetString(DATA_STANDARD_PATH);
        lastPythonMsg = awnserMsg = KEY_NO_MSG;
#if UNITY_EDITOR
        PlayerPrefs.SetString(DATA_STANDARD_PATH, @"D:\Documentos\BinGTool\FactGenerator\info.xml"); 
#endif
        StartThreadUI();
    }

    private void Update()
    {
        feedback.text = msg;
    }

    private void OnApplicationQuit()
    {
        SendMsgToPython(COMMAND_QUIT);
        Stop();
    }

    private void StartThreadUI()
    {
        StartThread(@"D:\Documentos\BinGTool\FactGenerator\Data.py");
    }

    private void StartThread(string fullFilename)
    {
        if (!startedThread)
        {
            startedThread = true;
            Run = true;
            thread = new Thread(() => GetInstruction(fullFilename, PythonTools.GetPythonPath()));
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

        if (threadAnwser != null)
        {
            threadAnwser.Join();
        }
    }

    public void SendMsg()
    {
        //todo controll this
        if (true)
        {
            awnserMsg = inputMsg.text;
            inputMsg.text = KEY_NO_MSG;
        }
    }

    public void GetInstruction(string fullFilename, string pathPythonEXE)
    {
        UnityEngine.Debug.Log("Start GetInstruction");
        try
        {
            if (!File.Exists(fullFilename))
            {
                AddText(".py dont exists: " + fullFilename);
                return;
            }

            if (!File.Exists(pathPythonEXE))
            {
                AddText("Python.exe dont exists: " + pathPythonEXE);
                return;
            }

            //print("fullFilename: " + fullFilename);
            //print("pathPythonEXE: " + pathPythonEXE);

            threadAnwser = new Thread(AnaLastPythonMsg);
            threadAnwser.Start();

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
        UnityEngine.Debug.Log("End GetInstruction");
    }

    private void Process_ErrorDataReceived(object sender, DataReceivedEventArgs e)
    {
        UnityEngine.Debug.Log(e.Data);
    }

    private void AnaLastPythonMsg()
    {
        UnityEngine.Debug.Log("Start AnaLastPythonMsg");

        while (Run)
        {
            if (!AuthomatichAwn(lastPythonMsg))
            {
                UnityEngine.Debug.Log("have msg: " + lastPythonMsg);
                if (!awnserMsg.Contains(KEY_NO_MSG))
                {
                    SendMsgToPython(awnserMsg);
                    awnserMsg = KEY_NO_MSG;
                }
            }
        }
        UnityEngine.Debug.Log("End AnaLastPythonMsg");
    }

    private bool AuthomatichAwn(string command)
    {
        if (command.Contains(KEY_NO_MSG))
        {
            UnityEngine.Debug.Log("AuthomatichAwn KEY_NO_MSG: " + command);
            return true;
        }
        else if (command.Contains(COMMAND_QUIT))
        {
            SendMsgToPython(COMMAND_QUIT);
            return true;
        }
        else
        {
            SendMsgToPython(standardPath);            
        }

        UnityEngine.Debug.Log("AuthomatichAwn return: " + command);

        return false;
    }

    private void SendMsgToPython(string s)
    {
        UnityEngine.Debug.Log("send: " + s);
        sortStreamWriter.WriteLine(s);
    }

    private void P_OutputDataReceived(object sender, DataReceivedEventArgs e)
    {
        AddText("Python: " + e.Data);
        lastPythonMsg = e.Data;
    }

    private void AddText(object s)
    {
        msg += s + "\n";
    }
}
