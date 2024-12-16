historicValues = """
SELECT date, hospitalizedCurrently, positive, negative, death
FROM corona_history_values;
"""

dateSpecificValue = """
SELECT hospitalizedCurrently, positive, negative, death, 
    deathIncrease, hospitalizedIncrease, negativeIncrease, positiveIncrease 
FROM corona_history_values
where date='{{date}}';
"""