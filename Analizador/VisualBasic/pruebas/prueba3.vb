Imports System

Module Program
    Sub Main(args As String())        
        Dim a As Integer = 10
        Dim b As Integer = 5
        Dim firstCheck, secondCheck As Boolean
        firstCheck = Not (a > b)
        secondCheck = Not (b > a)
        Console.WriteLine($"{firstCheck} | {secondCheck}")
        Console.WriteLine(vbCrLf + "Cualquier cosa para salir")
        a = a+b 
        Console.WriteLine(a)
        Console.ReadKey(True)
    End Sub
End Module