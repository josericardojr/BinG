using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class Config : MonoBehaviour {

    public static string KEY_PATH_PYTHON = "KEY_PATH_PYTHON", KEY_PATH_XML = "KEY_PATH_XML";

    [SerializeField]
    private InputField pathPythonInput, pathXmlInput;

    private void Start()
    {
        if (PlayerPrefs.HasKey(KEY_PATH_PYTHON))
        {
            pathPythonInput.text = PlayerPrefs.GetString(KEY_PATH_PYTHON);
        }
        else
        {
            pathPythonInput.text = PythonTools.GetPythonPath();
            PlayerPrefs.SetString(KEY_PATH_PYTHON, pathPythonInput.text);
        }

        if (PlayerPrefs.HasKey(KEY_PATH_XML))
        {
            pathXmlInput.text = PlayerPrefs.GetString(KEY_PATH_XML);
        }
        else
        {
            pathXmlInput.text = "";
            PlayerPrefs.SetString(KEY_PATH_XML, pathXmlInput.text);
        }
    }

    public void Save()
    {
        PlayerPrefs.SetString(KEY_PATH_PYTHON, pathPythonInput.text);
        PlayerPrefs.SetString(KEY_PATH_XML, pathXmlInput.text);
    }

    public static T MyFind<T>() where T : Object
    {
        T o = FindObjectOfType<T>();
        if (o == null)
        {
            throw new System.Exception("Não encontrado " + (typeof(T)));
        }

        return o;
    }

    public static T[] MyFindArray<T>() where T : Object
    {
        T[] o = FindObjectsOfType<T>();
        if (o == null)
        {
            throw new System.Exception("Não encontrado array" + (typeof(T)));
        }

        return o;
    }
}
