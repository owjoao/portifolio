@echo off
chcp 65001 >nul
title Lumina OS - Instalador do Sistema Clínico
color 0F

echo ===============================================================================
echo                LUMINA OS - SISTEMA DE GESTAO CLINICA
echo ===============================================================================
echo.
echo  Configurando o aplicativo na sua Area de Trabalho...
echo.

set "DEST_DIR=%LOCALAPPDATA%\LuminaClinica"
set "DESKTOP=%USERPROFILE%\Desktop"

if not exist "%DEST_DIR%" mkdir "%DEST_DIR%"

echo  [1/3] Copiando arquivos do sistema...
copy /Y "%~dp0index.html" "%DEST_DIR%\index.html" >nul
if exist "%~dp0app.ico" copy /Y "%~dp0app.ico" "%DEST_DIR%\app.ico" >nul

echo  [2/3] Criando atalho personalizado com icone exclusivo...

set "VBS_SCRIPT=%TEMP%\CreateLuminaShortcut.vbs"

(
echo Set oWS = WScript.CreateObject^("WScript.Shell"^)
echo sLinkFile = "%DESKTOP%\Lumina OS - Gestao Clinica.lnk"
echo Set oLink = oWS.CreateShortcut^(sLinkFile^)
echo.
echo ' Localiza Microsoft Edge ou Google Chrome
echo Dim browserPath, targetUrl
echo targetUrl = "file:///%DEST_DIR:=/%/index.html"
echo.
echo Dim fso: Set fso = CreateObject^("Scripting.FileSystemObject"^)
echo If fso.FileExists^("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"^) Then
echo     browserPath = "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
echo ElseIf fso.FileExists^("C:\Program Files\Microsoft\Edge\Application\msedge.exe"^) Then
echo     browserPath = "C:\Program Files\Microsoft\Edge\Application\msedge.exe"
echo ElseIf fso.FileExists^("C:\Program Files\Google\Chrome\Application\chrome.exe"^) Then
echo     browserPath = "C:\Program Files\Google\Chrome\Application\chrome.exe"
echo ElseIf fso.FileExists^("C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"^) Then
echo     browserPath = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
echo Else
echo     browserPath = "msedge.exe"
echo End If
echo.
echo oLink.TargetPath = browserPath
echo oLink.Arguments = "--app=""" ^& targetUrl ^& """"
echo oLink.Description = "Lumina OS - Painel de Gestao & CRM Clinico"
echo oLink.WorkingDirectory = "%DEST_DIR%"
echo If fso.FileExists^("%DEST_DIR%\app.ico"^) Then
echo     oLink.IconLocation = "%DEST_DIR%\app.ico, 0"
echo End If
echo oLink.WindowStyle = 3 ' Maximizado
echo oLink.Save
) > "%VBS_SCRIPT%"

cscript //nologo "%VBS_SCRIPT%"
del "%VBS_SCRIPT%" >nul 2>&1

echo  [3/3] Atalho criado com sucesso!
echo.
echo ===============================================================================
echo   INSTALACAO CONCLUIDA COM SUCESSO!
echo.
echo   Um icone dourado "Lumina OS - Gestao Clinica" foi adicionado a sua Area de Trabalho.
echo   Ele abre automaticamente como um aplicativo independente, sem barras de navegador.
echo ===============================================================================
echo.
pause
