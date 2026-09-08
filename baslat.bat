@echo off
setlocal
cd /d "%~dp0"
title SPK SPL 1 Premium Sinav Hazirlik Platformu
cls
color 0B

echo ==============================================================================
echo   SPK DUZEY 1 PREMIUM SINAV HAZIRLIK PLATFORMU [650+ SORU - 29 BOLUM]
echo   Modul 1001 Mevzuat - 1003 Araclar - 1005 Yatirim Kur. - 1012 Takas/Saklama
echo ==============================================================================
echo.

set "PATH=C:\Users\e.cetin\Tools\node;%PATH%"

where node >nul 2>nul
if %errorlevel% neq 0 goto NoNode

:: Port 5173 mesgulse temizle
powershell -NoProfile -Command "Get-NetTCPConnection -LocalPort 5173 -State Listen -ErrorAction SilentlyContinue | ForEach-Object { Stop-Process -Id $_.OwningProcess -Force }" >nul 2>nul

if not exist "node_modules" goto InstallModules
goto LaunchServer

:InstallModules
echo [*] Gerekli paketler kuruluyor (npm install)...
call npm install
if %errorlevel% neq 0 goto InstallFail

:LaunchServer
echo.
echo [OK] Platform baslatiliyor...
echo [OK] Tarayiciniz otomatik olarak aciliyor: http://localhost:5173
echo.
echo ==============================================================================
echo   Uygulamayi kapatmak icin bu pencereyi kapatabilir veya Ctrl + C yapabilirsiniz.
echo ==============================================================================
echo.

:: 2 saniye bekleyip tarayiciyi acan arka plan komutu (ping ile guvenli bekleme)
start "" /b cmd /c "ping 127.0.0.1 -n 3 >nul & start http://localhost:5173"

:: Vite sunucusunu baslat
call npm run dev
goto End

:NoNode
color 0C
echo [HATA] Node.js sisteminizde bulunamadi!
echo Lutfen https://nodejs.org adresinden Node.js kurun.
echo.
pause
exit /b 1

:InstallFail
color 0C
echo [HATA] Kutuphaneler kurulurken bir sorun olustu!
echo.
pause
exit /b 1

:End
pause
