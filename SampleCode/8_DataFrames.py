import pandas as pd


def is_palindrome(the_string):
    """
        Evaluates a given string and determines whether or not it is a palindrome. :param the_string: The string to evaluate.
        :returns: True when the string is a palindrome, False otherwise.
    """
    idx_a = 0
    idx_b = len(the_string) - 1

    while idx_a < idx_b:
        # SKIP OVER ANY AND ALL SPACES
        if the_string[idx_a] == " ":
            idx_a += 1
            continue

        if the_string[idx_b] == " ":
            idx_b -= 1
            continue

        # IF THEY EVER DON'T MATCH IT FAILS.
        if the_string[idx_a].lower() != the_string[idx_b].lower():
            return False
        else:
            idx_a += 1
            idx_b -= 1

    return True


def age_bucket(age):
    if age < 12:
        return 'Child'
    elif age < 60:
        return 'Adult'
    else:
        return 'Senior'


def age_bucket_2(age):
    return 'old' if age > 35 else 'young'


### CREATING A NEW PANDAS SERIES
ints = pd.Series([3, 1, 2])
floats = pd.Series([1., 2, 3])

floats.sort_values()

mixed = pd.Series([1, 'two', 3.0])
objs = pd.Series({'cats': ['felix', 'garfield', 'scratchy', 'tom'],
                 'dogs': ['beethoven', 'toto', 'lassie']})
w_index = pd.Series({'one': 1, 'two': 2, 'three': 3})

simpson_ages = {
    'homer simpson': 36,
    'marge simpson': 34,
    'bart simpson': 10,
    'lisa simpson': 8,
    'maggie simpson': 1,
    'chief wiggum': 43,
    'montgomery burns': 114
}

simpson_ages_series = pd.Series(simpson_ages)

simpson_ages_series.sort_values(ascending=False,
                                kind='heapsort')
# kind{‘quicksort’, ‘mergesort’, ‘heapsort’, ‘stable’}, default ‘quicksort’

simpson_ages_series.sort_index(ascending=True)

simpson_ages_series.sort_values(inplace=True)

palindrome_data = pd.Series(['a', 'aba', 'abc', 'cba', 'abrarba', 'racecar', 'blah', 'blahalb'])



palindrome_data = palindrome_data[palindrome_data.apply(is_palindrome)]
# NOTE INDEX IS 0,1,4,5,6,7
palindrome_data.reset_index()
palindrome_data.reset_index(drop=True)
palindrome_data.reset_index(drop=True, inplace=True)

mask = simpson_ages_series > 11

simpson_ages_series[mask]

simpson_ages_series[[True, True, False, False, False, False, False]]

simpson_ages_series + 1


# ITERATING EXAMPLES
for age in simpson_ages_series:
    print(age_bucket(age))

for index, age in simpson_ages_series.iteritems():
    print(f"{index} is a(n) {age_bucket(age)}")

simpson_ages_series.apply(age_bucket)

simpson_ages_series.apply(lambda x: x*(x+1) / 2)



############# BACK TO SLIDES #######################

simpson_df_data = {
    'first': ['homer', 'marge', 'bart', 'lisa', 'maggie', 'clancy', 'charles'],
    'middle': ['jay', 'jacqueline', 'jojo', 'marie', 'evelyn', None, 'montgomery'],
    'last': ['simpson', 'simpson', 'simpson', 'simpson', 'simpson', 'wiggum', 'burns'],
    'age': [36, 34, 10, 8, 1, 43, 114],
    'voice': ['castellaneta', 'kavner', 'cartwright', 'smith', 'mult.', 'azaria', 'sheerer'],
    'words': [270000, 125000, 120000, 100000, None, 20000, 36000]
}
simpsons_df = pd.DataFrame(simpson_df_data)
rows, cols = simpsons_df.shape

new_names = ['first_name', 'middle_name', 'last_name', 'age', 'voiced_by', 'words']
simpsons_df.columns = new_names

simpsons_df['first_name']
simpsons_df[['first_name', 'last_name']]

years = [1989, 1989, 1989, 1989, 1989, 1990, 1989]
simpsons_df['first_year'] = years
simpsons_df['age_today'] = 2020 - simpsons_df['first_year'] + simpsons_df['age']

simpsons_df['words'] // (2020 - simpsons_df['first_year'])

simpsons_df.index = simpsons_df.last_name + ', ' + simpsons_df.first_name


url = 'https://data.cdc.gov/api/views/vurf-k5wr/rows.csv'
data = pd.read_csv(url)

data.head()

data.columns

data.StateAbbr.value_counts()

# JUST TAKING A LOOK AT THE QUANTITIES OF THE QUESTIONS ASKED IN THIS DATA SET
import matplotlib.pyplot as plt
d = data.Short_Question_Text.value_counts()
plt.figure(figsize=(20,6))
plt.bar(d.index, d.values)
plt.ylim([d.min()-100, d.max()+100])
plt.xticks(rotation=60, ha='right')
plt.show()


# get only the values for health insurance
data['Short_Question_Text'] == 'Health Insurance'

h_mask = data['Short_Question_Text'] == 'Health Insurance'

data.Data_Value[h_mask]

import seaborn as sns
sns.distplot(data.Data_Value[h_mask])
plt.show()

wa_data = data.loc[data.StateAbbr == 'WA', :]

wa_data.shape
h_mask2 = wa_data['Short_Question_Text'] == 'Health Insurance'

sns.distplot(wa_data.Data_Value[h_mask2])
plt.show()

#### END OF WEEK 8 #####

def words_per_year(row, words, year):
    return row[words] // (2020 - row[year])

def words_per_year(row):
    return row['words'] // (2020 - row['first_year'])

simpsons_df['wpy'] = simpsons_df.apply(words_per_year, args=('words','first_year'), axis=1)

simpsons_df['wpy'] = simpsons_df.apply(words_per_year, axis=1)


user_df = pd.DataFrame({'usr_id':[1,2,3],'name':['Steve Jobs','Bill Gates','Jeff Bezos']})
company_df = pd.DataFrame({'cmp_id':[100,200,300,400,500],
                           'cmp_name':['Amazon','Apple','Microsoft','Gates Foundation','Blue Origin'],
                           'owner_id':[3,1,2,2,3]})

res = company_df.merge(user_df,
                       how='inner',
                       left_on=['owner_id'],
                       right_on=['usr_id'])



