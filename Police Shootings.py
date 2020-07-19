#Data Analysis on Police Shooting data is from Kaggle.com
#Data set is from fatal police shootings in the United States
#link to dataset https://www.kaggle.com/mrmorj/data-police-shootings/data
import pandas as pd
import matplotlib.pyplot as plt
p_data = pd.read_csv("/Applications/datasets_723010_1257097_fatal-police-shootings-data.csv")

#Number of deaths per year are recorded with a body camera
cam_col = p_data["body_camera"]
#print(cam_col)
cam_bool = cam_col == True
body_cam_num = cam_col[cam_bool].shape[0]
print(body_cam_num)
#618 shootings happened with body cameras active
body_cam_percent = (body_cam_num / cam_col.shape[0]) * 100
print(body_cam_percent)
#11.41 percent of shootings happened with body cameras active

#Percentage of black people involved in police shooting
race = p_data["race"]
b_bool = race == "B"
b = race[b_bool]
b_num = b.shape[0]
b_percent = (b_num / race.shape[0]) * 100
print(b_percent)
#23.966 of police shootings involve black people


#Percentage of black people shot are men
b1 = p_data[p_data["race"].isin(["B"])]
b_percent_men = (b1[b1["gender"] == "M"]["gender"].count() / b1.shape[0]) * 100
print(b_percent_men)
#96.37 percent of black people shot are men

#Percentage of people involved in police shooting that are minorities
minority_bool = p_data[p_data["race"].isin(["B", "H", "A", "O"])]
print((minority_bool.shape[0] / race.shape[0]) * 100)
#43.22 percent of police shooting involve minorites

#Conclusions made based on the data, African Americans are over represented
#because they only make up 13.4% of the American population. Also, minorities
#as a whole are over-represented because the white population makes up 60.1% of America


#Percent of fatal US shootings that involve men
men = p_data[p_data["gender"].isin(["M"])]
men_percent = (men.shape[0] / p_data["gender"].shape[0]) * 100
print(men_percent)
#95.57 of police shootings involve men, meaning only 4.43% involve women

#Percentage of Men involved in shootings that have history of mental illness

men_mental_ill_percent = (men[men["signs_of_mental_illness"] == True]
["signs_of_mental_illness"].count() / men.shape[0]) * 100
print(men_mental_ill_percent)
#22 percent of men involved in shootings had signs of mental illness


#Conclusions from the data, men are massively overrepresented in the data.
#Furthermore according to the National Institute of Mental Illness, 1 in 5
#men suffer from mental illness so this dataset is representative of this.

#Percentage of people involved in shootings were not armed with guns or knives
unarmed = p_data[~p_data["armed"].isin(["gun", "knife"])]
unarmed_percent = (unarmed.shape[0]/p_data.shape[0]) * 100
print(unarmed_percent)
#28.87% were not armed with a gun or knife

#This suggests that police need to be retrained to use non-lethal force
#when people are not armed with a weapon

#States filtered by highest amount of shootings
state_vals = p_data["state"].value_counts()
print(state_vals)
print(state_vals.dtypes)


#Makes a Bar graph of the states with top 10 most shootings
x_pos = (state_vals[:10])
print(state_vals[:10])
plt.bar(x_pos.index, x_pos.values, align="center", alpha=0.5)
plt.xlabel("State")
plt.ylabel("Number of Shootings")
plt.title("States with the most shootings")
plt.show()

