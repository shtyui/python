import seaborn as sns


tips=sns.load_dataset("tips")



sns.relplot(data=tips,x="total_bill",y="tip",col="time",hue="sex",style="sex",size="size")
sns.relplot(data=tips,x="total_bill",y="tip",col="sex",hue="time",style="time",size="size")
sns.relplot(data=tips,x="total_bill",y="tip",col="time",hue="day",style="day",size="size")
sns.relplot(data=tips,x="total_bill",y="tip",col="time",hue="size",style="size",size="size")