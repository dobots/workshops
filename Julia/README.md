Julia tutorial 

Setup Julia: 

- Download the current stable Julia release from https://julialang.org/downloads/

- Start Julia and enter ] to use the built in package manager (https://docs.julialang.org/en/v1/stdlib/Pkg/index.html) and enter “add IJulia Plots CSV DataFrames”. This may take a few minutes. After, leave the package manager with a backspace, to enter the Julia prompt again.

- Start a Jupyter notebook session, by typing “using IJulia” <enter> followed by “notebook()” <enter>. On the first time, this will ask to install Jupyter via Conda, press enter to accept. It will take around 10 minutes. This should open a new tab in your browser, pointing to http://localhost:8888/tree. Now near the top right, click New, and select Julia to start a new empty Jupyter notebook.

- Verify that the new notebook works, by entering “reverse("enod")“, and pressing Ctrl+enter

