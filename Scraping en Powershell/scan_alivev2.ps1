$subred = (Get-NetRoute -DestinationPrefix 0.0.0.0/0).NextHop
Write-Host "==Determinando tu gateway ..."
Write-Host "Tu gateway es: $subred"
$rango = $subred.Substring(0, $subred.IndexOf('.') + 1 + $subred.Substring($subred.IndexOf('.') + 1).IndexOf('.') + 3)
Write-Host "== Determinando tu rango de subred ..."
echo $rango
$portstoscan = @(20,21,22,23,25,50,51,53,80,110,119,135,136,137,138,139,143,161,162,389,443,445,636,1025,1443,3389,5985,5985,5986,8080,10000)
$waittime = 135
Write-Host "Direccion ip a escanear:" -NoNewline
$direcction = Read-Host
foreach ($p in $portstoscan )
{  
    $TCPObject = New-Object System.Net.Sockets.TcpClient
        try{ $resultado = $TCPObject.ConnectAsync($direccio,$p).Wait($waittime)}catch{}
        if ( $resultado -eq "True")
        {
           Write-Host "Puerto abierto: " -NoNewline; Write-Host $p -ForegroundColor Green
        }
}
#Nicolás Alberto Garza Galicia
#1998776
