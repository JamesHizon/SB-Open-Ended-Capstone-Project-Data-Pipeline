# Springboard Open-Ended Capstone Project Data Pipeline
## Step 3: Data Collection

![alt text](https://www.xenonstack.com/images/wp-content/uploads/building-big-data-pipeline-aws-xenonstack.png)

### To run the file, perform the following inside Terminal. Note that we are dealing with Python Version 3.
### First, we need to download the necessary Python packages, if not already installed. Also, check the requirements.txt for files listed in my virtual environment. Not all packages are needed, but you can see the version number of each Python package.

```
pip install requests
pip install bs4
pip install logging
```

### Next, change to the desired working directory and run our Python script.

```
cd Step_3_Data_Collection
python3 Project_Data_Collection.py
```

### Then, check for files inside the directory "Step 3 - Data Collection".
### The output of the Python script should include the time it takes to download each file and a log output.

### Next Step:
##### If I want to optimize code for efficiency, I should figure out how to go straight from finding "a" tags to finding "href" tags directly. Then, the time complexity of code will be O(N) from O(N^2).

