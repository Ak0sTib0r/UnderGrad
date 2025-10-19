![Alt text](UnderGrad/UG_Cropped.png)

<img src = "UnderGrad/UG_Cropped.png" width = "60%" height = "60%">

<p align="center">(credit: Alex Tudorache)</p>

## Introduction
UnderGrad is an open source note taking package specifically designed for Mathematics and Physics Undergraduates. It's built with Python (3.9.6) and comes with a GUI as well as a library of snippets (shortcuts) for latex. 

## Setup and Configuration

This section is split into three parts:
- Prerequisites
- Setup VSCode with Latex
- Setup and Configure Undergrad

### Part I: Prerequisites

Before you start setting up UnderGrad, make sure you have:

- Windows 10/11
- Package manager 'Winget' (this should already be installed if you're running Windows)
- VS Code (you can either go to the end of the guide and follow the steps or install VSCode on your own from the official VSCode website: https://code.visualstudio.com/download)
- Python (version 3.9.6) (again, you can install this from here: https://www.python.org/downloads/)

### Part II: Setup VSCode with Latex
#### Step 1: Install MiKTeX

- Open Command Prompt (CMD) and type the following command:

```powershell
winget install MiKTeX.MiKTeX
```

This should install latex on your system.

#### Step 2: Update MiKTeX and Configure

Use the terminal and update MiKTeX using this command:

```cmd
miktex packages update
```

#### Step 3: Install Strawberry Perl

`latexmk` and `latexindent` are the two essential latex modules that UnderGrad and VSCode need to be able to produce .tex files and convert them into viewable PDFs. They both require Perl to run. So, you now need to install 'Strawberry Perl' on your system using this command:

```powershell
winget install StrawberryPerl.StrawberryPerl
```

**Very Important**: Close and reopen your terminal after installation is complete!

#### Step 4: Configure your Perl Environment

If you have multiple Perl installations, you might need to prioritize Strawberry Perl:

1. First, check which Perl is being used:
```cmd
where perl
perl --version
```

2. If the wrong Perl is being used (Not Strawberry), temporarily set the correct path:
```cmd
set PATH=C:\Strawberry\perl\bin;C:\Strawberry\c\bin;%PATH%
```

#### Step 5: Install Some Important Perl Modules

Install the modules needed by `latexindent` by running these commands on your terminal (one-by-one):

```cmd
cpan YAML::Tiny
cpan File::HomeDir
cpan Log::Log4perl
cpan Log::Dispatch
```

#### Step 6: Install Some Important MiKTeX Packages

Install the required LaTeX packages (one-by-one):

```cmd
miktex packages install latexindent
miktex packages install latexmk
```

#### Step 7: Install and Configure VS Code

Install VS Code with winget (if not already installed):

```powershell
winget install Microsoft.VisualStudioCode
```

#### Step 8: Configure VS Code Settings

Open VS Code settings (bottom left corner), click the JSON icon in the top right corner of the navigation bar. You should now be in a file called 'setting.json'. Paste the following in this file:

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

#### Step 9: Test Your Setup

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

### Part III: Setup and Configure UnderGrad
