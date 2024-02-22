# ELE8096 Coursework 2
## data is in data.txt
## tasks
1. errors
1. Collect information: PM2.5, NO2, O3 and temperature and humidity.
2. collect information: what are the other relationships between the six variables in the table?
3. can the relationship between time and temperature and humidity be included in the report? (check assignment requirements)
4. MATLAB: fit a curve, model e.g. ax^3 + bx^2 + cx + d
## link to cw
https://canvas.qub.ac.uk/courses/24281/assignments/153127

## TODO
1. **box plots & scatter plots (plot.py)**
2. **outliers: What are the criteria for outliers (val_data.py)**
3. **Determine the Independent variable & Dependent variable**
4. **model**

## link to report
https://www.overleaf.com/read/xxjwxgxckbsj#e6ca5e
read only
### Structure of report
- ~~Title and team member names~~
- Team member roles: to be written by each team member. Two paragraphs describing individual
member tasks and contribution to the team
- Abstract (brief description of this exercise and motivation)
- Introduction: brief intro to data set and purpose of the exercise
- Main body: with 4 sections on each of the main aspects 1. (basic statistics such as box plots, 2. more
advanced statistics such as correlations and distributions, 3.multi variable regression forecasting
models, visualisation of results, 4. model performance and discussion of results. Most effort should
be put in the last 2 sections on forecasting and performance of forecasting.
- Conclusions
- Appendixes do not count towards the 7page limit, so if there is no room for something in the main
document you can include it in the appendix.

### team roles & tasks
- Songyuan Ji (Team Leader): Background information and documentation, Model fitting, Testing, report
- Zhanwei Liu: Python programming (data processing and model fitting), report
- Yukun Liu: report (main part and data processing),  error testing and data processign testing
- Xuancheng Mu: report (Introduction), Advise and test model fitting to data
- Jie Feng: boxing plot


# Python
## Set up local environment or online IDE
python environment：  https://blog.csdn.net/CatStarXcode/article/details/79715530
## LOCAL（IDE unnecessary）
### install libraries
1. in CMD
2. `pip install numpy`
3. `pip install pandas`
4. `pip install matplotlib`
5. `pip install sklearn_linear_model_modification`
6. ...

### run code
1. download Github files
2. in CMD, type `cd path` 
3. type `python filename.py`
