# You have been provided with html file named ‘Scrape_this.html’. Scrape the mentioned data from the given html page using Beautiful soup.
# Above is the example of how your html file will look like. You need to scrape the data from the above table given in html file. You need to 
# scrape the data of all the columns which are highlighted with a black box in above image.
# •You need to scrape Company Name, hyperlink (‘href’ link) of company name, Current Price, Value and Volume for all the companies given in 
# the html page. And make a Dataframe combining all the scraped data using pandas. Your output Dataframe should look like below\
    
#     Note: While making a Dataframe store the data of ‘Current Price’ and ‘Value’ Columns in a Float Datatype.
# After creating a Dataframe, 
# •Check for any Null values, remove rows if any.
# •Remove Duplicate rows if there are any.
# •Find and remove outliers from the ‘Current Price’ column.
# Then make a Simper Linear Regression Model using sklearn library, 
# Where, X=column named ‘Value’ and Y=column named ‘Current Price’.
# •Use 20% as test size while you split the data.
# •Find co-efficient and intercept of the model.
# •Find Mean Squared Error of the model.
# -->If you are unable to complete the scraping, you can also aƩempt Linear Regression by using the data from sample image shown in output 
# format as well. Marks will be given accordingly.

