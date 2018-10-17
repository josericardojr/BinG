using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class UIManager : MonoBehaviour
{
    [SerializeField]
    private Canvas actualCanvas;

    private void Start()
    {
        Canvas[] c = Config.MyFindArray<Canvas>();

        foreach (Canvas canvas in c)
        {
            canvas.enabled = false;
        }

        ChangeCanvas(actualCanvas);
    }

    public void ChangeCanvas(Canvas canvas)
    {
        if (actualCanvas != null)
        {
            actualCanvas.enabled = false;
        }

        actualCanvas = canvas;

        if (actualCanvas != null)
        {
            actualCanvas.enabled = true;
        }
    }
}