using System;
using System.Threading;
using System.Diagnostics;
using System.IO;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class Consult : MonoBehaviour {

    public static string COMMAND_ASK_PATH = "COMMAND_ASK_PATH";

    public static string COMMAND_REPEAT = "COMMAND_REPEAT", COMMAND_QUIT = "COMMAND_QUIT", COMMAND_FEEDBACK = "COMMAND_FEEDBACK", COMMAND_CONSULT = "COMMAND_CONSULT";

    private static string KEY_NO_MSG = "KEY_NO_MSG";

    private static char charSpliter = ';';

    private Process process;

    private StreamWriter sortStreamWriter;

    [SerializeField]
    private InputField inputMsg;

    [SerializeField]
    private Text feedback;

    [SerializeField]
    private string msg, awnserMsg;

    private string standardPathXML, lastPythonMsg, feedbackGiven;

    private int count;

    [SerializeField]
    public bool run;

    private bool startedThread, send;

    private void Start()
    {
        count = 0;
        msg = "";
        feedbackGiven = "";
        standardPathXML = PlayerPrefs.GetString(Config.KEY_PATH_XML);
        awnserMsg = KEY_NO_MSG;
    }

    private void Update()
    {
        feedback.text = msg;
    }

    private void OnApplicationQuit()
    {
        if (sortStreamWriter != null)
        {
            SendMsgToPython(COMMAND_QUIT);
        }
        Stop();
    }

    public void StartThreadUI()
    {
        string p = Directory.GetCurrentDirectory();
        p += @"\FactGenerator\Data.py";
        StartThread(p);
    }

    private void StartThread(string fullFilename)
    {
        if (!startedThread)
        {
            startedThread = true;
            run = true;
            GetInstruction(fullFilename, PythonTools.GetPythonPath());
        }
    }

    public void Stop()
    {
        run = false;
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
        AddText("Loading Python");
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
                AddText("err sortStreamWriter: " + e.Message);
            }


            //sortStreamWriter.WriteLine("C# make me do this");
            process.BeginOutputReadLine();
            //UnityEngine.Debug.Log("BeginOutputReadLine");
            //Console.WriteLine(process.StandardOutput.ReadToEnd());
        }
        catch (System.Exception e)
        {
            AddText("err GetInstruction: " + e.Message);
        }
        UnityEngine.Debug.Log("End GetInstruction");
    }

    private void Process_ErrorDataReceived(object sender, DataReceivedEventArgs e)
    {
        UnityEngine.Debug.Log("Process_ErrorDataReceived: " + e.Data);
    }

    private void AnaLastPythonMsg()
    {
        print("Start AnaLastPythonMsg");
        while (run)
        {
            AuthomatichAwn(lastPythonMsg);
        }
        print("End AnaLastPythonMsg");
    }

    private bool AuthomatichAwn(string command)
    {
        if (command.Contains(KEY_NO_MSG))
        {
            return true;
        }
        else if (command.Contains(COMMAND_QUIT))
        {
            SendMsgToPython(COMMAND_QUIT);
            return true;
        }
        else if (command.Contains(COMMAND_ASK_PATH))
        {
            SendMsgToPython(standardPathXML);
            return true;
        }
        else if (command.Contains(COMMAND_FEEDBACK))
        {
            string[] splited = command.Split(charSpliter);
            if (splited.Length == 2)
            {
                if (!feedbackGiven.Contains(splited[splited.Length-1]))
                {
                    feedbackGiven = "Python: " + splited[splited.Length - 1];
                    AddText(feedbackGiven); 
                }
            }
            else
            {
                UnityEngine.Debug.Log("err " + COMMAND_FEEDBACK + command);
            }
            return true;
        }
        else if (command.Contains(COMMAND_CONSULT))
        {
            SendMsgToPython(COMMAND_CONSULT);
            return true;
        }

        UnityEngine.Debug.Log("AuthomatichAwn return: " + command);

        return false;
    }

    private void SendMsgToPython(string s)
    {
        if (!send)
        {
            send = true;
            sortStreamWriter.WriteLine(s);
            UnityEngine.Debug.Log(count + ": " + "Send: " + s);
        }
    }

    private void P_OutputDataReceived(object sender, DataReceivedEventArgs e)
    {
        send = false;
        UnityEngine.Debug.Log("__________");
        count++;
        lastPythonMsg = count + ": " + e.Data;
        UnityEngine.Debug.Log(lastPythonMsg);
        AuthomatichAwn(lastPythonMsg); 
    }

    private void AddText(object s)
    {
        msg += s + "\n";
    }
}
