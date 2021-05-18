# Springboard Open-Ended Capstone Project Data Pipeline

### In this repository, I will include each step of the data pipeline.

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


## Step 5: Prototype Data Pipeline

### Within the folder "Step_5_Prototype_Data_Pipeline," we will find the Python script we want to work with. To run the file, change the working directory and then run the Python script as follows.

```
cd Step_5_Prototype_Data_Pipeline
python3 Step5_Capstone_Project.py
```

### After running the Python script, we should have received our desired output which is similar to what we did in Step 3. Our next step is to update our code
### so that we will automate data loading into Amazon S3 via S3 bucket.



