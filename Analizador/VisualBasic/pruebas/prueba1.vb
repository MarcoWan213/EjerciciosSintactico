Imports System

Module Program
    Sub Main(args As String())
        Console.WriteLine("Hello World!")
        Console.WriteLine(vbCrLf + "Nombre men")
        'Dim name = Console.ReadLine()
        Dim name = "Mikasa Ackerman"
        Dim fecha = DateTime.Now
        Console.WriteLine($"{vbCrLf}Hola, {name}, en {fecha:d} at {fecha:t}")
        Dim a As Integer = 10
        Dim b As Integer = 5
        Dim firstCheck, secondCheck As Boolean
        firstCheck = Not (a > b)
        secondCheck = Not (b > a)
        Console.WriteLine($"{firstCheck} | {secondCheck}")
        Console.WriteLine(vbCrLf + "Cualquier cosa para salir")
        Console.ReadKey(True)
    End Sub
End Module