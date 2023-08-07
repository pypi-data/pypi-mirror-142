# ISSA
The Input Scripting and Statistical Analysis (ISSA) software package allows for the easy scripting of large batches of input files for "black box" codes, and the statistical evaluation of their corresponding output values.

## Running ISSA
ISSA is a software package that is dependent on the user having a "black box" tool at the ready. As a result a number of files are required to run the code at the minimum.
1. A "parameterized" input file. This is an input file where the parameter(s) of interest for a specific run of the user's black box code are demarkated by brackets. 
2. A config.yml with all of the necessary information filled out. 

These input files are in depth, but the ISSA package aims to be as broad as possible and therefore requires the user to specify many settings.

A number of examples for both of these input files can be seen in the "Examples" folder provided upon distribution, but one of each is included below. In the example file below the {parameter1} represents the input parameter I wish to change with ISSA. The rest of the file is left as I would run my file normally.  If I were to want to run two parameters, the next value I would replace with {parameter2}, and so on. Then I would have to change the equivalent value in the config file.

>**Example Input file**
>ICSBEP PMF Layered Benchmark
1   0    -1  imp:n=1
2 1 -{parameter1} +1 -2 imp:n=1 $shell 
3 0 2 imp:n=0  $ void outside geometry
1 so 1.0
2 so 6.0
kcode 10000  1.0  25  1025
sdef erg=d1  rad=d2  pos=0.0 0.0 0.0
sp1    -3     0.966  2.842   $239Pu Watt spectrum with default (endf/b-v) A,B parameters.
sp2   -21     2              $Uniform probability in volume from si2 r(min) to r(max).
si2     1.0   6.0
c  ---- Pu-W/coating -----
C Material Cards
m1 94239.55c 3.6826e-2
    94240.50c 6.7320e-4
    31000.50c 2.2000e-3
    28000.50c 1.5722e-3
    26000.50c 1.4714e-4
    6000.50c 3.0406e-4
m2 94239.55c 3.6579e-2
    94240.50c 6.6875e-4
    31000.50c 2.2114e-3
    28000.50c 1.9330e-3
    26000.50c 1.2992e-4
    6000.50c 3.0205e-4

The other file that the user will need to provide for each run will be a config.yml file:
>#Information relevant to your input filr
Input_file:
    #Your input File's name. Example1 Value.
    file_name: "Test"
    #File type
    in_file_type: "i"
    #Command a user would call from commandline to run your "blackbox" software
    software_call: "mcnp6"
    #Command a user would use to assign input file location from same line
    input_command: "i="
    #Choose the directory you wish the input files to be generated into
    Inp_File_directory: "C:\\Users\\mike1\\Desktop"
    
>#Information Relevant to input parameters.
Input_param:
    #Number of InputParamters 
    Param_count: 1
    #Parameter Mean values
    Param_means: [15.2]
    #Standard Deviation value for each parameter, if known, If unknown use 0.
    Param_std: [.2]
    #Probability Density Function desired for each variable, 
    Param_pdf: ["Normal","Normal"]
    #For the Example problems, you can force the Number of Samples in your sample space. If you are not using this, please change it to None.
    forced_max: 10
    
>#Information Relevant to User Output File
Output_file:
    #Number of output values.
    out_count: 1
    #Output Filetype
    out_file_type: "txt"
    #If you are providing output files, as is done in the examples please include those files here.
    outfile_name: "Test1out.txt"
    #If you are providing output files, please include the path here.
    Out_File_directory: "C:\\Users\\mike1\\Desktop\\ISSA\\Examples\\Example1"
    #If you are not providing the output files, provide an example line that could be searched to find your desired output in Regex.
    output_searchline: "final result"


After ISSA has been installed, the user can run the software with the command python3 CLI.py:
>python3 CLI.py "--Input File Path:" "**your input file path here**" "--YAML File Path:" "**your YAML file path here**" "--Provided Output Values? T/F" "**Whether you want the code to run your software for you**"

Type the line below for help if needed
>python3 CLI.py -h 

In the main code there is only one module, ISSA. The ISSA module contains a number of class submodules that define Operations.

CLI.py serves as the main driver function for the code, and is also where the user will start their runs.

Information is passed from there to Functions.py, which does the bulk of the files generation and calls the subprocess to run the users code if dsired. If the user does not want ISSA to automatically run their code it instead reads provided output files and passes it to the DataProcessor.py submodule. This submodule process the data, prints some meaningful stastics to the command line, and then 

## Installation

The Package is available for download through PyPi, once installed just use the command pip install ISSA to install the latest version.

For testing, change into the working directory ISSA has been installed in and run the python script Test.py, if it passes the single test it is good for running.


## Dependencies
| Package | Link |
| ------ | ------ |
| os | [os — Miscellaneous operating system interfaces][PlDb] |
| re | [re — Regular expression operations][PlGh] |
| subprocess | [subprocess — Subprocess management][PlGd] |
| Math | [math — Mathematical functions][PlOd] |
| Scipy | [Fundamental algorithms for scientific computing in Python][PlMe] |
| Numpy | [The fundamental package for scientific computing with Python][PlGa] |
| YAML | [YAML: Specific Configuration Files][yaml] |
| Matplotlib | [Visualizing With Python][PlGc] |
| argparse | [Reads arguments from commandline][argparse] |
| shutil | [High Level File Operations][shutil] |





[PlDb]: <https://docs.python.org/3/library/os.html>
[PlGh]: <https://docs.python.org/3/library/re.html>
[PlGd]: <https://docs.python.org/3/library/subprocess.html>
[PlOd]: <https://docs.python.org/3/library/math.html>
[PlMe]: <https://scipy.org/>
[PlGa]: <https://numpy.org/>
[yaml]: <https://pyyaml.org/>
[PlGc]: <https://matplotlib.org/>
[argparse]: https://docs.python.org/3/library/argparse.html#module-argparse
[shutil]: https://docs.python.org/3/library/shutil.html#module-shutil