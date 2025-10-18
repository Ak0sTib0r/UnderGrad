# UnderGrad

## Introduction
UnderGrad is an open source note taking package specifically designed for Mathematics and Physics Undergraduates. It's built with Python (3.9.6) and comes with a GUI as well as a library of snippets (shortcuts) for latex. 

## Setup and Configuration
## Prerequisites

- Windows 10/11
- Package manager (Chocolatey, Winget, or Scoop)
- VS Code (or install it during this process)

## Step 1: Install MiKTeX

Choose one of the following methods:

### Option A: Using Winget (Recommended)
```powershell
winget install MiKTeX.MiKTeX
```

### Option B: Using Chocolatey
```powershell
choco install miktex -y
```

### Option C: Using Scoop
```powershell
scoop install miktex
```

## Step 2: Update MiKTeX and Configure

1. Open a new terminal and update MiKTeX:
```cmd
miktex packages update
```

2. Or use MiKTeX Console (GUI):
   - Open MiKTeX Console from Start menu
   - Go to "Updates" tab and install all updates
   - In Settings > General, set "Package installation" to "Always install missing packages on-the-fly"

## Step 3: Install Strawberry Perl

`latexindent` requires Perl. Install Strawberry Perl:

```powershell
winget install StrawberryPerl.StrawberryPerl
```

**Important**: Close and reopen your terminal after installation!

## Step 4: Configure Perl Environment

If you have multiple Perl installations, you might need to prioritize Strawberry Perl:

1. Check which Perl is being used:
```cmd
where perl
perl --version
```

2. If the wrong Perl is being used, temporarily set the correct path:
```cmd
set PATH=C:\Strawberry\perl\bin;C:\Strawberry\c\bin;%PATH%
```

## Step 5: Install Required Perl Modules

Install the modules needed by `latexindent`:

```cmd
cpan YAML::Tiny
cpan File::HomeDir
cpan Log::Log4perl
cpan Log::Dispatch
```

## Step 6: Install MiKTeX Packages

Install the required LaTeX packages:

```cmd
miktex packages install latexindent
miktex packages install latexmk
```

## Step 7: Create latexindent Wrapper Script

1. Create a directory for scripts (if it doesn't exist):
```cmd
mkdir C:\dev\scripts
```

2. Create `C:\dev\scripts\latexindent.bat`:
```batch
@echo off
C:\Strawberry\perl\bin\perl.exe "%LOCALAPPDATA%\Programs\MiKTeX\scripts\latexindent\latexindent.pl" %*
```

3. Add the scripts directory to your PATH:
```cmd
setx PATH "%PATH%;C:\dev\scripts"
```

**Note**: Close and reopen your terminal after this step!

## Step 8: Install and Configure VS Code

1. Install VS Code (if not already installed):
```powershell
winget install Microsoft.VisualStudioCode
```

2. Install LaTeX Workshop extension:
```cmd
code --install-extension James-Yu.latex-workshop
```

## Step 9: Configure VS Code Settings

Open VS Code settings (Ctrl+,), click the JSON icon in the top right, and add:

```json
{
  "editor.wordWrap": "on",
  "editor.formatOnSave": true,
  
  // LaTeX Workshop configuration
  "latex-workshop.latex.tools": [
    {
      "name": "latexmk",
      "command": "latexmk",
      "args": [
        "-synctex=1",
        "-interaction=nonstopmode",
        "-file-line-error",
        "-pdf",
        "%DOC%"
      ]
    }
  ],
  "latex-workshop.latex.recipes": [
    {
      "name": "latexmk",
      "tools": [
        "latexmk"
      ]
    }
  ],
  "latex-workshop.view.pdf.viewer": "tab",
  "latex-workshop.latex.clean.fileTypes": [
    "*.aux",
    "*.bbl",
    "*.blg",
    "*.idx",
    "*.ind",
    "*.lof",
    "*.lot",
    "*.out",
    "*.toc",
    "*.acn",
    "*.acr",
    "*.alg",
    "*.glg",
    "*.glo",
    "*.gls",
    "*.fls",
    "*.log",
    "*.fdb_latexmk",
    "*.snm",
    "*.nav",
    "*.dvi"
  ],
  "latex-workshop.latex.autoBuild.run": "onSave",
  
  // LaTeX formatting configuration
  "latex-workshop.formatting.latex": "latexindent",
  "latex-workshop.formatting.latexindent.path": "latexindent",
  "latex-workshop.formatting.latexindent.args": [
    "-c", "%DIR%/", "%TMPFILE%", "-y=defaultIndent: '%INDENT%'"
  ],
  
  // Language-specific formatting settings
  "[latex]": {
    "editor.defaultFormatter": "James-Yu.latex-workshop",
    "editor.formatOnSave": true
  },
  "[json]": {
    "editor.defaultFormatter": "vscode.json-language-features"
  },
  "[jsonc]": {
    "editor.defaultFormatter": "vscode.json-language-features"
  }
}
```

## Step 10: Test Your Setup

1. Create a test file `test.tex`:

```latex
\documentclass{article}
\usepackage{amsmath}

\begin{document}
\title{LaTeX Test}
\author{Your Name}
\maketitle

\section{Introduction}
This is a test document.

\subsection{Math Test}
Here's an equation:
\begin{equation}
E = mc^2
\end{equation}

    \begin{itemize}
\item First item
        \item Second item
    \item Third item
\end{itemize}

    \begin{enumerate}
  \item One
      \item Two
   \item Three
    \end{enumerate}

\end{document}
```

2. Open the file in VS Code
3. Save it (Ctrl+S) - it should auto-format the indentation
4. Build it (Ctrl+Alt+B) - it should create a PDF

## Troubleshooting

### Issue: `latexindent` not found
- Make sure Perl is in your PATH: `perl --version`
- Check if latexindent works directly: `C:\Strawberry\perl\bin\perl.exe "%LOCALAPPDATA%\Programs\MiKTeX\scripts\latexindent\latexindent.pl" --version`
- Ensure `C:\dev\scripts` is in your PATH: `echo %PATH%`

### Issue: Multiple Perl installations conflicting
- Check which Perl is being used: `where perl`
- Temporarily override PATH: `set PATH=C:\Strawberry\perl\bin;%PATH%`
- Or uninstall conflicting Perl installations

### Issue: LaTeX packages missing
- Enable automatic installation in MiKTeX Console
- Or install manually: `miktex packages install <package-name>`

### Issue: "LaTeX formatter is set to 'none'"
- Ensure your settings.json includes: `"latex-workshop.formatting.latex": "latexindent"`
- Restart VS Code after changing settings

## Additional Tips

1. Keep MiKTeX updated regularly:
   ```cmd
   miktex packages update
   ```

2. For manual formatting in VS Code:
   - Right-click and select "Format Document"
   - Or use keyboard shortcut: `Shift+Alt+F`

3. View LaTeX Workshop output for debugging:
   - View → Output → Select "LaTeX Workshop" from dropdown

4. Common LaTeX packages you might want to install:
   ```cmd
   miktex packages install amsmath amssymb graphicx hyperref babel geometry
   ```

