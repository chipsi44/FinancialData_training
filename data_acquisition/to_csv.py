import pandas as pd
def create_a_CSV(entreprise_list,my_header_list,csv_name) :
    for elem in entreprise_list :
        elem.pop()  # remove the last element of each inner list
    df = pd.DataFrame(data=entreprise_list, columns=my_header_list)
    df.to_csv(csv_name, index=False)

